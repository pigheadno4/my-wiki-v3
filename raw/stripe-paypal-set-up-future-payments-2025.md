<!-- Source URL: https://docs.stripe.com/payments/paypal/set-up-future-payments -->
<!-- Fetched: 2026-05-07 -->

# Set up future PayPal payments

Learn how to save PayPal details and charge your customers later.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Set up future PayPal payments to save customer payment details for subscriptions, delayed charges, and streamlined future purchases. Learn how to enable and use recurring payments with PayPal through Stripe.

## Enable recurring payments

Stripe automatically enables recurring payments for most users when they [activate PayPal payments](https://docs.stripe.com/payments/paypal/activate.md) in the Stripe Dashboard. However, due to PayPal’s policies and regional restrictions, some users might need to enable recurring payments manually. This includes users that set up their accounts before we introduced automatic enablement. To manually enable recurring payments:

1. Go to your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

1. Click **PayPal** > **Enable** in the **Recurring payments** section.

After you enable recurring payments, it appears as **pending** in the Dashboard. It usually takes up to five business days to get access.

When you’re granted access, recurring payments are available in your [PayPal settings](https://dashboard.stripe.com/settings/payment_methods). In testing environments, recurring payments are enabled by default.

Use [Stripe Checkout](https://docs.stripe.com/payments/checkout.md) to collect PayPal payment details in advance, and determine the final amount or payment date later. Use it to:

- Save payment methods to a wallet to streamline future purchases
- Collect surcharges after fulfilling a service
- [Start a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md)

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer before setup [Server-side]

To reuse a PayPal payment method for future payments, it must be attached to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

You should create a Customer object when your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer will enable you to retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a Checkout Session [Client-side] [Server-side]

Before you can accept PayPal payments, your customer must authorize you to use their PayPal account for future payments through Stripe Checkout.

Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md).

```html
<html>
  <head>
    <title>Checkout</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
```

Create a Checkout Session in `setup` mode to collect the required information. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["paypal"],
  mode: "setup",
  customer: customer.id,
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});

// 303 redirect to session.url
```

When your customer provides their payment method details, they’re redirected to the `success_url`, a page on your website that informs them that their payment method was saved successfully. Make the Session ID available on your success page by including the `{CHECKOUT_SESSION_ID}` template variable in the `success_url` as in the above example.

> Don’t rely on the redirect to the `success_url` alone for detecting payment initiation, because:
>
> - Malicious users could directly access the `success_url` without paying and gain access to your goods or services.

- After a successful payment, customers might close their browser tab before they’re redirected to the `success_url`.

## Retrieve the payment method [Server-side]

After a customer submits their payment details, retrieve the [PaymentMethod](https://docs.stripe.com/payments/payment-methods.md) object. A *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) stores the customer’s PayPal account information for future payments. You can retrieve the PaymentMethod synchronously using the `success_url` or asynchronously using *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests).

The decision to retrieve the PaymentMethod synchronously or asynchronously depends on your tolerance for dropoff, as customers might not always reach the `success_url` after a successful payment (for example, it’s possible for them to close their browser tab before the redirect occurs). Using webhooks prevents your integration from experiencing this form of dropoff.

#### Webhooks

Handle `checkout.session.completed` webhooks, which contain a Session object. To learn more, see [setting up webhooks](https://docs.stripe.com/webhooks.md). The following example is a `checkout.session.completed` response.

```json
{
  "id": "evt_1Ep24XHssDVaQm2PpwS19Yt0",
  "object": "event",
  "api_version": "2019-03-14",
  "created": 1561420781,
  "data": {
    "object": {
      "id": "cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k",
      "object": "checkout.session",
      "billing_address_collection": null,
      "client_reference_id": null,
      "customer": null,
      "customer_email": null,
      "display_items": [],
      "mode": "setup",
      "setup_intent": "seti_1EzVO3HssDVaQm2PJjXHmLlM",
      "submit_type": null,
      "subscription": null,
      "success_url": "https://example.com/success"
    }
  },
  "livemode": false,
  "pending_webhooks": 1,
  "request": {
    "id": null,
    "idempotency_key": null
  },
  "type": "checkout.session.completed"
}
```

Note the value of the `setup_intent` key, which is the ID for the SetupIntent created with the Checkout Session. A [SetupIntent](https://docs.stripe.com/payments/setup-intents.md) is an object used to set up the customer PayPal account information for future payments. [Retrieve](https://docs.stripe.com/api/setup_intents/retrieve.md) the SetupIntent object with the ID. The returned object contains the `payment_method` ID.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.retrieve(
  "seti_1EzVO3HssDVaQm2PJjXHmLlM",
);
```

#### Success URL

Obtain the `session_id` from the URL when a user redirects back to your site and [retrieve](https://docs.stripe.com/api/checkout/sessions/retrieve.md) the Session object.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.retrieve("{{SESSION_ID}}", {
  expand: ["setup_intent"],
});
```

> To ensure the `session_id` is available from the URL, include the `session_id={CHECKOUT_SESSION_ID}` template variable in the `success_url` when creating the Checkout Session.

Note the SetupIntent created during the Checkout Session. A [SetupIntent](https://docs.stripe.com/payments/setup-intents.md) is an object used to set up the customer PayPal account information for future payments. The returned object contains the `payment_method` ID.

## Handle post-setup events [Server-side]

Use a method such as [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the billing agreement was authorized successfully by your customer, instead of relying on your customer to return to the payment status page. When a customer successfully authorizes the billing agreement, the SetupIntent emits the [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. If a customer doesn’t successfully authorize the billing agreement, the SetupIntent will emit the [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) webhook event and returns to a status of `requires_payment_method`. When a customer revokes the billing agreement from their PayPal account, the [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) is emitted.

## Test the integration

Test your PayPal integration with your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **Fail test payment**. The PaymentIntent will transition from `requires_action` to `requires_payment_method`.

## Use the payment method for future payments [Server-side]

When you’re ready to charge your customer off-session, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).

To find a `paypal` instrument to charge, [list](https://docs.stripe.com/api/payment_methods/list.md) the PaymentMethods associated with your Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer: "{{CUSTOMER_ID}}",
  type: "paypal",
});
```

When you have the Customer and PaymentMethod IDs, create a PaymentIntent with the amount and currency of the payment. Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during this payment attempt. This causes the PaymentIntent to throw an error if authentication is required.
- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the ID of the PaymentMethod and [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["paypal"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: true,
  confirm: true,
});
```

## User-initiated payment method cancellation [Server-side]

A customer can cancel the subscription (Billing Agreement) through their PayPal account. When they do so, Stripe emits a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) webhook. All subsequent PaymentIntents using the saved Payment Method will fail until you change to a Payment Method with active mandates. When payments fail for Subscriptions, the status changes to the Subscription status configured in your [automatic collection settings](https://docs.stripe.com/invoicing/automatic-collection.md). Notify the customer of failure and [charge them with a different payment method](https://docs.stripe.com/billing/subscriptions/overview.md#requires-payment-method).

## Optional: Remove a saved PayPal account [Server-side]

You can use the [detach](https://docs.stripe.com/api/payment_methods/detach.md) API to remove a customer’s saved PayPal account as a payment method. When you detach a PayPal payment method, it revokes the [mandate](https://docs.stripe.com/api/mandates.md) and also calls the PayPal API to cancel the associated PayPal billing agreement.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.detach(
  "{{PAYMENT_METHOD_ID}}",
);
```

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/paypal/set-up-future-payments?payment-ui=direct-api.

You can use [Setup Intents](https://docs.stripe.com/api/setup_intents.md) to collect PayPal payment method details in advance, and determine the final amount or payment date later. Use it to:

- Save payment methods to a wallet to streamline future purchases
- Collect surcharges after fulfilling a service
- [Start a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md)

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer before setup [Server-side]

To reuse a PayPal payment method for future payments, it must be attached to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

You should create a Customer object when your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer will enable you to retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent and tracks the steps to set up your customer’s payment method for future payments.

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `paypal` and specify the ID of the customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-id) or [Customer](https://docs.stripe.com/api/customers/object.md#customer_object-id).

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method_types: ["paypal"],
  payment_method_data: {
    type: "paypal",
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["paypal"],
  payment_method_data: {
    type: "paypal",
  },
});
```

The SetupIntent object contains a [client_secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret), a unique key that you need to pass to Stripe on the client side to redirect your buyer to PayPal and authorize the mandate.

## Redirect your customer [Client-side]

When a customer attempts to set up their PayPal account for future payments, we recommend you use [Stripe.js](https://docs.stripe.com/js.md) to confirm the SetupIntent. Stripe.js is our foundational JavaScript library for building payment flows. It will automatically handle complexities like the redirect described below, and enables you to easily extend your integration to other payment methods in the future.

Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page.

```javascript
// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>", {});
```

To confirm the setup on the client side, pass the client secret of the SetupIntent object that you created in Step 3.

The client secret is different from your API keys that authenticate Stripe API requests. It should still be handled carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

### Confirm PayPal Setup

To authorize you to use their PayPal account for future payments, your customer will be redirected to a PayPal billing agreement page, which they will need to approve before being redirected back to your website. Use [stripe.confirmPayPalSetup](https://docs.stripe.com/js/setup_intents/confirm_paypal_setup) to handle the redirect away from your page and to complete the setup. Add a `return_url` to this function to indicate where Stripe should redirect the user to after they approve the billing agreement on PayPal’s website.

```javascript
// Redirects away from the client
const { error } = await stripe.confirmPayPalSetup(
  "{{SETUP_INTENT_CLIENT_SECRET}}",
  {
    return_url: "https://example.com/setup/complete",
    mandate_data: {
      customer_acceptance: {
        type: "online",
        online: {
          infer_from_client: true,
        },
      },
    },
  },
);

if (error) {
  // Inform the customer that there was an error.
}
```

You can find the Payment Method payer ID and Billing Agreement ID on the resulting [Mandate](https://docs.stripe.com/api/mandates/.md) under the [payment_method_details](https://docs.stripe.com/api/mandates/object.md#mandate_object-payment_method_details-paypal) property. You can also find the buyer’s email and payer ID in the [paypal](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-paypal) property on the [PaymentMethod](https://docs.stripe.com/api/payment_methods.md).

| Field                  | Value                                                                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `payer_email`          | The email address of the payer on their PayPal account.                                                                                       |
| `payer_id`             | A unique ID of the payer’s PayPal account.                                                                                                    |
| `billing_agreement_id` | The PayPal Billing Agreement ID (BAID). This is an ID generated by PayPal which represents the mandate between the business and the customer. |

## Monitor webhooks [Server-side]

Use a method such as [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the billing agreement was authorized successfully by your customer, instead of relying on your customer to return to the payment status page. When a customer successfully authorizes the billing agreement, the SetupIntent emits the [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. If a customer doesn’t successfully authorize the billing agreement, the SetupIntent will emit the [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) webhook event and returns to a status of `requires_payment_method`. When a customer revokes the billing agreement from their PayPal account, the [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) is emitted.

## Charge off-session payments with a saved PayPal payment method [Server-side]

When you’re ready to charge your customer off-session, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).

To find a `paypal` instrument to charge, [list](https://docs.stripe.com/api/payment_methods/list.md) the PaymentMethods associated with your Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer: "{{CUSTOMER_ID}}",
  type: "paypal",
});
```

When you have the Customer and PaymentMethod IDs, create a PaymentIntent with the amount and currency of the payment. Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during this payment attempt. This causes the PaymentIntent to throw an error if authentication is required.
- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the ID of the PaymentMethod and [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["paypal"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: true,
  confirm: true,
});
```

## Charge on-session payments with a saved PayPal payment method [Client-side]

When you’re ready to charge your customer on-session, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).

To find a `paypal` instrument to charge, [list the PaymentMethods](https://docs.stripe.com/api/payment_methods/list.md) associated with your Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer: "{{CUSTOMER_ID}}",
  type: "paypal",
});
```

When you have the Customer and PaymentMethod IDs, create a PaymentIntent with the amount and currency of the payment:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["paypal"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
});
```

Using Stripe.js SDK, call the [confirmPayPalPayment](https://docs.stripe.com/js/payment_intents/confirm_paypal_payment) function to execute the created PaymentIntent:

```javascript
// Confirms the on-session payment
const { error } = await stripe.confirmPayPalPayment(
  "{{PAYMENT_INTENT_CLIENT_SECRET}}",
  { payment_method: "{{PAYMENT_METHOD_ID}}" },
  // Note: return_url is not required here because the PayPal payment method was
  // previously set up using either a SetupIntent or a PaymentIntent with setup_future_usage
);

if (error) {
  // Inform the customer that there was an error.
}
```

> **Note**: The `return_url` parameter is conditionally required for `confirmPayPalPayment`:
>
> - It’s _not required_ when using a PayPal payment method that was previously set up with a SetupIntent or a PaymentIntent with `setup_future_usage`.

- It’s _required_ for all other cases, including when creating a new PayPal payment method on-session.

## User-initiated payment method cancellation [Server-side]

A customer can cancel the subscription (Billing Agreement) through their PayPal account. When they do so, Stripe emits a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) webhook. All subsequent PaymentIntents using the saved Payment Method will fail until you change to a Payment Method with active mandates. When payments fail for Subscriptions, the status changes to the Subscription status configured in your [automatic collection settings](https://docs.stripe.com/invoicing/automatic-collection.md). Notify the customer of failure and [charge them with a different payment method](https://docs.stripe.com/billing/subscriptions/overview.md#requires-payment-method).

## Optional: Set up future PayPal payments and capture a payment [Server-side]

It’s also possible to set up a PayPal Payment Method for future usage and also charge at the same time when creating a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).

Set [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to `off_session` to indicate that you want to set up the payment method for future usage.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["paypal"],
  setup_future_usage: "off_session",
});
```

## Optional: Handle the PayPal redirect manually [Server-side]

We recommend relying on Stripe.js to handle PayPal redirects and billing authorizations client-side with `confirmPayPalSetup`. Using Stripe.js makes it much easier to extend your integration to other payment methods. However, you can also manually redirect your customers on your server by following these steps:

You can *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the SetupIntent at creation time by setting `confirm: true` and providing data about the mandate in the [mandate_data](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-mandate_data) parameter. A `return_url` must be provided when confirming a SetupIntent to indicate where Stripe should redirect the user to after they complete the set-up on PayPal’s website or mobile application.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["paypal"],
  payment_method_data: {
    type: "paypal",
  },
  usage: "off_session",
  mandate_data: {
    customer_acceptance: {
      type: "online",
      online: {
        ip_address: "{{IP_ADDRESS}}",
        user_agent: "{{USER_AGENT}}",
      },
    },
  },
  confirm: true,
  return_url: "https://example.com/setup/complete",
});
```

Check that the SetupIntent has a status of `requires_action` and the type for `next_action` is `redirect_to_url`.

```json
{
  "id": "seti_1IQ9hjJJahOk1vSNevPWnhEN",
  "object": "setup_intent",
  "status": "requires_action",
  "next_action": {
    "type": "redirect_to_url",
    "redirect_to_url": {
      "url": "https://hooks.stripe.com/...",
      "return_url": "https://example.com/setup/complete"
    }
  },
  "application": null,
  "cancellation_reason": null,
  "client_secret": "seti_1IQ9hjJJahOk1vSNevPWnhEN_secret_J2EAlI0GQbQKV9tg7ITRcUWRBiAwvUV",
  "created": 1614597263,
  "customer": null,
  "description": null,
  "last_setup_error": null,
  "latest_attempt": "setatt_1IQ9hkJJahOk1vSN0rsCpnLI",
  "livemode": false,
  "mandate": null,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1IQ9hjJJahOk1vSNDc5lQWia",
  "payment_method_options": {},
  "payment_method_types": ["paypal"],
  "single_use_mandate": null,
  "usage": "off_session"
}
```

Redirect the customer to the URL provided in the `next_action.redirect_to_url.url` property. The code example here is approximate—the redirect method might be different in your web framework.

#### Node.js

```javascript
if (
  paymentIntent.status === "requires_action" &&
  paymentIntent.next_action.type === "redirect_to_url"
) {
  const url = paymentIntent.next_action.redirect_to_url.url;
  res.redirect(url);
}
```

When the customer finishes the authorization process, they’re sent to the `return_url` configured in step 1. The `setup_intent` and `setup_intent_client_secret` URL query parameters are included and you can pass through your own query parameters, as described above.

## Optional: Handle risk library integration for on-session payments manually [Server-side]

We recommend relying on Stripe.js to handle on-session payments with a saved PayPal payment method because it comes with a built-in [Fraudnet](https://developer.paypal.com/limited-release/fraudnet/) integration. However, you can also manually confirm PayPal PaymentIntents on your server by following these steps:

Integrate with PayPal’s risk libraries ([Fraudnet](https://developer.paypal.com/limited-release/fraudnet/) for web and [Magnes](https://developer.paypal.com/limited-release/magnes/) for mobile) to allow PayPal to collect risk data when the buyer is present in the payment session. This reduces fraud and can increase your payments conversion for on-session payments. You need the Client Metadata ID (also known as Risk Correlation ID) used to initialize the library when making the API call to Stripe.

After the library loads, you can create a PaymentIntent with the Client Metadata ID, amount, and currency of the payment:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["paypal"],
  payment_method_options: {
    paypal: {
      risk_correlation_id: "{{RISK_CORRELATION_ID}}",
    },
  },
  confirm: true,
  payment_method: "{{PAYMENT_METHOD_ID}}",
});
```

You’ll get a `paypal_risk_correlation_id_missing` message code if you fail to pass the [risk_correlation_id](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-paypal-risk_correlation_id) parameter when confirming an on-session payment.

## Optional: Remove a saved PayPal account [Server-side]

You can use the [detach](https://docs.stripe.com/api/payment_methods/detach.md) API to remove a customer’s saved PayPal account as a payment method. When you detach a PayPal payment method, it revokes the [mandate](https://docs.stripe.com/api/mandates.md) and also calls the PayPal API to cancel the associated PayPal billing agreement.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.detach(
  "{{PAYMENT_METHOD_ID}}",
);
```

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/paypal/set-up-future-payments?payment-ui=mobile&platform=ios.

You can use [Setup Intents](https://docs.stripe.com/api/setup_intents.md) to collect PayPal payment method details in advance, and determine the final amount or payment date later. Use it to:

## Create or retrieve a Customer [Server-side]

To reuse a PayPal payment method for future payments, you must attach it to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a Customer object when your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent and tracks the steps to set up your customer’s payment method for future payments.

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `paypal` and specify the ID of the customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-id) or [Customer](https://docs.stripe.com/api/customers/object.md#customer_object-id).

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method_types: ["paypal"],
  payment_method_data: {
    type: "paypal",
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["paypal"],
  payment_method_data: {
    type: "paypal",
  },
});
```

The SetupIntent object contains a [client_secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret), a unique key that you need to pass to Stripe on the client side to redirect your buyer to PayPal and authorize the mandate.

## Collect payment method details [Client-side]

#### Swift

```swift
// PayPal doesn't require additional parameters so we only need to pass the initialized
// STPPaymentMethodPayPalParams instance to STPPaymentMethodParams
let payPal = STPPaymentMethodPayPalParams()
let paymentMethodParams = STPPaymentMethodParams(payPal: payPal, billingDetails: nil, metadata: nil)
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the SetupIntent you created and call [STPPaymentHandler confirmSetupIntent](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:objc(cs)STPPaymentHandler(im)confirmSetupIntent:withAuthenticationContext:completion:>). This presents a webview where the customer can complete the payment in PayPal. Afterwards, the completion block is called with the result of the payment.

#### Swift

```swift
let setupIntentParams = STPSetupIntentConfirmParams(clientSecret: setupIntentClientSecret)
setupIntentParams.paymentMethodParams = paymentMethodParams
setupIntentParams.returnURL = "payments-example://stripe-redirect"

STPPaymentHandler.shared().confirmSetupIntent(withParams: setupIntentParams, authenticationContext: self) { (handlerStatus, setupIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // Setup succeeded

    case .canceled:
        // Setup was canceled

    case .failed:
        // Setup failed

    @unknown default:
        fatalError()
    }
}
```

## Monitor webhooks [Server-side]

Use a method such as [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the billing agreement was authorized successfully by your customer, instead of relying on your customer to return to the payment status page. When a customer successfully authorizes the billing agreement, the SetupIntent emits the [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. If a customer doesn’t successfully authorize the billing agreement, the SetupIntent will emit the [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) webhook event and returns to a status of `requires_payment_method`. When a customer revokes the billing agreement from their PayPal account, the [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) is emitted.

## Charge off-session payments with a saved PayPal payment method [Server-side]

When you’re ready to charge your customer off-session, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).

To find a `paypal` instrument to charge, [list](https://docs.stripe.com/api/payment_methods/list.md) the PaymentMethods associated with your Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer: "{{CUSTOMER_ID}}",
  type: "paypal",
});
```

When you have the Customer and PaymentMethod IDs, create a PaymentIntent with the amount and currency of the payment. Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during this payment attempt. This causes the PaymentIntent to throw an error if authentication is required.
- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the ID of the PaymentMethod and [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["paypal"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: true,
  confirm: true,
});
```

## User-initiated payment method cancellation [Server-side]

A customer can cancel the subscription (Billing Agreement) through their PayPal account. When they do so, Stripe emits a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) webhook. All subsequent PaymentIntents using the saved Payment Method will fail until you change to a Payment Method with active mandates. When payments fail for Subscriptions, the status changes to the Subscription status configured in your [automatic collection settings](https://docs.stripe.com/invoicing/automatic-collection.md). Notify the customer of failure and [charge them with a different payment method](https://docs.stripe.com/billing/subscriptions/overview.md#requires-payment-method).

## Optional: Set up future PayPal payments and capture a payment [Server-side]

It’s also possible to set up a PayPal Payment Method for future usage and also charge at the same time when creating a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).

Set [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to `off_session` to indicate that you want to set up the payment method for future usage.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["paypal"],
  setup_future_usage: "off_session",
});
```

## Optional: Handle risk library integration for on-session payments manually [Server-side]

We recommend relying on Stripe.js to handle on-session payments with a saved PayPal payment method because it comes with a built-in [Fraudnet](https://developer.paypal.com/limited-release/fraudnet/) integration. However, you can also manually confirm PayPal PaymentIntents on your server by following these steps:

Integrate with PayPal’s risk libraries ([Fraudnet](https://developer.paypal.com/limited-release/fraudnet/) for web and [Magnes](https://developer.paypal.com/limited-release/magnes/) for mobile) to allow PayPal to collect risk data when the buyer is present in the payment session. This reduces fraud and can increase your payments conversion for on-session payments. You need the Client Metadata ID (also known as Risk Correlation ID) used to initialize the library when making the API call to Stripe.

After the library loads, you can create a PaymentIntent with the Client Metadata ID, amount, and currency of the payment:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["paypal"],
  payment_method_options: {
    paypal: {
      risk_correlation_id: "{{RISK_CORRELATION_ID}}",
    },
  },
  confirm: true,
  payment_method: "{{PAYMENT_METHOD_ID}}",
});
```

You’ll get a `paypal_risk_correlation_id_missing` message code if you fail to pass the [risk_correlation_id](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-paypal-risk_correlation_id) parameter when confirming an on-session payment.

## Optional: Remove a saved PayPal account [Server-side]

You can use the [detach](https://docs.stripe.com/api/payment_methods/detach.md) API to remove a customer’s saved PayPal account as a payment method. When you detach a PayPal payment method, it revokes the [mandate](https://docs.stripe.com/api/mandates.md) and also calls the PayPal API to cancel the associated PayPal billing agreement.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.detach(
  "{{PAYMENT_METHOD_ID}}",
);
```

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/paypal/set-up-future-payments?payment-ui=mobile&platform=android.

You can use [Setup Intents](https://docs.stripe.com/api/setup_intents.md) to collect PayPal payment method details in advance, and determine the final amount or payment date later. Use it to:

- Save payment methods to a wallet to streamline future purchases
- Collect surcharges after fulfilling a service
- [Start a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md)

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [Stripe Android SDK](https://github.com/stripe/stripe-android) is open source and [fully documented](https://stripe.dev/stripe-android/).

To install the SDK, add `stripe-android` to the `dependencies` block of your [app/build.gradle](https://developer.android.com/studio/build/dependencies) file:

#### Kotlin

```kotlin
plugins {
    id("com.android.application")
}

android { ... }

dependencies {
  // ...

  // Stripe Android SDK
  implementation("com.stripe:stripe-android:23.7.0")
  // Include the financial connections SDK to support US bank account as a payment method
  implementation("com.stripe:financial-connections:23.7.0")
}
```

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-android/releases) page on GitHub. To receive notifications when a new release is published, [watch releases for the repository](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository).

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/apikeys) so that it can make requests to the Stripe API, such as in your `Application` subclass:

#### Kotlin

```kotlin
import com.stripe.android.PaymentConfiguration

class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        PaymentConfiguration.init(
            applicationContext,
            "<<YOUR_PUBLISHABLE_KEY>>"
        )
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

Stripe samples also use [OkHttp](https://github.com/square/okhttp) and [GSON](https://github.com/google/gson) to make HTTP requests to a server.

## Create or retrieve a Customer [Server-side]

To reuse a PayPal payment method for future payments, you must attach it to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a Customer object when your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent and tracks the steps to set up your customer’s payment method for future payments.

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `paypal` and specify the ID of the customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-id) or [Customer](https://docs.stripe.com/api/customers/object.md#customer_object-id).

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method_types: ["paypal"],
  payment_method_data: {
    type: "paypal",
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["paypal"],
  payment_method_data: {
    type: "paypal",
  },
});
```

The SetupIntent object contains a [client_secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret), a unique key that you need to pass to Stripe on the client side to redirect your buyer to PayPal and authorize the mandate.

## Submit the payment method details to Stripe [Client-side]

Retrieve the client secret from the SetupIntent you created and call [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/confirm.html). This presents a webview where the customer can complete the setup with PayPal. Upon completion, the provided `PaymentResultCallback` is called with the result of the payment.

#### Kotlin

```kotlin
class PayPalSetupActivity : AppCompatActivity() {

    // ...

    private val paymentLauncher: PaymentLauncher by lazy {
        val paymentConfiguration = PaymentConfiguration.getInstance(this)
        PaymentLauncher.create(
            activity = this,
            publishableKey = paymentConfiguration.publishableKey,
            stripeAccountId = paymentConfiguration.stripeAccountId,
            callback = ::onPaymentResult,
        )
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        // …
        startCheckout()
    }

    private fun startCheckout() {
        // Create a SetupIntent on your backend and return the client_secret here
        val setupIntentClientSecret = // …

        val payPalPayParams = PaymentMethodCreateParams.createPayPal()

        val confirmParams = ConfirmSetupIntentParams.create(
            paymentMethodCreateParams = payPalPayParams,
            clientSecret = setupIntentClientSecret,
            // Add a mandate ID or MandateDataParams…
        )

        paymentLauncher.confirm(confirmParams)
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        // Handle the setup result…
    }
}
```

## Monitor webhooks [Server-side]

Use a method such as [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the billing agreement was authorized successfully by your customer, instead of relying on your customer to return to the payment status page. When a customer successfully authorizes the billing agreement, the SetupIntent emits the [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. If a customer doesn’t successfully authorize the billing agreement, the SetupIntent will emit the [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) webhook event and returns to a status of `requires_payment_method`. When a customer revokes the billing agreement from their PayPal account, the [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) is emitted.

## Charge off-session payments with a saved PayPal payment method [Server-side]

When you’re ready to charge your customer off-session, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).

To find a `paypal` instrument to charge, [list](https://docs.stripe.com/api/payment_methods/list.md) the PaymentMethods associated with your Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer: "{{CUSTOMER_ID}}",
  type: "paypal",
});
```

When you have the Customer and PaymentMethod IDs, create a PaymentIntent with the amount and currency of the payment. Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during this payment attempt. This causes the PaymentIntent to throw an error if authentication is required.
- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the ID of the PaymentMethod and [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["paypal"],
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: true,
  confirm: true,
});
```

## User-initiated payment method cancellation [Server-side]

A customer can cancel the subscription (Billing Agreement) through their PayPal account. When they do so, Stripe emits a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) webhook. All subsequent PaymentIntents using the saved Payment Method will fail until you change to a Payment Method with active mandates. When payments fail for Subscriptions, the status changes to the Subscription status configured in your [automatic collection settings](https://docs.stripe.com/invoicing/automatic-collection.md). Notify the customer of failure and [charge them with a different payment method](https://docs.stripe.com/billing/subscriptions/overview.md#requires-payment-method).

## Optional: Set up future PayPal payments and capture a payment [Server-side]

It’s also possible to set up a PayPal Payment Method for future usage and also charge at the same time when creating a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md).

Set [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to `off_session` to indicate that you want to set up the payment method for future usage.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["paypal"],
  setup_future_usage: "off_session",
});
```

## Optional: Handle risk library integration for on-session payments manually [Server-side]

We recommend relying on Stripe.js to handle on-session payments with a saved PayPal payment method because it comes with a built-in [Fraudnet](https://developer.paypal.com/limited-release/fraudnet/) integration. However, you can also manually confirm PayPal PaymentIntents on your server by following these steps:

Integrate with PayPal’s risk libraries ([Fraudnet](https://developer.paypal.com/limited-release/fraudnet/) for web and [Magnes](https://developer.paypal.com/limited-release/magnes/) for mobile) to allow PayPal to collect risk data when the buyer is present in the payment session. This reduces fraud and can increase your payments conversion for on-session payments. You need the Client Metadata ID (also known as Risk Correlation ID) used to initialize the library when making the API call to Stripe.

After the library loads, you can create a PaymentIntent with the Client Metadata ID, amount, and currency of the payment:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["paypal"],
  payment_method_options: {
    paypal: {
      risk_correlation_id: "{{RISK_CORRELATION_ID}}",
    },
  },
  confirm: true,
  payment_method: "{{PAYMENT_METHOD_ID}}",
});
```

You’ll get a `paypal_risk_correlation_id_missing` message code if you fail to pass the [risk_correlation_id](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-paypal-risk_correlation_id) parameter when confirming an on-session payment.

## Optional: Remove a saved PayPal account [Server-side]

You can use the [detach](https://docs.stripe.com/api/payment_methods/detach.md) API to remove a customer’s saved PayPal account as a payment method. When you detach a PayPal payment method, it revokes the [mandate](https://docs.stripe.com/api/mandates.md) and also calls the PayPal API to cancel the associated PayPal billing agreement.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.detach(
  "{{PAYMENT_METHOD_ID}}",
);
```
