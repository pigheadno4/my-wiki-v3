<!-- Source URL: https://docs.stripe.com/payments/advanced/dashboard-payment-methods -->
<!-- Fetched: 2026-04-21 -->

# Migrate payment methods to the Dashboard

Learn how to turn on payment methods for your Checkout Session in the Dashboard.

# Checkout Sessions API

> This is a Checkout Sessions API for when payment-ui is embedded-components. View the full page at https://docs.stripe.com/payments/advanced/dashboard-payment-methods?payment-ui=embedded-components.

You can update your integration to use your payment method preferences from the Dashboard. This allows Stripe to display all compatible payment methods to your customers during checkout, depending on the chosen currency, location, or any payment method restrictions, such as maximum transaction amounts.

The checkout page shows payment methods known to increase conversion for your customer’s location, and hides other payment methods in an overflow menu. Customers can still choose from the payment methods in the overflow menu.

## Update your integration

For existing Stripe Checkout integrations, you must remove the `payment_method_types` parameter to migrate payment methods preferences to the Dashboard. Doing so allows some payment methods to turn on automatically, including cards and wallets. The `currency` parameter restricts the payment methods your customers see in the Checkout Session.

> When you upgrade your integration, non-default payment methods (such as bank redirects) are initially disabled. You must enable any payment methods you added to your Checkout integration from the payment methods settings page in the Dashboard.

#### Node.js

```javascript
const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "eur",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  return_url: "https://example.com/return",
  ui_mode: "elements",
});
```

## View available payment methods in the Dashboard

You can view the payment methods that you currently accept from the [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard. The list includes payment methods that Stripe enables by default, such as cards.

You can also enable or disable individual payment methods, such as Apple Pay or Google Pay. With the Checkout Sessions API, Stripe evaluates the currency and any restrictions, then dynamically presents the supported payment methods to the customer.

For example, Apple Pay is enabled and Google Pay is disabled, by default. In some cases, Stripe might not show these payment methods, even if you enabled them. Stripe doesn’t show Google Pay if you [enable automatic tax](https://docs.stripe.com/tax/checkout.md) without collecting a shipping address.

To see how Stripe displays your payment methods to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

## Add or remove payment methods in your integration

Enable payment methods for your integration from the [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard. You can select **Turn on** to enable some payment methods. For payment methods that require additional steps, select **Set up** or **Review terms**.

Learn about which payment methods are right for your business from our [payment methods guide](https://stripe.com/payments/payment-methods-guide).

## (Recommended) Handle delayed notification payment methods

The payment method you integrate might have a delayed payment confirmation. If you set up _webhooks_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to [automatically fulfill](https://docs.stripe.com/checkout/fulfillment.md#create-payment-event-handler) orders, you might need to update your Checkout integration when you add your first payment method that has delayed notifications.

> This step is only required if you plan to use any of the following payment methods: [Bacs Direct Debit](https://docs.stripe.com/payments/bacs-debit/accept-a-payment.md), [Bank transfers](https://docs.stripe.com/payments/bank-transfers/accept-a-payment.md), [Boleto](https://docs.stripe.com/payments/boleto/accept-a-payment.md), [Canadian pre-authorized debits](https://docs.stripe.com/payments/acss-debit/accept-a-payment.md), [Konbini](https://docs.stripe.com/payments/konbini/accept-a-payment.md), [OXXO](https://docs.stripe.com/payments/oxxo/accept-a-payment.md), [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank/accept-a-payment.md), [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit/accept-a-payment.md), or [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md).

When receiving payments with a delayed notification payment method, funds aren’t immediately available. It can take multiple days for funds to process so you should delay order _fulfillment_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) until the funds are available in your account. After the payment succeeds, the underlying _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) status changes from `processing` to `succeeded`.

You’ll need to handle the following Checkout events:

| Event Name                                                                                                                                   | Description                                                                                 | Next steps                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed)                             | The customer has successfully authorized the debit payment by submitting the Checkout form. | Wait for the payment to succeed or fail.                                    |
| [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) | The customer’s payment succeeded.                                                           | Fulfill the purchased goods or services.                                    |
| [checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_failed)       | The payment was declined, or failed for some other reason.                                  | Contact the customer through email and request that they place a new order. |

These events all include the [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) object.

Update your event handler to fulfill the order:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = "whsec_...";

// Using Express
const app = require("express")();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require("body-parser");

const fulfillOrder = (session) => {
  // TODO: fill me in
  console.log("Fulfilling order", session);
};
const createOrder = (session) => {
  // TODO: fill me in
  console.log("Creating order", session);
};

const emailCustomerAboutFailedPayment = (session) => {
  // TODO: fill me in
  console.log("Emailing customer", session);
};

app.post(
  "/webhook",
  bodyParser.raw({ type: "application/json" }),
  (request, response) => {
    const payload = request.body;
    const sig = request.headers["stripe-signature"];

    let event;

    try {
      event = stripe.webhooks.constructEvent(payload, sig, endpointSecret);
    } catch (err) {
      return response.status(400).send(`Webhook Error: ${err.message}`);
    }
    switch (event.type) {
      case "checkout.session.completed": {
        const session = event.data.object;
        // Save an order in your database, marked as 'awaiting payment'
        createOrder(session);

        // Check if the order is paid (for example, from a card payment)
        //
        // A delayed notification payment will have an `unpaid` status, as
        // you're still waiting for funds to be transferred from the customer's
        // account.
        if (session.payment_status === "paid") {
          fulfillOrder(session);
        }

        break;
      }

      case "checkout.session.async_payment_succeeded": {
        const session = event.data.object;

        // Fulfill the purchase...
        fulfillOrder(session);

        break;
      }

      case "checkout.session.async_payment_failed": {
        const session = event.data.object;

        // Send an email to the customer asking them to retry their order
        emailCustomerAboutFailedPayment(session);

        break;
      }
    }

    response.status(200).end();
  },
);

app.listen(4242, () => console.log("Running on port 4242"));
```

### Testing

Ensure that `stripe listen` is still running. Go through Checkout as a test user, like you did in the prior steps. Your event handler should receive a `checkout.session.completed` event, and you should have successfully handled it.

Now that you’ve completed these steps, you’re ready to go live in production.

## Test your integration

#### Cards

| Card number         | Scenario                                                                                                                                                                                                                                                                                      | How to test                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 4242424242424242    | The card payment succeeds and doesn’t require authentication.                                                                                                                                                                                                                                 | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000002500003155    | The card payment requires _authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000000000009995    | The card is declined with a decline code like `insufficient_funds`.                                                                                                                                                                                                                           | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 6205500000000000004 | The UnionPay card has a variable length of 13-19 digits.                                                                                                                                                                                                                                      | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |

#### Wallets

| Payment method | Scenario                                                                                                                                                                     | How to test                                                                                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Alipay         | Your customer successfully pays with a redirect-based and [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. | Choose any redirect-based payment method, fill out the required details, and confirm the payment. Then click **Complete test payment** on the redirect page. |

#### Bank redirects

| Payment method                         | Scenario                                                                                                                                                                                        | How to test                                                                                                                                                                                             |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BECS Direct Debit                      | Your customer successfully pays with BECS Direct Debit.                                                                                                                                         | Fill out the form using the account number `900123456` and BSB `000000`. The confirmed PaymentIntent initially transitions to `processing`, then transitions to the `succeeded` status 3 minutes later. |
| BECS Direct Debit                      | Your customer’s payment fails with an `account_closed` error code.                                                                                                                              | Fill out the form using the account number `111111113` and BSB `000000`.                                                                                                                                |
| Bancontact, EPS, iDEAL, and Przelewy24 | Your customer fails to authenticate on the redirect page for a redirect-based and immediate notification payment method.                                                                        | Choose any redirect-based payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page.                                                |
| Pay by Bank                            | Your customer successfully pays with a redirect-based and [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method.                      | Choose the payment method, fill out the required details, and confirm the payment. Then click **Complete test payment** on the redirect page.                                                           |
| Pay by Bank                            | Your customer fails to authenticate on the redirect page for a redirect-based and delayed notification payment method.                                                                          | Choose the payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page.                                                               |
| BLIK                                   | BLIK payments fail in a variety of ways—immediate failures (for example, the code is expired or invalid), delayed errors (the bank declines) or timeouts (the customer didn’t respond in time). | Use email patterns to [simulate the different failures.](https://docs.stripe.com/payments/blik/accept-a-payment.md#simulate-failures)                                                                   |

#### Bank debits

| Payment method    | Scenario                                                                                          | How to test                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SEPA Direct Debit | Your customer successfully pays with SEPA Direct Debit.                                           | Fill out the form using the account number `AT321904300235473204`. The confirmed PaymentIntent initially transitions to processing, then transitions to the succeeded status three minutes later. |
| SEPA Direct Debit | Your customer’s payment intent status transitions from `processing` to `requires_payment_method`. | Fill out the form using the account number `AT861904300235473202`.                                                                                                                                |

#### Vouchers

| Payment method | Scenario                                          | How to test                                                                                            |
| -------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Boleto, OXXO   | Your customer pays with a Boleto or OXXO voucher. | Select Boleto or OXXO as the payment method and submit the payment. Close the dialog after it appears. |

See [Testing](https://docs.stripe.com/testing.md) for additional information to test your integration.

# Payment Intents API

> This is a Payment Intents API for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/advanced/dashboard-payment-methods?payment-ui=elements.

You can update your integration to use your payment method preferences from the Dashboard. This allows Stripe to display all compatible payment methods to your customers when using Elements, depending on the chosen currency, location, or any payment method restrictions, such as maximum transaction amounts.

Elements shows payment methods known to increase conversion for your customer’s location, and hides other payment methods in an overflow menu. Customers can still choose from the payment methods in the overflow menu.

## Update your integration

For existing Payment Intents integrations, you must remove the `payment_method_types` parameter to migrate payment methods preferences to the Dashboard. Doing so allows some payment methods to turn on automatically, including cards and wallets. The `currency` parameter restricts the payment methods your customers see in Elements.

> When you upgrade your integration, non-default payment methods (such as bank redirects) are initially disabled. You must enable any payment methods you added to your Payment Intents integration from the payment methods settings page in the Dashboard.

#### Node.js

```javascript
const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,
  currency: "eur",
  metadata: {
    order_id: "12345",
  },
});
```

## View available payment methods in the Dashboard

You can view the payment methods that you currently accept from the [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard. The list includes payment methods that Stripe enables by default, such as cards.

You can also enable or disable individual payment methods, such as Apple Pay or Google Pay. With the Payment Intents API, Stripe evaluates the currency and any restrictions, then dynamically presents the supported payment methods to the customer.

For example, Apple Pay is enabled and Google Pay is disabled, by default. In some cases, Stripe might not show these payment methods, even if you enabled them. Stripe doesn’t show Google Pay if you [enable automatic tax](https://docs.stripe.com/tax/checkout.md) without collecting a shipping address.

To see how Stripe displays your payment methods to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

## Add or remove payment methods in your integration

Enable payment methods for your integration from the [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard. You can select **Turn on** to enable some payment methods. For payment methods that require additional steps, select **Set up** or **Review terms**.

Learn about which payment methods are right for your business from our [payment methods guide](https://stripe.com/payments/payment-methods-guide).

## (Recommended) Handle delayed notification payment methods

The payment method you integrate might have a delayed payment confirmation. If you set up _webhooks_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to [automatically fulfill](https://docs.stripe.com/webhooks/handling-payment-events.md) orders, you might need to update your Payment Intents integration when you add your first payment method that has delayed notifications.

Listen for the `payment_intent.succeeded` event to handle successful payments. For payment methods with delayed notifications, also listen for `payment_intent.payment_failed` to handle failed payments that might occur after the initial confirmation.

```javascript
// Handle the event
switch (event.type) {
  case "payment_intent.succeeded":
    const paymentIntent = event.data.object;
    // Fulfill the order
    console.log("PaymentIntent was successful!");
    break;
  case "payment_intent.payment_failed":
    const failedPaymentIntent = event.data.object;
    // Handle the failed payment
    console.log(
      "PaymentIntent failed:",
      failedPaymentIntent.last_payment_error?.message,
    );
    break;
  default:
    console.log(`Unhandled event type ${event.type}`);
}
```

## Test your integration

#### Cards

| Card number         | Scenario                                                                                                                                                                                                                                                                                      | How to test                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 4242424242424242    | The card payment succeeds and doesn’t require authentication.                                                                                                                                                                                                                                 | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000002500003155    | The card payment requires _authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase). | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 4000000000009995    | The card is declined with a decline code like `insufficient_funds`.                                                                                                                                                                                                                           | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |
| 6205500000000000004 | The UnionPay card has a variable length of 13-19 digits.                                                                                                                                                                                                                                      | Fill out the credit card form using the credit card number with any expiration, CVC, and postal code. |

#### Wallets

| Payment method | Scenario                                                                                                                                                                     | How to test                                                                                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Alipay         | Your customer successfully pays with a redirect-based and [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. | Choose any redirect-based payment method, fill out the required details, and confirm the payment. Then click **Complete test payment** on the redirect page. |

#### Bank redirects

| Payment method                         | Scenario                                                                                                                                                                                        | How to test                                                                                                                                                                                             |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BECS Direct Debit                      | Your customer successfully pays with BECS Direct Debit.                                                                                                                                         | Fill out the form using the account number `900123456` and BSB `000000`. The confirmed PaymentIntent initially transitions to `processing`, then transitions to the `succeeded` status 3 minutes later. |
| BECS Direct Debit                      | Your customer’s payment fails with an `account_closed` error code.                                                                                                                              | Fill out the form using the account number `111111113` and BSB `000000`.                                                                                                                                |
| Bancontact, EPS, iDEAL, and Przelewy24 | Your customer fails to authenticate on the redirect page for a redirect-based and immediate notification payment method.                                                                        | Choose any redirect-based payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page.                                                |
| Pay by Bank                            | Your customer successfully pays with a redirect-based and [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method.                      | Choose the payment method, fill out the required details, and confirm the payment. Then click **Complete test payment** on the redirect page.                                                           |
| Pay by Bank                            | Your customer fails to authenticate on the redirect page for a redirect-based and delayed notification payment method.                                                                          | Choose the payment method, fill out the required details, and confirm the payment. Then click **Fail test payment** on the redirect page.                                                               |
| BLIK                                   | BLIK payments fail in a variety of ways—immediate failures (for example, the code is expired or invalid), delayed errors (the bank declines) or timeouts (the customer didn’t respond in time). | Use email patterns to [simulate the different failures.](https://docs.stripe.com/payments/blik/accept-a-payment.md#simulate-failures)                                                                   |

#### Bank debits

| Payment method    | Scenario                                                                                          | How to test                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SEPA Direct Debit | Your customer successfully pays with SEPA Direct Debit.                                           | Fill out the form using the account number `AT321904300235473204`. The confirmed PaymentIntent initially transitions to processing, then transitions to the succeeded status three minutes later. |
| SEPA Direct Debit | Your customer’s payment intent status transitions from `processing` to `requires_payment_method`. | Fill out the form using the account number `AT861904300235473202`.                                                                                                                                |

#### Vouchers

| Payment method | Scenario                                          | How to test                                                                                            |
| -------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Boleto, OXXO   | Your customer pays with a Boleto or OXXO voucher. | Select Boleto or OXXO as the payment method and submit the payment. Close the dialog after it appears. |

See [Testing](https://docs.stripe.com/testing.md) for additional information to test your integration.
