<!-- Source URL: https://docs.stripe.com/payments/bacs-debit/accept-a-payment -->
<!-- Fetched: 2026-05-02 -->

# Bacs Direct Debit payments

Accept Bacs Direct Debit payments from customers with a UK bank account.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/bacs-debit/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Stripe users in the UK can use [Checkout](https://docs.stripe.com/payments/checkout.md) in payment mode to accept Bacs Direct Debit payments.

A [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) represents the details of your customer’s intent to purchase. You create a Checkout Session when your customer wants to pay for something. After redirecting your customer to a Checkout Session, Stripe presents a payment form where your customer can complete their purchase. When your customer has completed a purchase, they’re redirected back to your site.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create products and prices

To use Checkout, you first need to create a *Product* (Products represent what your business sells—whether that's a good or a service) and a *Price* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions). Different physical goods or levels of service should be represented by products. Each product’s pricing is represented by one or more prices.

For example, you can create a T-shirt *product* that has two *prices* for different currencies, 20 GBP and 25 EUR. This allows you to change and add prices without needing to change the details of your underlying products. You can either create a product and price [through the API](https://docs.stripe.com/api/prices.md) or in the [Dashboard](https://dashboard.stripe.com/products).

If you determine your price at checkout (for example, the customer sets a donation amount) or you prefer not to create prices upfront, you can also create [ad-hoc prices](https://docs.stripe.com/payments/accept-a-payment.md?platform=web#redirect-customers) at Checkout Session creation using an existing product.

> If you have an existing Checkout integration that doesn’t use Prices, the Checkout API has changed since we introduced Prices. You can use this [migration guide](https://docs.stripe.com/payments/checkout/migrating-prices.md) to upgrade, or [keep your existing integration](https://support.stripe.com/questions/prices-api-and-existing-checkout-integrations).

#### Dashboard

> Products created in a sandbox can be copied to live mode so that you don’t need to re-create them. In the Product detail view in the Dashboard, click **Copy to live mode** in the upper right corner. You can only do this once for each product created in a sandbox. Subsequent updates to the test product aren’t reflected for the live product.

Make sure you’re in a sandbox, and define the items you want to sell. To create a new product and price:

- Go to the [Products](https://dashboard.stripe.com/test/products) section in the Dashboard
- Click **Add product**
- Select **One time** when setting the price

The product name, description, and image that you supply are displayed to customers in Checkout.

#### API

To create a [Product](https://docs.stripe.com/api/products.md) with the API, only a `name` is required. The product `name`, `description`, and `images` that you supply are displayed to customers on Checkout.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const product = await stripe.products.create({
  name: 'T-shirt',
});
```

Next, create a [Price](https://docs.stripe.com/api/prices.md) to define how much to charge for your product. This includes how much the product costs and what currency to use. Bacs Direct Debit payments must be in GBP.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const price = await stripe.prices.create({
  product: '{{PRODUCT_ID}}',
  unit_amount: 2000,
  currency: 'gbp',
});
```

## Create a Checkout Session [Client-side] [Server-side]

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

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

Create a Checkout Session with [line_items](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items). Line items represent a list of items the customer is purchasing.

When your customer successfully completes their payment, they’re redirected to the `success_url`, a page on your website that informs the customer that their payment details have been successfully collected and their payment is being processed.

When your customer clicks on your logo in a Checkout Session without completing a payment, Checkout redirects them back to your website that the customer viewed prior to redirecting to Checkout.

Checkout can accept a payment and save the payment method for future use. Payment methods saved this way can be used for future payments using a [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method). After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  payment_method_types: ['bacs_debit'],
  line_items: [
    {
      price: '{{PRICE_ID}}',
      quantity: 1,
    },
  ],
  mode: 'payment',
  customer: customer.id,
  payment_intent_data: {
    setup_future_usage: 'off_session',
  },
  success_url: 'https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
});

// 303 redirect to session.url
```

> The Bacs Direct Debit rules require that customers receive [debit notification emails](https://docs.stripe.com/payments/payment-methods/bacs-debit.md#debit-notifications) when payment details are initially collected and when their account is debitted. Stripe sends these emails for you by default.

Creating a Checkout Session returns a [Session ID](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-id). Make the Session ID available on your success page by including the `{CHECKOUT_SESSION_ID}` template variable in the `success_url` as in the above example.

> Don’t rely on the redirect to the `success_url` alone for detecting payment initiation, because:
>
> - Malicious users could directly access the `success_url` without paying and gain access to your goods or services.

- After a successful payment, customers might close their browser tab before they’re redirected to the `success_url`.

## Handle post-payment events [Server-side]

When your customer completes a payment, Stripe redirects them to the URL that you specified in the `success_url` parameter. Typically, this is a page on your website that informs your customer that their payment was successful.

However, Bacs Direct Debit is a delayed notification payment method, which means that funds aren’t immediately available. A Bacs Direct Debit payment typically takes 3 business days to make the funds available. Because of this, you’ll want to delay order *fulfillment* (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) until the funds are available. Once the payment succeeds, the underlying *PaymentIntent* (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) status changes from `processing` to `succeeded`.

The following Checkout events are sent when the payment status changes:

| Event Name                                                                                                                                   | Description                                                                                 | Next steps                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed)                             | The customer has successfully authorized the debit payment by submitting the Checkout form. | Wait for the payment to succeed or fail.                                    |
| [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) | The customer’s payment succeeded.                                                           | Fulfill the goods or services that the customer purchased.                  |
| [checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_failed)       | The customer’s payment was declined, or failed for some other reason.                       | Contact the customer through email and request that they place a new order. |

Your *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) code will need to handle all 3 of these Checkout events.

Each Checkout webhook payload includes the [Checkout Session object](https://docs.stripe.com/api/checkout/sessions.md), which contains information about the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentIntent* (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods).

The `checkout.session.completed` webhook is sent to your server before your customer is redirected. Your webhook acknowledgement (any `2xx` status code) triggers the customer’s redirect to the `success_url`. If Stripe doesn’t receive successful acknowledgement within 10 seconds of a successful payment, your customer is automatically redirected to the `success_url` page.

On your `success_url` page, show a success message to your customer, and let them know that fulfillment of the order takes a few days as the Bacs Direct Debit payment method isn’t instant.

When accepting instant payments (such as credit cards) in addition to delayed notification payments, update your webhook endpoint to handle both kinds of payments when receiving a `checkout.session.completed` event.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = 'whsec_...';

// Using Express
const app = require('express')();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require('body-parser');

// Match the raw body to content type application/json
app.post(
  '/webhook',
  bodyParser.raw({ type: 'application/json' }),
  (request, response) => {
    const sig = request.headers['stripe-signature'];

    let event;

    try {
      event = stripe.webhooks.constructEvent(request.body, sig, endpointSecret);
    } catch (err) {
      return response.status(400).send(`Webhook Error: ${err.message}`);
    }

    switch (event.type) {
      case 'checkout.session.completed': {
        const session = event.data.object;

        // Check if the order is paid (for example, from a card payment)
        stripe.paymentIntents.retrieve(
          session.payment_intent,
          (err, paymentIntent) => {
            if (err) {
              return console.error(err);
            }

            // A delayed notification payment will have the status 'processing'
            const orderPaid = paymentIntent.status === 'succeeded';

            // Save an order in your database, marked as 'awaiting payment'
            createOrder(session);

            if (orderPaid) {
              fulfillOrder(session);
            }
          },
        );
      }

      case 'checkout.session.async_payment_succeeded': {
        const session = event.data.object;

        // Fulfill the purchase...
        fulfillOrder(session);
      }

      case 'checkout.session.async_payment_failed': {
        const session = event.data.object;

        // Send an email to the customer asking them to retry their order
        emailCustomerAboutFailedPayment(session);
      }
    }

    // Return a response to acknowledge receipt of the event
    response.json({ received: true });
  },
);

app.listen(8000, () => console.log('Running on port 8000'));
```

You can get information about the customer and payment by retrieving the Customer or PaymentIntent objects referenced by the `customer`, `payment_intent` properties in the webhook payload.

### Testing webhooks locally

To test webhooks locally, you can use [Stripe CLI](https://docs.stripe.com/stripe-cli.md). Once you have it installed, you can forward events to your server:

```bash
stripe listen --forward-to localhost:4242/webhook
Ready! Your webhook signing secret is '{{WEBHOOK_SIGNING_SECRET}}' (^C to quit)
```

Learn more about [setting up webhooks](https://docs.stripe.com/webhooks.md).

## Test the integration

By this point you should have a basic Bacs Direct Debit integration that collects bank account details and accepts a payment.

There are several [test bank account numbers](https://docs.stripe.com/keys.md#test-live-modes) you can use in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) to make sure this integration is ready. You can also use the corresponding token to skip manually entering bank account details.

| Sort code | Account number | Token                                    | Description                                                                                                                                                                                                                                                  |
| --------- | -------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `108800`  | `00012345`     | `pm_bacsDebit_success`                   | The payment succeeds and the PaymentIntent transitions from `processing` to `succeeded`.                                                                                                                                                                     |
| `108800`  | `90012345`     | `pm_bacsDebit_successDelayed`            | The payment succeeds after three minutes and the PaymentIntent transitions from `processing` to `succeeded`.                                                                                                                                                 |
| `108800`  | `33333335`     | `pm_bacsDebit_debitNotAuthorized`        | The payment is accepted but then immediately fails with a `debit_not_authorized` failure code and the PaymentIntent transitions from `processing` to `requires_payment_method`. The Mandate becomes `inactive` and the PaymentMethod can’t be used again.    |
| `108800`  | `93333335`     | `pm_bacsDebit_debitNotAuthorizedDelayed` | The payment fails after three minutes with a `debit_not_authorized` failure code and the PaymentIntent transitions from `processing` to `requires_payment_method`. The Mandate becomes `inactive` and the PaymentMethod can’t be used again.                 |
| `108800`  | `22222227`     | `pm_bacsDebit_insufficientFunds`         | The payment fails with an `insufficient_funds` failure code and the PaymentIntent transitions from `processing` to `requires_payment_method`. The Mandate remains `active` and the PaymentMethod can be used again.                                          |
| `108800`  | `92222227`     | `pm_bacsDebit_insufficientFundsDelayed`  | The payment fails after three minutes with an `insufficient_funds` failure code and the PaymentIntent transitions from `processing` to `requires_payment_method`. The Mandate remains `active` and the PaymentMethod can be used again.                      |
| `108800`  | `55555559`     | `pm_bacsDebit_dispute`                   | The payment succeeds after three minutes and the PaymentIntent transitions from `processing` to `succeeded`, but a dispute is immediately created.                                                                                                           |
| `108800`  | `00033333`     | `pm_bacsDebit_mandateRefused`            | Payment Method creation succeeds, but the Mandate is refused by the customer’s bank and immediately transitions to `inactive`.                                                                                                                               |
| `108800`  | `00044444`     | —                                        | The request to set up Bacs Direct Debit fails immediately due to an invalid account number and the customer is prompted to update their information before submitting. Payment details aren’t collected, so no synthetic token corresponds to this scenario. |
| `108800`  | `34343434`     | `pm_bacsDebit_exceedsWeeklyLimit`        | The payment fails with a `charge_exceeds_source_limit` failure code due to the payment amount causing the account to exceed its weekly payment volume limit.                                                                                                 |
| `108800`  | `12121212`     | `pm_bacsDebit_exceedsTransactionLimit`   | The payment fails with a `charge_exceeds_transaction_limit` failure code due to the payment amount exceeding the account’s transaction volume limit.                                                                                                         |

You can test using any of the account numbers provided above. However, because Bacs Direct Debit payments take several days to process, use the test account numbers that operate on a three-minute delay to better simulate the behavior of live payments.

> By default, Stripe automatically sends [emails](https://docs.stripe.com/payments/payment-methods/bacs-debit.md#debit-notifications) to the customer when payment details are initially collected and each time a debit will be made on their account. These notifications aren’t sent in sandboxes.

## Payment failures

Payments can fail for a variety of reasons. The reason for a failure is available through [charge.failure_code](https://docs.stripe.com/api/charges/object.md#charge_object-failure_code). You can only retry payments with certain failure codes. If you can’t retry a payment, we recommend reaching out to the customer and asking them to pay again using a different bank account or a different payment method.

Below is a list of failure codes we currently send for Bacs Direct Debit. We might add more at any time, so in developing and maintaining your code, don’t assume that only these types exist.

| Failure code                | Description                                                                                                                                                                                 | Retryable |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `account_closed`            | The bank account has been closed.                                                                                                                                                           | No        |
| `bank_ownership_changed`    | The account has been transferred to a new Payment Service Provider (PSP). Check if you’ve been notified of the new PSP’s details. If not, you must collect a new mandate from the customer. | No        |
| `debit_not_authorized`      | The customer has notified their bank that this payment was unauthorized or there is no mandate held by the paying bank.                                                                     | No        |
| `generic_could_not_process` | This payment couldn’t be processed.                                                                                                                                                         | Yes       |
| `insufficient_funds`        | The customer’s account has insufficient funds to cover this payment.                                                                                                                        | Yes       |
| `invalid_account_number`    | The account number isn’t valid. This could mean it isn’t for a GBP account or that the account can’t process Direct Debit payments.                                                         | No        |

To retry a payment, [confirm the PaymentIntent](https://docs.stripe.com/api/payment_intents/confirm.md) again using the same *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs).

To ensure success, we recommend reaching out to the payer before retrying a payment.

## Optional: Configure customer debit date

You can control the date that Stripe debits a customer’s bank account using the [target date](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_method_options-bacs_debit-target_date). The target date must be at least three days in the future and no more than 15 days from the current date.

The target date schedules money to leave the customer’s account on the target date.

Target dates that meet one of the following criteria delay the debit until the next available business day:

- Target date falls on a weekend, a bank holiday, or other non-business day.
- Target date is fewer than three business days in the future.

This parameter operates on a best-effort basis. Each customer’s bank might process debits on different dates, depending on local bank holidays or other reasons.

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/bacs-debit/accept-a-payment?payment-ui=elements.

Accepting Bacs Direct Debit payments on your website consists of creating an object to track a payment, collecting payment method information and mandate acknowledgement, submitting the payment to Stripe for processing, and verifying your customer’s bank account.

Stripe uses this payment object, the [PaymentIntent](https://docs.stripe.com/payments/payment-intents.md), to track and handle all the states of the payment until the payment completes.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer [Server-side]

To reuse a bank account for future payments, it must be attached to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a `Customer` object when your customer creates an account with your business. Associating the ID of the `Customer` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later.

Create a new `Customer` or retrieve an existing `Customer` to associate with this payment. Include the following code on your server to create a new `Customer`:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create();
```

## Collect payment method details

> The Bacs Direct Debit scheme rules require that your customer accept a mandate in order for Stripe to debit their account. The [Payment Element](https://docs.stripe.com/payments/payment-element.md) collects this mandate when accepting the customer’s payment details, so you don’t need to take any action to comply with this requirement.

You’re ready to collect payment details on the client with the Payment Element. The Payment Element is a prebuilt UI component that simplifies collecting payment details for a variety of payment methods.

The Payment Element contains an iframe that securely sends payment information to Stripe over an HTTPS connection. Avoid placing the Payment Element within another iframe because some payment methods require redirecting to another page for payment confirmation.

The checkout page address must start with `https://` rather than `http://` for your integration to work. You can test your integration without using HTTPS, but remember to [enable it](https://docs.stripe.com/security/guide.md#tls) when you’re ready to accept live payments.

#### HTML + JS

### Set up Stripe.js

The Payment Element is automatically available as a feature of Stripe.js. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe with the following JavaScript on your checkout page:

```javascript
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('<<YOUR_PUBLISHABLE_KEY>>');
```

### Add the Payment Element to your checkout page

The Payment Element needs a place on your checkout page. Create an empty DOM node (container) with a unique ID in your payment form:

```html
<form id="payment-form">
  <div id="payment-element">
    <!-- Elements will create form elements here -->
  </div>
  <button id="submit">Submit</button>
  <div id="error-message">
    <!-- Display error message to your customers here -->
  </div>
</form>
```

#### Control payment methods from the Dashboard

After the form above loads, create an Elements instance with a `mode`, `amount`, and `currency`. These values determine which payment methods your customer sees. To provide a new payment method in your form, make sure you enable it in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

```javascript
const options = {
  mode: 'payment',
  amount: 1099,
  currency: 'gbp',
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout formconst elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: 'accordion' };
const paymentElement = elements.create('payment', paymentElementOptions);
paymentElement.mount('#payment-element');
```

#### List payment methods manually

To manually list the payment methods you want to be available, add each one to `paymentMethodTypes`.

Then, create an instance of the Payment Element and mount it to the container DOM node.

```javascript
const options = {
  mode: 'payment',
  amount: 1099,
  currency: 'gbp',
  paymentMethodTypes: ['bacs_debit'],
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout formconst elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: 'accordion' };
const paymentElement = elements.create('payment', paymentElementOptions);
paymentElement.mount('#payment-element');
```

#### React

### Set up Stripe.js

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry.

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

### Add and configure the Elements provider to your checkout page

To use the Payment Element component, wrap your checkout page component in an [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Call `loadStripe` with your publishable key, and pass the returned `Promise` to the `Elements` provider.

#### Control payment methods from the Dashboard

The `Elements` provider also accepts a `mode`, `amount`, and `currency`. These values determine which payment methods your customer sees. To provide a new payment method in your form, make sure you enable it in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import { Elements } from '@stripe/react-stripe-js';
import { loadStripe } from '@stripe/stripe-js';

import CheckoutForm from './CheckoutForm';

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe('<<YOUR_PUBLISHABLE_KEY>>');

function App() {
  const options = {
    mode: 'payment',
    amount: 1099,
    currency: 'gbp',
    // Fully customizable with appearance API.
    appearance: {
      /*...*/
    },
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm />
    </Elements>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
```

#### List payment methods manually

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import { Elements } from '@stripe/react-stripe-js';
import { loadStripe } from '@stripe/stripe-js';

import CheckoutForm from './CheckoutForm';

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe('<<YOUR_PUBLISHABLE_KEY>>');

function App() {
  const options = {
    mode: 'payment',
    amount: 1099,
    currency: 'gbp',
    paymentMethodTypes: ['bacs_debit'],
    // Fully customizable with appearance API.
    appearance: {
      /*...*/
    },
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm />
    </Elements>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
```

### Add the Payment Element component

Use the `PaymentElement` component to build your form.

```jsx
import React from 'react';
import { PaymentElement } from '@stripe/react-stripe-js';

const CheckoutForm = () => {
  return (
    <form>
      <PaymentElement />
      <button>Submit</button>
    </form>
  );
};

export default CheckoutForm;
```

You can customize the Payment Element to match the design of your site by passing the [appearance object](https://docs.stripe.com/elements/appearance-api.md) into `options` when creating the `Elements` provider.

### Collect addresses

By default, the Payment Element only collects the necessary billing address details. Some behavior, such as [calculating tax](https://docs.stripe.com/api/tax/calculations/create.md) or entering shipping details, requires your customer’s full address. You can:

- Use the [Address Element](https://docs.stripe.com/elements/address-element.md) to take advantage of autocomplete and localization features to collect your customer’s full address. This helps ensure the most accurate tax calculation.
- Collect address details using your own custom form.

## Create a PaymentIntent [Server-side]

> #### Run custom business logic immediately before payment confirmation
>
> Navigate to [step 5](https://docs.stripe.com/payments/finalize-payments-on-the-server.md?platform=web&type=payment#submit-payment) in the finalize payments guide to run your custom business logic immediately before payment confirmation. Otherwise, follow the steps below for a simpler integration, which uses `stripe.confirmPayment` on the client to both confirm the payment and handle any next actions.

#### Control payment methods from the Dashboard

When the customer submits your payment form, use a *PaymentIntent* (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) to facilitate the confirmation and payment process. Create a PaymentIntent on your server with an `amount` and `currency`. To prevent malicious customers from choosing their own prices, always decide how much to charge on the server-side (a trusted environment) and not the client.

A `PaymentIntent` includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). Return this value to your client for Stripe.js to use to securely complete the payment process.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
const express = require('express');
const app = express();

app.use(express.static('.'));

app.post('/create-intent', async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the customer's Account ID.
    customer_account: '{{CUSTOMER_ACCOUNT_ID}}',
    amount: 1099,
    currency: 'gbp',
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
const express = require('express');
const app = express();

app.use(express.static('.'));

app.post('/create-intent', async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the Customer ID.
    customer: customer.id,
    amount: 1099,
    currency: 'gbp',
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

#### List payment methods manually

When the customer submits your payment form, use a *PaymentIntent* (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) to facilitate the confirmation and payment process. Create a PaymentIntent on your server with an `amount`, `currency`, and one or more payment methods using `payment_method_types`. To prevent malicious customers from choosing their own prices, always decide how much to charge on the server-side (a trusted environment) and not the client.

Included on a PaymentIntent is a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). Return this value to your client for Stripe.js to use to securely complete the payment process.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
const express = require('express');
const app = express();

app.use(express.static('.'));

app.post('/create-intent', async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the customer's Account ID.
    customer_account: customer_account.id,
    amount: 1099,
    currency: 'gbp',
    payment_method_types: ['bacs_debit'],
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
const express = require('express');
const app = express();

app.use(express.static('.'));

app.post('/create-intent', async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the Customer ID.
    customer: customer.id,
    amount: 1099,
    currency: 'gbp',
    payment_method_types: ['bacs_debit'],
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

## Submit the payment to Stripe [Client-side]

Use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) to complete the payment using details from the Payment Element.

Provide a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe redirects the user after they complete the payment. Your user might be initially redirected to an intermediate site, such as a bank authorization page, before being redirected to the `return_url`. Card payments immediately redirect to the `return_url` when a payment is successful.

If you don’t want to redirect for card payments after payment completion, you can set [redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect) to `if_required`. This only redirects customers that check out with redirect-based payment methods.

#### HTML + JS

```javascript
const form = document.getElementById('payment-form');
const submitBtn = document.getElementById('submit');

const handleError = (error) => {
  const messageContainer = document.querySelector('#error-message');
  messageContainer.textContent = error.message;
  submitBtn.disabled = false;
};

form.addEventListener('submit', async (event) => {
  // We don't want to let default form submission happen here,
  // which would refresh the page.
  event.preventDefault();

  // Prevent multiple form submissions
  if (submitBtn.disabled) {
    return;
  }

  // Disable form submission while loading
  submitBtn.disabled = true;

  // Trigger form validation and wallet collection
  const { error: submitError } = await elements.submit();
  if (submitError) {
    handleError(submitError);
    return;
  }

  // Create the PaymentIntent and obtain clientSecret
  const res = await fetch('/create-intent', {
    method: 'POST',
  });

  const { client_secret: clientSecret } = await res.json();

  // Confirm the PaymentIntent using the details collected by the Payment Element
  const { error } = await stripe.confirmPayment({
    elements,
    clientSecret,
    confirmParams: {
      return_url: 'https://example.com/order/123/complete',
    },
  });

  if (error) {
    // This point is only reached if there's an immediate error when
    // confirming the payment. Show the error to your customer (for example, payment details incomplete)
    handleError(error);
  } else {
    // Your customer is redirected to your `return_url`. For some payment
    // methods like iDEAL, your customer is redirected to an intermediate
    // site first to authorize the payment, then redirected to the `return_url`.
  }
});
```

#### React

```jsx
import React, { useState } from 'react';
import {
  useStripe,
  useElements,
  PaymentElement,
} from '@stripe/react-stripe-js';

export default function CheckoutForm() {
  const stripe = useStripe();
  const elements = useElements();

  const [errorMessage, setErrorMessage] = useState();
  const [loading, setLoading] = useState(false);

  const handleError = (error) => {
    setLoading(false);
    setErrorMessage(error.message);
  };

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    setLoading(true);

    // Trigger form validation and wallet collection
    const { error: submitError } = await elements.submit();
    if (submitError) {
      handleError(submitError);
      return;
    }

    // Create the PaymentIntent and obtain clientSecret
    const res = await fetch('/create-intent', {
      method: 'POST',
    });

    const { client_secret: clientSecret } = await res.json();

    // Confirm the PaymentIntent using the details collected by the Payment Element
    const { error } = await stripe.confirmPayment({
      elements,
      clientSecret,
      confirmParams: {
        return_url: 'https://example.com/order/123/complete',
      },
    });

    if (error) {
      // This point is only reached if there's an immediate error when
      // confirming the payment. Show the error to your customer (for example, payment details incomplete)
      handleError(error);
    } else {
      // Your customer is redirected to your `return_url`. For some payment
      // methods like iDEAL, your customer is redirected to an intermediate
      // site first to authorize the payment, then redirected to the `return_url`.
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button type="submit" disabled={!stripe || loading}>
        Submit Payment
      </button>
      {errorMessage && <div>{errorMessage}</div>}
    </form>
  );
}
```

## Handle post-payment events

Bacs Direct Debit is a *delayed notification payment method* (A payment method that can't immediately return payment status when a customer attempts a transaction (for example, ACH debits). Businesses commonly hold an order in a pending state until payment is successful with these payment methods), so funds aren’t immediately available.

### Timelines

With Bacs Direct Debit, it can take several business days for funds to become available in your Stripe balance. The number of business days it takes for funds to become available is called the settlement timing. Payments are generally submitted on the same day that they’re created, but are processed on the following business day if they’re created on a non-business day or after the cutoff time.

You can access the `expected_debit_date` for Bacs Direct Debit under [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details) for [Charges](https://docs.stripe.com/api/charges/object.md). This is an estimated date of when the funds might be debited. This estimate isn’t guaranteed and the actual date might vary. This information is available in API responses and in [charge.updated](https://docs.stripe.com/api/events/types.md#event_types-charge.updated), [charge.succeeded](https://docs.stripe.com/api/events/types.md#event_types-charge.succeeded), and [charge.failed](https://docs.stripe.com/api/events/types.md#event_types-charge.failed) webhook events when the debit date can be determined.

It takes 4 business days to confirm the success or failure of a Bacs Direct Debit payment when a mandate is already in place and 7 business days when you must collect a new mandate.

In some cases, the bank might notify us of a payment failure after the payment has been marked as successful in your Stripe account. In this case the payment failure is identified as a dispute with the appropriate reason code.

The following table describes the settlement timings for Bacs Direct Debit payments that Stripe offers. `T+x` refers to `x` business days after submission, which might differ from the payment creation date.

| Settlement type     | Payment Success  | Funds Available  | Cutoff time         |
| ------------------- | ---------------- | ---------------- | ------------------- |
| Standard Settlement | T+3 at 21:00 UTC | T+4 at 00:00 UTC | 20:00 Europe/London |

### Set up webhooks

Stripe sends multiple events during the payment process and after the payment is complete. Use the [Dashboard webhook tool](https://dashboard.stripe.com/webhooks) or follow the [webhook guide](https://docs.stripe.com/webhooks/quickstart.md) to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

For Bacs Direct Debit you need to handle the [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event to confirm that the payment has succeeded. Stripe also recommends handling the [payment_intent.processing](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.processing), and [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) events.

To test webhooks locally, you can use [Stripe CLI](https://docs.stripe.com/stripe-cli.md). After you have it installed, you can forward events to your server:

```bash
stripe listen --forward-to localhost:4242/webhook
Ready! Your webhook signing secret is '{{WEBHOOK_SIGNING_SECRET}}' (^C to quit)
```

Learn more about [setting up webhooks](https://docs.stripe.com/webhooks.md).

## Test the integration

There are several [test bank account numbers](https://docs.stripe.com/keys.md#test-live-modes) you can use in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) to make sure this integration is ready. You can also use the corresponding token to skip manually entering bank account details.

| Sort code | Account number | Token                                    | Description                                                                                                                                                                                                                                                  |
| --------- | -------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `108800`  | `00012345`     | `pm_bacsDebit_success`                   | The payment succeeds and the PaymentIntent transitions from `processing` to `succeeded`.                                                                                                                                                                     |
| `108800`  | `90012345`     | `pm_bacsDebit_successDelayed`            | The payment succeeds after three minutes and the PaymentIntent transitions from `processing` to `succeeded`.                                                                                                                                                 |
| `108800`  | `33333335`     | `pm_bacsDebit_debitNotAuthorized`        | The payment is accepted but then immediately fails with a `debit_not_authorized` failure code and the PaymentIntent transitions from `processing` to `requires_payment_method`. The Mandate becomes `inactive` and the PaymentMethod can’t be used again.    |
| `108800`  | `93333335`     | `pm_bacsDebit_debitNotAuthorizedDelayed` | The payment fails after three minutes with a `debit_not_authorized` failure code and the PaymentIntent transitions from `processing` to `requires_payment_method`. The Mandate becomes `inactive` and the PaymentMethod can’t be used again.                 |
| `108800`  | `22222227`     | `pm_bacsDebit_insufficientFunds`         | The payment fails with an `insufficient_funds` failure code and the PaymentIntent transitions from `processing` to `requires_payment_method`. The Mandate remains `active` and the PaymentMethod can be used again.                                          |
| `108800`  | `92222227`     | `pm_bacsDebit_insufficientFundsDelayed`  | The payment fails after three minutes with an `insufficient_funds` failure code and the PaymentIntent transitions from `processing` to `requires_payment_method`. The Mandate remains `active` and the PaymentMethod can be used again.                      |
| `108800`  | `55555559`     | `pm_bacsDebit_dispute`                   | The payment succeeds after three minutes and the PaymentIntent transitions from `processing` to `succeeded`, but a dispute is immediately created.                                                                                                           |
| `108800`  | `00033333`     | `pm_bacsDebit_mandateRefused`            | Payment Method creation succeeds, but the Mandate is refused by the customer’s bank and immediately transitions to `inactive`.                                                                                                                               |
| `108800`  | `00044444`     | —                                        | The request to set up Bacs Direct Debit fails immediately due to an invalid account number and the customer is prompted to update their information before submitting. Payment details aren’t collected, so no synthetic token corresponds to this scenario. |
| `108800`  | `34343434`     | `pm_bacsDebit_exceedsWeeklyLimit`        | The payment fails with a `charge_exceeds_source_limit` failure code due to the payment amount causing the account to exceed its weekly payment volume limit.                                                                                                 |
| `108800`  | `12121212`     | `pm_bacsDebit_exceedsTransactionLimit`   | The payment fails with a `charge_exceeds_transaction_limit` failure code due to the payment amount exceeding the account’s transaction volume limit.                                                                                                         |

You can test using any of the account numbers provided above. However, because Bacs Direct Debit payments take several days to process, use the test account numbers that operate on a three-minute delay to better simulate the behavior of live payments.

> By default, Stripe automatically sends [emails](https://docs.stripe.com/payments/payment-methods/bacs-debit.md#debit-notifications) to the customer when payment details are initially collected and each time a debit will be made on their account. These notifications aren’t sent in sandboxes.

## Payment failures

Payments can fail for a variety of reasons. The reason for a failure is available through [charge.failure_code](https://docs.stripe.com/api/charges/object.md#charge_object-failure_code). Only payments with certain failure codes may be retried. If a payment can’t be retried, we recommend reaching out to the customer and asking them to pay again using a different bank account or a different payment method.

Below is a list of failure codes we currently send for Bacs Direct Debit. We may add more at any time, so in developing and maintaining your code, you shouldn’t assume that only these types exist.

| Failure code                | Description                                                                                                                                                                                 | Retryable |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `account_closed`            | The bank account has been closed.                                                                                                                                                           | No        |
| `bank_ownership_changed`    | The account has been transferred to a new Payment Service Provider (PSP). Check if you’ve been notified of the new PSP’s details. If not, you must collect a new mandate from the customer. | No        |
| `debit_not_authorized`      | The customer has notified their bank that this payment was unauthorized or there is no mandate held by the paying bank.                                                                     | No        |
| `generic_could_not_process` | This payment couldn’t be processed.                                                                                                                                                         | Yes       |
| `insufficient_funds`        | The customer’s account has insufficient funds to cover this payment.                                                                                                                        | Yes       |
| `invalid_account_number`    | The account number isn’t valid. This could mean it isn’t for a GBP account or that the account can’t process Direct Debit payments.                                                         | No        |

To retry a payment, [confirm the PaymentIntent](https://docs.stripe.com/api/payment_intents/confirm.md) again using the same *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs).

To ensure success, we recommend reaching out to the payer before retrying a payment.

## Optional: Configure customer debit date

You can control the date that Stripe debits a customer’s bank account using the [target date](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-bacs_debit-target_date). The target date must be at least three days in the future and no more than 15 days from the current date.

The target date schedules money to leave the customer’s account on the target date. You can [cancel a PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) created with a target date up to three business days before the configured date.

Target dates that meet one of the following criteria delay the debit until next available business day:

- Target date falls on a weekend, a bank holiday, or other non-business day.
- Target date is fewer than three business days in the future.

This parameter operates on a best-effort basis. Each customer’s bank might process debits on different dates, depending on local bank holidays or other reasons.

## Optional: Customize mandate references with a prefix

You can customize Bacs Direct Debit mandate references to simplify mandate identification. To do this, provide the optional `payment_method_options.bacs_debit.mandate_options.reference_prefix` value. We add the `reference_prefix` to the beginning of a unique sequence to ensure the entire reference remains unique.

The `reference_prefix` must meet these requirements:

- Maximum length: 12 characters
- Must begin with a number or an uppercase letter
- Allowed characters:
  - Uppercase letters
  - Numbers
  - Spaces
  - Special characters: `.`, `/`, `&`, `-`, `_`
- Can’t begin with `DDIC` or `STRIPE`

Include any desired delimiter in the prefix, as we don’t add one by default. We trim trailing spaces to a maximum of one space. With a valid prefix, the resulting reference is always 18 characters long.

#### Payment Intent

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  currency: 'gbp',
  amount: 100,
  payment_method_types: ['bacs_debit'],
  payment_method_options: {
    bacs_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

#### Setup Intent

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['bacs_debit'],
  payment_method_options: {
    bacs_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

#### Checkout Session in Payment Mode

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'payment',
  currency: 'gbp',
  line_items: [
    {
      price_data: {
        currency: 'gbp',
        product_data: {
          name: 'Llama',
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  payment_method_types: ['bacs_debit'],
  payment_method_options: {
    bacs_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

#### Checkout Session in Setup Mode

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'setup',
  payment_method_types: ['bacs_debit'],
  payment_method_options: {
    bacs_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

The generated reference looks like `EX4MPL3-19CNCI920C`.

| Error Code                                     | Message                                                                                                                                                                                                           |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `invalid_bacs_mandate_reference_prefix_format` | The `reference_prefix` must be at most 12 characters long and can only contain uppercase letters, numbers, spaces, or the special characters `/`, `_`, `-`, `&`, and `.`. It can’t begin with `DDIC` or `STRIPE`. |

## See also

- [PaymentIntent webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks)
- [Manage mandates](https://docs.stripe.com/payments/payment-methods/bacs-debit.md#mandates)
