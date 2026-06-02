<!-- Source URL: https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment -->
<!-- Fetched: 2026-05-06 -->

# Accept an Afterpay or Clearpay payment

Learn how to accept Afterpay (also known as Clearpay in the UK), a payment method in the US, CA, UK, AU, and NZ.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Afterpay is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage), [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method that requires customers to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers are redirected to the Afterpay site, where they agree to the terms of an installment plan. When the customer accepts the terms, Afterpay guarantees that the funds are available to the customer and transfers the funds to your Stripe account. The customer repays Afterpay directly over time.

> Before you start the integration, make sure your account is eligible for Afterpay by navigating to your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

## Determine compatibility

**Customer Geography**: Australia, Canada, New Zealand, UK, US

**Supported currencies**: `aud, cad, nzd, gbp, usd`

**Presentment currencies**: `aud, cad, nzd, gbp, usd`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support Afterpay payments:

- You can only use one-time line items (recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans aren’t supported).
- You must express *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) in your domestic currency.

## Accept a payment

> This guide builds on the foundational [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?ui=stripe-hosted) Checkout integration.

This guides you through enabling Afterpay and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable Afterpay as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `afterpay_clearpay` to the list of `payment_method_types`.
1. Make sure all your `line_items` use your domestic currency and the total amount doesn’t exceed Afterpay’s [transaction amount limits](https://docs.stripe.com/payments/afterpay-clearpay.md#collection-schedule).
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
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "afterpay_clearpay"],
  shipping_address_collection: {
    allowed_countries: ["AU", "CA", "GB", "NZ", "US"],
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
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "afterpay_clearpay"],
  return_url: "https://example.com/return",
  shipping_address_collection: {
    allowed_countries: ["AU", "CA", "GB", "NZ", "US"],
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
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
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
  payment_method_types: ["card", "afterpay_clearpay"],
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
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
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
  payment_method_types: ["card", "afterpay_clearpay"],
  return_url: "https://example.com/return",
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

When testing your Checkout integration, select Afterpay as the payment method and click the **Pay** button.

Test your Afterpay integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **Fail test payment**. The PaymentIntent will transition from `requires_action` to `requires_payment_method`.

For [manual capture](https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment.md#manual-capture) PaymentIntents in testmode, the uncaptured PaymentIntent will auto-expire 10 minutes after successful authorization.

## Failed payments

Afterpay takes into account multiple factors when deciding to accept or decline a transaction (for example, length of time buyer has been using Afterpay, outstanding amount customer has to repay, value of the current order).

You should always present additional payment options such as `card` in your checkout flow, as Afterpay payments have a higher rate of decline than many payment methods. In these cases, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

For an Afterpay [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) with a status of `requires_action`, customers need to complete the payment within 3 hours after you redirect them to the Afterpay site (this doesn’t apply to declined payments). If they take no action within 3 hours, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) detaches and the object status for the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) automatically transitions to `requires_payment_method`.

In these cases, inform your customer to try again with a different payment option presented in your checkout flow.

## Error codes

These are the common error codes and corresponding recommended actions:

| Error code                               | Recommended action                                                                                                                                                                                                                  |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_payment_attempt_failed`  | A generic failure indicating the Afterpay checkout failed. This can also be a decline which doesn’t appear as a decline error code.                                                                                                 |
| `payment_method_provider_decline`        | Afterpay declined the customer’s payment. As a next step, the customer needs to contact Afterpay for more information.                                                                                                              |
| `payment_intent_payment_attempt_expired` | The customer never completed the payment on Afterpay’s checkout page, and the payment session has expired. Stripe automatically expires PaymentIntents that aren’t successfully authorized 3 hours after initial checkout creation. |
| `payment_method_not_available`           | Afterpay experienced a service related error and is unable to complete the request. Retry at a later time.                                                                                                                          |
| `amount_too_small`                       | Enter an amount within Afterpay’s [default transactions limits](https://docs.stripe.com/payments/afterpay-clearpay.md#collection-schedule) for the country.                                                                         |
| `amount_too_large`                       | Enter an amount within Afterpay’s [default transactions limits](https://docs.stripe.com/payments/afterpay-clearpay.md#collection-schedule) for the country.                                                                         |

## See also

- [More about Afterpay](https://docs.stripe.com/payments/afterpay-clearpay.md)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Checkout Sessions API

> This is a Checkout Sessions API for when payment-ui is elements and api-integration is checkout. View the full page at https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment?payment-ui=elements&api-integration=checkout.

To determine which API meets your business needs, see the [comparison guide](https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md).

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to embed a custom Stripe payment form in your website or application and offer payment methods to customers. For advanced configurations and customizations, refer to the [Accept a Payment](https://docs.stripe.com/payments/accept-a-payment.md) integration guide.

## Determine compatibility

**Customer Geography**: Australia, Canada, New Zealand, UK, US

**Supported currencies**: `aud, cad, nzd, gbp, usd`

**Presentment currencies**: `aud, cad, nzd, gbp, usd`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support Afterpay payments:

- You can only use one-time line items (recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans aren’t supported).
- You must express *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) in your domestic currency.

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
          unit_amount: 1099,
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
          unit_amount: 1099,
        },
        quantity: 1,
      },
    ],
    mode: 'payment',
    ui_mode: 'elements',
    payment_method_types: ['afterpay_clearpay'],
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

In live mode, tapping **Pay** redirects you to the Afterpay website—you don’t have the option to approve or decline the payment with Afterpay.

# Payment Intents API

> This is a Payment Intents API for when payment-ui is elements and api-integration is paymentintents. View the full page at https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment?payment-ui=elements&api-integration=paymentintents.

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
  amount: 1099,
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
  amount: 1099,
  currency: "usd",
  paymentMethodTypes: ["afterpay_clearpay"],
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
    amount: 1099,
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
    amount: 1099,
    currency: "usd",
    paymentMethodTypes: ["afterpay_clearpay"],
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
    amount: 1099,
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
    amount: 1099,
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
    amount: 1099,
    currency: "usd",
    payment_method_types: ["afterpay_clearpay"],
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
    amount: 1099,
    currency: "usd",
    payment_method_types: ["afterpay_clearpay"],
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

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s Afterpay account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  confirm: true,
  currency: "usd",
  payment_method_types: ["afterpay_clearpay"],
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

In live mode, tapping **Pay** redirects you to the Afterpay website—you don’t have the option to approve or decline the payment with Afterpay.

## Error codes

The following table details common error codes and recommended actions:

| Error code                                                | Recommended action                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_invalid_currency`                         | Enter a supported currency.                                                                                                                                                                                                                                                                                                                                       |
| `missing_required_parameter`                              | Check the error message for more information about the required parameter.                                                                                                                                                                                                                                                                                        |
| `payment_intent_payment_attempt_failed`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling.                                                                                      |
| `payment_intent_authentication_failure`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling. This error occurs when you manually trigger a failure when testing your integration. |
| `payment_intent_redirect_confirmation_without_return_url` | Provide a `return_url` when confirming a PaymentIntent.                                                                                                                                                                                                                                                                                                           |

> The content of this section refers to a _Legacy_ (Technology that's no longer recommended) product. You should use the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide for the most recent integration path instead. While Stripe still supports this product, this support might end if the product is deprecated.

Stripe users can use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md)—a single integration path for creating payments using any supported method—to accept [Afterpay](https://www.afterpay.com/) payments from customers in the following countries:

- Australia
- Canada
- New Zealand
- United Kingdom
- United States

Afterpay is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage), [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method that requires customers to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers are redirected to the Afterpay site, where they agree to the terms of an installment plan. When the customer accepts the terms, funds are guaranteed and transferred to your Stripe account. The customer repays Afterpay directly over time.

> Before you start the integration, make sure your account is eligible for Afterpay by navigating to your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage. First, create a `PaymentIntent` on your server and specify the amount to collect and the currency. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `afterpay_clearpay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow. The example below uses the [automatic_payment_methods](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-automatic_payment_methods-enabled) attribute but you can list `afterpay_clearpay` with [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types). In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default. Regardless of which option you choose, make sure that you enable Afterpay Clearpay in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  automatic_payment_methods: {
    enabled: true,
  },
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
});
```

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

### Improve payment success rates with additional details

Optionally, pass [shipping](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-shipping) details to improve conversion rates. In this integration, pass shipping details from the client after your customer selects a payment method.

If you send a shipping address, it must include valid values for `line1`, `city`, `state`, `postal_code`, and `country`.

### Additional payment method options

You can specify an optional `reference` parameter in the [payment method options](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-afterpay_clearpay-reference) for your `PaymentIntent` that sets an internal order identifier for the payment. Although this isn’t typically visible to either the business or the consumer, Afterpay’s internal support team can access it during manual support requests. The identifier is limited to 128 characters and might contain only letters, digits, underscores, backslashes, and dashes.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  // Make sure the total amount fits within Afterpay transaction amount limits:
  // https://stripe.com/docs/payments/afterpay-clearpay#collection-schedule
  amount: 1099,
  currency: "usd",
  payment_method_types: ["afterpay_clearpay"],
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
  payment_method_options: {
    afterpay_clearpay: {
      reference: "order_123",
    },
  },
});
```

## Submit the payment to Stripe [Client-side]

In this step, you’ll complete Afterpay payments on the client with [Stripe.js](https://docs.stripe.com/payments/elements.md).

### Set up Stripe.js

When a customer clicks to pay with Afterpay, we recommend using Stripe.js to submit the payment to Stripe. Stripe.js is our foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and enables you to easily extend your integration to other payment methods in the future. Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page.

```javascript
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
var stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Rather than sending the entire PaymentIntent object to the client, use its [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) from [step 2](https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment.md#web-create-payment-intent). This is different from your API keys that authenticate Stripe API requests.

You should still handle the client secret carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Use [stripe.confirmAfterpayClearpayPayment](https://docs.stripe.com/js/payment_intents/confirm_afterpay_clearpay_payment) to handle the redirect away from your page and to complete the payment. Add a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to specify where Stripe redirects the user after they complete the payment on the Afterpay website or mobile application.

```javascript
// Redirects away from the client
const { error } = await stripe.confirmAfterpayClearpayPayment(
  "{{PAYMENT_INTENT_CLIENT_SECRET}}",
  {
    payment_method: {
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
    return_url: "https://example.com/checkout/complete",
  },
);
if (error) {
  // Inform the customer that there was an error.
}
```

When your customer submits a payment, Stripe redirects them to the `return_url` and includes the following URL query parameters. The return page can use them to get the status of the PaymentIntent so it can display the payment status to the customer.

When you specify the `return_url`, you can also append your own query parameters for use on the return page.

| Parameter                      | Description                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                                                                                                                                                                                                                             |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. For subscription integrations, this client_secret is also exposed on the `Invoice` object through [`confirmation_secret`](https://docs.stripe.com/api/invoices/object.md#invoice_object-confirmation_secret) |

When the customer is redirected back to your site, you can use the `payment_intent_client_secret` to query for the PaymentIntent and display the transaction status to your customer.

## Optional: Add line items to the PaymentIntent

You can optionally accept line item data to provide more risk signals to Afterpay. This feature is currently in private beta. Contact us using the form at [Stripe support](https://support.stripe.com) if you want to request access.

## Optional: Separate authorization and capture

Unlike [separate authorization and capture for card payments](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md), Afterpay charges the customer the first installment of the payment at the time of authorization. You then have up to 13 days after authorization to capture the rest of the payment. If you don’t capture the payment in this window, the customer receives a refund of the first installment, and they aren’t charged for any further installments. In these cases, Stripe also cancels the PaymentIntent and sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event.

If you know that you can’t capture the payment, we recommend [canceling the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment) instead of waiting for the 13-day window to elapse. Proactively canceling the PaymentIntent immediately refunds the first installment to your customer, avoiding any confusion about charges on their statement.

### 1. Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s Afterpay account.

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  payment_method_types: ['afterpay_clearpay'],
  capture_method: 'manual',
  shipping: {
    name: 'Jenny Rosen',
    address: {
      line1: '1234 Main Street',
      city: 'San Francisco',
      state: 'CA',
      country: 'US',
      postal_code: '94111',
    },
  },
```

Upon authorization success, Stripe sends a [payment_intent.amount_capturable_updated](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.amount_capturable_updated) event. Check out our [Events guide](https://docs.stripe.com/api/events.md) for how it may help.

### 2. Capture the funds

After the authorization succeeds, the PaymentIntent [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture`. To capture the authorized funds, make a PaymentIntent [capture](https://docs.stripe.com/api/payment_intents/capture.md) request. The total authorized amount is captured by default—you can’t capture more than this, but you can capture less.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{{PAYMENTINTENT_ID}}",
  {
    amount_to_capture: 750,
  },
);
```

### (Optional) Cancel the authorization

If you need to cancel an authorization, you can [cancel the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment).

## Optional: Handle the Afterpay redirect manually

We recommend relying on Stripe.js to handle Afterpay redirects and payments client-side with `confirmAfterpayClearpayPayment`. Using Stripe.js helps extend your integration to other payment methods. However, you can also manually redirect your customers on your server by following these steps:

- Create and confirm a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) of type `afterpay_clearpay`. You must provide the `payment_method_data.billing_details` property that is required by Afterpay. `payment_intent.shipping` is optional but recommended for improved authentication rates. By specifying `payment_method_data`, Stripe creates a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) and immediately uses it with this PaymentIntent.

  You must also provide the redirect URL for your customer after they complete their payment in the `return_url` field. You can also provide your own query parameters in this URL. These parameters are included in the final URL upon completing the redirect flow.

  #### Node.js

  ```javascript
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const paymentIntent = await stripe.paymentIntents.create({
    amount: 1099,
    currency: "usd",
    confirm: true,
    payment_method_types: ["afterpay_clearpay"],
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
    payment_method_data: {
      type: "afterpay_clearpay",
      billing_details: {
        name: "Jenny Rosen",
        email: "jenny@example.com",
        address: {
          line1: "1234 Main Street",
          city: "San Francisco",
          state: "CA",
          country: "US",
          postal_code: "94111",
        },
      },
    },
    return_url: "https://example.com/checkout/complete",
  });
  ```

  The created `PaymentIntent` has a status of `requires_action` and the type for `next_action` is `redirect_to_url`.

  #### Json

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
    "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
    "object": "payment_intent",
    "amount": 1099,
    "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
    "confirmation_method": "automatic",
    "created": 1579259303,
    "currency": "usd",
    "livemode": true,
    "charges": {
      "data": [],
      "object": "list",
      "has_more": false,
      "url": "/v1/charges?payment_intent=pi_1G1sgdKi6xqXeNtkldRRE6HT"
    },
    "payment_method_options": {
      "afterpay_clearpay": {}
    },
    "payment_method_types": ["afterpay_clearpay"]
  }
  ```

- Redirect the customer to the URL provided in the `next_action.redirect_to_url.url` property. The code example here is approximate—the redirect method might be different in your web framework.

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

When the customer finishes the payment process, they’re sent to the `return_url` configured in step 1. The `payment_intent` and `payment_intent_client_secret` URL query parameters are included and you can pass through your own query parameters, as described above.

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

## Optional: Test Afterpay integration

Test your Afterpay integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **Fail test payment**. The PaymentIntent will transition from `requires_action` to `requires_payment_method`.

For [manual capture](https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment.md#manual-capture) PaymentIntents in testmode, the uncaptured PaymentIntent will auto-expire 10 minutes after successful authorization.

## Optional: Display payment method messaging on your website

The [Payment Method Messaging Element](https://docs.stripe.com/js/elements_object/create_element?type=paymentMethodMessaging) is an embeddable UI component that helps your customers know which buy now, pay later payment options they have at checkout directly from your product, cart, or payment pages.

To add the Payment Method Messaging Element to your website, see [Display payment method messaging](https://docs.stripe.com/elements/payment-method-messaging.md).

## Failed payments

Afterpay takes into account multiple factors when deciding to accept or decline a transaction (for example, length of time buyer has been using Afterpay, outstanding amount customer has to repay, value of the current order).

You should always present additional payment options such as `card` in your checkout flow, as Afterpay payments have a higher rate of decline than many payment methods. In these cases, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

For an Afterpay [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) with a status of `requires_action`, customers need to complete the payment within 3 hours after you redirect them to the Afterpay site (this doesn’t apply to declined payments). If they take no action within 3 hours, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) detaches and the object status for the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) automatically transitions to `requires_payment_method`.

In these cases, inform your customer to try again with a different payment option presented in your checkout flow.

## Error codes

These are the common error codes and corresponding recommended actions:

| Error code                               | Recommended action                                                                                                                                                                                                                  |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_payment_attempt_failed`  | A generic failure indicating the Afterpay checkout failed. This can also be a decline which doesn’t appear as a decline error code.                                                                                                 |
| `payment_method_provider_decline`        | Afterpay declined the customer’s payment. As a next step, the customer needs to contact Afterpay for more information.                                                                                                              |
| `payment_intent_payment_attempt_expired` | The customer never completed the payment on Afterpay’s checkout page, and the payment session has expired. Stripe automatically expires PaymentIntents that aren’t successfully authorized 3 hours after initial checkout creation. |
| `payment_method_not_available`           | Afterpay experienced a service related error and is unable to complete the request. Retry at a later time.                                                                                                                          |
| `amount_too_small`                       | Enter an amount within Afterpay’s [default transactions limits](https://docs.stripe.com/payments/afterpay-clearpay.md#collection-schedule) for the country.                                                                         |
| `amount_too_large`                       | Enter an amount within Afterpay’s [default transactions limits](https://docs.stripe.com/payments/afterpay-clearpay.md#collection-schedule) for the country.                                                                         |

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment?payment-ui=mobile&platform=ios.

Accepting Afterpay in your app consists of displaying a webview for a customer to authenticate their payment. The customer then returns to your app, and you can immediately _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) whether the payment succeeded or failed.

> Before you start the integration, make sure your account is eligible for Afterpay by navigating to your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

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

The [Stripe iOS SDK](https://github.com/stripe/stripe-ios) is open source, [fully documented](https://stripe.dev/stripe-ios/index.html), and compatible with apps supporting iOS 13 or above.

#### Swift Package Manager

To install the SDK, follow these steps:

1. In Xcode, select **File** > **Add Package Dependencies…** and enter `https://github.com/stripe/stripe-ios-spm` as the repository URL.
1. Select the latest version number from our [releases page](https://github.com/stripe/stripe-ios/releases).
1. Add the **StripePaymentsUI** product to the [target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### CocoaPods

1. If you haven’t already, install the latest version of [CocoaPods](https://guides.cocoapods.org/using/getting-started.html).
1. If you don’t have an existing [Podfile](https://guides.cocoapods.org/syntax/podfile.html), run the following command to create one:
   ```bash
   pod init
   ```
1. Add this line to your `Podfile`:
   ```podfile
   pod 'StripePaymentsUI'
   ```
1. Run the following command:
   ```bash
   pod install
   ```
1. Don’t forget to use the `.xcworkspace` file to open your project in Xcode, instead of the `.xcodeproj` file, from here on out.
1. In the future, to update to the latest version of the SDK, run:
   ```bash
   pod update StripePaymentsUI
   ```

#### Carthage

1. If you haven’t already, install the latest version of [Carthage](https://github.com/Carthage/Carthage#installing-carthage).
1. Add this line to your `Cartfile`:
   ```cartfile
   github "stripe/stripe-ios"
   ```
1. Follow the [Carthage installation instructions](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos). Make sure to embed all of the required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentsUI/README.md#manual-linking).
1. In the future, to update to the latest version of the SDK, run the following command:
   ```bash
   carthage update stripe-ios --platform ios
   ```

#### Manual Framework

1. Head to our [GitHub releases page](https://github.com/stripe/stripe-ios/releases/latest) and download and unzip **Stripe.xcframework.zip**.
1. Drag **StripePaymentsUI.xcframework** to the **Embedded Binaries** section of the **General** settings in your Xcode project. Make sure to select **Copy items if needed**.
1. Repeat step 2 for all required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentsUI/README.md#manual-linking).
1. In the future, to update to the latest version of our SDK, repeat steps 1–3.

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-ios/releases) page on GitHub. To receive notifications when a new release is published, [watch releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository) for the repository.

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/test/apikeys) on app start. This enables your app to make requests to the Stripe API.

#### Swift

```swift
import UIKitimportStripePaymentsUI

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {StripeAPI.defaultPublishableKey = "<<YOUR_PUBLISHABLE_KEY>>"
        // do any other necessary launch configuration
        return true
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Create a PaymentIntent [Server-side] [Client-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

### Server-side

First, create a `PaymentIntent` on your server and specify the amount to collect and the currency. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `afterpay_clearpay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  // Make sure the total amount fits with Afterpay transaction amount limits:
  // https://stripe.com/docs/payments/afterpay-clearpay#collection-schedule
  amount: 1099,
  currency: "usd",
  payment_method_types: ["afterpay_clearpay"],
});
```

### Additional payment method options

You can specify an optional `reference` parameter in the [payment method options](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-afterpay_clearpay-reference) for your `PaymentIntent` that sets an internal order identifier for the payment. Although this isn’t typically visible to either the business or the consumer, Afterpay’s internal support team can access it during manual support requests. The identifier is limited to 128 characters and might contain only letters, digits, underscores, backslashes, and dashes.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  // Make sure the total amount fits within Afterpay transaction amount limits:
  // https://stripe.com/docs/payments/afterpay-clearpay#collection-schedule
  amount: 1099,
  currency: "usd",
  payment_method_types: ["afterpay_clearpay"],
  payment_method_options: {
    afterpay_clearpay: {
      reference: "order_123",
    },
  },
});
```

### Client-side

Included in the returned PaymentIntent is a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which the client side can use to securely complete the payment process instead of passing the entire PaymentIntent object. On the client, request a PaymentIntent from your server and store its client secret.

#### Swift

```swift
import UIKit
import StripePayments

class CheckoutViewController: UIViewController {
  var paymentIntentClientSecret: String?

  func startCheckout() {
      // Request a PaymentIntent from your server and store its client secret
  }
}
```

## Collect payment method details [Client-side]

Afterpay requires billing details to be present for the payment to succeed. In your app, collect the required billing details from the customer:

- Full name (first and last)
- Email address
- Full billing address

Create an [STPPaymentMethodParams](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentMethodParams.html) object with these details.

Additionally, while shipping details aren’t required they can help improve authentication rates. To collect shipping details, collect the following from the customer:

- Full name
- Full shipping address

Create an [STPPaymentIntentShippingDetailsAddressParams](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentIntentShippingDetailsAddressParams.html) with these details.

#### Swift

```swift
// Billing details
let billingDetails = STPPaymentMethodBillingDetails()
billingDetails.name = "Jane Doe"
billingDetails.email = "email@email.com"
let billingAddress = STPPaymentMethodAddress()
billingAddress.line1 = "510 Townsend St."
billingAddress.postalCode = "94102"
billingAddress.country = "US"
billingDetails.address = billingAddress

// Afterpay PaymentMethod params
let afterpayParams = STPPaymentMethodParams(afterpayClearpay: STPPaymentMethodAfterpayClearpayParams(),
                                                                             billingDetails: billingDetails,
                                                                             metadata: nil)

// Shipping details
// Shipping details are optional but recommended to pass in.
let shippingAddress = STPPaymentIntentShippingDetailsAddressParams(line1: "510 Townsend St.")
shippingAddress.country = "US"
shippingAddress.postalCode = "94102"
let shippingDetails = STPPaymentIntentShippingDetailsParams(address: shippingAddress, name: "Jane Doe")
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created in step 2 and call the [STPPaymentHandler confirmPayment:](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>) method. This presents a webview where the customer can complete the payment, after which the completion block is called with the result of the payment.

#### Swift

```swift
let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)
paymentIntentParams.paymentMethodParams = afterpayParams
// Shipping details are optional but recommended to pass in.
paymentIntentParams.shipping = shippingDetails

STPPaymentHandler.shared().confirmPayment(paymentIntentParams, with: self) { (handlerStatus, paymentIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // Payment succeeded

    case .canceled:
        // Payment was canceled

    case .failed:
        // Payment failed

    @unknown default:
        fatalError()
    }
}
```

## Optional: Add line items to the PaymentIntent

You can optionally accept line item data to provide more risk signals to Afterpay. This feature is currently in private beta. Contact us using the form at [Stripe support](https://support.stripe.com) if you want to request access.

## Optional: Separate authorization and capture

Unlike [separate authorization and capture for card payments](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md), Afterpay charges the customer the first installment of the payment at the time of authorization. You then have up to 13 days after authorization to capture the rest of the payment. If you don’t capture the payment in this window, the customer receives a refund of the first installment, and they aren’t charged for any further installments. In these cases, Stripe also cancels the PaymentIntent and sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event.

If you know that you can’t capture the payment, we recommend [canceling the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment) instead of waiting for the 13-day window to elapse. Proactively canceling the PaymentIntent immediately refunds the first installment to your customer, avoiding any confusion about charges on their statement.

### 1. Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s Afterpay account.

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  payment_method_types: ['afterpay_clearpay'],
  capture_method: 'manual',
  shipping: {
    name: 'Jenny Rosen',
    address: {
      line1: '1234 Main Street',
      city: 'San Francisco',
      state: 'CA',
      country: 'US',
      postal_code: '94111',
    },
  },
```

Upon authorization success, Stripe sends a [payment_intent.amount_capturable_updated](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.amount_capturable_updated) event. Check out our [Events guide](https://docs.stripe.com/api/events.md) for how it may help.

### 2. Capture the funds

After the authorization succeeds, the PaymentIntent [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture`. To capture the authorized funds, make a PaymentIntent [capture](https://docs.stripe.com/api/payment_intents/capture.md) request. The total authorized amount is captured by default—you can’t capture more than this, but you can capture less.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{{PAYMENTINTENT_ID}}",
  {
    amount_to_capture: 750,
  },
);
```

### (Optional) Cancel the authorization

If you need to cancel an authorization, you can [cancel the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment).

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Test Afterpay integration

Test your Afterpay integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **Fail test payment**. The PaymentIntent will transition from `requires_action` to `requires_payment_method`.

For [manual capture](https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment.md#manual-capture) PaymentIntents in testmode, the uncaptured PaymentIntent will auto-expire 10 minutes after successful authorization.

## Failed payments

Afterpay takes into account multiple factors when deciding to accept or decline a transaction (for example, length of time buyer has been using Afterpay, outstanding amount customer has to repay, value of the current order).

You should always present additional payment options such as `card` in your checkout flow, as Afterpay payments have a higher rate of decline than many payment methods. In these cases, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

For an Afterpay [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) with a status of `requires_action`, customers need to complete the payment within 3 hours after you redirect them to the Afterpay site (this doesn’t apply to declined payments). If they take no action within 3 hours, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) detaches and the object status for the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) automatically transitions to `requires_payment_method`.

In these cases, inform your customer to try again with a different payment option presented in your checkout flow.

## Error codes

These are the common error codes and corresponding recommended actions:

| Error code                               | Recommended action                                                                                                                                                                                                                  |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_payment_attempt_failed`  | A generic failure indicating the Afterpay checkout failed. This can also be a decline which doesn’t appear as a decline error code.                                                                                                 |
| `payment_method_provider_decline`        | Afterpay declined the customer’s payment. As a next step, the customer needs to contact Afterpay for more information.                                                                                                              |
| `payment_intent_payment_attempt_expired` | The customer never completed the payment on Afterpay’s checkout page, and the payment session has expired. Stripe automatically expires PaymentIntents that aren’t successfully authorized 3 hours after initial checkout creation. |
| `payment_method_not_available`           | Afterpay experienced a service related error and is unable to complete the request. Retry at a later time.                                                                                                                          |
| `amount_too_small`                       | Enter an amount within Afterpay’s [default transactions limits](https://docs.stripe.com/payments/afterpay-clearpay.md#collection-schedule) for the country.                                                                         |
| `amount_too_large`                       | Enter an amount within Afterpay’s [default transactions limits](https://docs.stripe.com/payments/afterpay-clearpay.md#collection-schedule) for the country.                                                                         |

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment?payment-ui=mobile&platform=android.

Accepting Afterpay in your app consists of displaying a webview for a customer to authenticate their payment. The customer then returns to your app, and you can immediately _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) whether the payment succeeded or failed.

> Before you start the integration, make sure your account is eligible for Afterpay by navigating to your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

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

## Create a PaymentIntent [Server-side] [Client-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

### Server-side

First, create a `PaymentIntent` on your server and specify the amount to collect and the currency. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `afterpay_clearpay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  // Make sure the total amount fits with Afterpay transaction amount limits:
  // https://stripe.com/docs/payments/afterpay-clearpay#collection-schedule
  amount: 1099,
  currency: "usd",
  payment_method_types: ["afterpay_clearpay"],
});
```

### Additional payment method options

You can specify an optional `reference` parameter in the [payment method options](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-afterpay_clearpay-reference) for your `PaymentIntent` that sets an internal order identifier for the payment. Although this isn’t typically visible to either the business or the consumer, Afterpay’s internal support team can access it during manual support requests. The identifier is limited to 128 characters and might contain only letters, digits, underscores, backslashes, and dashes.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  // Make sure the total amount fits within Afterpay transaction amount limits:
  // https://stripe.com/docs/payments/afterpay-clearpay#collection-schedule
  amount: 1099,
  currency: "usd",
  payment_method_types: ["afterpay_clearpay"],
  payment_method_options: {
    afterpay_clearpay: {
      reference: "order_123",
    },
  },
});
```

### Client-side

Included in the returned PaymentIntent is a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which the client side can use to securely complete the payment process instead of passing the entire PaymentIntent object. On the client, request a PaymentIntent from your server and store its client secret.

#### Kotlin

```kotlin
class AfterpayPaymentActivity: AppCompatActivity() {
    private lateinit var paymentIntentClientSecret: String

    override fun onCreate(savedInstanceState: Bundle?) {
        // ...
        startCheckout()
    }


    private fun startCheckout() {
        // Request a PaymentIntent from your server and store its client secret
    }
}
```

## Collect payment method details [Client-side]

Afterpay requires billing details to be present for the payment to succeed. In your app, collect the required billing details from the customer:

- Full name (first and last)
- Email address
- Full billing address

Create a [PaymentMethodCreateParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-payment-method-create-params/index.html) with these details.

Additionally, while shipping details aren’t required they can help improve authentication rates. To collect shipping details, collect the following from the customer:

- Full name
- Full shipping address

Create a [ConfirmPaymentIntentParams.Shipping](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirm-payment-intent-params/-shipping/index.html) with these details.

#### Kotlin

```kotlin
val billingDetails = PaymentMethod.BillingDetails(
  name = "Jenny Rosen",
  email = "jenny@rosen.com",
  address = Address.Builder()
    .setLine1("1234 Market St")
    .setCity("San Francisco")
    .setState("CA")
    .setCountry("US")
    .setPostalCode("94111")
    .build()
)
val paymentMethodCreateParams = PaymentMethodCreateParams.createAfterpayClearpay(billingDetails)

// Shipping details are optional but recommended to pass in.
val shippingDetails = ConfirmPaymentIntentParams.Shipping(
  name = "Jenny Rosen",
  address = Address.Builder()
    .setLine1("1234 Market St")
    .setCity("San Francisco")
    .setState("CA")
    .setCountry("US")
    .setPostalCode("94111")
    .build()
)
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created in step 2 and call the [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/index.html#74063765%2FFunctions%2F-1622557690) method. This presents a webview where the customer can complete the payment on their bank’s website or app. Afterwards, onActivityResult is called with the result of the payment.

#### Kotlin

```kotlin

class AfterpayPaymentActivity : AppCompatActivity() {
    // ...
    private lateinit var paymentIntentClientSecret: String
    private val paymentLauncher: PaymentLauncher by lazy {
        val paymentConfiguration = PaymentConfiguration.getInstance(applicationContext)
        PaymentLauncher.Companion.create(
            this,
            paymentConfiguration.publishableKey,
            paymentConfiguration.stripeAccountId,
            ::onPaymentResult
        )
    }

    private fun startCheckout() {
        // ...

        // Shipping details are optional but recommended to pass in.
        val confirmParams = ConfirmPaymentIntentParams
            .createWithPaymentMethodCreateParams(
                paymentMethodCreateParams = paymentMethodCreateParams,
                clientSecret = paymentIntentClientSecret,
                shipping = shippingDetails
            )
        paymentLauncher.confirm(confirmParams)
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        when (paymentResult) {
            is PaymentResult.Completed -> {
                // show success UI
            }
            is PaymentResult.Canceled -> {
                // handle cancel flow
            }
            is PaymentResult.Failed -> {
                // handle failures
                // (for example, the customer may need to choose a new payment
                // method)
            }
        }
    }
}
```

## Optional: Add line items to the PaymentIntent

You can optionally accept line item data to provide more risk signals to Afterpay. This feature is currently in private beta. Contact us using the form at [Stripe support](https://support.stripe.com) if you want to request access.

## Optional: Separate authorization and capture

Unlike [separate authorization and capture for card payments](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md), Afterpay charges the customer the first installment of the payment at the time of authorization. You then have up to 13 days after authorization to capture the rest of the payment. If you don’t capture the payment in this window, the customer receives a refund of the first installment, and they aren’t charged for any further installments. In these cases, Stripe also cancels the PaymentIntent and sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event.

If you know that you can’t capture the payment, we recommend [canceling the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment) instead of waiting for the 13-day window to elapse. Proactively canceling the PaymentIntent immediately refunds the first installment to your customer, avoiding any confusion about charges on their statement.

### 1. Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s Afterpay account.

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  payment_method_types: ['afterpay_clearpay'],
  capture_method: 'manual',
  shipping: {
    name: 'Jenny Rosen',
    address: {
      line1: '1234 Main Street',
      city: 'San Francisco',
      state: 'CA',
      country: 'US',
      postal_code: '94111',
    },
  },
```

Upon authorization success, Stripe sends a [payment_intent.amount_capturable_updated](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.amount_capturable_updated) event. Check out our [Events guide](https://docs.stripe.com/api/events.md) for how it may help.

### 2. Capture the funds

After the authorization succeeds, the PaymentIntent [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture`. To capture the authorized funds, make a PaymentIntent [capture](https://docs.stripe.com/api/payment_intents/capture.md) request. The total authorized amount is captured by default—you can’t capture more than this, but you can capture less.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{{PAYMENTINTENT_ID}}",
  {
    amount_to_capture: 750,
  },
);
```

### (Optional) Cancel the authorization

If you need to cancel an authorization, you can [cancel the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment).

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Test Afterpay integration

Test your Afterpay integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **Fail test payment**. The PaymentIntent will transition from `requires_action` to `requires_payment_method`.

For [manual capture](https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment.md#manual-capture) PaymentIntents in testmode, the uncaptured PaymentIntent will auto-expire 10 minutes after successful authorization.

## Failed payments

Afterpay takes into account multiple factors when deciding to accept or decline a transaction (for example, length of time buyer has been using Afterpay, outstanding amount customer has to repay, value of the current order).

You should always present additional payment options such as `card` in your checkout flow, as Afterpay payments have a higher rate of decline than many payment methods. In these cases, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

For an Afterpay [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) with a status of `requires_action`, customers need to complete the payment within 3 hours after you redirect them to the Afterpay site (this doesn’t apply to declined payments). If they take no action within 3 hours, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) detaches and the object status for the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) automatically transitions to `requires_payment_method`.

In these cases, inform your customer to try again with a different payment option presented in your checkout flow.

## Error codes

These are the common error codes and corresponding recommended actions:

| Error code                               | Recommended action                                                                                                                                                                                                                  |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_payment_attempt_failed`  | A generic failure indicating the Afterpay checkout failed. This can also be a decline which doesn’t appear as a decline error code.                                                                                                 |
| `payment_method_provider_decline`        | Afterpay declined the customer’s payment. As a next step, the customer needs to contact Afterpay for more information.                                                                                                              |
| `payment_intent_payment_attempt_expired` | The customer never completed the payment on Afterpay’s checkout page, and the payment session has expired. Stripe automatically expires PaymentIntents that aren’t successfully authorized 3 hours after initial checkout creation. |
| `payment_method_not_available`           | Afterpay experienced a service related error and is unable to complete the request. Retry at a later time.                                                                                                                          |
| `amount_too_small`                       | Enter an amount within Afterpay’s [default transactions limits](https://docs.stripe.com/payments/afterpay-clearpay.md#collection-schedule) for the country.                                                                         |
| `amount_too_large`                       | Enter an amount within Afterpay’s [default transactions limits](https://docs.stripe.com/payments/afterpay-clearpay.md#collection-schedule) for the country.                                                                         |

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment?payment-ui=mobile&platform=react-native.

> The content of this section refers to a _Legacy_ (Technology that's no longer recommended) product. You should use the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide for the most recent integration path instead. While Stripe still supports this product, this support might end if the product is deprecated.

Stripe users can use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md)—a single integration path for creating payments using any supported method—to accept [Afterpay](https://www.afterpay.com/) payments from customers in the following countries:

- Australia
- Canada
- New Zealand
- United Kingdom
- United States

Afterpay is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage), [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method that requires customers to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payment. Customers are redirected to the Afterpay site, where they agree to the terms of an installment plan. When the customer accepts the terms, funds are guaranteed and transferred to your Stripe account. The customer repays Afterpay directly over time.

> Before you start the integration, make sure your account is eligible for Afterpay by navigating to your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

## Set up Stripe [Server-side] [Client-side]

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [React Native SDK](https://github.com/stripe/stripe-react-native) is open source and fully documented. Internally, it uses the [native iOS](https://github.com/stripe/stripe-ios) and [Android](https://github.com/stripe/stripe-android) SDKs. To install Stripe’s React Native SDK, run one of the following commands in your project’s directory (depending on which package manager you use):

#### yarn

```bash
yarn add @stripe/stripe-react-native
```

#### npm

```bash
npm install @stripe/stripe-react-native
```

Next, install some other necessary dependencies:

- For iOS, go to the **ios** directory and run `pod install` to ensure that you also install the required native dependencies.
- For Android, there are no more dependencies to install.

> We recommend following the [official TypeScript guide](https://reactnative.dev/docs/typescript#adding-typescript-to-an-existing-project) to add TypeScript support.

### Stripe initialization

To initialize Stripe in your React Native app, either wrap your payment screen with the `StripeProvider` component, or use the `initStripe` initialization method. Only the API [publishable key](https://docs.stripe.com/keys.md#obtain-api-keys) in `publishableKey` is required. The following example shows how to initialize Stripe using the `StripeProvider` component.

```jsx
import { useState, useEffect } from "react";
import { StripeProvider } from "@stripe/stripe-react-native";

function App() {
  const [publishableKey, setPublishableKey] = useState("");

  const fetchPublishableKey = async () => {
    const key = await fetchKey(); // fetch key from your server here
    setPublishableKey(key);
  };

  useEffect(() => {
    fetchPublishableKey();
  }, []);

  return (
    <StripeProvider
      publishableKey={publishableKey}
      merchantIdentifier="merchant.identifier" // required for Apple Pay
      urlScheme="your-url-scheme" // required for 3D Secure and bank redirects
    >
      {/* Your app code here */}
    </StripeProvider>
  );
}
```

> Use your API [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Create a PaymentIntent [Server-side] [Client-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage.

### Server-side

First, create a `PaymentIntent` on your server and specify the amount to collect and the currency. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `afterpay_clearpay` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  // Make sure the total amount fits with Afterpay transaction amount limits:
  // https://stripe.com/docs/payments/afterpay-clearpay#collection-schedule
  amount: 1099,
  currency: "usd",
  payment_method_types: ["afterpay_clearpay"],
});
```

### Client-side

Included in the returned PaymentIntent is a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which the client side can use to securely complete the payment process instead of passing the entire PaymentIntent object. On the client, request a PaymentIntent from your server and store its client secret.

```javascript
const fetchPaymentIntentClientSecret = async () => {
  const response = await fetch(`${API_URL}/create-payment-intent`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      currency: "usd",
      payment_method_types: ["afterpay_clearpay"],
    }),
  });
  const { clientSecret, error } = await response.json();

  return { clientSecret, error };
};
```

## Collect payment method details [Client-side]

Afterpay requires billing details to be present for the payment to succeed. In your app, collect the required billing details from the customer:

- Full name (first and last)
- Email address
- Full billing address

Additionally, while shipping details aren’t required they can help improve authentication rates. To collect shipping details, collect the following from the customer:

- Full name
- Full shipping address

```javascript
export default function AfterpayClearpayPaymentScreen() {
  const [email, setEmail] = useState('');

  const handlePayPress = async () => {
    const billingDetails: PaymentMethodCreateParams.BillingDetails = {
      email,
      phone: '+48888000888',
      addressCity: 'Houston',
      addressCountry: 'US',
      addressLine1: '1459  Circle Drive',
      addressLine2: 'Texas',
      addressPostalCode: '77063',
      name: 'Jenny Rosen',
    };

    // Shipping details are optional but recommended to pass in.
    const shippingDetails: PaymentMethodCreateParams.ShippingDetails = {
      addressLine1: '1459  Circle Drive',
      addressCountry: 'US',
      addressPostalCode: '77063',
      name: 'Jenny Rosen',
    };

    // ...
  };

  return (
    <Screen>
      <TextInput
        placeholder="E-mail"
        onChange={(value) => setEmail(value.nativeEvent.text)}
      />
    </Screen>
  );
}
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created and call `confirmPayment`. You should still handle the client secret carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

```javascript
export default function AfterpayClearpayPaymentScreen() {
  const [email, setEmail] = useState("");

  const handlePayPress = async () => {
    // ...

    const { error, paymentIntent } = await confirmPayment(clientSecret, {
      paymentMethodType: "AfterpayClearpay",
      paymentMethodData: {
        billingDetails,
        // Shipping details are optional but recommended to pass in.
        shippingDetails,
      },
    });

    if (error) {
      Alert.alert(`Error code: ${error.code}`, error.message);
    } else if (paymentIntent) {
      Alert.alert(
        "Success",
        `The payment was confirmed successfully! currency: ${paymentIntent.currency}`,
      );
    }
  };

  return <Screen>{/* ... */}</Screen>;
}
```

## Optional: Handle deep linking

When a customer exits your app (for example to authenticate in Safari or their banking app), provide a way for them to automatically return to your app. Many payment method types _require_ a return URL. If you don’t provide one, we can’t present payment methods that require a return URL to your users, even if you’ve enabled them.

To provide a return URL:

1. [Register](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app#Register-your-URL-scheme) a custom URL. Universal links aren’t supported.
1. [Configure](https://reactnative.dev/docs/linking) your custom URL.
1. Set up your root component to forward the URL to the Stripe SDK as shown below.

> If you’re using Expo, [set your scheme](https://docs.expo.io/guides/linking/#in-a-standalone-app) in the `app.json` file.

```jsx
import { useEffect, useCallback } from 'react';
import { Linking } from 'react-native';
import { useStripe } from '@stripe/stripe-react-native';

export default function MyApp() {
  const { handleURLCallback } = useStripe();

  const handleDeepLink = useCallback(
    async (url: string | null) => {
      if (url) {
        const stripeHandled = await handleURLCallback(url);
        if (stripeHandled) {
          // This was a Stripe URL - you can return or add extra handling here as you see fit
        } else {
          // This was NOT a Stripe URL – handle as you normally would
        }
      }
    },
    [handleURLCallback]
  );

  useEffect(() => {
    const getUrlAsync = async () => {
      const initialUrl = await Linking.getInitialURL();
      handleDeepLink(initialUrl);
    };

    getUrlAsync();

    const deepLinkListener = Linking.addEventListener(
      'url',
      (event: { url: string }) => {
        handleDeepLink(event.url);
      }
    );

    return () => deepLinkListener.remove();
  }, [handleDeepLink]);

  return (
    <View>
      <AwesomeAppComponent />
    </View>
  );
}
```

For more information on native URL schemes, refer to the [Android](https://developer.android.com/training/app-links/deep-linking) and [iOS](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app) docs.

## Optional: Add line items to the PaymentIntent

You can optionally accept line item data to provide more risk signals to Afterpay. This feature is currently in private beta. Contact us using the form at [Stripe support](https://support.stripe.com) if you want to request access.

## Optional: Separate authorization and capture

Unlike [separate authorization and capture for card payments](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md), Afterpay charges the customer the first installment of the payment at the time of authorization. You then have up to 13 days after authorization to capture the rest of the payment. If you don’t capture the payment in this window, the customer receives a refund of the first installment, and they aren’t charged for any further installments. In these cases, Stripe also cancels the PaymentIntent and sends a [payment_intent.canceled](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.canceled) event.

If you know that you can’t capture the payment, we recommend [canceling the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment) instead of waiting for the 13-day window to elapse. Proactively canceling the PaymentIntent immediately refunds the first installment to your customer, avoiding any confusion about charges on their statement.

### 1. Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s Afterpay account.

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'usd',
  payment_method_types: ['afterpay_clearpay'],
  capture_method: 'manual',
  shipping: {
    name: 'Jenny Rosen',
    address: {
      line1: '1234 Main Street',
      city: 'San Francisco',
      state: 'CA',
      country: 'US',
      postal_code: '94111',
    },
  },
```

Upon authorization success, Stripe sends a [payment_intent.amount_capturable_updated](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.amount_capturable_updated) event. Check out our [Events guide](https://docs.stripe.com/api/events.md) for how it may help.

### 2. Capture the funds

After the authorization succeeds, the PaymentIntent [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture`. To capture the authorized funds, make a PaymentIntent [capture](https://docs.stripe.com/api/payment_intents/capture.md) request. The total authorized amount is captured by default—you can’t capture more than this, but you can capture less.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{{PAYMENTINTENT_ID}}",
  {
    amount_to_capture: 750,
  },
);
```

### (Optional) Cancel the authorization

If you need to cancel an authorization, you can [cancel the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment).

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Test Afterpay integration

Test your Afterpay integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **Fail test payment**. The PaymentIntent will transition from `requires_action` to `requires_payment_method`.

For [manual capture](https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment.md#manual-capture) PaymentIntents in testmode, the uncaptured PaymentIntent will auto-expire 10 minutes after successful authorization.

## Failed payments

Afterpay takes into account multiple factors when deciding to accept or decline a transaction (for example, length of time buyer has been using Afterpay, outstanding amount customer has to repay, value of the current order).

You should always present additional payment options such as `card` in your checkout flow, as Afterpay payments have a higher rate of decline than many payment methods. In these cases, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) is detached and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object’s status automatically transitions to `requires_payment_method`.

For an Afterpay [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) with a status of `requires_action`, customers need to complete the payment within 3 hours after you redirect them to the Afterpay site (this doesn’t apply to declined payments). If they take no action within 3 hours, the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) detaches and the object status for the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) automatically transitions to `requires_payment_method`.

In these cases, inform your customer to try again with a different payment option presented in your checkout flow.

## Error codes

These are the common error codes and corresponding recommended actions:

| Error code                               | Recommended action                                                                                                                                                                                                                  |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_payment_attempt_failed`  | A generic failure indicating the Afterpay checkout failed. This can also be a decline which doesn’t appear as a decline error code.                                                                                                 |
| `payment_method_provider_decline`        | Afterpay declined the customer’s payment. As a next step, the customer needs to contact Afterpay for more information.                                                                                                              |
| `payment_intent_payment_attempt_expired` | The customer never completed the payment on Afterpay’s checkout page, and the payment session has expired. Stripe automatically expires PaymentIntents that aren’t successfully authorized 3 hours after initial checkout creation. |
| `payment_method_not_available`           | Afterpay experienced a service related error and is unable to complete the request. Retry at a later time.                                                                                                                          |
| `amount_too_small`                       | Enter an amount within Afterpay’s [default transactions limits](https://docs.stripe.com/payments/afterpay-clearpay.md#collection-schedule) for the country.                                                                         |
| `amount_too_large`                       | Enter an amount within Afterpay’s [default transactions limits](https://docs.stripe.com/payments/afterpay-clearpay.md#collection-schedule) for the country.                                                                         |
