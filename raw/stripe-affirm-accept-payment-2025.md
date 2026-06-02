<!-- Source URL: https://docs.stripe.com/payments/affirm/accept-a-payment -->
<!-- Fetched: 2026-05-06 -->

# Accept an Affirm payment

Learn how to accept Affirm, a buy now and pay later payment method.

> This guide helps you integrate Affirm in your online checkout flow. For in-person payments with Stripe Terminal, visit [Additional payment methods](https://docs.stripe.com/terminal/payments/additional-payment-methods.md).

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/affirm/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Affirm is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage), [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method that requires customers to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers are redirected to the Affirm site, where they agree to the terms of an installment plan. When the customer accepts the terms, funds are guaranteed and transferred to your Stripe account. The customer repays Affirm directly over time.

> Before you start the integration, make sure your account is eligible for Affirm by navigating to your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

## Determine compatibility

**Customer Geography**: Canada, US

**Supported currencies**: `cad, usd`

**Presentment currencies**: `cad, usd`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support Affirm payments:

- You can only use one-time line items. Affirm doesn’t support recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans.
- Express all *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) in your domestic currency.

## Accept a payment

> This guide builds on the foundational [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?ui=stripe-hosted) Checkout integration.

This guides you through enabling Affirm and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable Affirm as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `affirm` to the list of `payment_method_types`.
1. Make sure all your `line_items` use your domestic currency and the total amount doesn’t exceed Affirm’s [transaction amount limits](https://docs.stripe.com/payments/affirm.md#payment-options).
1. Optionally, specify which countries Checkout allows for shipping locations through `shipping_address_collection[allowed_countries]`.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "usd",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 5000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "affirm"],
  shipping_address_collection: {
    allowed_countries: ["CA", "US"],
  },
  success_url: "https://example.com/success",
});
```

#### Full embedded page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "usd",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 5000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "affirm"],
  return_url: "https://example.com/return",
  shipping_address_collection: {
    allowed_countries: ["CA", "US"],
  },
  ui_mode: "embedded_page",
});
```

If you don’t want to collect shipping addresses with Checkout, you can also provide the shipping address using `payment_intent_data[shipping]`. Doing so helps with loan acceptance rates.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "usd",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 5000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "affirm"],
  payment_intent_data: {
    shipping: {
      name: "Jenny Rosen",
      address: {
        line1: "1234 Main Street",
        city: "San Francisco",
        state: "CA",
        country: "US",
        postal_code: "94111",
      },
    },
  },
  success_url: "https://example.com/success",
});
```

#### Full embedded page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "usd",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 5000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "affirm"],
  return_url: "https://example.com/return",
  payment_intent_data: {
    shipping: {
      name: "Jenny Rosen",
      address: {
        line1: "1234 Main Street",
        city: "San Francisco",
        state: "CA",
        country: "US",
        postal_code: "94111",
      },
    },
  },
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

[Use a method such as webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to handle order *fulfillment* (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected), instead of relying on your customer to return to the payment status page.

The following events are sent when the payment status changes:

| Event Name                                                                                                             | Description                                                                                                                                | Next steps                                                 |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed)       | The customer successfully authorized the payment by submitting the Checkout form.                                                          | Wait for the payment to succeed or fail.                   |
| [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded)           | The customer’s payment succeeded. The `PaymentIntent` transitions to `succeeded`.                                                          | Fulfill the goods or services that the customer purchased. |
| [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) | The customer’s payment was declined, or failed for some other reason. The `PaymentIntent` returns to the `requires_payment_method` status. | Email the customer to request that they place a new order. |

Learn more about [fulfilling orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

When testing your Checkout integration, select Affirm as the payment method and click the **Pay** button.

Test your Affirm integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent transitions from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, close the Affirm modal window and verify that payment failed. The PaymentIntent transitions from `requires_action` to `requires_payment_method`.

When redirected to the Affirm sandbox, Affirm may ask for the last four digits of your SSN. Affirm suggests using `'0000'` or `'5678'`.

For [manual capture](https://docs.stripe.com/payments/affirm/accept-a-payment.md#manual-capture) PaymentIntents in testmode, the uncaptured PaymentIntent auto-expires 10 minutes after successful authorization.

## Failed payments

Affirm takes into account multiple factors when deciding to accept or decline a transaction (for example, the length of time buyer has used Affirm, the outstanding amount the customer has to repay, and the value of the current order).

Always present additional payment options such as `card` in your checkout flow, as Affirm payments have a higher rate of decline than many payment methods. In these cases, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

Other than a payment being declined, for an Affirm [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) with a status of `requires_action`, customers need to complete the payment within 12 hours after you redirect them to the Affirm site. If the customer takes no action within 12 hours, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

In these cases, inform your customer to try again with a different payment option presented in your checkout flow.

## Error codes

These are the common error codes and corresponding recommended actions:

| Error code                               | Recommended action                                                                                                                                                                                                                 |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_payment_attempt_failed`  | A generic failure indicating the Affirm checkout failed. Additional information might be available in the charge outcome reason.                                                                                                   |
| `payment_method_provider_decline`        | Affirm declined the customer’s payment. As a next step, the customer needs to contact Affirm for more information.                                                                                                                 |
| `payment_intent_payment_attempt_expired` | The customer never completed the payment on Affirm’s checkout page, and the payment session has expired. Stripe automatically expires PaymentIntents that aren’t successfully authorized 12 hours after initial checkout creation. |
| `payment_method_not_available`           | Affirm experienced a service related error and is unable to complete the request. Retry at a later time.                                                                                                                           |
| `amount_too_small`                       | Enter an amount within Affirm’s [default transactions limits](https://docs.stripe.com/payments/affirm.md#payment-options).                                                                                                         |
| `amount_too_large`                       | Enter an amount within Affirm’s [default transactions limits](https://docs.stripe.com/payments/affirm.md#payment-options).                                                                                                         |

Some errors might have additional insight included in the charge outcome reason:

| Outcome Reason             | What this means                                                                                                                                                                                                                                                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `generic_decline`          | The default outcome reason for a payment error. This usually indicates that the partner declined the payment (for example, because of insufficient funds), the bank issuer declined the charge, the transaction included a high-risk purchase, or a similar reason. Stripe might not always receive a decline reason for these cases. |
| `affirm_checkout_canceled` | Either the customer has explicitly canceled the Affirm checkout or Affirm has rejected the customer’s loan eligibility. Stripe can’t distinguish the difference between these two types of events.                                                                                                                                    |

# Checkout Sessions API

> This is a Checkout Sessions API for when payment-ui is elements and api-integration is checkout. View the full page at https://docs.stripe.com/payments/affirm/accept-a-payment?payment-ui=elements&api-integration=checkout.

To determine which API meets your business needs, see the [comparison guide](https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md).

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to embed a custom Stripe payment form in your website or application and offer payment methods to customers. For advanced configurations and customizations, refer to the [Accept a Payment](https://docs.stripe.com/payments/accept-a-payment.md) integration guide.

## Determine compatibility

**Customer Geography**: Canada, US

**Supported currencies**: `cad, usd`

**Presentment currencies**: `cad, usd`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support Affirm payments:

- You can only use one-time line items. Affirm doesn’t support recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans.
- Express all *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) in your domestic currency.

## Set up the server [Server-side]

Use the official Stripe libraries to access the API from your application.

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a Checkout Session [Server-side]

Add an endpoint on your server that creates a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) and returns its [client secret](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-client_secret) to your front end. A Checkout Session represents your customer’s session as they pay for one-time purchases or subscriptions. Checkout Sessions expire 24 hours after creation.

We recommend using [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) to dynamically display the most relevant eligible payment methods to each customer to maximize conversion. You can also [manually list payment methods](https://docs.stripe.com/payments/payment-methods/integration-options.md#listing-payment-methods-manually), which disables dynamic payment methods.

#### Manage payment methods from the Dashboard

#### TypeScript

```javascript
import express, {Express} from 'express';

const app: Express = express();

app.post('/create-checkout-session', async (req: Express.Request, res: Express.Response) => {
  const session = await stripe.checkout.sessions.create({
    line_items: [
      {
        price_data: {
          currency: 'usd',
          product_data: {
            name: 'T-shirt',
          },
          unit_amount: 5000,
        },
        quantity: 1,
      },
    ],
    mode: 'payment',
    ui_mode: 'elements',
    return_url: 'https://example.com/return?session_id={CHECKOUT_SESSION_ID}'
  });

  res.json({checkoutSessionClientSecret: session.client_secret});
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

#### Manually list payment methods

#### TypeScript

```javascript
import express, {Express} from 'express';

const app: Express = express();

app.post('/create-checkout-session', async (req: Express.Request, res: Express.Response) => {
  const session = await stripe.checkout.sessions.create({
    line_items: [
      {
        price_data: {
          currency: 'usd',
          product_data: {
            name: 'T-shirt',
          },
          unit_amount: 5000,
        },
        quantity: 1,
      },
    ],
    mode: 'payment',
    ui_mode: 'elements',
    payment_method_types: ['affirm'],
    return_url: 'https://example.com/return?session_id={CHECKOUT_SESSION_ID}'
  });

  res.json({checkoutSessionClientSecret: session.client_secret});
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

## Set up the front end [Client-side]

#### HTML + JS

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

Make sure you’re on the latest Stripe.js version by including the following script tag `<script src=“https://js.stripe.com/dahlia/stripe.js”></script>`. Learn more about [Stripe.js versioning](https://docs.stripe.com/sdks/stripejs-versioning.md).

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

> Stripe provides an npm package that you can use to load Stripe.js as a module. See the [project on GitHub](https://github.com/stripe/stripe-js). Version [7.0.0](https://www.npmjs.com/package/%40stripe/stripe-js/v/7.0.0) or later is required.

Initialize stripe.js.

```js
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

#### React

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry. You need at least version 5.0.0 for React Stripe.js and version 8.0.0 for the Stripe.js loader.

```bash
npm install --save @stripe/react-stripe-js@^5.0.0 @stripe/stripe-js@^8.0.0
```

Initialize a `stripe` instance on your front end with your publishable key.

```javascript
import { loadStripe } from "@stripe/stripe-js";
const stripe = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");
```

## Initialize Checkout [Client-side]

#### HTML + JS

Call [initCheckoutElementsSdk](https://docs.stripe.com/js/custom_checkout/init), passing in `clientSecret`.

`initCheckoutElementsSdk` returns a [Checkout](https://docs.stripe.com/js/custom_checkout) object that contains data from the Checkout Session and methods to update it.

Read the `total` and `lineItems` from [actions.getSession()](https://docs.stripe.com/js/custom_checkout/session), and display them in your UI. This lets you turn on new features with minimal code changes. For example, adding [manual currency prices](https://docs.stripe.com/payments/custom/localize-prices/manual-currency-prices.md) requires no UI changes if you display the `total`.

```html
<div id="checkout-container"></div>
```

```javascript
const clientSecret = fetch("/create-checkout-session", { method: "POST" })
  .then((response) => response.json())
  .then((json) => json.client_secret);

const checkout = stripe.initCheckoutElementsSdk({ clientSecret });
const loadActionsResult = await checkout.loadActions();

if (loadActionsResult.type === "success") {
  const session = loadActionsResult.actions.getSession();
  const checkoutContainer = document.getElementById("checkout-container");

  checkoutContainer.append(JSON.stringify(session.lineItems, null, 2));
  checkoutContainer.append(document.createElement("br"));
  checkoutContainer.append(`Total: ${session.total.total.amount}`);
}
```

#### React

Wrap your application with the [CheckoutElementsProvider](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider) component, passing in `clientSecret` and the `stripe` instance.

```jsx
import React from "react";
import { CheckoutElementsProvider } from "@stripe/react-stripe-js/checkout";
import CheckoutForm from "./CheckoutForm";

const clientSecret = fetch("/create-checkout-session", { method: "POST" })
  .then((response) => response.json())
  .then((json) => json.client_secret);

const App = () => {
  return (
    <CheckoutElementsProvider stripe={stripe} options={{ clientSecret }}>
      <CheckoutForm />
    </CheckoutElementsProvider>
  );
};

export default App;
```

Access the [Checkout](https://docs.stripe.com/js/custom_checkout) object in your checkout form component by using the `useCheckoutElements()` hook. The `Checkout` object contains data from the Checkout Session and methods to update it.

Read the `total` and `lineItems` from the `Checkout` object, and display them in your UI. This lets you enable features with minimal code changes. For example, adding [manual currency prices](https://docs.stripe.com/payments/custom/localize-prices/manual-currency-prices.md) requires no UI changes if you display the `total`.

```jsx
import React from "react";
import { useCheckoutElements } from "@stripe/react-stripe-js/checkout";

const CheckoutForm = () => {
  const checkoutState = useCheckoutElements();

  if (checkoutState.type === "loading") {
    return <div>Loading...</div>;
  }

  if (checkoutState.type === "error") {
    return <div>Error: {checkoutState.error.message}</div>;
  }

  return (
    <form>
      {JSON.stringify(checkoutState.checkout.lineItems, null, 2)}
      {/* A formatted total amount */}
      Total: {checkoutState.checkout.total.total.amount}
    </form>
  );
};
```

## Collect customer email [Client-side]

#### HTML + JS

You must provide a valid customer email when completing a Checkout Session.

These instructions create an email input and use [updateEmail](https://docs.stripe.com/js/custom_checkout/update_email) from the `Checkout` object.

Alternatively, you can:

- Pass in [customer_email](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_email), [customer_account](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_account) (for customers represented as customer-configured `Account` objects), or [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) (for customers represented as `Customer` objects) when creating the Checkout Session. Stripe validates emails provided this way.
- Pass in an email you already validated on [checkout.confirm](https://docs.stripe.com/js/custom_checkout/confirm).

```html
<input type="text" id="email" />
<div id="email-errors"></div>
```

```javascript
const checkout = stripe.initCheckoutElementsSdk({ clientSecret });
const loadActionsResult = await checkout.loadActions();

if (loadActionsResult.type === "success") {
  const { actions } = loadActionsResult;
  const emailInput = document.getElementById("email");
  const emailErrors = document.getElementById("email-errors");

  emailInput.addEventListener("input", () => {
    // Clear any validation errors
    emailErrors.textContent = "";
  });

  emailInput.addEventListener("blur", () => {
    const newEmail = emailInput.value;
    actions.updateEmail(newEmail).then((result) => {
      if (result.error) {
        emailErrors.textContent = result.error.message;
      }
    });
  });
}
```

#### React

You must provide a valid customer email when completing a Checkout Session.

These instructions create an email input and use [updateEmail](https://docs.stripe.com/js/react_stripe_js/checkout/update_email) from the `Checkout` object.

Alternatively, you can:

- Pass in [customer_email](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_email), [customer_account](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_account) (for customers represented as customer-configured `Account` objects), or [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) (for customers represented as `Customer` objects) when creating the Checkout Session. Stripe validates emails provided this way.
- Pass in an email you already validated on [confirm](https://docs.stripe.com/js/react_stripe_js/checkout/confirm).

```jsx
import React from "react";
import { useCheckoutElements } from "@stripe/react-stripe-js/checkout";

const EmailInput = () => {
  const checkoutState = useCheckoutElements();
  const [email, setEmail] = React.useState("");
  const [error, setError] = React.useState(null);

  if (checkoutState.type === "loading") {
    return <div>Loading...</div>;
  } else if (checkoutState.type === "error") {
    return <div>Error: {checkoutState.error.message}</div>;
  }

  const handleBlur = () => {
    checkoutState.checkout.updateEmail(email).then((result) => {
      if (result.type === "error") {
        setError(result.error);
      }
    });
  };

  const handleChange = (e) => {
    setError(null);
    setEmail(e.target.value);
  };

  return (
    <div>
      <label htmlFor="checkout-form-email">Email</label>
      <input
        id="checkout-form-email"
        type="email"
        value={email}
        onChange={handleChange}
        onBlur={handleBlur}
      />
      {error && <div>{error.message}</div>}
    </div>
  );
};

export default EmailInput;
```

## Collect payment details [Client-side]

Collect payment details on the client with the [Payment Element](https://docs.stripe.com/payments/payment-element.md). The Payment Element is a prebuilt UI component that simplifies collecting payment details for a variety of payment methods.

The Payment Element contains an iframe that securely sends payment information to Stripe over an HTTPS connection. Avoid placing the Payment Element within another iframe because some payment methods require redirecting to another page for payment confirmation.

If you choose to use an iframe and want to accept Apple Pay or Google Pay, the iframe must have the [allow](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-allowpaymentrequest) attribute set to equal `"payment *"`.

The checkout page address must start with `https://` rather than `http://` for your integration to work. You can test your integration without using HTTPS, but remember to [enable it](https://docs.stripe.com/security/guide.md#tls) when you’re ready to accept live payments.

#### HTML + JS

First, create a container DOM element to mount the [Payment Element](https://docs.stripe.com/payments/payment-element.md). Then create an instance of the `Payment Element` using [checkout.createPaymentElement](https://docs.stripe.com/js/custom_checkout/create_payment_element) and mount it by calling [element.mount](https://docs.stripe.com/js/element/mount), providing either a CSS selector or the container DOM element.

```html
<div id="payment-element"></div>
```

```javascript
const paymentElement = checkout.createPaymentElement();
paymentElement.mount("#payment-element");
```

See the [Stripe.js docs](https://docs.stripe.com/js/custom_checkout/create_payment_element#custom_checkout_create_payment_element-options) to view the supported options.

You can [customize the appearance](https://docs.stripe.com/payments/checkout/customization/appearance.md) of all Elements by passing [elementsOptions.appearance](https://docs.stripe.com/js/custom_checkout/init#custom_checkout_init-options-elementsOptions-appearance) when initializing Checkout on the front end.

#### React

Mount the [Payment Element](https://docs.stripe.com/payments/payment-element.md) component within the [CheckoutElementsProvider](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider).

```jsx
import React from "react";
import {
  PaymentElement,
  useCheckoutElements,
} from "@stripe/react-stripe-js/checkout";

const CheckoutForm = () => {
  const checkoutState = useCheckoutElements();

  if (checkoutState.type === "loading") {
    return <div>Loading...</div>;
  }

  if (checkoutState.type === "error") {
    return <div>Error: {checkoutState.error.message}</div>;
  }

  return (
    <form>
      {JSON.stringify(checkoutState.checkout.lineItems, null, 2)}
      {/* A formatted total amount */}
      Total: {checkoutState.checkout.total.total.amount}
      <PaymentElement options={{ layout: "accordion" }} />
    </form>
  );
};

export default CheckoutForm;
```

See the [Stripe.js docs](https://docs.stripe.com/js/custom_checkout/create_payment_element#custom_checkout_create_payment_element-options) to view the supported options.

You can [customize the appearance](https://docs.stripe.com/payments/checkout/customization/appearance.md) of all Elements by passing [elementsOptions.appearance](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider#react_checkout_provider-options-elementsOptions-appearance) to the [CheckoutElementsProvider](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider).

## Submit the payment [Client-side]

#### HTML + JS

Render a **Pay** button that calls [confirm](https://docs.stripe.com/js/custom_checkout/confirm) from the `Checkout` instance to submit the payment.

```html
<button id="pay-button">Pay</button>
<div id="confirm-errors"></div>
```

```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret });

checkout.on("change", (session) => {
  document.getElementById("pay-button").disabled = !session.canConfirm;
});

const loadActionsResult = await checkout.loadActions();

if (loadActionsResult.type === "success") {
  const { actions } = loadActionsResult;
  const button = document.getElementById("pay-button");
  const errors = document.getElementById("confirm-errors");
  button.addEventListener("click", () => {
    // Clear any validation errors
    errors.textContent = "";

    actions.confirm().then((result) => {
      if (result.type === "error") {
        errors.textContent = result.error.message;
      }
    });
  });
}
```

#### React

Render a **Pay** button that calls [confirm](https://docs.stripe.com/js/custom_checkout/confirm) from [useCheckoutElements](https://docs.stripe.com/js/react_stripe_js/checkout/use_checkout_elements) to submit the payment.

```jsx
import React from "react";
import { useCheckoutElements } from "@stripe/react-stripe-js/checkout";

const PayButton = () => {
  const checkoutState = useCheckoutElements();
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState(null);

  if (checkoutState.type !== "success") {
    return null;
  }

  const handleClick = () => {
    setLoading(true);
    checkoutState.checkout.confirm().then((result) => {
      if (result.type === "error") {
        setError(result.error);
      }
      setLoading(false);
    });
  };

  return (
    <div>
      <button
        disabled={!checkoutState.checkout.canConfirm || loading}
        onClick={handleClick}
      >
        Pay
      </button>
      {error && <div>{error.message}</div>}
    </div>
  );
};

export default PayButton;
```

## Test your integration

To test your integration, choose the payment method and tap **Pay**. In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), this redirects you to a test payment page where you can approve or decline the payment.

In live mode, tapping **Pay** redirects you to the Affirm website—you don’t have the option to approve or decline the payment with Affirm.

# Payment Intents API

> This is a Payment Intents API for when payment-ui is elements and api-integration is paymentintents. View the full page at https://docs.stripe.com/payments/affirm/accept-a-payment?payment-ui=elements&api-integration=paymentintents.

To determine which API meets your business needs, see the [comparison guide](https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md).

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to embed a custom Stripe payment form in your website or application and offer payment methods to customers. For advanced configurations and customizations, refer to the [Accept a Payment](https://docs.stripe.com/payments/accept-a-payment.md) integration guide.

## Set up Stripe [Server-side]

To get started, [create a Stripe account](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Collect payment details [Client-side]

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
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
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
  mode: "payment",
  amount: 5000,
  currency: "usd",
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout formconst elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: "accordion" };
const paymentElement = elements.create("payment", paymentElementOptions);
paymentElement.mount("#payment-element");
```

#### List payment methods manually

To manually list the payment methods you want to be available, add each one to `paymentMethodTypes`.

Then, create an instance of the Payment Element and mount it to the container DOM node.

```javascript
const options = {
  mode: "payment",
  amount: 5000,
  currency: "usd",
  paymentMethodTypes: ["affirm"],
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout formconst elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: "accordion" };
const paymentElement = elements.create("payment", paymentElementOptions);
paymentElement.mount("#payment-element");
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
    mode: "payment",
    amount: 5000,
    currency: "usd",
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

#### List payment methods manually

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
    mode: "payment",
    amount: 5000,
    currency: "usd",
    paymentMethodTypes: ["affirm"],
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

Use the `PaymentElement` component to build your form.

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
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the customer's Account ID.
    customer_account: "{{CUSTOMER_ACCOUNT_ID}}",
    amount: 5000,
    currency: "usd",
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the Customer ID.
    customer: customer.id,
    amount: 5000,
    currency: "usd",
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### List payment methods manually

When the customer submits your payment form, use a *PaymentIntent* (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) to facilitate the confirmation and payment process. Create a PaymentIntent on your server with an `amount`, `currency`, and one or more payment methods using `payment_method_types`. To prevent malicious customers from choosing their own prices, always decide how much to charge on the server-side (a trusted environment) and not the client.

Included on a PaymentIntent is a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)). Return this value to your client for Stripe.js to use to securely complete the payment process.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the customer's Account ID.
    customer_account: customer_account.id,
    amount: 5000,
    currency: "usd",
    payment_method_types: ["affirm"],
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    // To allow saving and retrieving payment methods, provide the Customer ID.
    customer: customer.id,
    amount: 5000,
    currency: "usd",
    payment_method_types: ["affirm"],
  });
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

## Submit the payment to Stripe [Client-side]

Use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) to complete the payment using details from the Payment Element.

Provide a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe redirects the user after they complete the payment. Your user might be initially redirected to an intermediate site, such as a bank authorization page, before being redirected to the `return_url`. Card payments immediately redirect to the `return_url` when a payment is successful.

If you don’t want to redirect for card payments after payment completion, you can set [redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect) to `if_required`. This only redirects customers that check out with redirect-based payment methods.

#### HTML + JS

```javascript
const form = document.getElementById("payment-form");
const submitBtn = document.getElementById("submit");

const handleError = (error) => {
  const messageContainer = document.querySelector("#error-message");
  messageContainer.textContent = error.message;
  submitBtn.disabled = false;
};

form.addEventListener("submit", async (event) => {
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
  const res = await fetch("/create-intent", {
    method: "POST",
  });

  const { client_secret: clientSecret } = await res.json();

  // Confirm the PaymentIntent using the details collected by the Payment Element
  const { error } = await stripe.confirmPayment({
    elements,
    clientSecret,
    confirmParams: {
      return_url: "https://example.com/order/123/complete",
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
import React, { useState } from "react";
import {
  useStripe,
  useElements,
  PaymentElement,
} from "@stripe/react-stripe-js";

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
    const res = await fetch("/create-intent", {
      method: "POST",
    });

    const { client_secret: clientSecret } = await res.json();

    // Confirm the PaymentIntent using the details collected by the Payment Element
    const { error } = await stripe.confirmPayment({
      elements,
      clientSecret,
      confirmParams: {
        return_url: "https://example.com/order/123/complete",
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

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Separate authorization and capture

You can separate authorization and capture to create a charge now, but capture funds later. Stripe cancels the PaymentIntent and sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event if the payment isn’t captured during the 7-day window.

If you’re certain you can’t capture the payment, we recommend [canceling the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment) instead of waiting for the 7-day window to elapse.

### 1. Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s Affirm account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  confirm: true,
  currency: "usd",
  payment_method_types: ["affirm"],
  payment_method_data: {
    type: "payment_method",
  },
  capture_method: "manual",
  return_url: "https://www.example.com/checkout/done",
});
```

### 2. Capture the funds

After the authorization succeeds, the [PaymentIntent status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture`. To capture the authorized funds, make a PaymentIntent [capture](https://docs.stripe.com/api/payment_intents/capture.md) request.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{PAYMENT_INTENT_ID}",
);
```

Stripe captures the total authorized amount by default. You can also specify `amount_to_capture` to be less than or equal to the total.

### (Optional) Cancel the authorization

If you need to cancel an authorization, you can [cancel the PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md).

## Test your integration

To test your integration, choose the payment method and tap **Pay**. In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), this redirects you to a test payment page where you can approve or decline the payment.

In live mode, tapping **Pay** redirects you to the Affirm website—you don’t have the option to approve or decline the payment with Affirm.

## Error codes

The following table details common error codes and recommended actions:

| Error code                                                | Recommended action                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_invalid_currency`                         | Enter a supported currency.                                                                                                                                                                                                                                                                                                                                       |
| `missing_required_parameter`                              | Check the error message for more information about the required parameter.                                                                                                                                                                                                                                                                                        |
| `payment_intent_payment_attempt_failed`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling.                                                                                      |
| `payment_intent_authentication_failure`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling. This error occurs when you manually trigger a failure when testing your integration. |
| `payment_intent_redirect_confirmation_without_return_url` | Provide a `return_url` when confirming a PaymentIntent.                                                                                                                                                                                                                                                                                                           |

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/affirm/accept-a-payment?payment-ui=direct-api.

Stripe users can use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md)– a single integration path for creating payments using any supported method–to accept [Affirm](https://www.affirm.com/) payments from customers in the following countries:

- Canada
- United States

Accepting Affirm payments on your website consists of:

- Creating an object to track a payment
- Collecting payment method information
- Submitting the payment to Stripe for processing
- Handling the Affirm redirect and relevant webhook events

## Set up Stripe [Server-side]

First, [create a Stripe account](https://dashboard.stripe.com/register) or [sign in](https://dashboard.stripe.com/login).

Use our official libraries to access the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

First, create a `PaymentIntent` on your server and specify the amount to collect and the currency. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add affirm to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 6000,
  currency: "usd",
  payment_method_types: ["affirm"],
});
```

You can also use the Payment Element and manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow. See [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=elements&api-integration=checkout) for more details.

### Retrieve the client secret

The PaymentIntent includes a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

#### Single-page application

Retrieve the client secret from an endpoint on your server, using the browser’s `fetch` function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

#### Node.js

```javascript
const express = require("express");
const app = express();

app.get("/secret", async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
    res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

And then fetch the client secret with JavaScript on the client side:

```javascript
(async () => {
  const response = await fetch("/secret");
  const { client_secret: clientSecret } = await response.json();
  // Render the form using the clientSecret
})();
```

#### Server-side rendering

Pass the client secret to the client from your server. This approach works best if your application generates static content on the server before sending it to the browser.

Add the [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) in your checkout form. In your server-side code, retrieve the client secret from the PaymentIntent:

#### Node.js

```html
<form id="payment-form" data-secret="{{ client_secret }}">
  <div id="payment-element">
    <!-- Elements will create form elements here -->
  </div>

  <button id="submit">Submit</button>
</form>
```

```javascript
const express = require("express");
const expressHandlebars = require("express-handlebars");
const app = express();

app.engine(".hbs", expressHandlebars({ extname: ".hbs" }));
app.set("view engine", ".hbs");
app.set("views", "./views");

app.get("/checkout", async (req, res) => {
  const intent = // ... Fetch or create the PaymentIntent
    res.render("checkout", { client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

## Collect payment method details and submit [Client-side]

When a customer clicks to pay with Affirm, we recommend you use [Stripe.js](https://docs.stripe.com/payments/elements.md) to submit the payment to Stripe. Stripe.js is our foundational JavaScript library for building payment flows. It will automatically handle integration complexities, and enables you to easily extend your integration to other payment methods in the future.

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
var stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Rather than sending the entire PaymentIntent object to the client, use its client secret from Step 1. This is different from your API keys that authenticate Stripe API requests.

Handle the client secret carefully, because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

**Improve payment success rates with additional details**

We recommend passing [shipping](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-shipping) and [billing](https://docs.stripe.com/api/payment_methods/create.md#create_payment_method-billing_details) details to improve conversion rates, although these aren’t required.

This integration guide suggests passing the shipping and billing information on the client after the customer selects their payment method.

If you pass these fields, the shipping address should include valid data in `line1`, `city`, `state`, `postal_code`, and `country`. Similarly, billing details must include valid data in all of `line1`, `city`, `state`, `postal_code`, and `country`.

**Confirm the PaymentIntent**

Use `stripe.confirmAffirmPayment` to handle the redirect away from your page and to complete the payment. You must also pass a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe redirects the user after they complete the payment on the Affirm website or mobile application.

On Affirm’s payments page, the customer selects the payment options available to them. See the overview page for more details. You can’t limit or pre-select payment options on the Affirm payments page—deferring this choice to the consumer maximizes their opportunity to transact with you.

```javascript
// Redirects away from the client
stripe
  .confirmAffirmPayment("{{PAYMENT_INTENT_CLIENT_SECRET}}", {
    payment_method: {
      // Billing information is optional but recommended to pass in.
      billing_details: {
        email: "jenny@rosen.com",
        name: "Jenny Rosen",
        address: {
          line1: "1234 Main Street",
          city: "San Francisco",
          state: "CA",
          country: "US",
          postal_code: "94111",
        },
      },
    },

    // Shipping information is optional but recommended to pass in.
    shipping: {
      name: "Jenny Rosen",
      address: {
        line1: "1234 Main Street",
        city: "San Francisco",
        state: "CA",
        country: "US",
        postal_code: "94111",
      },
    },
    // Return URL where the customer should be redirected after the authorization.
    return_url: "https://example.com/checkout/complete",
  })
  .then(function (result) {
    if (result.error) {
      // Inform the customer that there was an error.
      console.log(result.error.message);
    }
  });
```

When your customer submits a payment, Stripe redirects them to the `return_url` and includes the following URL query parameters. The return page can use them to get the status of the PaymentIntent so it can display the payment status to the customer.

When you specify the `return_url`, you can also append your own query parameters for use on the return page.

| Parameter                      | Description                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                                                                                                                                                                                                                             |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. For subscription integrations, this client_secret is also exposed on the `Invoice` object through [`confirmation_secret`](https://docs.stripe.com/api/invoices/object.md#invoice_object-confirmation_secret) |

When the customer is redirected back to your site, you can use the `payment_intent_client_secret` to query for the PaymentIntent and display the transaction status to your customer.

## Test Affirm integration

Test your Affirm integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent transitions from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **X** in the top left corner. The PaymentIntent will transition from `requires_action` to `requires_payment_method`.

When redirected to the Affirm sandbox, Affirm may ask for the last four digits of your SSN. Affirm suggests using `'0000'` or `'5678'`.

## Optional: Separate authorization and capture

Affirm supports [separate authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md). If there’s a delay between the payment and delivering the goods to your customer, authorize the payment first and capture it later. At the point of capture, Affirm initiates the due dates on the customer’s subsequent repayments. **You must capture an authorized Affirm payment within 30 days of the authorization**. Otherwise, the authorization automatically cancels and you can no longer capture the payment. Stripe will also cancel the PaymentIntent and send a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event if this happens.

> For very large order amounts, Affirm might require a down payment from the customer during authorization. If you cancel the payment or the authorization expires, Affirm refunds the down payment.

If you know that you can’t capture the payment, we recommend [canceling the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment) instead of waiting for the 30-day window to elapse. Proactively canceling the PaymentIntent immediately refunds the first installment to your customer, avoiding any confusion about charges on their statement.

### 1. Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s Affirm account.

```bash
curl https://api.stripe.com/v1/payment_intents \
  -u <<YOUR_SECRET_KEY>>: \
  -d "amount"=6000 \
  -d "confirm"="true" \
  -d "currency"="usd" \
  -d "payment_method_types[]"="affirm" \
  -d "capture_method"="manual" \
  // Shipping address is optional but recommended to pass in.
  -d "shipping[name]"="Jenny Rosen" \
  -d "shipping[address][line1]"="1234 Main Street" \
  -d "shipping[address][city]"="San Francisco" \
  -d "shipping[address][state]"="CA" \
  -d "shipping[address][country]"="US" \
  -d "shipping[address][postal_code]"=94111 \
  -d "payment_method_data[type]"="affirm" \
  -d "return_url"="https://www.example.com/checkout/done"
```

### 2. Capture the funds

After the authorization succeeds, the PaymentIntent [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture`. To capture the authorized funds, make a PaymentIntent [capture](https://docs.stripe.com/api/payment_intents/capture.md) request. The total authorized amount is captured by default. You can’t capture more or less than the total.

```bash
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/capture \
  -u <<YOUR_SECRET_KEY>>: \
```

### (Optional) Cancel the authorization

If you need to cancel an authorization, you can [cancel the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment).

## Optional: Handle the Affirm redirect manually

We recommend relying on Stripe.js to handle Affirm redirects and payments client-side with `confirmAffirmPayment`. Using Stripe.js makes it much easier to extend your integration to other payment methods. However, you can also manually redirect your customers on your server by following these steps:

- Create and confirm a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) of type `affirm`. By specifying `payment_method_data`, we create a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) and immediately use it with this PaymentIntent.

  You must also provide the redirect URL for your customer after they complete their payment in the `return_url` field. You can provide your own query parameters in this URL. These parameters are included in the final URL upon completing the redirect flow.

  ```bash
  curl https://api.stripe.com/v1/payment_intents \
  -u <<YOUR_SECRET_KEY>>: \
  -d "amount"=6000 \
  -d "confirm"="true" \
  -d "currency"="usd" \
  -d "payment_method_types[]"="affirm" \
  // Shipping address is optional but recommended to pass in.
  -d "shipping[name]"="Jenny Rosen" \
  -d "shipping[address][line1]"="1234 Main Street" \
  -d "shipping[address][city]"="San Francisco" \
  -d "shipping[address][state]"="CA" \
  -d "shipping[address][country]"="US" \
  -d "shipping[address][postal_code]"=94111 \
  // Billing details are optional but recommended to pass in.
  -d "payment_method_data[billing_details][name]"="Jenny Rosen" \
  -d "payment_method_data[billing_details][email]"="jenny@example.com" \
  -d "payment_method_data[billing_details][address][line1]"="1234 Main Street" \
  -d "payment_method_data[billing_details][address][city]"="San Francisco" \
  -d "payment_method_data[billing_details][address][state]"="CA" \
  -d "payment_method_data[billing_details][address][country]"="US" \
  -d "payment_method_data[billing_details][address][postal_code]"=94111 \
  -d "payment_method_data[type]"="affirm" \
  -d "return_url"="https://example.com/checkout/complete"
  ```

  The created `PaymentIntent` has a status of `requires_action` and the type for `next_action` is `redirect_to_url`.

  ```json
  {
    "status": "requires_action",
    "next_action": {
      "type": "redirect_to_url",
      "redirect_to_url": {
        "url": "https://hooks.stripe.com/...",
        "return_url": "https://example.com/checkout/complete"
      }
    },
    "id": "pi_xxx",
    "object": "payment_intent",
    "amount": 6000,
    "client_secret": "pi_xxx_secret_xxx",
    "confirm": "true",
    "confirmation_method": "automatic",
    "created": 1579259303,
    "currency": "usd",
    "livemode": true,
    "charges": {
      "data": [],
      "object": "list",
      "has_more": false,
      "url": "/v1/charges?payment_intent=pi_xxx"
    },
    "payment_method_types": ["affirm"]
  }
  ```

- Redirect the customer to the URL provided in the `next_action.redirect_to_url.url` property. The code example here is approximate—the redirect method might be different in your web framework.

  When the customer finishes the payment process, they’re redirected to the `return_url` configured in step 1. The `payment_intent` and `payment_intent_client_secret` URL query parameters are included. If the `return_url` already included query parameters, they’re preserved too.

  We recommend that you [rely on webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm the status of a payment.

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Display payment method messaging on your website

The [Payment Method Messaging Element](https://docs.stripe.com/js/elements_object/create_element?type=paymentMethodMessaging) is an embeddable UI component that helps your customers know which buy now, pay later payment options they have at checkout directly from your product, cart, or payment pages.

To add the Payment Method Messaging Element to your website, see [Display payment method messaging](https://docs.stripe.com/elements/payment-method-messaging.md).

## Failed payments

Affirm takes into account multiple factors when deciding to accept or decline a transaction (for example, the length of time buyer has used Affirm, the outstanding amount the customer has to repay, and the value of the current order).

Always present additional payment options such as `card` in your checkout flow, as Affirm payments have a higher rate of decline than many payment methods. In these cases, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

Other than a payment being declined, for an Affirm [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) with a status of `requires_action`, customers are expected to complete the payment within 12 hours after they’re redirected to the Affirm site. If no action is taken after 12 hours, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

In these cases, inform your customer to try again with a different payment option presented in your checkout flow.

## Error codes

These are the common error codes and corresponding recommended actions:

| Error code                               | Recommended action                                                                                                                                                                                                                 |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_payment_attempt_failed`  | A generic failure indicating the Affirm checkout failed. Additional information might be available in the charge outcome reason.                                                                                                   |
| `payment_method_provider_decline`        | Affirm declined the customer’s payment. As a next step, the customer needs to contact Affirm for more information.                                                                                                                 |
| `payment_intent_payment_attempt_expired` | The customer never completed the payment on Affirm’s checkout page, and the payment session has expired. Stripe automatically expires PaymentIntents that aren’t successfully authorized 12 hours after initial checkout creation. |
| `payment_method_not_available`           | Affirm experienced a service related error and is unable to complete the request. Retry at a later time.                                                                                                                           |
| `amount_too_small`                       | Enter an amount within Affirm’s [default transactions limits](https://docs.stripe.com/payments/affirm.md#payment-options).                                                                                                         |
| `amount_too_large`                       | Enter an amount within Affirm’s [default transactions limits](https://docs.stripe.com/payments/affirm.md#payment-options).                                                                                                         |

Some errors might have additional insight included in the charge outcome reason:

| Outcome Reason             | What this means                                                                                                                                                                                                                                                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `generic_decline`          | The default outcome reason for a payment error. This usually indicates that the partner declined the payment (for example, because of insufficient funds), the bank issuer declined the charge, the transaction included a high-risk purchase, or a similar reason. Stripe might not always receive a decline reason for these cases. |
| `affirm_checkout_canceled` | Either the customer has explicitly canceled the Affirm checkout or Affirm has rejected the customer’s loan eligibility. Stripe can’t distinguish the difference between these two types of events.                                                                                                                                    |
