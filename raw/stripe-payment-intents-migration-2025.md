<!-- Source URL: https://docs.stripe.com/payments/payment-intents/migration -->
<!-- Fetched: 2026-04-20 -->

# Migrate to the Payment Intents API

> #### Payment Element integration features
>
> You can integrate with the Payment Element to manage subscriptions, tax, discounts, shipping, and currency conversion. To learn more, see the [Build a checkout page](https://docs.stripe.com/payments/quickstart-checkout-sessions.md) guide.

Learn how to migrate your existing cards and Charges API integration.

Migrating your payment flow can be daunting. It’s safe to incrementally adopt the Payment Intents API and use it in parallel with the Charges API. To this end, you can split up the migration into the following steps:

1. [Update your API version and your client library](https://docs.stripe.com/payments/payment-intents/migration.md#api-version).
1. If applicable, [migrate code that reads from Charge properties](https://docs.stripe.com/payments/payment-intents/migration/charges.md) so that you have a consistent read path between charges created by the Charges API and charges created by the Payment Intents API. This ensures a read-side integration that works for both your old and new payments integrations.
1. Migrate your existing Charges API integration on [Web](https://docs.stripe.com/payments/payment-intents/migration.md#web), [iOS](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=ios), and [Android](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=android) to use the Payment Intents API.
1. Migrate your integration that [saves cards on Customer objects](https://docs.stripe.com/payments/payment-intents/migration.md#saved-cards).
1. [Test with regulatory test cards](https://docs.stripe.com/testing.md#regulatory-cards) to ensure your upgraded integration handles authentication correctly.

## Update your API version and your client library

While the Payment Intents API works on all API versions, we recommend that you [upgrade to the latest API version](https://docs.stripe.com/upgrades.md#how-can-i-upgrade-my-api). If you decide to use an API version older than [2019-02-11](https://docs.stripe.com/upgrades.md#2019-02-11), note the following two changes as you go through the code examples:

- `requires_source` has been renamed to `requires_payment_method`
- `requires_source_action` has been renamed to `requires_action`

In addition, if you use one of our [SDKs](https://docs.stripe.com/sdks.md), upgrade to the latest version of the library to use the Payment Intents API.

## Migrate your one-time payment flows

#### Elements

An integration built with Stripe.js & Elements consists of the following steps:

1. Register your intent to collect payment on the server side
1. Collect payment details on the client side
1. Initiate creation of the payment
1. Fulfill the customer’s order on the server side

### Step 1: Register intent to collect payment on the server side

[Create a PaymentIntent](https://docs.stripe.com/payments/payment-intents.md) on your server and make it [accessible on the client side](https://docs.stripe.com/payments/payment-intents.md#passing-to-client).

### Step 2: Collect payment details on the client side

Use the [confirmCardPayment](https://docs.stripe.com/js.md#stripe-confirm-card-payment) function, which collects the payment information and submits it directly to Stripe.

### Step 3: Initiate creation of the payment

In your existing integration, the final step is using tokenized payment information to create a charge on your server. This is no longer necessary, as the `confirmCardPayment` function—called in the previous step—initiates creation of the charge.

### Step 4: Fulfill the customer’s order

With automatic confirmation, the charge is created for you asynchronously based on customer action on the client side, so you must [monitor webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md) to determine when the payment completes successfully. To perform steps like order fulfillment after a customer’s payment is successful, implement support for webhooks and monitor the `payment_intent.succeeded` event.

### Before

If charge succeeds, fulfill.

### After

Subscribe to the `payment_intent.succeeded` webhook and fulfill in the webhook handler.

Now that you have migrated, use the test cards in the following section to verify your upgraded integration handles 3D Secure authentication.

#### Payment Request Button

The Stripe.js [Payment Request Button](https://docs.stripe.com/stripe-js/elements/payment-request-button.md) works with the Payment Intents API by using the token obtained in a traditional PaymentRequest integration and attaching it to a PaymentIntent.

An integration built with PaymentRequest consists of the following steps:

1. Register your intent to collect payment on the server side
1. Collect payment details on the client side
1. Initiate creation of the payment
1. Fulfill the customer’s order on the server side

Alternatively, use the [Express Checkout Element](https://docs.stripe.com/elements/express-checkout-element.md) to offer multiple one-click payment buttons to your customers, including Apple Pay, Google Pay, Link, and PayPal.

### Step 1: Register intent to collect payment on the server side

[Create a PaymentIntent](https://docs.stripe.com/payments/payment-intents.md) on your server and make it [accessible on the client side](https://docs.stripe.com/payments/payment-intents.md#passing-to-client).

### Step 2: Collect payment details on the client side

Listen for the `PaymentRequest` object’s `token` event, which provides a token and a callback function that you can use to indicate when the payment process is complete.

To adapt this integration to support the Payment Intents API, use the [confirmCardPayment](https://docs.stripe.com/js.md#stripe-confirm-card-payment) function and pass it the token ID instead of sending the token to your server. When the promise returned by the `confirmCardPayment` function resolves, invoke the completion callback.

### Step 3: Initiate creation of the payment

In your existing integration, the final step is using tokenized payment information to create a charge on your server. This is no longer necessary, as the `confirmCardPayment` function—called in the previous step—initiates creation of the charge.

### Step 4: Fulfill the customer’s order

With automatic confirmation, the charge is created for you asynchronously based on customer action on the client side, so you must [monitor webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md) to determine when the payment completes successfully. To perform steps like order fulfillment after a customer’s payment is successful, implement support for webhooks and monitor the `payment_intent.succeeded` event.

### Before

If charge succeeds, fulfill.

### After

Subscribe to the `payment_intent.succeeded` webhook and fulfill in the webhook handler.

Now that you have migrated, use the test cards in the following section to verify your upgraded integration handles 3D Secure authentication.

#### Legacy Checkout

If you’re using the legacy version of Checkout, upgrade to the [new version of Checkout](https://docs.stripe.com/payments/checkout.md)—the fastest way to accept payments with Stripe. With it, you can accept one-time payments and subscriptions. You can also use Checkout without using the Stripe API on your server. Follow the [Checkout migration guide](https://docs.stripe.com/payments/checkout/migration.md) to migrate your existing integration.

If you prefer to build your own checkout flow instead, switch to [Elements](https://docs.stripe.com/payments/elements.md). Assuming you’ve upgraded to Elements, you can build a Payment Intents API integration using the [Elements migration guide](https://docs.stripe.com/payments/payment-intents/migration.md#web).

#### Stripe.js v2

To upgrade an existing Stripe.js v2 integration to use the Payment Intents API, first update your integration to collect payment information with Elements. Elements provides prebuilt UI components and offers simple [PCI compliance](https://docs.stripe.com/security/guide.md) with SAQ A reporting.

After you’ve upgraded to Elements, you can build a Payment Intents API integration using the [Elements migration guide](https://docs.stripe.com/payments/payment-intents/migration.md#web).

## Migrate your integration that saves cards on Customer objects

#### Saving cards in checkout flow

A Payment Intents API integration that collects card information in the checkout flow consists of the following steps:

1. Register your intent to collect payment on the server side
1. Collect payment details on the client side
1. Initiate creation of the payment
1. Fulfill the customer’s order on the server side

### Step 1: Register intent to collect payment on the server side

[Create a PaymentIntent](https://docs.stripe.com/payments/payment-intents.md) on your server. Set [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to `off_session` if you primarily intend to charge users when they’re outside of your application, or `on_session` if you plan to charge them in the application. If you plan to use the card for both on and off session payments use `off_session`. Providing the `setup_future_usage` parameter along with a Customer ID will save the resulting PaymentMethod to that Customer after the PaymentIntent has been confirmed and any required actions from the customer are complete. Next, make the PaymentIntent [accessible on the client side](https://docs.stripe.com/payments/payment-intents.md#passing-to-client).

### Step 2: Collect payment details on the client side

Use the [confirmCardPayment](https://docs.stripe.com/js.md#stripe-confirm-card-payment) function, which collects the payment information and submits it directly to Stripe.

Finally, attach the payment method (`paymentIntent.payment_method`) to the customer.

### Step 3: Initiate creation of the payment

In your existing integration, the final step is using tokenized payment information to create a charge on your server. This is no longer necessary, as the `confirmCardPayment` function—called in the previous step—initiates creation of the charge.

### Step 4: Fulfill the customer’s order

With automatic confirmation, the charge is created for you asynchronously based on customer action on the client side, so you must [monitor webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md) to determine when the payment completes successfully. To perform steps like order fulfillment after a customer’s payment is successful, implement support for webhooks and monitor the `payment_intent.succeeded` event.

### Before

If charge succeeds, fulfill.

### After

Subscribe to the `payment_intent.succeeded` webhook and fulfill in the webhook handler.

Now that you have migrated, use the test cards in the following section to verify your upgraded integration handles 3D Secure authentication.

#### Saving cards outside checkout flow

There are a couple of changes you’ll need to make to your existing integration that saves card details outside of a checkout flow. First, create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) on your server. A SetupIntent authenticates the card without making an initial payment.

Pass the SetupIntent’s [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret) to your client and use the [confirmCardSetup](https://docs.stripe.com/js.md#stripe-confirm-card-setup) function instead of [createToken](https://docs.stripe.com/js.md#stripe-create-token) or [createSource](https://docs.stripe.com/js.md#stripe-create-source) after your customer enters their card details.

If required by regulation, [confirmCardSetup](https://docs.stripe.com/js.md#stripe-confirm-card-setup) will prompt the user to authenticate the card.

When [confirmCardSetup](https://docs.stripe.com/js.md#stripe-confirm-card-setup) succeeds, `setupIntent.payment_method` will contain a [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) that you can attach to a Customer.

Pass the ID of that PaymentMethod to your server, and [attach the payment method](https://docs.stripe.com/api/payment_methods/attach.md) to the Customer object using the Payment Methods API instead of the Customers API.

#### Paying with saved cards

When paying with a previously saved payment method, you must specify both the ID of the Customer and the ID of the previously saved Card, Source, or PaymentMethod. Previously, the default source on the customer is used if one wasn’t provided. You must now explicitly pass in the desired payment method.

If the customer is _off-session_ (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information), you must flag the payment as an off-session payment. See [Charging Saved Cards](https://docs.stripe.com/payments/save-and-reuse.md?platform=web&ui=elements#charge-saved-payment-method) for more information.

## Access saved payment methods

To display the customer’s previously saved Cards, Sources, and PaymentMethods, [list the payment methods](https://docs.stripe.com/api/payment_methods/list.md) instead of reading the [sources](https://docs.stripe.com/api/customers/object.md#customer_object-sources) property of the customer object. This is required because new PaymentMethods added to a customer won’t be duplicated in the sources property of the customer object.

## Test the integration

It’s important to thoroughly test your integration to make sure you’re correctly handling cards that require additional authentication and cards that don’t. Use these card numbers in a [sandbox](https://docs.stripe.com/keys.md#test-live-modes) with any expiration date in the future and any three digit CVC code to validate your integration when authentication is required and when it’s not required.

| Number           | Authentication                         | Description                                                                                                                                                                                                                                                                                                                                |
| ---------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 4000002500003155 | Required on setup or first transaction | This test card requires authentication for [one-time payments](https://docs.stripe.com/payments/accept-a-payment.md?platform=web). However, if you set up this card using the [Setup Intents API](https://docs.stripe.com/payments/save-and-reuse.md) and use the saved card for subsequent payments, no further authentication is needed. |
| 4000002760003184 | Required                               | This test card requires authentication on all transactions.                                                                                                                                                                                                                                                                                |
| 4000008260003178 | Required                               | This test card requires authentication, but payments will be declined with an `insufficient_funds` failure code after successful authentication.                                                                                                                                                                                           |
| 4000000000003055 | Supported                              | This test card supports authentication through 3D Secure 2, but doesn’t require it. Payments using this card don’t require additional authentication in a sandbox unless your [sandbox Radar rules](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#three-ds-radar) request authentication.                              |

Use these cards in your application or the [payments demo](https://stripe-payments-demo.appspot.com) to see the different behavior.

## See also

- [PaymentIntents on iOS](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=ios)
- [PaymentIntents on Android](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=android)
