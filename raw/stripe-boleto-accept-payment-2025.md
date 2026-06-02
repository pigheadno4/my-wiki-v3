<!-- Source URL: https://docs.stripe.com/payments/boleto/accept-a-payment -->
<!-- Fetched: 2026-05-07 -->

# Boleto payments

Learn how to accept Boleto, a common payment method in Brazil.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/boleto/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Boleto is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method where customers are required to [take additional steps](https://docs.stripe.com/payments/payment-methods.md#customer-actions) to complete their payment. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay by using a Boleto voucher with a generated number either in ATMs, banks, bank portals or authorized agencies.

## Determine compatibility

**Supported business locations**: BR

**Supported currencies**: `brl`

**Presentment currencies**: `brl`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: Yes

A Checkout Session must satisfy the following condition to support Boleto payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.

## Accept a payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

This guides you through enabling Boleto and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable Boleto as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `boleto` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the `brl` currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "brl",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "boleto"],
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
        currency: "brl",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "boleto"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Additional payment method options

You can specify an optional `expires_after_days` parameter in the [payment method options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-boleto-expires_after_days) for your `Session` that sets the number of calendar days before a Boleto voucher expires. For example, if you create a Boleto voucher on Monday and you set `expires_after_days` to 2, the Boleto voucher expires on Wednesday at 23:59 America/Sao_Paulo (UTC-3) time. If you set it to 0, the Boleto voucher expires at the end of the day. The `expires_after_days` parameter can be set from 0 to 60 days. The default is 3 days. You can customize the default expiration days on your account in the [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "brl",
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
    boleto: {
      expires_after_days: 7,
    },
  },
  payment_method_types: ["card", "boleto"],
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
        currency: "brl",
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
    boleto: {
      expires_after_days: 7,
    },
  },
  payment_method_types: ["card", "boleto"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Redirect to Stripe hosted voucher page

> Unlike card payments, the customer won’t be redirected to the [success_url](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-success_url) with Boleto payment.

After submitting the Checkout form successfully, the customer is redirected to the `hosted_voucher_url`. The customer can copy the Boleto number or download the voucher PDF from the hosted voucher page.

Stripe sends a [payment_intent.requires_action](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.requires_action) event when a Boleto voucher is created successfully. If you need to email your customers the voucher link, you can locate the `hosted_voucher_url` in [payment_intent.next_action.boleto_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-boleto_display_details-hosted_voucher_url). Learn more about how to [monitor a PaymentIntent with webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks).

Stripe allows customization of customer-facing UIs on the [Branding Settings](https://dashboard.stripe.com/account/branding) page. The following brand settings can be applied to the voucher:

- **Icon**—your brand image and public business name
- **Accent color**—used as the color of the Copy Number button
- **Brand color**—used as the background color

### Fulfill your orders

Because Boleto is a delayed notification payment method, you need to use a method such as *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to monitor the payment status and handle order *fulfillment* (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected). Learn more about [setting up webhooks and fulfilling orders](https://docs.stripe.com/checkout/fulfillment.md).

The following events are sent when the payment status changes:

| Event Name                                                                                                       | Description                                                                                         | Next steps |
| ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ---------- |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) | The customer has successfully submitted the Checkout form. Stripe has generated the Boleto voucher. |

You can choose to email the `hosted_voucher_url` to your customer in case they lose the Boleto voucher. | Wait for the customer to pay the Boleto. |
| [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) | The customer has successfully paid the Boleto. The `PaymentIntent` transitions to `succeeded`. | Fulfill the goods or services that the customer purchased. |
| [checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_failed) | The Boleto voucher has expired, or the payment has failed for some other reason. The `PaymentIntent` returns to a status of `requires_payment_method`. | Contact the customer through email and request that they place a new order. |

## Test your integration

When testing your Checkout integration, select Boleto as the payment method and click the **Pay** button.

| Email                       | Description                                                                                                                                                                                                    |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | Simulates a Boleto voucher which a customer pays after 3 minutes and the `payment_intent.succeeded` webhook arrives after about 3 minutes. In production, this webhook arrives 1 business day after a payment. |

Example: fulaninho@example.com |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates a Boleto voucher which a customer pays immediately and the `payment_intent.succeeded` webhook arrives within several seconds. In production, this webhook arrives 1 business day after a payment.

Example: succeed_immediately@example.com |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates a Boleto voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives within several seconds.

The `expires_at` field in [next_action.boleto_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-boleto_display_details-expires_at) is set to the current time regardless of what the `expires_after_days` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-boleto-expires_after_days) is set to.

Example: expire_immediately@example.com |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates a Boleto voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives after about 3 minutes.

The `expires_at` field in [next_action.boleto_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-boleto_display_details-expires_at) is set to 3 minutes in the future regardless of what the `expires_after_days` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-boleto-expires_after_days) is set to.

Example: expire_with_delay@example.com |
| `{any_prefix}fill_never@{any_domain}` | Simulates a Boleto voucher which never succeeds; it expires according to the `expires_at` field in [next_action.boleto_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-boleto_display_details-expires_at) per the provided parameters in the [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-boleto-expires_after_days) and the `payment_intent.payment_failed` webhook arrives after that.

Example: fill_never@example.com |

| Tax ID | Description |
| ------ | ----------- |

| CPF `000.000.000-00`

CNPJ `00.000.000/0000-00` | In a sandbox, set `tax_id` to these values, so they bypass the tax ID validation. |

## Handle refunds

Boleto payments can’t be refunded. Some merchants have created a separate process to credit their customers who reach out directly.

## Handle disputes

Boleto payments can’t be disputed by the customer.

## Optional: Send payment instruction emails

You can enable Boleto payment instruction emails on the [Email Settings](https://dashboard.stripe.com/settings/emails) page in the Dashboard. Once enabled, Stripe sends payment instruction emails upon PaymentIntent confirmation. The emails contain the Boleto number and a link to the Stripe hosted voucher page.

> In test environments, instruction emails are only sent to email addresses linked to the Stripe account.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Checkout Sessions API

> This is a Checkout Sessions API for when payment-ui is elements and api-integration is checkout. View the full page at https://docs.stripe.com/payments/boleto/accept-a-payment?payment-ui=elements&api-integration=checkout.

To determine which API meets your business needs, see the [comparison guide](https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md).

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to embed a custom Stripe payment form in your website or application and offer payment methods to customers. For advanced configurations and customizations, refer to the [Accept a Payment](https://docs.stripe.com/payments/accept-a-payment.md) integration guide.

## Determine compatibility

**Supported business locations**: BR

**Supported currencies**: `brl`

**Presentment currencies**: `brl`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: Yes

A Checkout Session must satisfy all of the following conditions to support Boleto payments:

- Prices for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.

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
          currency: 'brl',
          product_data: {
            name: 'T-shirt',
          },
          unit_amount: 2000,
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
          currency: 'brl',
          product_data: {
            name: 'T-shirt',
          },
          unit_amount: 2000,
        },
        quantity: 1,
      },
    ],
    mode: 'payment',
    ui_mode: 'elements',
    payment_method_types: ['boleto'],
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

In live mode, tapping **Pay** redirects you to the boleto website—you don’t have the option to approve or decline the payment with boleto.

# Payment Intents API

> This is a Payment Intents API for when payment-ui is elements and api-integration is paymentintents. View the full page at https://docs.stripe.com/payments/boleto/accept-a-payment?payment-ui=elements&api-integration=paymentintents.

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
  amount: 2000,
  currency: "brl",
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
  amount: 2000,
  currency: "brl",
  paymentMethodTypes: ["boleto"],
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
    amount: 2000,
    currency: "brl",
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
    amount: 2000,
    currency: "brl",
    paymentMethodTypes: ["boleto"],
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
    amount: 2000,
    currency: "brl",
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
    amount: 2000,
    currency: "brl",
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
    amount: 2000,
    currency: "brl",
    payment_method_types: ["boleto"],
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
    amount: 2000,
    currency: "brl",
    payment_method_types: ["boleto"],
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

In live mode, tapping **Pay** redirects you to the boleto website—you don’t have the option to approve or decline the payment with boleto.

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

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/boleto/accept-a-payment?payment-ui=direct-api.

Stripe users in Brazil can accept Boleto payments from customers in Brazil by using the Payment Intents and Payment Methods APIs. *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) pay by using a Boleto voucher with a generated number either in ATMs, banks, bank portals or authorized agencies.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

Stripe uses a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) object to represent your intent to collect payment from a customer, tracking state changes from Boleto voucher creation to payment completion.

Create a PaymentIntent on your server with an amount and the `brl` currency (Boleto doesn’t support other currencies). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `boleto` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntent`.

Included in the returned PaymentIntent is a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which you have to use to securely complete the payment process. Send the client secret back to the client so you can use it in later steps.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "brl",
  payment_method_types: ["boleto"],
});
```

### Additional payment method options

You can specify an optional `expires_after_days` parameter in the [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-boleto-expires_after_days) for your `PaymentIntent` that sets the number of calendar days before a Boleto voucher expires. For example, if you create a Boleto voucher on Monday and you set `expires_after_days` to 2, the Boleto voucher will expire on Wednesday at 23:59 America/Sao_Paulo (UTC-3) time. If you set it to 0, the Boleto voucher will expire at the end of the day. The `expires_after_days` parameter can be set from 0 to 60 days. The default is 3 days. You can customize the default expiration days on your account in the [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

## Collect payment method details [Client-side]

Create a payment form on your client to collect the required billing details from the customer:

| Field         | Value                                                                                                                                                                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`        | The full name of the customer.                                                                                                                                                                                                                                                    |
| `email`       | The email address of the customer.                                                                                                                                                                                                                                                |
| `tax_id`      | The CPF (for individuals) or CNPJ (for businesses) of the customer. The CPF must have 11 digits in either of the following formats: `000.000.000-00` or `00000000000`. The CNPJ must have 14 digits in either of the following formats: `00.000.000/0000-00` or `00000000000000`. |
| `address`     | Street name and number of the customer’s address.                                                                                                                                                                                                                                 |
| `city`        | City of the customer’s address.                                                                                                                                                                                                                                                   |
| `state`       | Two-letter Brazilian state code ([ISO_3166-2:BR](https://en.wikipedia.org/wiki/ISO_3166-2:BR)) of the customer’s address.                                                                                                                                                         |
| `postal_code` | Postal code of the customer’s address. The postal code must be in either of the following formats: `XXXXX-XXX` or `XXXXXXXX`.                                                                                                                                                     |

> These fields `name`, `address`, `city` must contain at least one alphanumeric character from the [Basic Latin (ASCII) Unicode Block](<https://en.wikipedia.org/wiki/Basic_Latin_(Unicode_block)>).

```html
<form id="payment-form">
  <div class="form-row">
    <label for="name"> Name </label>
    <input id="name" name="name" required />
  </div>

  <div class="form-row">
    <label for="tax_id"> CPF/CNPJ </label>
    <input id="tax_id" name="tax_id" required />
  </div>

  <div class="form-row">
    <label for="email"> Email </label>
    <input id="email" name="email" required />
  </div>

  <div class="form-row">
    <label for="address"> Address </label>
    <input id="address" name="address" required />
  </div>

  <div class="form-row">
    <label for="city"> City </label>
    <input id="city" name="city" required />
  </div>

  <div class="form-row">
    <label for="state"> State </label>
    <input id="state" name="state" required />
  </div>

  <div class="form-row">
    <label for="postal_code"> Postal Code </label>
    <input id="postal_code" name="postal_code" required />
  </div>

  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>

  <button id="submit-button">Pay with Boleto</button>
</form>
```

## Submit the payment to Stripe [Client-side]

When a customer clicks to pay with Boleto, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is our foundational JavaScript library for building payment flows.

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

Use [stripe.confirmBoletoPayment](https://docs.stripe.com/js/payment_intents/confirm_boleto_payment) and the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object that you created in Step 2 to submit the customer’s billing details.

Upon confirmation, Stripe will automatically open a modal to display the Boleto voucher to your customer.

```javascript
var form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const result = await stripe.confirmBoletoPayment(
    "{{PAYMENT_INTENT_CLIENT_SECRET}}",
    {
      payment_method: {
        boleto: {
          tax_id: document.getElementById("tax_id").value,
        },
        billing_details: {
          name: document.getElementById("name").value,
          email: document.getElementById("email").value,
          address: {
            line1: document.getElementById("address").value,
            city: document.getElementById("city").value,
            state: document.getElementById("state").value,
            postal_code: document.getElementById("postal_code").value,
            country: "BR",
          },
        },
      },
    },
  );
  // Stripe.js will open a modal to display the Boleto voucher to your customer
  // This async function finishes when the customer closes the modal

  if (result.error) {
    // Display error to your customer
    const errorMsg = document.getElementById("error-message");
    errorMsg.innerText = result.error.message;
  }
});
```

> `stripe.confirmBoletoPayment` may take several seconds to complete. During that time, disable your form from being resubmitted and show a waiting indicator like a spinner. If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator.

When a Boleto voucher is created successfully, the value of the returned PaymentIntent’s `status` property is `requires_action`. Check the status of a PaymentIntent in the [Dashboard](https://dashboard.stripe.com/test/payments) or by inspecting the status property on the object. If the Boleto voucher wasn’t created successfully, inspect the returned `error` to determine the cause (for example, invalid email format).

### Optional: Email voucher link to your customer

Stripe sends a [payment_intent.requires_action](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.requires_action) event when a Boleto voucher is created successfully. If you need to email your customers the voucher link, you can locate the `hosted_voucher_url` in [payment_intent.next_action.boleto_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-boleto_display_details-hosted_voucher_url).

### Optional: Customize your voucher

Stripe allows customization of customer-facing UIs on the [Branding Settings](https://dashboard.stripe.com/account/branding) page.

The following brand settings can be applied to the voucher:

- **Icon**—your brand image and public business name
- **Accent color**—used as the color of the Copy Number button
- **Brand color**—used as the background color

## Handle post-payment events [Server-side]

Boleto payments are asynchronous, so funds aren’t immediately available. Customers might not pay for the Boleto voucher immediately after checking out.

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event on the next business day (Monday through Friday excluding Brazilian holidays) for each Boleto voucher that was paid. Use the Dashboard or a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to receive these events and run actions (for example, sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow).

If a Boleto voucher isn’t paid before 23:59 America/Sao_Paulo (UTC-3) on the expiry date, Stripe sends a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) event after 1 business day. For example, if a Boleto voucher expires on Thursday, the event is sent on Friday. If a Boleto voucher expires on Friday, the event is sent the following Monday.

| Event                           | Description                                                   | Next steps                                                                                  |
| ------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `payment_intent.succeeded`      | The customer paid for the Boleto voucher before expiration.   | Fulfill the goods or services that the customer purchased.                                  |
| `payment_intent.payment_failed` | The customer didn’t pay the Boleto voucher before expiration. | Contact the customer through email or push notification and request another payment method. |

## Test the integration

In a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), set `payment_method.billing_details.email` to the following values when you call [stripe.confirmBoletoPayment](https://docs.stripe.com/js/payment_intents/confirm_boleto_payment) to test different scenarios.

| Email                       | Description                                                                                                                                                                                                    |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{any_prefix}@{any_domain}` | Simulates a Boleto voucher which a customer pays after 3 minutes and the `payment_intent.succeeded` webhook arrives after about 3 minutes. In production, this webhook arrives 1 business day after a payment. |

Example: fulaninho@example.com |
| `{any_prefix}succeed_immediately@{any_domain}` | Simulates a Boleto voucher which a customer pays immediately and the `payment_intent.succeeded` webhook arrives within several seconds. In production, this webhook arrives 1 business day after a payment.

Example: succeed_immediately@example.com |
| `{any_prefix}expire_immediately@{any_domain}` | Simulates a Boleto voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives within several seconds.

The `expires_at` field in [next_action.boleto_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-boleto_display_details-expires_at) is set to the current time regardless of what the `expires_after_days` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-boleto-expires_after_days) is set to.

Example: expire_immediately@example.com |
| `{any_prefix}expire_with_delay@{any_domain}` | Simulates a Boleto voucher which expires before a customer pays and the `payment_intent.payment_failed` webhook arrives after about 3 minutes.

The `expires_at` field in [next_action.boleto_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-boleto_display_details-expires_at) is set to 3 minutes in the future regardless of what the `expires_after_days` parameter in [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-boleto-expires_after_days) is set to.

Example: expire_with_delay@example.com |
| `{any_prefix}fill_never@{any_domain}` | Simulates a Boleto voucher which never succeeds; it expires according to the `expires_at` field in [next_action.boleto_display_details](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-boleto_display_details-expires_at) per the provided parameters in the [payment method options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-boleto-expires_after_days) and the `payment_intent.payment_failed` webhook arrives after that.

Example: fill_never@example.com |

| Tax ID | Description |
| ------ | ----------- |

| CPF `000.000.000-00`

CNPJ `00.000.000/0000-00` | In a sandbox, set `tax_id` to these values, so they bypass the tax ID validation. |

## Optional: Build your own voucher page [Client-side]

We recommend relying on Stripe.js to handle displaying the Boleto voucher with `confirmBoletoPayment`. However, you can also manually display the voucher to your customers.

You can specify `handleActions: false` when calling stripe.confirmBoletoPayment in step 4 to indicate that you’ll handle the next action to display the Boleto details to your customer.

```javascript
var form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const result = await stripe.confirmBoletoPayment(
    "{{PAYMENT_INTENT_CLIENT_SECRET}}",
    {
      payment_method: {
        boleto: {
          tax_id: document.getElementById("tax_id").value,
        },
        billing_details: {
          name: document.getElementById("name").value,
          email: document.getElementById("email").value,
          address: {
            line1: document.getElementById("address").value,
            city: document.getElementById("city").value,
            state: document.getElementById("state").value,
            postal_code: document.getElementById("postal_code").value,
            country: "BR",
          },
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
    // An Boleto voucher was successfully created
    const amount = result.paymentIntent.amount;
    const currency = result.paymentIntent.currency;

    const details = result.paymentIntent.next_action.boleto_display_details;
    const number = details.number;
    const expires_at = details.expires_at;

    // Handle the next action by displaying the Boleto details to your customer

    // You can also use the generated hosted voucher
    const hosted_voucher_url = details.hosted_voucher_url;
  }
});
```

Include, at minimum, the following:

| Detail       | Description                                                                                                                                                                                                                                                                                                                                     |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number       | Display the boleto voucher number such that it’s easy for your customers to copy them to their clipboard. Locate the number on the `PaymentIntent` object at [next_action.boleto_display_details.number](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-boleto_display_details-number).                |
| Expiry date  | Display the boleto voucher expiry date is. Locate the UNIX timestamp after which the Boleto voucher expires on the `PaymentIntent` at [next_action.boleto_display_details.expires_at](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-boleto_display_details-expires_at).                               |
| Download pdf | Display a download button that allows your customer to download the boleto pdf. Locate the pdf, where the customer can download the Boleto voucher PDF, on the `PaymentIntent` at [next_action.boleto_display_details.pdf](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action-boleto_display_details-pdf). |

## Optional: Confirm Payment Intent server-side [Server-side]

We recommend relying on Stripe.js to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) a Boleto Payment Intent with `confirmBoletoPayment`. Using Stripe.js makes it much easier to extend your integration to other payment methods. However, you can also confirm a Payment Intent server-side as follows:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "brl",
  confirm: true,
  payment_method_types: ["boleto"],
  payment_method_data: {
    type: "boleto",
    billing_details: {
      name: "João da Silva",
      email: "joao@exemplo.com",
      address: {
        line1: "1234 Av. Paulista",
        city: "São Paulo",
        state: "SP",
        postal_code: "01310-000",
        country: "BR",
      },
    },
    boleto: {
      tax_id: "000.000.000-00",
    },
  },
});
```

## Optional: Send payment instruction emails

You can enable Boleto payment instruction emails on the [Email Settings](https://dashboard.stripe.com/settings/emails) page in the Dashboard. Once enabled, Stripe sends payment instruction emails upon PaymentIntent confirmation. The emails contain the Boleto number and a link to the Stripe hosted voucher page.

> In test environments, instruction emails are only sent to email addresses linked to the Stripe account.

## Expiration and cancellation

Boleto vouchers expire after the `expires_at` UNIX timestamp and a customer can’t pay a Boleto voucher once it has expired. Boleto vouchers can’t be canceled before expiration.

After a Boleto voucher expires, the PaymentIntent’s status changes to `requires_payment_method`. At this point, you can confirm the PaymentIntent with another payment method or cancel.
