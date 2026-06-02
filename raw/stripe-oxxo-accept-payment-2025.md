<!-- Source URL: https://docs.stripe.com/payments/oxxo/accept-a-payment -->
<!-- Fetched: 2026-05-07 -->

# Accept an OXXO payment

Learn how to accept OXXO, a common payment method in Mexico.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/oxxo/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

OXXO is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [take additional steps](https://docs.stripe.com/payments/payment-methods.md#customer-actions) to complete their payment. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay by providing an OXXO voucher with a generated number and cash payment at an OXXO convenience store.

## Determine compatibility

**Supported business locations**: MX

**Supported currencies**: `mxn`

**Presentment currencies**: `mxn`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support OXXO payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.
- You can only use one-time line items (recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans aren’t supported).

## Accept a payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

This guides you through enabling OXXO and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable OXXO as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `oxxo` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the `mxn` currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "mxn",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "oxxo"],
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
        currency: "mxn",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "oxxo"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Additional payment method options

You can specify an optional `expires_after_days` parameter in the [payment method options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-oxxo-expires_after_days) for your `Session` that sets the number of calendar days before an OXXO voucher expires. For example, if you create an OXXO voucher on Monday and you set `expires_after_days` to 2, the OXXO voucher will expire on Wednesday at 23:59 America/Mexico_City (UTC-6) time. The `expires_after_days` parameter can be set from 1 to 7 days. The default is 3 days.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "mxn",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_options: {
    oxxo: {
      expires_after_days: 2,
    },
  },
  payment_method_types: ["card", "oxxo"],
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
        currency: "mxn",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_options: {
    oxxo: {
      expires_after_days: 2,
    },
  },
  payment_method_types: ["card", "oxxo"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Redirect to Stripe hosted voucher page

After submitting the Checkout form successfully, the customer is redirected to the `hosted_voucher_url`. The customer can find the barcode or print the OXXO voucher from the hosted voucher page. You can locate the `hosted_voucher_url` in [payment_intent.next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-hosted_voucher_url).

Stripe allows customization of customer-facing UIs on the [Branding Settings](https://dashboard.stripe.com/account/branding) page. The following brand settings can be applied to the voucher:

- **Icon**—your brand image and public business name
- **Accent color**—used as the color of Print button
- **Brand color**—used as the background color

### Fulfill your orders

Because OXXO is a delayed notification payment method, you need to use a method such as *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to monitor the payment status and handle order *fulfillment* (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected). Learn more about [setting up webhooks and fulfilling orders](https://docs.stripe.com/checkout/fulfillment.md).

The following events are sent when the payment status changes:

| Event Name                                                                                                       | Description                                                                                       | Next steps |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------- |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) | The customer has successfully submitted the Checkout form. Stripe has generated the OXXO voucher. |

You can choose to email the `hosted_voucher_url` to your customer in case they lose the OXXO voucher. | Wait for the customer to pay the OXXO voucher. |
| [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) | The customer has successfully paid the OXXO. The `PaymentIntent` transitions to `succeeded`. | Fulfill the goods or services that the customer purchased. |
| [checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_failed) | The OXXO voucher has expired, or the payment has failed for some other reason. The `PaymentIntent` returns to a status of `requires_payment_method`. | Contact the customer through email and request that they place a new order. |

## Test your integration

When testing your Checkout integration, select OXXO as the payment method and click the **Pay** button.

| Email                       | Description                                                                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | Simulates an OXXO voucher which a customer pays after 3 minutes and the `payment_intent.succeeded` webhook arrives after about 3 minutes. In production, this webhook arrives after 1 business day. |

Example: fulano@test.com |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates an OXXO voucher which a customer pays immediately and the `payment_intent.succeeded` webhook arrives within several seconds. In production, this webhook arrives after 1 business day.

Example: succeed_immediately@test.com |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives within several seconds.

The `expires_after` field in [next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-expires_after) is set to the current time regardless of what the `expires_after_days` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-oxxo-expires_after_days) is set to.

Example: expire_immediately@test.com |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives after about 3 minutes.

The `expires_after` field in [next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-expires_after) is set to 3 minutes in the future regardless of what the `expires_after_days` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-oxxo-expires_after_days) is set to.

Example: expire_with_delay@test.com |
| `{any_prefix}fill_never@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives after 1 business day and 2 calendar days. In production, this webhook arrives at the same time as in testmode.

Example: fill_never@test.com |

## Optional: Send payment instruction emails

You can enable OXXO payment instruction emails on the [Email Settings](https://dashboard.stripe.com/settings/emails) page in the Dashboard. Once enabled, Stripe sends payment instruction emails upon PaymentIntent confirmation. The emails contain the OXXO number and a link to the Stripe hosted voucher page.

> In testing environments, instruction emails are only sent to email addresses linked to the Stripe account.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Checkout Sessions API

> This is a Checkout Sessions API for when payment-ui is elements and api-integration is checkout. View the full page at https://docs.stripe.com/payments/oxxo/accept-a-payment?payment-ui=elements&api-integration=checkout.

To determine which API meets your business needs, see the [comparison guide](https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md).

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to embed a custom Stripe payment form in your website or application and offer payment methods to customers. For advanced configurations and customizations, refer to the [Accept a Payment](https://docs.stripe.com/payments/accept-a-payment.md) integration guide.

## Determine compatibility

**Supported business locations**: MX

**Supported currencies**: `mxn`

**Presentment currencies**: `mxn`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support OXXO payments:

- Prices for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.
- You can only use one-time line items (recurring subscription plans aren’t supported).

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
          currency: 'mxn',
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
          currency: 'mxn',
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
    payment_method_types: ['oxxo'],
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

In live mode, tapping **Pay** redirects you to the oxxo website—you don’t have the option to approve or decline the payment with oxxo.

# Payment Intents API

> This is a Payment Intents API for when payment-ui is elements and api-integration is paymentintents. View the full page at https://docs.stripe.com/payments/oxxo/accept-a-payment?payment-ui=elements&api-integration=paymentintents.

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
  currency: "mxn",
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
  currency: "mxn",
  paymentMethodTypes: ["oxxo"],
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
    currency: "mxn",
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
    currency: "mxn",
    paymentMethodTypes: ["oxxo"],
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
    currency: "mxn",
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
    currency: "mxn",
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
    currency: "mxn",
    payment_method_types: ["oxxo"],
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
    currency: "mxn",
    payment_method_types: ["oxxo"],
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

## Test your integration

To test your integration, choose the payment method and tap **Pay**. In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), this redirects you to a test payment page where you can approve or decline the payment.

In live mode, tapping **Pay** redirects you to the oxxo website—you don’t have the option to approve or decline the payment with oxxo.

## Error codes

The following table details common error codes and recommended actions:

| Error code                                                | Recommended action                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent_invalid_currency`                         | Enter a supported currency.                                                                                                                                                                                                                                                                                                                                       |
| `missing_required_parameter`                              | Check the error message for more information about the required parameter.                                                                                                                                                                                                                                                                                        |
| `payment_intent_payment_attempt_failed`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling.                                                                                      |
| `payment_intent_authentication_failure`                   | This code can appear in the [last_payment_error.code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-code) field of a PaymentIntent. Check the error message for a detailed failure reason and suggestion on error handling. This error occurs when you manually trigger a failure when testing your integration. |
| `payment_intent_redirect_confirmation_without_return_url` | Provide a `return_url` when confirming a PaymentIntent.                                                                                                                                                                                                                                                                                                           |

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/oxxo/accept-a-payment?payment-ui=mobile&platform=ios.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Accepting OXXO in your app consists of displaying a webview to show the OXXO voucher. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay by providing an OXXO voucher with a generated number and cash payment at an OXXO convenience store. Stripe notifies you when the payment is completed.

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

Create a PaymentIntent on your server with an amount and the `mxn` currency (OXXO doesn’t support other currencies). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `oxxo` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "mxn",
  payment_method_types: ["oxxo"],
});

// Send the paymentIntent.client_secret back to the client so you can use it in later steps.
```

### Additional payment method options

You can specify an optional `expires_after_days` parameter in the [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-oxxo-expires_after_days) for your `PaymentIntent` that sets the number of calendar days before an OXXO voucher expires. For example, if you create an OXXO voucher on Monday and you set `expires_after_days` to 2, the OXXO voucher will expire on Wednesday at 23:59 America/Mexico_City (UTC-6) time. The `expires_after_days` parameter can be set from 1 to 7 days. The default is 3 days.

### Client-side

On the client, request a PaymentIntent from your server and store its client secret.

#### Swift

```swift
class CheckoutViewController: UIViewController {
    var paymentIntentClientSecret: String?

    func startCheckout() {
        // Request a PaymentIntent from your server and store its client secret
    }
}
```

## Collect payment method details [Client-side]

In your app, collect the following required billing details from the customer. Create a [STPPaymentIntentParams](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentIntentParams.html) with the billing details.

| Field   | Value                                                                                                                  |
| ------- | ---------------------------------------------------------------------------------------------------------------------- |
| `name`  | The full name (first and last) of the customer. The first name and last name must each be a minimum of two characters. |
| `email` | The full email address of the customer.                                                                                |

#### Swift

```swift
let billingDetails = STPPaymentMethodBillingDetails()
billingDetails.name = "Jane Doe"
billingDetails.email = "test@example.com" EOF )
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created in step 2 and call [STPPaymentHandler confirmPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>). This presents a webview to display the OXXO voucher. Upon completion, the completion block is called with the result of the payment.

#### Swift

```swift
let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)
let oxxoParams = STPPaymentMethodOXXOParams();
paymentIntentParams.paymentMethodParams = STPPaymentMethodParams(
    oxxo: oxxoParams,
    billingDetails: billingDetails,
    metadata: nil
)

STPPaymentHandler.shared().confirmPayment(paymentIntentParams, with: self) { (handlerStatus, paymentIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // The OXXO voucher was displayed successfully. The customer can now pay the OXXO voucher at the OXXO convenience store.
    case .canceled:
        // Payment was canceled

    case .failed:
        // Payment failed

    @unknown default:
        fatalError()
    }
}
```

### Optional: Email voucher link to your customer

Stripe sends a [payment_intent.requires_action](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.requires_action) event when an OXXO voucher is created successfully. If you need to email your customers the voucher link, you can [retrieve the PaymentIntent](https://docs.stripe.com/api/payment_intents/retrieve.md) to get the link upon receiving the event. The `hosted_voucher_url` field in [payment_intent.next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-hosted_voucher_url) contains the link to the voucher.

### Optional: Customize your voucher

Stripe allows customization of customer-facing UIs on the [Branding Settings](https://dashboard.stripe.com/account/branding) page.

The following brand settings can be applied to the voucher:

- **Icon**—your brand image and public business name
- **Accent color**—used as the color of the Copy Number button
- **Brand color**—used as the background color

## Handle post-payment events [Server-side]

OXXO is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, so funds aren’t immediately available. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) might not pay for the OXXO voucher at an OXXO convenience store immediately after checking out.

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event on the next business day (Monday through Friday excluding Mexican holidays) for each OXXO voucher that was paid. Use the Dashboard or build a *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) handler to receive these events and run actions (for example, sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow).

After the expiry date, the PaymentIntent’s status transitions to `processing` and the customer can no longer pay for the expired OXXO voucher. If the OXXO voucher wasn’t paid for before 23:59 America/Mexico_City (UTC-6) on the expiry date, Stripe sends a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) event within 10 calendar days after the expiry date (in most cases, this event is sent within 7 calendar days). For example, if the OXXO voucher expires on September 1, this event is sent by September 10 at the latest.

| Event                            | Description                                                     | Next steps                                                                                  |
| -------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `payment_intent.requires_action` | The OXXO voucher is created successfully.                       | Wait for the customer to pay for the OXXO voucher.                                          |
| `payment_intent.processing`      | The customer can no longer pay for the OXXO voucher.            | Wait for the payment to succeed or fail.                                                    |
| `payment_intent.succeeded`       | The customer paid for the OXXO voucher before expiration.       | Fulfill the goods or services that the customer purchased.                                  |
| `payment_intent.payment_failed`  | The customer didn’t pay for the OXXO voucher before expiration. | Contact the customer through email or push notification and request another payment method. |

### Receive events and run business actions

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom Code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

## Test the integration

In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), set [STPPaymentMethodBillingDetails email](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentMethodBillingDetails.html#/c:@M@StripePayments@objc(cs)STPPaymentMethodBillingDetails(py)email>) to the following values when you call [STPPaymentHandler confirmPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:>) to test different scenarios.

| Email                       | Description                                                                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | Simulates an OXXO voucher which a customer pays after 3 minutes and the `payment_intent.succeeded` webhook arrives after about 3 minutes. In production, this webhook arrives after 1 business day. |

Example: fulano@test.com |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates an OXXO voucher which a customer pays immediately and the `payment_intent.succeeded` webhook arrives within several seconds. In production, this webhook arrives after 1 business day.

Example: succeed_immediately@test.com |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives within several seconds.

The `expires_after` field in [next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-expires_after) is set to the current time regardless of what the `expires_after_days` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-oxxo-expires_after_days) is set to.

Example: expire_immediately@test.com |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives after about 3 minutes.

The `expires_after` field in [next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-expires_after) is set to 3 minutes in the future regardless of what the `expires_after_days` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-oxxo-expires_after_days) is set to.

Example: expire_with_delay@test.com |
| `{any_prefix}fill_never@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives after 1 business day and 2 calendar days. In production, this webhook arrives at the same time as in testmode.

Example: fill_never@test.com |

## Expiration and cancellation

OXXO vouchers expire after the `expires_after` UNIX timestamp and a customer can’t pay an OXXO voucher once it has expired. OXXO vouchers can’t be canceled before expiration.

After an OXXO voucher expires, the PaymentIntent’s status changes to `requires_payment_method`. At this point, you can confirm the PaymentIntent with another payment method or cancel.

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/oxxo/accept-a-payment?payment-ui=mobile&platform=android.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Accepting OXXO in your app consists of displaying a webview to show the OXXO voucher. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay by providing an OXXO voucher with a generated number and cash payment at an OXXO convenience store. Stripe notifies you when the payment is completed.

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

Create a PaymentIntent on your server with an amount and the `mxn` currency (OXXO doesn’t support other currencies). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `oxxo` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "mxn",
  payment_method_types: ["oxxo"],
});

// Send the paymentIntent.client_secret back to the client so you can use it in later steps.
```

### Additional payment method options

You can specify an optional `expires_after_days` parameter in the [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-oxxo-expires_after_days) for your `PaymentIntent` that sets the number of calendar days before an OXXO voucher expires. For example, if you create an OXXO voucher on Monday and you set `expires_after_days` to 2, the OXXO voucher will expire on Wednesday at 23:59 America/Mexico_City (UTC-6) time. The `expires_after_days` parameter can be set from 1 to 7 days. The default is 3 days.

### Client-side

On the client, request a PaymentIntent from your server and store its client secret.

#### Kotlin

```kotlin
class OXXOActivity: AppCompatActivity() {
    private lateinit var paymentIntentClientSecret: String

    private fun startCheckout() {
        // Request a PaymentIntent from your server and store its client secret
    }
}
```

## Collect payment method details [Client-side]

In your app, collect the following required billing details from the customer. Create a [PaymentMethodCreateParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-payment-method-create-params/index.html) with the billing details.

| Field   | Value                                                                                                                  |
| ------- | ---------------------------------------------------------------------------------------------------------------------- |
| `name`  | The full name (first and last) of the customer. The first name and last name must each be a minimum of two characters. |
| `email` | The full email address of the customer.                                                                                |

#### Kotlin

```kotlin
val billingDetails =
  PaymentMethod.BillingDetails(email = "email@email.com", name = "Jenny Rosen")
val paymentMethodCreateParams = PaymentMethodCreateParams.createOxxo(billingDetails)
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created in step 2 and call [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/index.html#74063765%2FFunctions%2F-1622557690). This presents a webview to display the OXXO voucher. Afterwards, `onPaymentResult` is called with the result of the payment.

#### Kotlin

```kotlin
class OXXOActivity : AppCompatActivity() {
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

        val confirmParams = ConfirmPaymentIntentParams
                .createWithPaymentMethodCreateParams(
                  paymentMethodCreateParams = paymentMethodCreateParams,
                  clientSecret = paymentIntentClientSecret
                )
        paymentLauncher.confirm(confirmParams)
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        when (paymentResult) {
            is PaymentResult.Completed -> {
                // The OXXO voucher was displayed successfully.
                // The customer can now pay the OXXO voucher at the OXXO convenience store.
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

### Optional: Email voucher link to your customer

Stripe sends a [payment_intent.requires_action](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.requires_action) event when an OXXO voucher is created successfully. If you need to email your customers the voucher link, you can [retrieve the PaymentIntent](https://docs.stripe.com/api/payment_intents/retrieve.md) to get the link upon receiving the event. The `hosted_voucher_url` field in [payment_intent.next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-hosted_voucher_url) contains the link to the voucher.

### Optional: Customize your voucher

Stripe allows customization of customer-facing UIs on the [Branding Settings](https://dashboard.stripe.com/account/branding) page.

The following brand settings can be applied to the voucher:

- **Icon**—your brand image and public business name
- **Accent color**—used as the color of the Copy Number button
- **Brand color**—used as the background color

## Handle post-payment events [Server-side]

OXXO is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, so funds aren’t immediately available. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) might not pay for the OXXO voucher at an OXXO convenience store immediately after checking out.

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event on the next business day (Monday through Friday excluding Mexican holidays) for each OXXO voucher that was paid. Use the Dashboard or build a *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) handler to receive these events and run actions (for example, sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow).

After the expiry date, the PaymentIntent’s status transitions to `processing` and the customer can no longer pay for the expired OXXO voucher. If the OXXO voucher wasn’t paid for before 23:59 America/Mexico_City (UTC-6) on the expiry date, Stripe sends a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) event within 10 calendar days after the expiry date (in most cases, this event is sent within 7 calendar days). For example, if the OXXO voucher expires on September 1, this event is sent by September 10 at the latest.

| Event                            | Description                                                     | Next steps                                                                                  |
| -------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `payment_intent.requires_action` | The OXXO voucher is created successfully.                       | Wait for the customer to pay for the OXXO voucher.                                          |
| `payment_intent.processing`      | The customer can no longer pay for the OXXO voucher.            | Wait for the payment to succeed or fail.                                                    |
| `payment_intent.succeeded`       | The customer paid for the OXXO voucher before expiration.       | Fulfill the goods or services that the customer purchased.                                  |
| `payment_intent.payment_failed`  | The customer didn’t pay for the OXXO voucher before expiration. | Contact the customer through email or push notification and request another payment method. |

### Receive events and run business actions

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom Code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

## Test the integration

In a sandbox, set [PaymentMethod.BillingDetails#email](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-payment-method/-billing-details/index.html) to the following values when you call [Stripe\# confirmPayment()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/confirm-payment.html) to test different scenarios.

| Email                       | Description                                                                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | Simulates an OXXO voucher which a customer pays after 3 minutes and the `payment_intent.succeeded` webhook arrives after about 3 minutes. In production, this webhook arrives after 1 business day. |

Example: fulano@test.com |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates an OXXO voucher which a customer pays immediately and the `payment_intent.succeeded` webhook arrives within several seconds. In production, this webhook arrives after 1 business day.

Example: succeed_immediately@test.com |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives within several seconds.

The `expires_after` field in [next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-expires_after) is set to the current time regardless of what the `expires_after_days` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-oxxo-expires_after_days) is set to.

Example: expire_immediately@test.com |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives after about 3 minutes.

The `expires_after` field in [next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-expires_after) is set to 3 minutes in the future regardless of what the `expires_after_days` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-oxxo-expires_after_days) is set to.

Example: expire_with_delay@test.com |
| `{any_prefix}fill_never@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives after 1 business day and 2 calendar days. In production, this webhook arrives at the same time as in testmode.

Example: fill_never@test.com |

## Expiration and cancellation

OXXO vouchers expire after the `expires_after` UNIX timestamp and a customer can’t pay an OXXO voucher once it has expired. OXXO vouchers can’t be canceled before expiration.

After an OXXO voucher expires, the PaymentIntent’s status changes to `requires_payment_method`. At this point, you can confirm the PaymentIntent with another payment method or cancel.

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/oxxo/accept-a-payment?payment-ui=mobile&platform=react-native.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Accepting OXXO in your app consists of displaying a webview to show the OXXO voucher. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay by providing an OXXO voucher with a generated number and cash payment at an OXXO convenience store. Stripe notifies you when the payment is completed.

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

Create a PaymentIntent on your server with an amount and the `mxn` currency (OXXO doesn’t support other currencies). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `oxxo` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "mxn",
  payment_method_types: ["oxxo"],
});

// Send the paymentIntent.client_secret back to the client so you can use it in later steps.
```

### Additional payment method options

You can specify an optional `expires_after_days` parameter in the [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-oxxo-expires_after_days) for your `PaymentIntent` that sets the number of calendar days before an OXXO voucher expires. For example, if you create an OXXO voucher on Monday and you set `expires_after_days` to 2, the OXXO voucher will expire on Wednesday at 23:59 America/Mexico_City (UTC-6) time. The `expires_after_days` parameter can be set from 1 to 7 days. The default is 3 days.

### Client-side

On the client, request a PaymentIntent from your server and store its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)).

```javascript
const fetchPaymentIntentClientSecret = async () => {
  const response = await fetch(`${API_URL}/create-payment-intent`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      currency: "mxn",
      payment_method_types: ["oxxo"],
    }),
  });
  const { clientSecret, error } = await response.json();

  return { clientSecret, error };
};
```

## Collect payment method details [Client-side]

In your app, collect your customer’s full name and email address.

```javascript
export default function OxxoPaymentScreen() {
  const [name, setName] = useState();
  const [email, setEmail] = useState();

  const handlePayPress = async () => {
    // ...
  };

  return (
    <Screen>
      <TextInput
        placeholder="Name"
        onChange={(value) => setName(value.nativeEvent.text)}
      />
      <TextInput
        placeholder="E-mail"
        onChange={(value) => setEmail(value.nativeEvent.text)}
      />
    </Screen>
  );
}
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created and call `confirmPayment`. This presents a webview to display the OXXO voucher.

```javascript
export default function OxxoPaymentScreen() {
  const [name, setName] = useState();
  const [email, setEmail] = useState();

  const handlePayPress = async () => {
    const billingDetails: PaymentMethodCreateParams.BillingDetails = {
      name,
      email,
    };

    const { error, paymentIntent } = await confirmPayment(clientSecret, {
      paymentMethodType: 'Oxxo',
      paymentMethodData: {
        billingDetails,
      }
    });

    if (error) {
      Alert.alert(`Error code: ${error.code}`, error.message);
      console.log('Payment confirmation error', error.message);
    } else if (paymentIntent) {
      if (paymentIntent.status === PaymentIntents.Status.RequiresAction) {
        Alert.alert(
          'Success',
          `The OXXO voucher was created successfully. Awaiting payment from customer.`
        );
      } else {
        Alert.alert('Payment intent status:', paymentIntent.status);
      }
    }
  };

  return (
    <Screen>
      <TextInput
        placeholder="Name"
        onChange={(value) => setName(value.nativeEvent.text)}
      />
      <TextInput
        placeholder="E-mail"
        onChange={(value) => setEmail(value.nativeEvent.text)}
      />
    </Screen>
  );
}
```

### Optional: Email voucher link to your customer

Stripe sends a [payment_intent.requires_action](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.requires_action) event when an OXXO voucher is created successfully. If you need to email your customers the voucher link, you can [retrieve the PaymentIntent](https://docs.stripe.com/api/payment_intents/retrieve.md) to get the link upon receiving the event. The `hosted_voucher_url` field in [payment_intent.next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-hosted_voucher_url) contains the link to the voucher.

### Optional: Customize your voucher

Stripe allows customization of customer-facing UIs on the [Branding Settings](https://dashboard.stripe.com/account/branding) page.

The following brand settings can be applied to the voucher:

- **Icon**—your brand image and public business name
- **Accent color**—used as the color of the Copy Number button
- **Brand color**—used as the background color

## Handle post-payment events [Server-side]

OXXO is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, so funds aren’t immediately available. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) might not pay for the OXXO voucher at an OXXO convenience store immediately after checking out.

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event on the next business day (Monday through Friday excluding Mexican holidays) for each OXXO voucher that was paid. Use the Dashboard or build a *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) handler to receive these events and run actions (for example, sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow).

After the expiry date, the PaymentIntent’s status transitions to `processing` and the customer can no longer pay for the expired OXXO voucher. If the OXXO voucher wasn’t paid for before 23:59 America/Mexico_City (UTC-6) on the expiry date, Stripe sends a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) event within 10 calendar days after the expiry date (in most cases, this event is sent within 7 calendar days). For example, if the OXXO voucher expires on September 1, this event is sent by September 10 at the latest.

| Event                            | Description                                                     | Next steps                                                                                  |
| -------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `payment_intent.requires_action` | The OXXO voucher is created successfully.                       | Wait for the customer to pay for the OXXO voucher.                                          |
| `payment_intent.processing`      | The customer can no longer pay for the OXXO voucher.            | Wait for the payment to succeed or fail.                                                    |
| `payment_intent.succeeded`       | The customer paid for the OXXO voucher before expiration.       | Fulfill the goods or services that the customer purchased.                                  |
| `payment_intent.payment_failed`  | The customer didn’t pay for the OXXO voucher before expiration. | Contact the customer through email or push notification and request another payment method. |

### Receive events and run business actions

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom Code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

## Test the integration

In a sandbox, use the following emails when you call `confirmPayment` to test different scenarios.

| Email                       | Description                                                                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | Simulates an OXXO voucher which a customer pays after 3 minutes and the `payment_intent.succeeded` webhook arrives after about 3 minutes. In production, this webhook arrives after 1 business day. |

Example: fulano@test.com |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates an OXXO voucher which a customer pays immediately and the `payment_intent.succeeded` webhook arrives within several seconds. In production, this webhook arrives after 1 business day.

Example: succeed_immediately@test.com |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives within several seconds.

The `expires_after` field in [next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-expires_after) is set to the current time regardless of what the `expires_after_days` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-oxxo-expires_after_days) is set to.

Example: expire_immediately@test.com |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives after about 3 minutes.

The `expires_after` field in [next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-expires_after) is set to 3 minutes in the future regardless of what the `expires_after_days` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-oxxo-expires_after_days) is set to.

Example: expire_with_delay@test.com |
| `{any_prefix}fill_never@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives after 1 business day and 2 calendar days. In production, this webhook arrives at the same time as in testmode.

Example: fill_never@test.com |

## Expiration and cancellation

OXXO vouchers expire after the `expires_after` UNIX timestamp and a customer can’t pay an OXXO voucher once it has expired. OXXO vouchers can’t be canceled before expiration.

After an OXXO voucher expires, the PaymentIntent’s status changes to `requires_payment_method`. At this point, you can confirm the PaymentIntent with another payment method or cancel.

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/oxxo/accept-a-payment?payment-ui=direct-api.

> The content of this section refers to a *Legacy* (Technology that's no longer recommended) product. You should use the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide for the most recent integration path instead. While Stripe still supports this product, this support might end if the product is deprecated.

Stripe users in Mexico can accept OXXO payments from customers in Mexico by using the Payment Intents and Payment Methods APIs. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay by providing an OXXO voucher with a generated number and cash payment at an OXXO convenience store. Stripe notifies you when the payment is completed.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/test/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) object to represent your intent to collect payment from a customer, tracking state changes from OXXO voucher creation to payment completion.

Create a PaymentIntent on your server with an amount and the `mxn` currency (OXXO doesn’t support other currencies). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `oxxo` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "mxn",
  payment_method_types: ["oxxo"],
});

// Send the paymentIntent.client_secret back to the client so you can use it in later steps.
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

### Additional payment method options

You can specify an optional `expires_after_days` parameter in the [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-oxxo-expires_after_days) for your `PaymentIntent` that sets the number of calendar days before an OXXO voucher expires. For example, if you create an OXXO voucher on Monday and you set `expires_after_days` to 2, the OXXO voucher will expire on Wednesday at 23:59 America/Mexico_City (UTC-6) time. The `expires_after_days` parameter can be set from 1 to 7 days. The default is 3 days.

## Collect payment method details [Client-side]

Create a payment form on your client to collect the required billing details from the customer:

| Field   | Value                                                                                                                  |
| ------- | ---------------------------------------------------------------------------------------------------------------------- |
| `name`  | The full name (first and last) of the customer. The first name and last name must each be a minimum of two characters. |
| `email` | The full email address of the customer.                                                                                |

```html
<form id="payment-form">
  <div class="form-row">
    <label for="name"> Name </label>
    <input id="name" name="name" required />
  </div>

  <div class="form-row">
    <label for="email"> Email </label>
    <input id="email" name="email" required />
  </div>

  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>

  <button id="submit-button">Pay with OXXO</button>
</form>
```

## Submit the payment to Stripe [Client-side]

When a customer clicks to pay with OXXO, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is our foundational JavaScript library for building payment flows.

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page.

```javascript
// Set your publishable key. Remember to switch to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

Use [stripe.confirmOxxoPayment](https://docs.stripe.com/js/payment_intents/confirm_oxxo_payment) and the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object that you created in Step 2 to submit the customer’s billing details.

Upon confirmation, Stripe will automatically open a modal to display the OXXO voucher to your customer.

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const result = await stripe.confirmOxxoPayment(
    "{{PAYMENT_INTENT_CLIENT_SECRET}}",
    {
      payment_method: {
        billing_details: {
          name: document.getElementById("name").value,
          email: document.getElementById("email").value,
        },
      },
    },
  );
  // Stripe.js will open a modal to display the OXXO voucher to your customer
  // This async function finishes when the customer closes the modal

  if (result.error) {
    // Display error to your customer
    const errorMsg = document.getElementById("error-message");
    errorMsg.innerText = result.error.message;
  }
});
```

> `stripe.confirmOxxoPayment` may take several seconds to complete. During that time, disable your form from being resubmitted and show a waiting indicator like a spinner. If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

When an OXXO voucher is created successfully, the value of the returned PaymentIntent’s `status` property is `requires_action`. Check the status of a PaymentIntent in the [Dashboard](https://dashboard.stripe.com/test/payments) or by inspecting the status property on the object. If the OXXO voucher wasn’t created successfully, inspect the returned `error` to determine the cause (for example, invalid email format).

### Optional: Email voucher link to your customer

Stripe sends a [payment_intent.requires_action](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.requires_action) event when an OXXO voucher is created successfully. If you need to email your customers the voucher link, you can [retrieve the PaymentIntent](https://docs.stripe.com/api/payment_intents/retrieve.md) to get the link upon receiving the event. The `hosted_voucher_url` field in [payment_intent.next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-hosted_voucher_url) contains the link to the voucher.

### Optional: Customize your voucher

Stripe allows customization of customer-facing UIs on the [Branding Settings](https://dashboard.stripe.com/account/branding) page.

The following brand settings can be applied to the voucher:

- **Icon**—your brand image and public business name
- **Accent color**—used as the color of the Copy Number button
- **Brand color**—used as the background color

## Handle post-payment events [Server-side]

OXXO is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, so funds aren’t immediately available. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) might not pay for the OXXO voucher at an OXXO convenience store immediately after checking out.

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event on the next business day (Monday through Friday excluding Mexican holidays) for each OXXO voucher that was paid. Use the Dashboard or build a *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) handler to receive these events and run actions (for example, sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow).

After the expiry date, the PaymentIntent’s status transitions to `processing` and the customer can no longer pay for the expired OXXO voucher. If the OXXO voucher wasn’t paid for before 23:59 America/Mexico_City (UTC-6) on the expiry date, Stripe sends a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) event within 10 calendar days after the expiry date (in most cases, this event is sent within 7 calendar days). For example, if the OXXO voucher expires on September 1, this event is sent by September 10 at the latest.

| Event                            | Description                                                     | Next steps                                                                                  |
| -------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `payment_intent.requires_action` | The OXXO voucher is created successfully.                       | Wait for the customer to pay for the OXXO voucher.                                          |
| `payment_intent.processing`      | The customer can no longer pay for the OXXO voucher.            | Wait for the payment to succeed or fail.                                                    |
| `payment_intent.succeeded`       | The customer paid for the OXXO voucher before expiration.       | Fulfill the goods or services that the customer purchased.                                  |
| `payment_intent.payment_failed`  | The customer didn’t pay for the OXXO voucher before expiration. | Contact the customer through email or push notification and request another payment method. |

### Receive events and run business actions

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom Code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

## Test the integration

In a sandbox, set `payment_method.billing_details.email` to the following values when you call [stripe.confirmOxxoPayment](https://docs.stripe.com/js/payment_intents/confirm_oxxo_payment) to test different scenarios.

| Email                       | Description                                                                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | Simulates an OXXO voucher which a customer pays after 3 minutes and the `payment_intent.succeeded` webhook arrives after about 3 minutes. In production, this webhook arrives after 1 business day. |

Example: fulano@test.com |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates an OXXO voucher which a customer pays immediately and the `payment_intent.succeeded` webhook arrives within several seconds. In production, this webhook arrives after 1 business day.

Example: succeed_immediately@test.com |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives within several seconds.

The `expires_after` field in [next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-expires_after) is set to the current time regardless of what the `expires_after_days` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-oxxo-expires_after_days) is set to.

Example: expire_immediately@test.com |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives after about 3 minutes.

The `expires_after` field in [next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-expires_after) is set to 3 minutes in the future regardless of what the `expires_after_days` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-oxxo-expires_after_days) is set to.

Example: expire_with_delay@test.com |
| `{any_prefix}fill_never@{any_domain}` | Simulates an OXXO voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives after 1 business day and 2 calendar days. In production, this webhook arrives at the same time as in testmode.

Example: fill_never@test.com |

## Optional: Display the OXXO details to your customer [Client-side]

We recommend relying on Stripe.js to handle displaying the OXXO voucher with `confirmOxxoPayment`. However, you can also manually display the voucher to your customers.

You can specify `handleActions: false` when calling `stripe.confirmOxxoPayment` in step 4 to indicate that you’ll handle the next action to display the OXXO details to your customer.

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const result = await stripe.confirmOxxoPayment(
    "{{PAYMENT_INTENT_CLIENT_SECRET}}",
    {
      payment_method: {
        billing_details: {
          name: document.getElementById("name").value,
          email: document.getElementById("email").value,
        },
      },
    },
    { handleActions: false },
  );

  if (result.error) {
    // Display error to your customer
    const errorMsg = document.getElementById("error-message");
    errorMsg.innerText = result.error.message;
  } else {
    // An OXXO voucher was successfully created
    const amount = result.paymentIntent.amount;
    const currency = result.paymentIntent.currency;

    const details = result.paymentIntent.next_action.oxxo_display_details;
    const number = details.number;
    const expires_after = details.expires_after;

    // Handle the next action by displaying the OXXO details to your customer

    // You can also use the generated hosted voucher
    const hosted_voucher_url =
      result.paymentIntent.next_action.oxxo_display_details.hosted_voucher_url;
  }
});
```

Include, at minimum, the following:

| Detail               | Description                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OXXO logo            | [Download](https://stripe.com/img/docs/payments/oxxo.png) and display the OXXO logo on the voucher.                                                                                                                                                                                                                                                                               |
| oxxo                 |
| Number               | Locate the number on the `PaymentIntent` object at [next_action.oxxo_display_details.number](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-number).                                                                                                                                                                |
| Expiry date          | Locate the UNIX timestamp after which the OXXO voucher expires on the `PaymentIntent` at [next_action.oxxo_display_details.expires_after](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-oxxo_display_details-expires_after).                                                                                                            |
| Amount               | The amount to be collected.                                                                                                                                                                                                                                                                                                                                                       |
| Currency             | OXXO vouchers are always in Mexican pesos.                                                                                                                                                                                                                                                                                                                                        |
| Barcode              | Generate the barcode from the number using [Code 128](https://en.wikipedia.org/wiki/Code_128). The barcode should be approximately 7.5 cm wide when printed. For mobile displays, make sure the barcode can be zoomed in. This will help the OXXO convenience store cashier scan the barcode. You can use an external library such as [JSBarcode](https://lindell.me/JsBarcode/). |
| Payment instructions | The payment instructions for the customer. See the English and Spanish translations below.                                                                                                                                                                                                                                                                                        |

### OXXO payment instructions

#### English

OXXO payment instructions:

1. Give the voucher to the cashier to scan the barcode.
1. Provide cash payment to the cashier.
1. After the payment is complete, keep the receipt of your payment for your records.
1. For any questions or clarification, please contact the business.

#### HTML

```html
<!-- Include a library for generating OXXO bar codes, such as JsBarcode -->
<!-- <script src="https://cdn.jsdelivr.net/jsbarcode/3.6.0/barcodes/JsBarcode.code128.min.js"></script> -->

<div class="result-oxxo">
  <img width="100px" src="/images/payments/oxxo.png" />
  <div class="amount">MX <span class="order-amount"></span></div>
  <div>Expires <span class="oxxo-expiry-date"></span></div>
  <div class="oxxo-display"></div>

  <button onclick="window.print()">Print</button>

  <div class="instructions">
    Instructions to pay your OXXO:
    <ol>
      <li><p>Give the voucher to the cashier to scan the barcode.</p></li>
      <li><p>Provide cash payment to the cashier.</p></li>
      <li>
        <p>
          After the payment is complete, keep the receipt of your payment for
          your records.
        </p>
      </li>
      <li>
        <p>For any questions or clarification, please contact the merchant.</p>
      </li>
    </ol>
  </div>
</div>
```

#### Spanish

Instrucciones de pago en OXXO:

1. Entregue el código al cajero en cualquier OXXO para que lo escanee.
1. Proporcione el pago en efectivo al cajero.
1. Una vez completado el pago, guarde el recibo de su pago para sus archivos.
1. Para cualquier duda o aclaración, por favor contacte al comerciante.

#### HTML

```html
<!-- Include a library for generating OXXO bar codes, such as JsBarcode -->
<!-- <script src="https://cdn.jsdelivr.net/jsbarcode/3.6.0/barcodes/JsBarcode.code128.min.js"></script> -->

<div class="result-oxxo section-to-print">
  <img width="100px" src="/images/payments/oxxo.png" />
  <div class="amount">MX <span class="order-amount"></span></div>
  <div>Expira el <span class="oxxo-expiry-date"></span></div>
  <div class="oxxo-display"></div>

  <button onclick="window.print()">Imprimir</button>

  <div class="instructions">
    Instrucciones de pago en OXXO:
    <ol>
      <li>
        <p>
          Entregue el código al cajero en cualquier OXXO para que lo escanee.
        </p>
      </li>
      <li><p>Proporcione el pago en efectivo al cajero.</p></li>
      <li>
        <p>
          Una vez completado el pago, guarde el recibo de su pago para sus
          archivos.
        </p>
      </li>
      <li>
        <p>
          Para cualquier duda o aclaración, por favor contacte al comerciante.
        </p>
      </li>
    </ol>
  </div>
</div>
```

*Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) will typically print out the OXXO voucher to bring to an OXXO convenience store. You can provide an easy print button and/or email the OXXO voucher to the customer. Try printing the OXXO voucher yourself to check the barcode size (which should be approximately 7.5 cm wide).

## Optional: Send payment instruction emails

You can enable OXXO payment instruction emails on the [Email Settings](https://dashboard.stripe.com/settings/emails) page in the Dashboard. Once enabled, Stripe sends payment instruction emails upon PaymentIntent confirmation. The emails contain the OXXO number and a link to the Stripe hosted voucher page.

> In testing environments, instruction emails are only sent to email addresses linked to the Stripe account.

## Expiration and cancellation

OXXO vouchers expire after the `expires_after` UNIX timestamp and a customer can’t pay an OXXO voucher once it has expired. OXXO vouchers can’t be canceled before expiration.

After an OXXO voucher expires, the PaymentIntent’s status changes to `requires_payment_method`. At this point, you can confirm the PaymentIntent with another payment method or cancel.
