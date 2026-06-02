<!-- Source URL: https://docs.stripe.com/payments/bank-transfers/accept-a-payment -->
<!-- Fetched: 2026-05-05 -->

# Accept a bank transfer

Use the Payment Intents API to accept bank transfer payments.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

The first time you accept a bank transfer payment from a customer, Stripe generates a virtual bank account for them, which you can then share with them directly. All future bank transfer payments from this customer get sent to this bank account. In some countries, Stripe also provides you with a unique transfer reference number that your customer should include with each transfer to make it easier to match the transfer against outstanding payments. Some countries have limits on the number of virtual bank account numbers that you can create for free.

You can find an overview of the common steps when accepting a bank transfer payment in the following sequence diagram:

#### With Invoices

Common steps when accepting a bank transfer payment (See full diagram at https://docs.stripe.com/payments/bank-transfers/accept-a-payment)

#### Without Invoices

![Without invoices payment flow diagram 1](assets/stripe-bank-transfers-without-invoices-diagram-1.svg)

## Handling underpayments and overpayments

With bank transfer payments, it’s possible that the customer sends you more or less than the expected payment amount. If the customer sends too little, Stripe partially funds an open Payment Intent. Invoices won’t be partially funded and remain open until incoming funds cover the full invoice amount.

If the customer sends more than the expected amount, Stripe attempts to reconcile the incoming funds against an open payment and keep the remaining excess amount in the customer balance. Learn more about [how Stripe handles reconciliation](https://docs.stripe.com/payments/customer-balance/reconciliation.md).

#### With Invoices

When a customer underpays:
A customer has sent a bank transfer for less than the expected amount (See full diagram at https://docs.stripe.com/payments/bank-transfers/accept-a-payment)
When a customer overpays:
A customer has sent a bank transfer for more than the expected amount (See full diagram at https://docs.stripe.com/payments/bank-transfers/accept-a-payment)

#### Without Invoices

![Without invoices underpayment flow diagram](assets/stripe-bank-transfers-without-invoices-diagram-2.svg)
![Without invoices overpayment flow diagram](assets/stripe-bank-transfers-without-invoices-diagram-3.svg)

## Handling multiple open payments or invoices

You might have multiple open payments or invoices which can be paid with a bank transfer. In the default setup, Stripe attempts to [automatically reconcile](https://docs.stripe.com/payments/customer-balance/reconciliation.md) the bank transfer by using information like the transfer’s reference code or the amount transferred.

You can disable automatic reconciliation and [manually reconcile](https://docs.stripe.com/payments/customer-balance/reconciliation.md#cash-manual-reconciliation) payments and invoices yourself. You can override the automatic reconciliation behavior on a per-customer basis by setting [reconciliation mode](https://docs.stripe.com/api/customers/create.md#create_customer-cash_balance-settings-reconciliation_mode) to manual.

> If your integration uses invoices, see [Send an invoice with bank transfer instructions](https://docs.stripe.com/invoicing/bank-transfer.md).

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=elements.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer [Server-side]

You must associate a [Customer](https://docs.stripe.com/api/customers.md) object to reconcile each bank transfer payment. If you have an existing Customer object, you can skip this step. Otherwise, create a new Customer object.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage. Create a PaymentIntent on the server, specifying the amount and currency you want to collect. You must also populate the [customer parameter](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) of the PaymentIntent creation request. Bank transfers aren’t available on PaymentIntents without a customer.

#### Manage payment methods from the Dashboard

Before creating a Payment Intent, make sure to turn **Bank transfer** on in the [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) page of your Dashboard.

> With [Dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md), Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

#### US

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  customer: "{{CUSTOMER_ID}}",
  currency: "usd",
  automatic_payment_methods: {
    enabled: true,
  },
});
```

#### UK

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  customer: "{{CUSTOMER_ID}}",
  currency: "gbp",
  automatic_payment_methods: {
    enabled: true,
  },
});
```

#### EU

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  customer: "{{CUSTOMER_ID}}",
  currency: "eur",
  automatic_payment_methods: {
    enabled: true,
  },
});
```

To localize the IBAN displayed to the customer you can configure the country of the Customer by setting the [`address.country`](https://docs.stripe.com/api/customers/object.md#customer_object-address-country) property or by [editing the Customer in the Dashboard](https://docs.stripe.com/invoicing/customer.md#edit-a-customer).

We support IBAN localization for :

- If you haven’t configured a country for your Customer, or if their country doesn’t support IBAN localization, we fall back to the country of your Stripe account.
- If IBAN localization isn’t supported for the country of your Stripe account, we fall back to `IE`.

> Creating new localized virtual bank account numbers is currently unavailable for Spain (ES). Use any of the other EU VBAN countries instead.

#### JP

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 19000,
  customer: "{{CUSTOMER_ID}}",
  currency: "jpy",
  automatic_payment_methods: {
    enabled: true,
  },
  return_url: "https://example.com/return_url",
});
```

#### MX

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  customer: "{{CUSTOMER_ID}}",
  currency: "mxn",
  automatic_payment_methods: {
    enabled: true,
  },
  return_url: "https://example.com/return_url",
});
```

In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.

If the customer already has a balance high enough to cover the payment amount, the PaymentIntent immediately succeeds with a `succeeded` status. Customers can accrue a balance when they accidentally overpay for a transaction—a common occurrence with bank transfers. You must [reconcile customer balances within a certain period based on your location](https://docs.stripe.com/payments/customer-balance/reconciliation.md).

#### List payment methods manually

To manually specify payment methods with the API, add `customer_balance` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your PaymentIntent. Specify the [id](https://docs.stripe.com/api/customers/object.md#customer_object-id) of the Customer.

#### US

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["customer_balance"],
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "us_bank_transfer",
      },
    },
  },
});
```

If the customer already has a balance high enough to cover the payment amount, the PaymentIntent immediately succeeds with a `succeeded` status. Customers can accrue a balance when they accidentally overpay for a transaction—a common occurrence with bank transfers. You must [reconcile customer balances within a certain period based on your location](https://docs.stripe.com/payments/customer-balance/reconciliation.md).

- Use `bank_transfer` as the [funding_type](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-funding_type) to specify what to do when the customer doesn’t have enough balance to cover the payment amount.
- Use `us_bank_transfer` as the [bank_transfer[type]](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-bank_transfer-type) to specify the bank transfer types that can be used to fund the payment.

#### UK

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "gbp",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["customer_balance"],
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "gb_bank_transfer",
      },
    },
  },
});
```

If the customer already has a balance high enough to cover the payment amount, the PaymentIntent immediately succeeds with a `succeeded` status. Customers can accrue a balance when they accidentally overpay for a transaction—a common occurrence with bank transfers. You must [reconcile customer balances within a certain period based on your location](https://docs.stripe.com/payments/customer-balance/reconciliation.md).

- Use `bank_transfer` as the [funding_type](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-funding_type) to specify what to do when the customer doesn’t have enough balance to cover the payment amount.
- Use `gb_bank_transfer` as the [bank_transfer[type]](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-bank_transfer-type) to specify the bank transfer types that can be used to fund the payment.

#### EU

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["customer_balance"],
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "eu_bank_transfer",
        eu_bank_transfer: {
          country: "FR",
        },
      },
    },
  },
});
```

If the customer already has a balance high enough to cover the payment amount, the PaymentIntent immediately succeeds with a `succeeded` status. Customers can accrue a balance when they accidentally overpay for a transaction—a common occurrence with bank transfers. You must [reconcile customer balances within a certain period based on your location](https://docs.stripe.com/payments/customer-balance/reconciliation.md).

- Use `bank_transfer` as the [funding_type](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-funding_type) to specify what to do when the customer doesn’t have enough balance to cover the payment amount.
- Use `eu_bank_transfer` as the [bank_transfer[type]](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-bank_transfer-type) to specify the bank transfer types that can be used to fund the payment.
- Set [payment_method_options[customer_balance][bank_transfer][eu_bank_transfer][country]](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-bank_transfer-eu_bank_account-country) to one of . The IBAN displayed to the customer is localized to the chosen country.

> Creating new localized virtual bank account numbers is currently unavailable for Spain (ES). Use any of the other EU VBAN countries instead.

#### JP

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 19000,
  currency: "jpy",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["customer_balance"],
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "jp_bank_transfer",
      },
    },
  },
});
```

If the customer already has a balance high enough to cover the payment amount, the PaymentIntent immediately succeeds with a `succeeded` status. Customers can accrue a balance when they accidentally overpay for a transaction—a common occurrence with bank transfers. You must [reconcile customer balances within a certain period based on your location](https://docs.stripe.com/payments/customer-balance/reconciliation.md).

- Use `bank_transfer` as the [funding_type](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-funding_type) to specify what to do when the customer doesn’t have enough balance to cover the payment amount.
- Use `jp_bank_transfer` as the [bank_transfer[type]](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-bank_transfer-type) to specify the bank transfer types that can be used to fund the payment.

#### MX

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "mxn",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["customer_balance"],
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "mx_bank_transfer",
      },
    },
  },
});
```

If the customer already has a balance high enough to cover the payment amount, the PaymentIntent immediately succeeds with a `succeeded` status. Customers can accrue a balance when they accidentally overpay for a transaction—a common occurrence with bank transfers. You must [reconcile customer balances within a certain period based on your location](https://docs.stripe.com/payments/customer-balance/reconciliation.md).

- Use `bank_transfer` as the [funding_type](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-funding_type) to specify what to do when the customer doesn’t have enough balance to cover the payment amount.
- Use `mx_bank_transfer` as the [bank_transfer[type]](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-bank_transfer-type) to specify the bank transfer types that can be used to fund the payment.

> Always specify the `payment_method_types` when creating a payment. You can’t use `customer_balance` for [future payments](https://docs.stripe.com/payments/save-and-reuse.md).

## Collect payment details [Client-side]

Collect payment details on the client with the [Payment Element](https://docs.stripe.com/payments/payment-element.md). The Payment Element is a prebuilt UI component that simplifies collecting payment details for a variety of payment methods.

The Payment Element contains an iframe that securely sends payment information to Stripe over an HTTPS connection. Avoid placing the Payment Element within another iframe because some payment methods require redirecting to another page for payment confirmation.

If you choose to use an iframe and want to accept Apple Pay or Google Pay, the iframe must have the [allow](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-allowpaymentrequest) attribute set to equal `"payment *"`.

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
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

### Add the Payment Element to your payment page

The Payment Element needs a place to live on your payment page. Create an empty DOM node (container) with a unique ID in your payment form:

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

When the previous form loads, create an instance of the Payment Element and mount it to the container DOM node. Pass the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) from the previous step into `options` when you create the [Elements](https://docs.stripe.com/js/elements_object/create) instance:

Handle the client secret carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

```javascript
const options = {
  clientSecret: "{{CLIENT_SECRET}}",
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout form, passing the client secret obtained in a previous stepconst elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: "accordion" };
const paymentElement = elements.create("payment", paymentElementOptions);
paymentElement.mount("#payment-element");
```

#### React

### Set up Stripe.js

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry:

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

### Add and configure the Elements provider to your payment page

To use the Payment Element component, wrap your checkout page component in an [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Call `loadStripe` with your publishable key, and pass the returned `Promise` to the `Elements` provider. Also pass the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) from the previous step as `options` to the `Elements` provider.

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";

import CheckoutForm from "./CheckoutForm";

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

function App() {
  const options = {
    // passing the client secret obtained in step 3
    clientSecret: "{{CLIENT_SECRET}}",
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

ReactDOM.render(<App />, document.getElementById("root"));
```

### Add the Payment Element component

Use the `PaymentElement` component to build your form:

```jsx
import React from "react";
import { PaymentElement } from "@stripe/react-stripe-js";

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

Stripe Elements is a collection of drop-in UI components. To further customize your form or collect different customer information, browse the [Elements docs](https://docs.stripe.com/payments/elements.md).

The Payment Element renders a dynamic form that allows your customer to pick a payment method. For each payment method, the form automatically asks the customer to fill in all necessary payment details.

### Customize appearance

Customize the Payment Element to match the design of your site by passing the [appearance object](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-appearance) into `options` when creating the `Elements` provider.

### Collect addresses

By default, the Payment Element only collects the necessary billing address details. Some behavior, such as [calculating tax](https://docs.stripe.com/api/tax/calculations/create.md) or entering shipping details, requires your customer’s full address. You can:

- Use the [Address Element](https://docs.stripe.com/elements/address-element.md) to take advantage of autocomplete and localization features to collect your customer’s full address. This helps ensure the most accurate tax calculation.
- Collect address details using your own custom form.

Upon confirmation, Stripe automatically opens a modal to display the bank transfer details to your customer.

## Submit payment to Stripe [Client-side]

Use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) to complete the payment using details from the Payment Element. Provide a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe should redirect the user after they complete the payment. Your user may be first redirected to an intermediate site, like a bank authorization page, before being redirected to the `return_url`. Card payments immediately redirect to the `return_url` when a payment is successful.

If you don’t want to redirect for card payments after payment completion, you can set [redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect) to `if_required`. This only redirects customers that check out with redirect-based payment methods.

#### HTML + JS

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const { error } = await stripe.confirmPayment({
    //`Elements` instance that was used to create the Payment Element
    elements,
    confirmParams: {
      return_url: "https://example.com/order/123/complete",
    },
  });

  if (error) {
    // This point will only be reached if there is an immediate error when
    // confirming the payment. Show error to your customer (for example, payment
    // details incomplete)
    const messageContainer = document.querySelector("#error-message");
    messageContainer.textContent = error.message;
  } else {
    // Your customer will be redirected to your `return_url`. For some payment
    // methods like iDEAL, your customer will be redirected to an intermediate
    // site first to authorize the payment, then redirected to the `return_url`.
  }
});
```

#### React

To call [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) from your payment form component, use the [useStripe](https://docs.stripe.com/sdks/stripejs-react.md#usestripe-hook) and [useElements](https://docs.stripe.com/sdks/stripejs-react.md#useelements-hook) hooks.

If you prefer traditional class components over hooks, you can instead use an [ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react.md#elements-consumer).

```jsx
import React, { useState } from "react";
import {
  useStripe,
  useElements,
  PaymentElement,
} from "@stripe/react-stripe-js";

const CheckoutForm = () => {
  const stripe = useStripe();
  const elements = useElements();

  const [errorMessage, setErrorMessage] = useState(null);

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }
    const { error } = await stripe.confirmPayment({
      //`Elements` instance that was used to create the Payment Element
      elements,
      confirmParams: {
        return_url: "https://example.com/order/123/complete",
      },
    });

    if (error) {
      // This point will only be reached if there is an immediate error when
      // confirming the payment. Show error to your customer (for example, payment
      // details incomplete)
      setErrorMessage(error.message);
    } else {
      // Your customer will be redirected to your `return_url`. For some payment
      // methods like iDEAL, your customer will be redirected to an intermediate
      // site first to authorize the payment, then redirected to the `return_url`.
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button disabled={!stripe}>Submit</button>
      {/* Show error message to your customers */}
      {errorMessage && <div>{errorMessage}</div>}
    </form>
  );
};

export default CheckoutForm;
```

Make sure the `return_url` corresponds to a page on your website that provides the status of the payment. When Stripe redirects the customer to the `return_url`, we provide the following URL query parameters:

| Parameter                      | Description                                                                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. |

> If you have tooling that tracks the customer’s browser session, you might need to add the `stripe.com` domain to the referrer exclude list. Redirects cause some tools to create new sessions, which prevents you from tracking the complete session.

Use one of the query parameters to retrieve the PaymentIntent. Inspect the [status of the PaymentIntent](https://docs.stripe.com/payments/paymentintents/lifecycle.md) to decide what to show your customers. You can also append your own query parameters when providing the `return_url`, which persist through the redirect process.

#### HTML + JS

```javascript
// Initialize Stripe.js using your publishable key
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");

// Retrieve the "payment_intent_client_secret" query parameter appended to
// your return_url by Stripe.js
const clientSecret = new URLSearchParams(window.location.search).get(
  "payment_intent_client_secret",
);

// Retrieve the PaymentIntent
stripe.retrievePaymentIntent(clientSecret).then(({ paymentIntent }) => {
  const message = document.querySelector("#message");

  // Inspect the PaymentIntent `status` to indicate the status of the payment
  // to your customer.
  //
  // Some payment methods will [immediately succeed or fail][0] upon
  // confirmation, while others will first enter a `processing` state.
  //
  // [0]: https://stripe.com/docs/payments/payment-methods#payment-notification
  switch (paymentIntent.status) {
    case "succeeded":
      message.innerText = "Success! Payment received.";
      break;

    case "processing":
      message.innerText =
        "Payment processing. We'll update you when payment is received.";
      break;

    case "requires_payment_method":
      message.innerText = "Payment failed. Please try another payment method.";
      // Redirect your user back to your payment page to attempt collecting
      // payment again
      break;

    default:
      message.innerText = "Something went wrong.";
      break;
  }
});
```

#### React

```jsx
import React, { useState, useEffect } from "react";
import { useStripe } from "@stripe/react-stripe-js";

const PaymentStatus = () => {
  const stripe = useStripe();
  const [message, setMessage] = useState(null);

  useEffect(() => {
    if (!stripe) {
      return;
    }

    // Retrieve the "payment_intent_client_secret" query parameter appended to
    // your return_url by Stripe.js
    const clientSecret = new URLSearchParams(window.location.search).get(
      "payment_intent_client_secret",
    );

    // Retrieve the PaymentIntent
    stripe.retrievePaymentIntent(clientSecret).then(({ paymentIntent }) => {
      // Inspect the PaymentIntent `status` to indicate the status of the payment
      // to your customer.
      //
      // Some payment methods will [immediately succeed or fail][0] upon
      // confirmation, while others will first enter a `processing` state.
      //
      // [0]: https://stripe.com/docs/payments/payment-methods#payment-notification
      switch (paymentIntent.status) {
        case "succeeded":
          setMessage("Success! Payment received.");
          break;

        case "processing":
          setMessage(
            "Payment processing. We'll update you when payment is received.",
          );
          break;

        case "requires_payment_method":
          // Redirect your user back to your payment page to attempt collecting
          // payment again
          setMessage("Payment failed. Please try another payment method.");
          break;

        default:
          setMessage("Something went wrong.");
          break;
      }
    });
  }, [stripe]);

  return message;
};

export default PaymentStatus;
```

## Optional: Send payment instruction emails

You can enable Bank Transfer payment instruction emails from the [Dashboard](https://dashboard.stripe.com/settings/emails). After you enable payment instruction emails, Stripe sends your customer an email when:

- A PaymentIntent is confirmed but the customer doesn’t have sufficient balance.
- The customer sends a bank transfer but doesn’t have sufficient funds to complete the pending payments.

A Bank Transfer payment instruction email contains the amount due, the bank information for transferring funds, and a link to the Stripe hosted instruction page.

> In a sandbox, payment instruction emails are only sent to email addresses linked to the Stripe account.

## Confirm the PaymentIntent succeeded

The PaymentIntent stays in a `requires_action` status until funds arrive in the bank account. When funds are ready, the PaymentIntent status updates from `requires_action` to `succeeded`.

Your *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) endpoint needs to be set up to receive the `payment_intent.partially_funded` event. Stripe sends this event if funds are applied to a PaymentIntent but the payment remains incomplete. Note that when you first confirm a PaymentIntent and it transitions to `requires_action`, Stripe sends `payment_intent.requires_action` instead, even if existing customer balance funds were applied at the same time.

You can [add a webhook from the Dashboard](https://dashboard.stripe.com/webhooks/create).

Alternatively, you can use the [Webhook Endpoints API](https://docs.stripe.com/api/webhook_endpoints.md) to start receiving the [payment_intent.partially_funded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.partially_funded) event.

> The [Stripe CLI](https://docs.stripe.com/stripe-cli.md) doesn’t support triggering beta API version events, such as `payment_intent.partially_funded`.

The following events are sent during the payment funding flow when the PaymentIntent is updated.

| Event                             | Description                                                                                                                                                                                                                                                                                                                                                                                        | Next steps                                                                                                                                                                                                                                                                                                     |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent.requires_action`  | Sent during confirmation when the customer balance doesn’t have sufficient funds to reconcile the PaymentIntent, the PaymentIntent transitions to `requires_action`.                                                                                                                                                                                                                               | Instruct your customer to send a bank transfer with the `amount_remaining`.                                                                                                                                                                                                                                    |
| `payment_intent.partially_funded` | The customer sent a bank transfer that was applied to the PaymentIntent, but it wasn’t enough to complete the payment. This might happen because the customer underpaid, bank fees reduced the amount received, or a remaining customer balance was applied to the PaymentIntent. PaymentIntents that are partially funded aren’t reflected in your account balance until the payment is complete. | Instruct your customer to send another bank transfer with the new `amount_remaining` to complete the payment. If you want to complete the payment with the partially applied funds, you can update the `amount` and [confirm](https://docs.stripe.com/api/payment_intents/confirm.md) the PaymentIntent again. |
| `payment_intent.succeeded`        | The customer’s payment succeeded.                                                                                                                                                                                                                                                                                                                                                                  | Fulfill the goods or services that the customer purchased.                                                                                                                                                                                                                                                     |

> When you change the amount of a partially funded PaymentIntent, the funds are returned to the customer balance. If other PaymentIntents are open, Stripe funds those automatically. If the customer is configured for manual reconciliation, you need to [apply the funds](https://docs.stripe.com/api/payment_intents/apply_customer_balance.md) again.

We recommend [using webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the charge has succeeded and to notify the customer that the payment is complete.

### Sample code

#### Node.js

```javascript
// This example uses Express to receive webhooks
const express = require("express");
const app = express();

// Match the raw body to content type application/json
// If you are using Express v4 - v4.16 you need to use body-parser, not express, to retrieve
// the request body
app.post(
  "/webhook",
  express.json({ type: "application/json" }),
  (request, response) => {
    const event = request.body;

    // Handle the event
    switch (event.type) {
      case "payment_intent.requires_action":
        const paymentIntent = event.data.object;
        // The payment intent was not fully funded due to insufficient funds on the customer balance.
        // Define and call a method to handle the payment intent.
        // handlePaymentIntentRequiresAction(paymentIntent);
        break;
      case "payment_intent.partially_funded":
        const paymentIntent = event.data.object;
        // Then define and call a method to handle the payment intent being partially funded.
        // handlePaymentIntentPartiallyFunded(paymentIntent);
        break;
      case "payment_intent.succeeded":
        const paymentIntent = event.data.object;
        // Then define and call a method to handle the successful payment intent.
        // handlePaymentIntentSucceeded(paymentIntent);
        break;
      default:
        console.log(`Unhandled event type ${event.type}`);
    }

    // Return a response to acknowledge receipt of the event
    response.json({ received: true });
  },
);

app.listen(8000, () => console.log("Running on port 8000"));
```

### View pending payments in the Dashboard

You can view all pending bank transfer PaymentIntents in the [Dashboard](https://dashboard.stripe.com/payments) by applying the **Waiting on funding** filter to **Status** .

## Test your integration

You can test your integration by simulating an incoming bank transfer using the API, Dashboard, or a beta version of the Stripe CLI.

#### Dashboard

To simulate a bank transfer using the Dashboard in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), go to the customer’s page in the Dashboard. Under **Payment methods**, click **Add** and select **Fund cash balance (test only)**.

#### API

To simulate a bank transfer using the API:

#### US

```bash
curl https://api.stripe.com/v1/test_helpers/customers/{{CUSTOMER_ID}}/fund_cash_balance \
  -X POST \
  -u <<YOUR_SECRET_KEY>>: \
  -d "reference"="REF-4242" \
  -d "amount"="1000" \
  -d "currency"="usd"
```

#### UK

```bash
curl https://api.stripe.com/v1/test_helpers/customers/{{CUSTOMER_ID}}/fund_cash_balance \
  -X POST \
  -u <<YOUR_SECRET_KEY>>: \
  -d "reference"="REF-4242" \
  -d "amount"="1000" \
  -d "currency"="gbp"
```

#### EU

```bash
curl https://api.stripe.com/v1/test_helpers/customers/{{CUSTOMER_ID}}/fund_cash_balance \
  -X POST \
  -u <<YOUR_SECRET_KEY>>: \
  -d "reference"="REF-4242" \
  -d "amount"="1000" \
  -d "currency"="eur"
```

#### JP

```bash
curl https://api.stripe.com/v1/test_helpers/customers/{{CUSTOMER_ID}}/fund_cash_balance \
  -X POST \
  -u <<YOUR_SECRET_KEY>>: \
  -d "amount"="1000" \
  -d "currency"="jpy"
```

#### MX

```bash
curl https://api.stripe.com/v1/test_helpers/customers/{{CUSTOMER_ID}}/fund_cash_balance \
  -X POST \
  -u <<YOUR_SECRET_KEY>>: \
  -d "reference"="123456" \
  -d "amount"="1000" \
  -d "currency"="mxn"
```

#### Stripe CLI

To simulate a bank transfer with the Stripe CLI:

1. [Install the Stripe CLI](https://docs.stripe.com/stripe-cli.md).

1. Log in to the CLI using the same account you logged in to the Stripe Dashboard with.

   ```bash
   stripe login
   ```

1. Simulate an incoming bank transfer for an existing customer.

   #### US

   ```bash
   stripe test_helpers customers fund_cash_balance "{{CUSTOMER_ID}}" \
     --amount=1099 \
     --reference=DVGBG97TZ6ZV \
     --currency=usd
   ```

   The `reference` parameter is optional and simulates the value that the customer filled out for the bank transfer’s reference field.

   #### UK

   ```bash
   stripe test_helpers customers fund_cash_balance "{{CUSTOMER_ID}}" \
     --amount=1099 \
     --reference=DVGBG97TZ6ZV \
     --currency=gbp
   ```

   The `reference` parameter is optional and simulates the value that the customer filled out for the bank transfer’s reference field.

   #### EU

   ```bash
   stripe test_helpers customers fund_cash_balance "{{CUSTOMER_ID}}" \
     --amount=1099 \
     --reference=DVGBG97TZ6ZV \
     --currency=eur
   ```

   The `reference` parameter is optional and simulates the value that the customer filled out for the bank transfer’s reference field.

   #### JP

   ```bash
   stripe test_helpers customers fund_cash_balance "{{CUSTOMER_ID}}" \
     --amount=1000 \
     --currency=jpy
   ```

   #### MX

   ```bash
   stripe test_helpers customers fund_cash_balance "{{CUSTOMER_ID}}" \
     --amount=1099 \
     --reference=123456 \
     --currency=mxn
   ```

   The `reference` parameter is optional and simulates the value that the customer filled out for the bank transfer’s reference field.

## Handling temporary availability issues

The following error codes indicate temporary issues with the availability of the payment method:

| Code                                 | Description                                                                                                                                                                 | Handling                                                                                                                                                                                                                                 |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_method_rate_limit_exceeded` | Too many requests were made in quick succession for this payment method, which has stricter limits than the [API-wide rate limits](https://docs.stripe.com/rate-limits.md). | These errors can persist for several API requests when many of your customers try to use the same payment method, such as during an ongoing sale on your website. In this case, ask your customers to choose a different payment method. |

> If you anticipate heavy usage in general or because of an upcoming event, contact us as soon as you know about it.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Bank transfer is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method for Checkout where customers pay with a bank transfer using payment instructions presented. When selecting to pay, the user is redirected to a hosted page which displays bank transfer instructions and the status of the transfer payment.

Bank transfer is also a *delayed notification payment method* (A payment method that can't immediately return payment status when a customer attempts a transaction (for example, ACH debits). Businesses commonly hold an order in a pending state until payment is successful with these payment methods), which means that funds aren’t immediately available after payment.

> Bank transfers aren’t available on Checkout Sessions that didn’t include an existing [Customer object](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) as part of the of the session creation request.

## Determine compatibility

**Supported business locations**: Europe (SEPA area), UK, JP, MX, US

**Supported currencies**: `eur, gbp, jpy, mxn, usd`

**Presentment currencies**: `eur, gbp, jpy, mxn, usd`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support Bank Transfer payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.

- You can only use one-time line items (Bank Transfer Checkout Sessions don’t support recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans).

## Accept a payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

Use this guide to enable Bank Transfer.

### Create or retrieve a Customer

You must associate a [Customer](https://docs.stripe.com/api/customers.md) object to reconcile each bank transfer payment. If you have an existing Customer object, you can skip this step. Otherwise, create a new Customer object.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

### Enable Bank Transfer as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Set `customer`
1. Add `customer_balance` to the list of `payment_method_types`
1. Make sure all your `line_items` use the same currency

#### US

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer: "{{CUSTOMER_ID}}",
  line_items: [
    {
      price_data: {
        currency: "usd",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "customer_balance"],
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "us_bank_transfer",
      },
    },
  },
  success_url: "https://example.com/success",
});
```

#### UK

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer: "{{CUSTOMER_ID}}",
  line_items: [
    {
      price_data: {
        currency: "gbp",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "customer_balance"],
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "gb_bank_transfer",
      },
    },
  },
  success_url: "https://example.com/success",
});
```

#### EU

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer: "{{CUSTOMER_ID}}",
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
  payment_method_types: ["card", "customer_balance"],
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "eu_bank_transfer",
        eu_bank_transfer: {
          country: "FR",
        },
      },
    },
  },
  success_url: "https://example.com/success",
});
```

Set [payment_method_options[customer_balance][bank_transfer][eu_bank_transfer][country]](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-bank_transfer-eu_bank_account-country) to one of to display the localized IBAN to the customer.

#### JP

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer: "{{CUSTOMER_ID}}",
  line_items: [
    {
      price_data: {
        currency: "jpy",
        product_data: {
          name: "Tシャツ",
        },
        unit_amount: 19000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "customer_balance"],
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "jp_bank_transfer",
      },
    },
  },
  success_url: "https://example.com/success",
});
```

#### MX

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer: "{{CUSTOMER_ID}}",
  line_items: [
    {
      price_data: {
        currency: "mxn",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 18000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "customer_balance"],
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "mx_bank_transfer",
      },
    },
  },
  success_url: "https://example.com/success",
});
```

### Redirect to Stripe hosted bank transfer instructions page

> Unlike card payments, the customer isn’t always redirected to the [success_url](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-success_url) with bank transfer payment.

After *submit* (Submitting an order indicates that the customer intends to pay. Upon submission, the order can no longer be updated and is ready for payment) the Checkout form successfully,

- If the customer already has a balance high enough to cover the request amount, the payment immediately succeeds and the customer is redirected to the [success_url](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-success_url).
- If the customer balance isn’t high enough to cover the request amount, the customer is redirected to the [hosted_instructions_url](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-hosted_instructions_url). The page has the instructions to guide your customer through completing the transfer.

Stripe allows customization of customer-facing UIs on the [Branding Settings](https://dashboard.stripe.com/account/branding) page. The following brand settings can be applied to the hosted instructions page:

- **Icon**—your brand image and public business name
- **Brand color**—used as the background color

### Fulfill your orders

Because bank transfer is a *delayed notification payment method* (A payment method that can't immediately return payment status when a customer attempts a transaction (for example, ACH debits). Businesses commonly hold an order in a pending state until payment is successful with these payment methods), you need to use a method such as *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to monitor the payment status and handle order *fulfillment* (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected). Learn more about [setting up webhooks and fulfilling orders](https://docs.stripe.com/checkout/fulfillment.md).

The following events are sent when the payment status changes:

| Event Name                                                                                                                                   | Description                                                                                               | Next steps                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed)                             | The customer has successfully submitted the Checkout form and is redirected to `hosted_instructions_url`. | Wait for the customer to make the bank transfer.           |
| [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) | The customer has successfully made the bank transfer. The `PaymentIntent` transitions to `succeeded`.     | Fulfill the goods or services that the customer purchased. |

## Optional: Send payment instruction emails

You can enable Bank Transfer payment instruction emails from the [Dashboard](https://dashboard.stripe.com/settings/emails). After you enable payment instruction emails, Stripe sends your customer an email when:

- A PaymentIntent is confirmed but the customer doesn’t have sufficient balance.
- The customer sends a bank transfer but doesn’t have sufficient funds to complete the pending payments.

A Bank Transfer payment instruction email contains the amount due, the bank information for transferring funds, and a link to the Stripe hosted instruction page.

> In a sandbox, payment instruction emails are only sent to email addresses linked to the Stripe account.

## Test your integration

You can test your integration by simulating an incoming bank transfer using the API, Dashboard, or a beta version of the Stripe CLI.

#### Dashboard

To simulate a bank transfer using the Dashboard in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), go to the customer’s page in the Dashboard. Under **Payment methods**, click **Add** and select **Fund cash balance (test only)**.

#### API

To simulate a bank transfer using the API:

#### US

```bash
curl https://api.stripe.com/v1/test_helpers/customers/{{CUSTOMER_ID}}/fund_cash_balance \
  -X POST \
  -u <<YOUR_SECRET_KEY>>: \
  -d "reference"="REF-4242" \
  -d "amount"="1000" \
  -d "currency"="usd"
```

#### UK

```bash
curl https://api.stripe.com/v1/test_helpers/customers/{{CUSTOMER_ID}}/fund_cash_balance \
  -X POST \
  -u <<YOUR_SECRET_KEY>>: \
  -d "reference"="REF-4242" \
  -d "amount"="1000" \
  -d "currency"="gbp"
```

#### EU

```bash
curl https://api.stripe.com/v1/test_helpers/customers/{{CUSTOMER_ID}}/fund_cash_balance \
  -X POST \
  -u <<YOUR_SECRET_KEY>>: \
  -d "reference"="REF-4242" \
  -d "amount"="1000" \
  -d "currency"="eur"
```

#### JP

```bash
curl https://api.stripe.com/v1/test_helpers/customers/{{CUSTOMER_ID}}/fund_cash_balance \
  -X POST \
  -u <<YOUR_SECRET_KEY>>: \
  -d "amount"="1000" \
  -d "currency"="jpy"
```

#### MX

```bash
curl https://api.stripe.com/v1/test_helpers/customers/{{CUSTOMER_ID}}/fund_cash_balance \
  -X POST \
  -u <<YOUR_SECRET_KEY>>: \
  -d "reference"="123456" \
  -d "amount"="1000" \
  -d "currency"="mxn"
```

#### Stripe CLI

To simulate a bank transfer with the Stripe CLI:

1. [Install the Stripe CLI](https://docs.stripe.com/stripe-cli.md).

1. Log in to the CLI using the same account you logged in to the Stripe Dashboard with.

   ```bash
   stripe login
   ```

1. Simulate an incoming bank transfer for an existing customer.

   #### US

   ```bash
   stripe test_helpers customers fund_cash_balance "{{CUSTOMER_ID}}" \
     --amount=1099 \
     --reference=DVGBG97TZ6ZV \
     --currency=usd
   ```

   The `reference` parameter is optional and simulates the value that the customer filled out for the bank transfer’s reference field.

   #### UK

   ```bash
   stripe test_helpers customers fund_cash_balance "{{CUSTOMER_ID}}" \
     --amount=1099 \
     --reference=DVGBG97TZ6ZV \
     --currency=gbp
   ```

   The `reference` parameter is optional and simulates the value that the customer filled out for the bank transfer’s reference field.

   #### EU

   ```bash
   stripe test_helpers customers fund_cash_balance "{{CUSTOMER_ID}}" \
     --amount=1099 \
     --reference=DVGBG97TZ6ZV \
     --currency=eur
   ```

   The `reference` parameter is optional and simulates the value that the customer filled out for the bank transfer’s reference field.

   #### JP

   ```bash
   stripe test_helpers customers fund_cash_balance "{{CUSTOMER_ID}}" \
     --amount=1000 \
     --currency=jpy
   ```

   #### MX

   ```bash
   stripe test_helpers customers fund_cash_balance "{{CUSTOMER_ID}}" \
     --amount=1099 \
     --reference=123456 \
     --currency=mxn
   ```

   The `reference` parameter is optional and simulates the value that the customer filled out for the bank transfer’s reference field.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=direct-api.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer [Server-side]

You must associate a [Customer](https://docs.stripe.com/api/customers.md) object to reconcile each bank transfer payment. If you have an existing Customer object, you can skip this step. Otherwise, create a new Customer object.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create and confirm a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage. Create and confirm a PaymentIntent on the server, specifying the amount and currency you want to collect. You must also populate the [customer parameter](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) of the PaymentIntent creation request. Bank transfers aren’t available on PaymentIntents without a customer.

#### Manage payment methods from the Dashboard

Before creating a Payment Intent, make sure to turn **Bank transfer** on in the [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) page of your Dashboard.

> With [Dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md), Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

#### US

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  customer: "{{CUSTOMER_ID}}",
  currency: "usd",
  automatic_payment_methods: {
    enabled: true,
  },
  return_url: "https://example.com/return_url",
  payment_method_data: {
    type: "customer_balance",
  },
  confirm: true,
});
```

#### UK

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  customer: "{{CUSTOMER_ID}}",
  currency: "gbp",
  automatic_payment_methods: {
    enabled: true,
  },
  return_url: "https://example.com/return_url",
  payment_method_data: {
    type: "customer_balance",
  },
  confirm: true,
});
```

#### EU

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  customer: "{{CUSTOMER_ID}}",
  currency: "eur",
  automatic_payment_methods: {
    enabled: true,
  },
  return_url: "https://example.com/return_url",
  payment_method_data: {
    type: "customer_balance",
  },
  confirm: true,
});
```

To localize the IBAN displayed to the customer you can configure the country of the Customer by setting the [`address.country`](https://docs.stripe.com/api/customers/object.md#customer_object-address-country) property or by [editing the Customer in the Dashboard](https://docs.stripe.com/invoicing/customer.md#edit-a-customer).

We support IBAN localization for :

- If you haven’t configured a country for your Customer, or if their country doesn’t support IBAN localization, we fall back to the country of your Stripe account.
- If IBAN localization isn’t supported for the country of your Stripe account, we fall back to `IE`.

> Creating new localized virtual bank account numbers is currently unavailable for Spain (ES). Use any of the other EU VBAN countries instead.

#### JP

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 19000,
  customer: "{{CUSTOMER_ID}}",
  currency: "jpy",
  automatic_payment_methods: {
    enabled: true,
  },
  return_url: "https://example.com/return_url",
  payment_method_data: {
    type: "customer_balance",
  },
  confirm: true,
});
```

#### MX

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  customer: "{{CUSTOMER_ID}}",
  currency: "mxn",
  automatic_payment_methods: {
    enabled: true,
  },
  return_url: "https://example.com/return_url",
  payment_method_data: {
    type: "customer_balance",
  },
  confirm: true,
});
```

In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.

If the customer already has a balance high enough to cover the payment amount, the PaymentIntent immediately succeeds with a `succeeded` status. Customers can accrue a balance when they accidentally overpay for a transaction—a common occurrence with bank transfers. You must [reconcile customer balances within a certain period based on your location](https://docs.stripe.com/payments/customer-balance/reconciliation.md).

#### List payment methods manually

To manually specify payment methods with the API, add `customer_balance` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your PaymentIntent. Specify the [id](https://docs.stripe.com/api/customers/object.md#customer_object-id) of the Customer.

#### US

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["customer_balance"],
  payment_method_data: {
    type: "customer_balance",
  },
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "us_bank_transfer",
      },
    },
  },
  confirm: true,
});
```

If the customer already has a balance high enough to cover the payment amount, the PaymentIntent immediately succeeds with a `succeeded` status. Customers can accrue a balance when they accidentally overpay for a transaction—a common occurrence with bank transfers. You must [reconcile customer balances within a certain period based on your location](https://docs.stripe.com/payments/customer-balance/reconciliation.md).

- Use `bank_transfer` as the [funding_type](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-funding_type) to specify what to do when the customer doesn’t have enough balance to cover the payment amount.
- Use `us_bank_transfer` as the [bank_transfer[type]](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-bank_transfer-type) to specify the bank transfer types that can be used to fund the payment.

#### UK

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "gbp",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["customer_balance"],
  payment_method_data: {
    type: "customer_balance",
  },
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "gb_bank_transfer",
      },
    },
  },
  confirm: true,
});
```

If the customer already has a balance high enough to cover the payment amount, the PaymentIntent immediately succeeds with a `succeeded` status. Customers can accrue a balance when they accidentally overpay for a transaction—a common occurrence with bank transfers. You must [reconcile customer balances within a certain period based on your location](https://docs.stripe.com/payments/customer-balance/reconciliation.md).

- Use `bank_transfer` as the [funding_type](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-funding_type) to specify what to do when the customer doesn’t have enough balance to cover the payment amount.
- Use `gb_bank_transfer` as the [bank_transfer[type]](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-bank_transfer-type) to specify the bank transfer types that can be used to fund the payment.

#### EU

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["customer_balance"],
  payment_method_data: {
    type: "customer_balance",
  },
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "eu_bank_transfer",
        eu_bank_transfer: {
          country: "FR",
        },
      },
    },
  },
  confirm: true,
});
```

If the customer already has a balance high enough to cover the payment amount, the PaymentIntent immediately succeeds with a `succeeded` status. Customers can accrue a balance when they accidentally overpay for a transaction—a common occurrence with bank transfers. You must [reconcile customer balances within a certain period based on your location](https://docs.stripe.com/payments/customer-balance/reconciliation.md).

- Use `bank_transfer` as the [funding_type](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-funding_type) to specify what to do when the customer doesn’t have enough balance to cover the payment amount.
- Use `eu_bank_transfer` as the [bank_transfer[type]](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-bank_transfer-type) to specify the bank transfer types that can be used to fund the payment.
- Set [payment_method_options[customer_balance][bank_transfer][eu_bank_transfer][country]](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-bank_transfer-eu_bank_account-country) to one of . The IBAN displayed to the customer is localized to the chosen country.

> Creating new localized virtual bank account numbers is currently unavailable for Spain (ES). Use any of the other EU VBAN countries instead.

#### JP

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 19000,
  currency: "jpy",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["customer_balance"],
  payment_method_data: {
    type: "customer_balance",
  },
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "jp_bank_transfer",
      },
    },
  },
  confirm: true,
});
```

If the customer already has a balance high enough to cover the payment amount, the PaymentIntent immediately succeeds with a `succeeded` status. Customers can accrue a balance when they accidentally overpay for a transaction—a common occurrence with bank transfers. You must [reconcile customer balances within a certain period based on your location](https://docs.stripe.com/payments/customer-balance/reconciliation.md).

- Use `bank_transfer` as the [funding_type](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-funding_type) to specify what to do when the customer doesn’t have enough balance to cover the payment amount.
- Use `jp_bank_transfer` as the [bank_transfer[type]](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-bank_transfer-type) to specify the bank transfer types that can be used to fund the payment.

#### MX

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "mxn",
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["customer_balance"],
  payment_method_data: {
    type: "customer_balance",
  },
  payment_method_options: {
    customer_balance: {
      funding_type: "bank_transfer",
      bank_transfer: {
        type: "mx_bank_transfer",
      },
    },
  },
  confirm: true,
});
```

If the customer already has a balance high enough to cover the payment amount, the PaymentIntent immediately succeeds with a `succeeded` status. Customers can accrue a balance when they accidentally overpay for a transaction—a common occurrence with bank transfers. You must [reconcile customer balances within a certain period based on your location](https://docs.stripe.com/payments/customer-balance/reconciliation.md).

- Use `bank_transfer` as the [funding_type](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-funding_type) to specify what to do when the customer doesn’t have enough balance to cover the payment amount.
- Use `mx_bank_transfer` as the [bank_transfer[type]](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-bank_transfer-type) to specify the bank transfer types that can be used to fund the payment.

> Always specify the `payment_method_types` when creating a payment. You can’t use `customer_balance` for [future payments](https://docs.stripe.com/payments/save-and-reuse.md).

## Optional: Send payment instruction emails

You can enable Bank Transfer payment instruction emails from the [Dashboard](https://dashboard.stripe.com/settings/emails). After you enable payment instruction emails, Stripe sends your customer an email when:

- A PaymentIntent is confirmed but the customer doesn’t have sufficient balance.
- The customer sends a bank transfer but doesn’t have sufficient funds to complete the pending payments.

A Bank Transfer payment instruction email contains the amount due, the bank information for transferring funds, and a link to the Stripe hosted instruction page.

> In a sandbox, payment instruction emails are only sent to email addresses linked to the Stripe account.

## Instruct the customer to complete a bank transfer [Client-side]

If the customer balance isn’t high enough to cover the request amount, the PaymentIntent shows a `requires_action` status. The response has a `next_action` field containing a `type` value of `display_bank_transfer_instructions`. The `next_action[display_bank_transfer_instructions]` hash contains information to display to your customer so that they can complete the bank transfer. To ensure fund settlements, instruct your customers to use the exact details provided, particularly for the account name and account number, if applicable.

> In *live mode* (Use this mode when you’re ready to launch your app. Card networks or payment providers process payments), Stripe supplies each customer with a unique set of bank transfer details. In contrast, Stripe offers invalid bank transfer details to all customers in testing environments. Unlike live mode, these invalid details might not always be unique.

#### US

| Field                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-type)                                       | The type of bank transfer to use. Type must be `us_bank_transfer` in the US.                                                                                                                                                                                                                    |
| [reference](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-reference)                             | A unique reference code to identify the bank transfer. Instruct your customer to include this code in the reference field of their bank transfer.                                                                                                                                               |
| [amount_remaining](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-amount_remaining)               | The remaining amount that needs to be transferred to complete the payment. Instruct your customer to transfer this amount. This might be different from the PaymentIntent amount if pre-existing funds in the customer balance were applied to the PaymentIntent or if your customer underpaid. |
| [currency](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-currency)                               | The currency for the remaining amount.                                                                                                                                                                                                                                                          |
| [financial_addresses](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions)                             | List of financial addresses for US bank accounts. Types include `aba` and `swift`. See below for details.                                                                                                                                                                                       |
| [hosted_instructions_url](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-hosted_instructions_url) | A link to a hosted page that guides your customer through completing the transfer.                                                                                                                                                                                                              |

#### aba hash

Example of an `aba` hash:

```json
{
  "aba": {
    "account_number": "111222333444",
    "bank_name": "Wells Fargo Bank, NA",
    "routing_number": "444555666"
  },
  "supported_networks": ["ach", "domestic_wire_us"],
  "type": "aba"
}
```

| Field                | Values                                          | Description                    |
| -------------------- | ----------------------------------------------- | ------------------------------ |
| `type`               | `aba`                                           | The type of financial address. |
| `supported_networks` | - `ach`                                         |
| - `domestic_wire_us` | The list of networks supported by this address. |
| `aba.account_number` | 111222333444                                    | The ABA account number.        |
| `aba.routing_number` | 444555666                                       | The ABA routing number.        |
| `aba.bank_name`      | Wells Fargo Bank, NA                            | The name of the bank.          |

#### swift hash

Example of a `swift` hash:

```json
{
  "swift": {
    "account_number": "111222333444",
    "bank_name": "Wells Fargo Bank, NA",
    "swift_code": "AAAA-BB-CC-123"
  },
  "supported_networks": ["swift"],
  "type": "swift"
}
```

| Field                  | Values               | Description                                     |
| ---------------------- | -------------------- | ----------------------------------------------- |
| `type`                 | `swift`              | The type of financial address.                  |
| `supported_networks`   | - `swift`            | The list of networks supported by this address. |
| `swift.account_number` | 111222333444         | The SWIFT account number.                       |
| `swift.swift_code`     | AAAA-BB-CC-123       | The SWIFT code.                                 |
| `swift.bank_name`      | Wells Fargo Bank, NA | The name of the bank.                           |

#### Settlement timing

After instructing your customer to initiate a transfer with their bank using the information you provide, it can take up to 5 days for the transfer to complete. The settlement timing depends on the banking rails that the transfer arrived through to Stripe:

- ACH transfers arrive within 1-3 business days.
- Domestic wire transfers (Fedwire) arrive on the same day (depending on whether the transfer is sent before the bank’s cut-off time).
- International wire transfers (SWIFT) arrive within 1-5 business days.

#### UK

| Field                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-type)                                       | The type of bank transfer to use. Type must be `gb_bank_transfer` in the UK.                                                                                                                                                                                                                    |
| [reference](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-reference)                             | A unique reference code to identify the bank transfer. Instruct your customer to include this code in the reference field of their bank transfer.                                                                                                                                               |
| [amount_remaining](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-amount_remaining)               | The remaining amount that needs to be transferred to complete the payment. Instruct your customer to transfer this amount. This might be different from the PaymentIntent amount if pre-existing funds in the customer balance were applied to the PaymentIntent or if your customer underpaid. |
| [currency](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-currency)                               | The currency for the remaining amount.                                                                                                                                                                                                                                                          |
| [financial_addresses](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions)                             | List of financial addresses for UK bank accounts. Types include `sort_code`. See below for details.                                                                                                                                                                                             |
| [hosted_instructions_url](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-hosted_instructions_url) | A link to a hosted page that guides your customer through completing the transfer.                                                                                                                                                                                                              |

### sort_code hash

Example of a `sort_code` hash:

```json
{
  "sort_code": {
    "account_holder_name": "Demo Test Inc.",
    "account_number": "98765432",
    "sort_code": "200000"
  },
  "supported_networks": ["bacs", "fps"],
  "type": "sort_code"
}
```

| Field                                                                                                                                                                                                         | Values                                          | Description                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------- |
| [type](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-type)                                                   | `sort_code`                                     | The type of financial address.                                 |
| [supported_networks](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-supported_networks)                       | - `bacs`                                        |
| - `fps`                                                                                                                                                                                                       | The list of networks supported by this address. |
| [sort_code.account_number](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-sort_code-account_number)           | 98765432                                        | The 8 digit account number.                                    |
| [sort_code.sort_code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-sort_code-sort_code)                     | 200000                                          | The 6 digit sort code.                                         |
| [sort_code.account_holder_name](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-sort_code-account_holder_name) | Demo Test Inc.                                  | The name of the person or business that owns the bank account. |

#### Settlement timing

After instructing your customer to initiate a transfer with their bank using the information you provide, it can take up to 5 days for the transfer to complete. The settlement timing depends on the banking rails that the transfer arrived through to Stripe:

- FPS transfers arrive within 15 minutes.
- BACS transfers arrive within 5 days.

> Bank transfers sent over the [CHAPS](https://www.bankofengland.co.uk/payment-and-settlement/chaps) payment network are currently not supported.

#### EU

| Field                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-type)                                       | The type of bank transfer to use. Type must be `eu_bank_transfer` in the EU.                                                                                                                                                                                                                    |
| [reference](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-reference)                             | A unique reference code to identify the bank transfer. Instruct your customer to include this code in the reference field of their bank transfer.                                                                                                                                               |
| [amount_remaining](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-amount_remaining)               | The remaining amount that needs to be transferred to complete the payment. Instruct your customer to transfer this amount. This might be different from the PaymentIntent amount if pre-existing funds in the customer balance were applied to the PaymentIntent or if your customer underpaid. |
| [currency](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-currency)                               | The currency for the remaining amount.                                                                                                                                                                                                                                                          |
| [financial_addresses](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions)                             | List of financial addresses for EU bank accounts. Types include `iban`. See below for details.                                                                                                                                                                                                  |
| [hosted_instructions_url](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-hosted_instructions_url) | A link to a hosted page that guides your customer through completing the transfer.                                                                                                                                                                                                              |

### iban hash

Example of an `iban` hash:

```json
{
  "iban": {
    "account_holder_name": "Demo Test Inc.",
    "bic": "CITINL2XXXX",
    "country": "NL",
    "iban": "NL40CITI7000799556	"
  },
  "supported_networks": ["sepa"],
  "type": "iban"
}
```

| Field                                                                                                                                                                                   | Values             | Description                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------------------------------------- |
| [type](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-type)                             | `iban`             | The type of financial address.                  |
| [supported_networks](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-supported_networks) | - `sepa`           | The list of networks supported by this address. |
| [iban.iban](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-iban-iban)                   | NL40CITI7000799556 | The IBAN the customer needs to pay to.          |

If you’re managing payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods), the IBAN’s country is selected based on the Customer [country](https://docs.stripe.com/api/customers/object.md#customer_object-country) or the country of your Stripe account.

If you’re listing payment methods manually using the [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) parameter, the IBAN’s country is selected based on the [country](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-customer_balance-bank_transfer-eu_bank_transfer-country) parameter passed in the request. |
| [iban.bic](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-iban-bic) | CITINL2XXXX | The BIC for this IBAN. |
| [iban.country](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-iban-country) | `NL` | The two-letter country code of bank account to transfer to. |
| [iban.account_holder_name](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-iban-account_holder_name) | Demo Test Inc. | The name of the person or business that owns the bank account. |

#### Settlement timing

For domestic transfers, ask your customer to initiate a SEPA Instant transfer (when available) using the details you provide. Funds are typically credited within seconds and arrive within 30 minutes. Longer settlement might occur on weekends, bank holidays, or if the sender’s bank can’t route the payment through the Instant scheme. In these cases, the transfer is processed as a standard SEPA payment.

> Accepting international EUR transfers is in preview. For early access eligibility, contact [sepa-bank-transfers-beta@stripe.com](mailto:sepa-bank-transfers-beta@stripe.com).

#### JP

| Field                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-type)                                       | The type of bank transfer to use. Type must be `jp_bank_transfer` in Japan.                                                                                                                                                                                                                     |
| [reference](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-reference)                             | This field isn’t used.                                                                                                                                                                                                                                                                          |
| [amount_remaining](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-amount_remaining)               | The remaining amount that needs to be transferred to complete the payment. Instruct your customer to transfer this amount. This might be different from the PaymentIntent amount if pre-existing funds in the customer balance were applied to the PaymentIntent or if your customer underpaid. |
| [currency](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-currency)                               | The currency for the remaining amount.                                                                                                                                                                                                                                                          |
| [financial_addresses](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses)         | List of financial addresses for JP bank accounts. Types include `zengin`. See below for details.                                                                                                                                                                                                |
| [hosted_instructions_url](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-hosted_instructions_url) | A link to a hosted page that guides your customer through completing the transfer.                                                                                                                                                                                                              |

### zengin hash

Example of a `zengin` hash:

```json
{
  "zengin": {
    "account_holder_name": "ストライプジャパン（カ　シュウノウダイコウ",
    "account_number": "1234567",
    "account_type": "futsu",
    "bank_code": "0009",
    "bank_name": "三井住友銀行",
    "branch_code": "950",
    "branch_name": "東京第二"
  },
  "supported_networks": ["zengin"],
  "type": "zengin"
}
```

| Field                                                                                                                                                                                                   | Values                                     | Description                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------- |
| [type](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-type)                                             | `zengin`                                   | The type of financial address.                  |
| [supported_networks](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-supported_networks)                 | - `zengin`                                 | The list of networks supported by this address. |
| [zengin.bank_code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-zengin-bank_code)                     | 0009                                       | The 4 digit bank code.                          |
| [zengin.bank_name](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-zengin-bank_name)                     | 三井住友銀行                               | The bank name.                                  |
| [zengin.branch_code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-zengin-branch_code)                 | 950                                        | The 3 digit branch code.                        |
| [zengin.branch_name](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-zengin-branch_name)                 | 東京第二                                   | The branch name.                                |
| [zengin.account_type](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-zengin-account_type)               | `futsu`, `toza`                            | The account type.                               |
| [zengin.account_holder_name](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-zengin-account_holder_name) | ストライプジャパン（カ　シュウノウダイコウ | The account holder name.                        |
| [zengin.account_number](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-zengin-account_number)           | 1234567                                    | The 7 digit account number.                     |

#### Settlement timing

Instruct your customer to initiate a transfer with their bank using the information you provide.

Transfers made during business hours arrive on the same day. Transfers made outside business hours arrive on the next business day.

#### MX

| Field                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-type)                                       | The type of bank transfer to use. Type must be `mx_bank_transfer` in Mexico.                                                                                                                                                                                                                    |
| [reference](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-reference)                             | A unique reference code to identify the bank transfer. Instruct your customer to include this code in the reference field of their bank transfer.                                                                                                                                               |
| [amount_remaining](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-amount_remaining)               | The remaining amount that needs to be transferred to complete the payment. Instruct your customer to transfer this amount. This might be different from the PaymentIntent amount if pre-existing funds in the customer balance were applied to the PaymentIntent or if your customer underpaid. |
| [currency](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-currency)                               | The currency for the remaining amount.                                                                                                                                                                                                                                                          |
| [financial_addresses](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions)                             | List of financial addresses for MX bank accounts. Types include `spei`. See below for details.                                                                                                                                                                                                  |
| [hosted_instructions_url](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-hosted_instructions_url) | A link to a hosted page that guides your customer through completing the transfer.                                                                                                                                                                                                              |

### spei hash

Example of a `spei` hash:

```json
{
  "spei": {
    "bank_code": "002",
    "bank_name": "BANAMEX",
    "clabe": "002180650612345670"
  },
  "supported_networks": ["spei"],
  "type": "spei"
}
```

| Field                                                                                                                                                                                   | Values             | Description                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------------------------------------------- |
| [type](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-type)                             | `spei`             | The type of financial address.                  |
| [supported_networks](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-supported_networks) | - `spei`           | The list of networks supported by this address. |
| [spei.clabe](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-spei-clabe)                 | 002180650612345670 | The 18 digit CLABE number.                      |
| [spei.bank_code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-spei-bank_code)         | 002                | The 3 digit bank code.                          |
| [spei.bank_name](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-spei-bank_name)         | BANAMEX            | The short name of the banking institution       |

Instruct your customer to initiate a transfer with their bank using the information you provide.

We expect most payments to arrive in less than 10 minutes, on both banking and non-banking days.

## Confirm the PaymentIntent succeeded

The PaymentIntent stays in a `requires_action` status until funds arrive in the bank account. When funds are ready, the PaymentIntent status updates from `requires_action` to `succeeded`.

You need to set up your *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) endpoint to start receiving the `payment_intent.partially_funded` event.

You can [add a webhook from the Dashboard](https://dashboard.stripe.com/webhooks/create).

Alternatively, you can use the [Webhook Endpoints API](https://docs.stripe.com/api/webhook_endpoints.md) to start receiving the [payment_intent.partially_funded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.partially_funded) event.

Stripe sends the following events during the payment funding flow when we update the PaymentIntent.

| Event                             | Description                                                                                                                                                                                                                                                                                                                                                                                                               | Next steps                                                                                                                                                                                                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent.requires_action`  | Sent during confirmation when the customer balance doesn’t have sufficient funds to reconcile the PaymentIntent, the PaymentIntent transitions to `requires_action`. If a customer cash balance has been automatically applied to the PaymentIntent at confirmation time and the amount doesn’t fully cover the PaymentIntent `amount`, Stripe emits this event with an accurate `amount_remaining`.                      | Instruct your customer to send a bank transfer with the `amount_remaining`.                                                                                                                                                                                                                                    |
| `payment_intent.partially_funded` | The customer sent a bank transfer that was applied to the PaymentIntent, but wasn’t enough to complete the payment. This can happen if the customer transfers an insufficient amount after you confirm the `PaymentIntent`. This can result from an underpayment or fees charged by the customer’s bank. PaymentIntents that are partially funded aren’t reflected in your account balance until the payment is complete. | Instruct your customer to send another bank transfer with the new `amount_remaining` to complete the payment. If you want to complete the payment with the partially applied funds, you can update the `amount` and [confirm](https://docs.stripe.com/api/payment_intents/confirm.md) the PaymentIntent again. |
| `payment_intent.succeeded`        | The customer’s payment succeeded.                                                                                                                                                                                                                                                                                                                                                                                         | Fulfill the goods or services that the customer purchased.                                                                                                                                                                                                                                                     |

To listen to all events related to partial funding, listen to both `requires_action` and `partially_funded`. Stripe emits `requires_action` when funding is still required after confirmation. We emit `partially_funded` when we later receive additional funds from the customer that don’t fully cover the remaining amount.

> When you change the amount of a partially funded PaymentIntent, the funds are returned to the customer balance. If other PaymentIntents are open, Stripe funds those automatically. If the customer is configured for manual reconciliation, you need to [apply the funds](https://docs.stripe.com/api/payment_intents/apply_customer_balance.md) again.

We recommend [using webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the charge has succeeded and to notify the customer that the payment is complete.

### Sample code

#### Node.js

```javascript
// This example uses Express to receive webhooks
const express = require("express");
const app = express();

// Match the raw body to content type application/json
// If you are using Express v4 - v4.16 you need to use body-parser, not express, to retrieve
// the request body
app.post(
  "/webhook",
  express.json({ type: "application/json" }),
  (request, response) => {
    const event = request.body;

    // Handle the event
    switch (event.type) {
      case "payment_intent.requires_action":
        const paymentIntent = event.data.object;
        // The payment intent was not fully funded due to insufficient funds on the customer balance.
        // Define and call a method to handle the payment intent.
        // handlePaymentIntentRequiresAction(paymentIntent);
        break;
      case "payment_intent.partially_funded":
        const paymentIntent = event.data.object;
        // Then define and call a method to handle the payment intent being partially funded.
        // handlePaymentIntentPartiallyFunded(paymentIntent);
        break;
      case "payment_intent.succeeded":
        const paymentIntent = event.data.object;
        // Then define and call a method to handle the successful payment intent.
        // handlePaymentIntentSucceeded(paymentIntent);
        break;
      default:
        console.log(`Unhandled event type ${event.type}`);
    }

    // Return a response to acknowledge receipt of the event
    response.json({ received: true });
  },
);

app.listen(8000, () => console.log("Running on port 8000"));
```

### View pending payments in the Dashboard

You can view all pending bank transfer PaymentIntents in the [Dashboard](https://dashboard.stripe.com/payments) by applying the **Waiting on funding** filter to **Status** .

## Test your integration

You can test your integration by simulating an incoming bank transfer using either the Dashboard or an HTTP request.

### With the Dashboard

To simulate a bank transfer using the Dashboard in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), go to the customer’s page in the Dashboard. Under **Payment methods**, click **Add** and select **Fund cash balance (test only)**.

### With the Stripe API

You can make an API call to simulate a bank transfer.

#### US

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customerCashBalanceTransaction =
  await stripe.testHelpers.customers.fundCashBalance("cus_xxxxxxxxx", {
    amount: 1000,
    currency: "usd",
    reference: "REF-4242",
  });
```

You can simulate a reversal by prefixing the `reference` parameter with `reversal_` (for example, `reversal_123`).

#### UK

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customerCashBalanceTransaction =
  await stripe.testHelpers.customers.fundCashBalance("cus_xxxxxxxxx", {
    amount: 1000,
    currency: "gbp",
    reference: "REF-4242",
  });
```

#### EU

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customerCashBalanceTransaction =
  await stripe.testHelpers.customers.fundCashBalance("cus_xxxx", {
    amount: 1000,
    currency: "eur",
    reference: "REF-4242",
  });
```

#### JP

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customerCashBalanceTransaction =
  await stripe.testHelpers.customers.fundCashBalance("cus_xxxx", {
    amount: 10000,
    currency: "jpy",
  });
```

#### MX

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customerCashBalanceTransaction =
  await stripe.testHelpers.customers.fundCashBalance("cus_xxxx", {
    amount: 1000,
    currency: "mxn",
    reference: "123456",
  });
```

## Handling temporary availability issues

The following error codes indicate temporary issues with the availability of the payment method:

| Code                                 | Description                                                                                                                                                                 | Handling                                                                                                                                                                                                                                 |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_method_rate_limit_exceeded` | Too many requests were made in quick succession for this payment method, which has stricter limits than the [API-wide rate limits](https://docs.stripe.com/rate-limits.md). | These errors can persist for several API requests when many of your customers try to use the same payment method, such as during an ongoing sale on your website. In this case, ask your customers to choose a different payment method. |

> If you anticipate heavy usage in general or because of an upcoming event, contact us as soon as you know about it.

## Optional: Collecting payment method options from your customer

If needed, collect your customer’s preferred funding type on your site and confirm the payment intent using [confirmCustomerBalancePayment](https://docs.stripe.com/js/payment_intents/confirm_customer_balance_payment) method for [Stripe.js](https://docs.stripe.com/js.md).

Display an HTML form to collect the customer’s preferred bank transfer funding details. Use this input to populate the `payment_method_options`.

See the [JS reference docs](https://docs.stripe.com/js/payment_intents/confirm_customer_balance_payment) for a full list of available `payment_method_options` parameters for `confirmCustomerBalancePayment`.

Here’s an example use case: If you’re a merchant in Ireland, and you’re not sure about which country a customer is in, you can create a `PaymentIntent` with `payment_method_options[customer_balance][bank_transfer][eu_bank_transfer][country]` set to ‘IE’ first. Then use [confirmCustomerBalancePayment](https://docs.stripe.com/js/payment_intents/confirm_customer_balance_payment) method to update the country based on user input.

### Sample code

```javascript
const { paymentIntent, error } = await stripe.confirmCustomerBalancePayment(
  "{PAYMENT_INTENT_CLIENT_SECRET}",
  {
    payment_method: {
      customer_balance: {},
    },
    payment_method_options: {
      customer_balance: {
        funding_type: "bank_transfer",
        bank_transfer: {
          type: "eu_bank_transfer",
          eu_bank_transfer: {
            country: "FR",
          },
        },
      },
    },
  },
  {
    handleActions: false,
  },
);
if (error) {
  // Inform the customer that there was an error.
} else if (paymentIntent.status === "requires_payment_method") {
  // If `payment_method_options.funding_type` wasn't set this
  // is where you would need to handle the insufficient customer
  // balance state.
} else if (paymentIntent.status === "requires_action") {
  // If the current customer balance is insufficient to cover
  // the amount, and you've passed
  // `payment_method_options.funding_type` for funding the
  // customer balance, you can display the bank transfer
  // instructions to your user.
  if (paymentIntent.next_action.type === "display_bank_transfer_instructions") {
    // Bank transfer details can be found under:
    // paymentIntent.next_action.display_bank_transfer_instructions
  }
}
```
