<!-- Source URL: https://docs.stripe.com/payments/existing-customers -->
<!-- Fetched: 2026-05-11 -->

# Payments for existing customers

Learn how to charge an existing payment method while a customer is on-session.

# Stripe-hosted page

> This is a Stripe-hosted page for when platform is web and ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/existing-customers?platform=web&ui=stripe-hosted.

A Checkout Session allows buyers to enter their payment details. If the buyer is an existing customer, you can configure the Checkout Session to prefill the details with one of the customer’s [saved cards](https://docs.stripe.com/payments/save-and-reuse.md?platform=web&ui=stripe-hosted). The Checkout Session displays up to 50 saved cards that a customer can choose to pay with.
![Checkout with one saved card](assets/stripe-checkout-saved-card.png)

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

Checkout supports reusing existing customer-configured `Account` objects with the [customer_account](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_account) parameter or `Customer` objects with the [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) parameter. When reusing existing customers, all objects created by Checkout, such as `PaymentIntents` and `Subscriptions`, are associated with the object that represents that customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Append the `{CHECKOUT_SESSION_ID}` template variable to the `success_url` to get access to the Session ID after your customer successfully completes a Checkout Session. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  customer: "{{CUSTOMER_ID}}",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});
```

## Optional: Display additional saved payment methods [Server-side]

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. When rendering past payment methods to a customer for future purchases, make sure you’ve collected consent to save the payment method details for this specific future use.

By default, we only show payment methods set to [always allow redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay).

You can’t reuse Apple Pay and Google Pay during a Checkout Session, so these payment methods don’t appear in the list of saved options. You must display the Google Pay and Apple Pay UI, and the payment request button UI, each time the Checkout Session is active.

You can display other previously saved payment methods by including other redisplay values in the Checkout Session, or by updating a payment method’s `allow_redisplay` setting to `always`.

- Use the `allow_redisplay_filters` [parameter](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-saved_payment_method_options-allow_redisplay_filters) to specify which saved payment methods to show in Checkout. You can set any of the valid values: `limited`, `unspecified` and `always`.

  If you specify redisplay filtering in your Checkout Session, it overrides the default behavior, so you must include the `always` value to see those saved payment methods.

  #### Accounts v2

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const session = await stripe.checkout.sessions.create({
    mode: "payment",
    line_items: [
      {
        price: "{{PRICE_ID}}",
        quantity: 1,
      },
    ],
    customer_account: "{{CUSTOMERACCOUNT_ID}}",
    success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
    saved_payment_method_options: {
      allow_redisplay_filters: ["always", "limited", "unspecified"],
    },
  });
  ```

  #### Customers v1

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const session = await stripe.checkout.sessions.create({
    mode: "payment",
    line_items: [
      {
        price: "{{PRICE_ID}}",
        quantity: 1,
      },
    ],
    customer: "{{CUSTOMER_ID}}",
    success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
    saved_payment_method_options: {
      allow_redisplay_filters: ["always", "limited", "unspecified"],
    },
  });
  ```

- [Update the Payment Method](https://docs.stripe.com/api/payment_methods/update.md) to set the `allow_redisplay` value on individual payment methods.

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const paymentMethod = await stripe.paymentMethods.update(
    "{{PAYMENTMETHOD_ID}}",
    {
      allow_redisplay: "always",
    },
  );
  ```

## Prefill fields on payment page

If all the following conditions are true, Checkout prefills the **email**, **name**, **card**, and **billing address** fields on the payment page using details from the customer’s saved card:

- Checkout is in `payment` or `subscription` mode; `setup` mode doesn’t support prefilling fields.
- The customer has a saved card. Checkout only supports prefilling card payment methods.
- The saved card has `allow_redisplay` set to `always` or you adjusted the [default display setting](https://docs.stripe.com/payments/existing-customers.md#display-additional-saved-payment-methods).
- The payment method includes [`billing_details`](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-billing_details) required by the Checkout Session’s [`billing_address_collection`](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-billing_address_collection) value:
  - `auto` requires values for `email`, `name`, and `address[country]`. US, CA, and GB billing addresses also require `address[postal_code]`.
  - `required` requires values for `email`, `name`, and all `address` fields.

If your customer has multiple saved cards, Checkout prefills details from the card matching the following prioritization:

- In `payment` mode, Stripe prefills the fields using the customer’s newest saved card.
- In `subscription` mode, Stripe prefills the customer’s default payment method if it’s a card. Otherwise, Stripe prefills the newest saved card.

When Checkout is [collecting a shipping address](https://docs.stripe.com/payments/collect-addresses.md), it prefills shipping address fields if the customer’s shipping address is in one of the Checkout Session’s [supported countries](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_address_collection-allowed_countries).

To let your customers remove saved cards during a Checkout Session, set [save_payment_method_options[payment_method_remove]](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-saved_payment_method_options-payment_method_remove) to `enabled`.

> #### Prefill timeout
>
> The prefilled payment method displays for 30 minutes following Checkout Session creation. After it expires, loading the same Checkout Session doesn’t prefill the payment method anymore for security reasons.

## Handle post-payment events [Server-side]

Stripe sends a [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) event when a customer completes a Checkout Session payment. Use the [Dashboard webhook tool](https://dashboard.stripe.com/webhooks) or follow the [webhook guide](https://docs.stripe.com/webhooks/quickstart.md) to receive and handle these events, which might trigger you to:

- Send an order confirmation email to your customer.
- Log the sale in a database.
- Start a shipping workflow.

Listen for these events rather than waiting for your customer to be redirected back to your website. Triggering fulfillment only from your Checkout landing page is unreliable. Setting up your integration to listen for asynchronous events allows you to accept [different types of payment methods](https://stripe.com/payments/payment-methods-guide) with a single integration.

Learn more in our [fulfillment guide for Checkout](https://docs.stripe.com/checkout/fulfillment.md).

Handle the following events when collecting payments with the Checkout:

| Event                                                                                                                                        | Description                                                                                | Action                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed)                             | Sent when a customer successfully completes a Checkout Session.                            | Send the customer an order confirmation and _fulfill_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) their order. |
| [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) | Sent when a payment made with a delayed payment method, such as ACH direct debt, succeeds. | Send the customer an order confirmation and _fulfill_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) their order. |
| [checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_failed)       | Sent when a payment made with a delayed payment method, such as ACH direct debt, fails.    | Notify the customer of the failure and bring them back on-session to attempt payment again.                                                                                                      |

# Full embedded page

> This is a Full embedded page for when platform is web and ui is embedded-page. View the full page at https://docs.stripe.com/payments/existing-customers?platform=web&ui=embedded-page.

A Checkout Session allows buyers to enter their payment details. If the buyer is an existing customer, you can configure the Checkout Session to prefill the details with one of the customer’s [saved cards](https://docs.stripe.com/payments/save-and-reuse.md?platform=web&ui=embedded-page). The Checkout Session displays up to 50 saved cards that a customer can choose to pay with.
![Checkout with one saved card](assets/stripe-checkout-saved-card.png)

## Create a Checkout Session [Server-side]

Checkout supports reusing existing customer-configured `Account` objects with the [customer_account](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_account) parameter or `Customer` objects with the [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) parameter. When reusing existing customers, all objects created by Checkout, such as `PaymentIntents` and `Subscriptions`, are associated with the object that represents that customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

From your server, create a _Checkout Session_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription)

and set the [ui_mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-ui_mode) to `embedded_page`.

To return customers to a custom page that you host on your website, specify that page’s URL in the [return_url](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-return_url) parameter. Include the `{CHECKOUT_SESSION_ID}` template variable in the URL to retrieve the session’s status on the return page. Checkout automatically substitutes the variable with the Checkout Session ID before redirecting.

Read more about [configuring the return page](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=embedded-page#return-page) and other options for [customizing redirect behavior](https://docs.stripe.com/payments/checkout/custom-success-page.md?payment-ui=embedded-page).

After you create the Checkout Session, use the `client_secret` returned in the response to [mount Checkout](https://docs.stripe.com/payments/existing-customers.md#mount-checkout).

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  ui_mode: "embedded_page",
  return_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  customer: "{{CUSTOMER_ID}}",
  ui_mode: "embedded_page",
  return_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});
```

## Optional: Display additional saved payment methods [Server-side]

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. When rendering past payment methods to a customer for future purchases, make sure you’ve collected consent to save the payment method details for this specific future use.

By default, we only show payment methods set to [always allow redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay).

You can’t reuse Apple Pay and Google Pay during a Checkout Session, so these payment methods don’t appear in the list of saved options. You must display the Google Pay and Apple Pay UI, and the payment request button UI, each time the Checkout Session is active.

You can display other previously saved payment methods by including other redisplay values in the Checkout Session, or by updating a payment method’s `allow_redisplay` setting to `always`.

- Use the `allow_redisplay_filters` [parameter](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-saved_payment_method_options-allow_redisplay_filters) to specify which saved payment methods to show in Checkout. You can set any of the valid values: `limited`, `unspecified` and `always`.

  If you specify redisplay filtering in your Checkout Session, it overrides the default behavior, so you must include the `always` value to see those saved payment methods.

  #### Accounts v2

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const session = await stripe.checkout.sessions.create({
    mode: "payment",
    ui_mode: "embedded_page",
    line_items: [
      {
        price: "{{PRICE_ID}}",
        quantity: 1,
      },
    ],
    customer_account: "{{CUSTOMERACCOUNT_ID}}",
    return_url: "https://example.com/return?session_id={CHECKOUT_SESSION_ID}",
    saved_payment_method_options: {
      allow_redisplay_filters: ["always", "limited", "unspecified"],
    },
  });
  ```

  #### Customers v1

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const session = await stripe.checkout.sessions.create({
    mode: "payment",
    ui_mode: "embedded_page",
    line_items: [
      {
        price: "{{PRICE_ID}}",
        quantity: 1,
      },
    ],
    customer: "{{CUSTOMER_ID}}",
    return_url: "https://example.com/return?session_id={CHECKOUT_SESSION_ID}",
    saved_payment_method_options: {
      allow_redisplay_filters: ["always", "limited", "unspecified"],
    },
  });
  ```

- [Update the Payment Method](https://docs.stripe.com/api/payment_methods/update.md) to set the `allow_redisplay` value on individual payment methods.

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const paymentMethod = await stripe.paymentMethods.update(
    "{{PAYMENTMETHOD_ID}}",
    {
      allow_redisplay: "always",
    },
  );
  ```

## Mount Checkout [Client-side]

#### HTML + JS

Checkout is available as part of [Stripe.js](https://docs.stripe.com/js.md). Include the Stripe.js script on your page by adding it to the head of your HTML file. Next, create an empty DOM node (container) to use for mounting.

```html
<head>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
<body>
  <div id="checkout">
    <!-- Checkout will insert the payment form here -->
  </div>
</body>
```

Initialize Stripe.js with your publishable API key.

Create an asynchronous `fetchClientSecret` function that makes a request to your server to create the Checkout Session and retrieve the client secret. Pass this function into `options` when you create the Checkout instance:

```javascript
// Initialize Stripe.js
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");

initialize();

// Fetch Checkout Session and retrieve the client secret
async function initialize() {
  const fetchClientSecret = async () => {
    const response = await fetch("/create-checkout-session", {
      method: "POST",
    });
    const { clientSecret } = await response.json();
    return clientSecret;
  };

  // Initialize Checkout
  const checkout = await stripe.createEmbeddedCheckoutPage({
    fetchClientSecret,
  });

  // Mount Checkout
  checkout.mount("#checkout");
}
```

#### React

Install [react-stripe-js](https://docs.stripe.com/sdks/stripejs-react.md) and the Stripe.js loader from npm:

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

To use the Embedded Checkout component, create an `EmbeddedCheckoutProvider`. Call `loadStripe` with your publishable API key and pass the returned `Promise` to the provider.

Create an asynchronous `fetchClientSecret` function that makes a request to your server to create the Checkout Session and retrieve the client secret. Pass this function into the `options` prop accepted by the provider.

```jsx
import * as React from "react";
import { loadStripe } from "@stripe/stripe-js";
import {
  EmbeddedCheckoutProvider,
  EmbeddedCheckout,
} from "@stripe/react-stripe-js";

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("pk_test_123");

const App = () => {
  const fetchClientSecret = React.useCallback(() => {
    // Create a Checkout Session
    return fetch("/create-checkout-session", {
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => data.clientSecret);
  }, []);

  const options = { fetchClientSecret };

  return (
    <div id="checkout">
      <EmbeddedCheckoutProvider stripe={stripePromise} options={options}>
        <EmbeddedCheckout />
      </EmbeddedCheckoutProvider>
    </div>
  );
};
```

Checkout renders in an iframe that securely sends payment information to Stripe over an HTTPS connection.

> Avoid placing Checkout within another iframe because some payment methods require redirecting to another page for payment confirmation.

### Customize appearance

Customize Checkout to match the design of your site by setting the background color, button color, border radius, and fonts in your account’s [branding settings](https://dashboard.stripe.com/settings/branding).

By default, Checkout renders with no external padding or margin. We recommend using a container element such as a div to apply your desired margin (for example, 16px on all sides).

## Prefill fields on payment page

If all the following conditions are true, Checkout prefills the **email**, **name**, **card**, and **billing address** fields on the payment page using details from the customer’s saved card:

- Checkout is in `payment` or `subscription` mode; `setup` mode doesn’t support prefilling fields.
- The customer has a saved card. Checkout only supports prefilling card payment methods.
- The saved card has `allow_redisplay` set to `always` or you adjusted the [default display setting](https://docs.stripe.com/payments/existing-customers.md#display-additional-saved-payment-methods).
- The payment method includes [`billing_details`](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-billing_details) required by the Checkout Session’s [`billing_address_collection`](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-billing_address_collection) value:
  - `auto` requires values for `email`, `name`, and `address[country]`. US, CA, and GB billing addresses also require `address[postal_code]`.
  - `required` requires values for `email`, `name`, and all `address` fields.

If your customer has multiple saved cards, Checkout prefills details from the card matching the following prioritization:

- In `payment` mode, Stripe prefills the fields using the customer’s newest saved card.
- In `subscription` mode, Stripe prefills the customer’s default payment method if it’s a card. Otherwise, Stripe prefills the newest saved card.

When Checkout is [collecting a shipping address](https://docs.stripe.com/payments/collect-addresses.md), it prefills shipping address fields if the customer’s shipping address is in one of the Checkout Session’s [supported countries](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_address_collection-allowed_countries).

To let your customers remove saved cards during a Checkout Session, set [save_payment_method_options[payment_method_remove]](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-saved_payment_method_options-payment_method_remove) to `enabled`.

> #### Prefill timeout
>
> The prefilled payment method displays for 30 minutes following Checkout Session creation. After it expires, loading the same Checkout Session doesn’t prefill the payment method anymore for security reasons.

## Handle post-payment events [Server-side]

Stripe sends a [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) event when a customer completes a Checkout Session payment. Use the [Dashboard webhook tool](https://dashboard.stripe.com/webhooks) or follow the [webhook guide](https://docs.stripe.com/webhooks/quickstart.md) to receive and handle these events, which might trigger you to:

- Send an order confirmation email to your customer.
- Log the sale in a database.
- Start a shipping workflow.

Listen for these events rather than waiting for your customer to be redirected back to your website. Triggering fulfillment only from your Checkout landing page is unreliable. Setting up your integration to listen for asynchronous events allows you to accept [different types of payment methods](https://stripe.com/payments/payment-methods-guide) with a single integration.

Learn more in our [fulfillment guide for Checkout](https://docs.stripe.com/checkout/fulfillment.md).

Handle the following events when collecting payments with the Checkout:

| Event                                                                                                                                        | Description                                                                                | Action                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed)                             | Sent when a customer successfully completes a Checkout Session.                            | Send the customer an order confirmation and _fulfill_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) their order. |
| [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) | Sent when a payment made with a delayed payment method, such as ACH direct debt, succeeds. | Send the customer an order confirmation and _fulfill_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) their order. |
| [checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_failed)       | Sent when a payment made with a delayed payment method, such as ACH direct debt, fails.    | Notify the customer of the failure and bring them back on-session to attempt payment again.                                                                                                      |

# Elements

> This is a Elements for when platform is web and ui is embedded-components. View the full page at https://docs.stripe.com/payments/existing-customers?platform=web&ui=embedded-components.

A Checkout Session allows buyers to enter their payment details. If the buyer is an existing customer, you can configure the Checkout Session to prefill the details with one of the customer’s [saved cards](https://docs.stripe.com/payments/checkout/save-during-payment.md?payment-ui=embedded-components). The Checkout Session displays up to 50 saved cards that a customer can choose to pay with.
![Payment Element with one saved card](assets/stripe-payment-element-saved-card.png)

## Create a Checkout Session [Client-side] [Server-side]

Checkout Sessions supports reusing existing customer-configured `Account` objects with the [customer_account](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_account) parameter or `Customer` objects with the [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) parameter. When reusing existing customers, all objects created by Checkout, such as `PaymentIntents` and `Subscriptions`, are associated with the object that represents that customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  ui_mode: "elements",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  return_url: "https://example.com/return?session_id={CHECKOUT_SESSION_ID}",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  ui_mode: "elements",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  customer: "{{CUSTOMER_ID}}",
  return_url: "https://example.com/return?session_id={CHECKOUT_SESSION_ID}",
});
```

## Optional: Display additional saved payment methods [Server-side]

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. When rendering past payment methods to a customer for future purchases, make sure you’ve collected consent to save the payment method details for this specific future use.

By default, we only show payment methods set to [always allow redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay).

You can’t reuse Apple Pay and Google Pay during a Checkout Session, so these payment methods don’t appear in the list of saved options. You must display the Google Pay and Apple Pay UI, and the payment request button UI, each time the Checkout Session is active.

You can display other previously saved payment methods by including other redisplay values in the Checkout Session, or by updating a payment method’s `allow_redisplay` setting to `always`.

- Use the `allow_redisplay_filters` [parameter](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-saved_payment_method_options-allow_redisplay_filters) to specify which saved payment methods to show in Checkout. You can set any of the valid values: `limited`, `unspecified` and `always`.

  If you specify redisplay filtering in your Checkout Session, it overrides the default behavior, so you must include the `always` value to see those saved payment methods.

  #### Accounts v2

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const session = await stripe.checkout.sessions.create({
    mode: "payment",
    ui_mode: "elements",
    line_items: [
      {
        price: "{{PRICE_ID}}",
        quantity: 1,
      },
    ],
    customer_account: "{{CUSTOMERACCOUNT_ID}}",
    return_url: "https://example.com/return?session_id={CHECKOUT_SESSION_ID}",
    saved_payment_method_options: {
      allow_redisplay_filters: ["always", "limited", "unspecified"],
    },
  });
  ```

  #### Customers v1

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const session = await stripe.checkout.sessions.create({
    mode: "payment",
    ui_mode: "elements",
    line_items: [
      {
        price: "{{PRICE_ID}}",
        quantity: 1,
      },
    ],
    customer: "{{CUSTOMER_ID}}",
    return_url: "https://example.com/return?session_id={CHECKOUT_SESSION_ID}",
    saved_payment_method_options: {
      allow_redisplay_filters: ["always", "limited", "unspecified"],
    },
  });
  ```

- [Update the Payment Method](https://docs.stripe.com/api/payment_methods/update.md) to set the `allow_redisplay` value on individual payment methods.

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const paymentMethod = await stripe.paymentMethods.update(
    "{{PAYMENTMETHOD_ID}}",
    {
      allow_redisplay: "always",
    },
  );
  ```

## Display the Payment Element [Client-side]

#### HTML + JS

### Set up Stripe.js

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

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
    <!-- Checkout will create form elements here -->
  </div>
  <button id="submit">Submit</button>
  <div id="error-message">
    <!-- Display error message to your customers here -->
  </div>
</form>
```

Fetch the Checkout Session `client_secret` from the previous step to initialize the `Checkout` object. Then create and mount the Payment Element.

```javascript
const promise = fetch("/create-checkout-session", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
})
  .then((r) => r.json())
  .then((r) => r.clientSecret);

// Initialize Checkout
const checkout = stripe.initCheckoutElementsSdk({
  clientSecret: promise,
});

// Create and mount the Payment Element
const paymentElement = checkout.createPaymentElement();
paymentElement.mount("#payment-element");
```

#### React

### Set up Stripe.js

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry:

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

### Add and configure the CheckoutElementsProvider to your payment page

Fetch the Checkout Session `client_secret` from the previous step to initialize the [CheckoutElementsProvider](https://docs.stripe.com/js/react_stripe_js/checkout/checkout_provider). Then render the `CheckoutForm` component that contains the payment form.

```jsx
import React, { useMemo } from "react";
import ReactDOM from "react-dom";
import { CheckoutElementsProvider } from "@stripe/react-stripe-js/checkout";
import { loadStripe } from "@stripe/stripe-js";
import CheckoutForm from "./CheckoutForm";

// Make sure to call `loadStripe` outside of a component's render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

function App() {
  const promise = useMemo(() => {
    return fetch("/create-checkout-session", {
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => data.clientSecret);
  }, []);

  return (
    <div>
      <CheckoutElementsProvider
        stripe={stripePromise}
        options={{
          clientSecret: promise,
        }}
      >
        <CheckoutForm />
      </CheckoutElementsProvider>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
```

### Add the Payment Element component

Use the `PaymentElement` component to display the payment form.

```jsx
import React from "react";
import { PaymentElement } from "@stripe/react-stripe-js/checkout";

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

## Prefill fields on payment page

If all the following conditions are true, the [Session object](https://docs.stripe.com/js/custom_checkout/session_object) contains the **email**, **name**, **card**, and **billing address** using details from the customer’s saved card for you to display on your payment page, and the Payment Element to display the saved card:

- Checkout is in `payment` or `subscription` mode; `setup` mode doesn’t support prefilling fields.
- The customer has a saved card. Checkout only supports prefilling card payment methods.
- The saved card has `allow_redisplay` set to `always` or you adjusted the [default display setting](https://docs.stripe.com/payments/existing-customers.md#display-additional-saved-payment-methods).
- The payment method includes [`billing_details`](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-billing_details) required by the Checkout Session’s [`billing_address_collection`](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-billing_address_collection) value:
  - `auto` requires values for `email`, `name`, and `address[country]`. US, CA, and GB billing addresses also require `address[postal_code]`.
  - `required` requires values for `email`, `name`, and all `address` fields.

If your customer has multiple saved cards, the Payment Element displays the saved card matching the following prioritization:

- In `payment` mode, Stripe prefills the fields using the customer’s newest saved card.
- In `subscription` mode, Stripe prefills the customer’s default payment method if it’s a card. Otherwise, Stripe prefills the newest saved card.

When [collecting a shipping address](https://docs.stripe.com/payments/collect-addresses.md), the [Session object](https://docs.stripe.com/js/custom_checkout/session_object) contains the shipping address fields if the Customer’s [shipping.address](https://docs.stripe.com/api/customers/object.md#customer_object-shipping-address) meets the Checkout Session’s [supported countries](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_address_collection-allowed_countries).

To let your customers remove saved cards during a Checkout Session, set [save_payment_method_options[payment_method_remove]](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-saved_payment_method_options-payment_method_remove) to `enabled`.

> #### Prefill timeout
>
> The prefilled payment method displays for 30 minutes following Checkout Session creation. After it expires, loading the same Checkout Session doesn’t prefill the payment method anymore for security reasons.

## Submit the payment to Stripe [Client-side]

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

## Handle post-payment events [Server-side]

Stripe sends a [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) event when a customer completes a Checkout Session payment. Use the [Dashboard webhook tool](https://dashboard.stripe.com/webhooks) or follow the [webhook guide](https://docs.stripe.com/webhooks/quickstart.md) to receive and handle these events, which might trigger you to:

- Send an order confirmation email to your customer.
- Log the sale in a database.
- Start a shipping workflow.

Listen for these events rather than waiting for your customer to be redirected back to your website. Triggering fulfillment only from your Checkout landing page is unreliable. Setting up your integration to listen for asynchronous events allows you to accept [different types of payment methods](https://stripe.com/payments/payment-methods-guide) with a single integration.

Learn more in our [fulfillment guide for Checkout](https://docs.stripe.com/checkout/fulfillment.md).

Handle the following events when collecting payments with the Checkout:

| Event                                                                                                                                        | Description                                                                                | Action                                                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed)                             | Sent when a customer successfully completes a Checkout Session.                            | Send the customer an order confirmation and _fulfill_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) their order. |
| [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) | Sent when a payment made with a delayed payment method, such as ACH direct debt, succeeds. | Send the customer an order confirmation and _fulfill_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) their order. |
| [checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_failed)       | Sent when a payment made with a delayed payment method, such as ACH direct debt, fails.    | Notify the customer of the failure and bring them back on-session to attempt payment again.                                                                                                      |

# Custom flow

> This is a Custom flow for when platform is web and ui is elements. View the full page at https://docs.stripe.com/payments/existing-customers?platform=web&ui=elements.

The Payment Element allows buyers to enter their payment details. If the buyer is an existing customer or account, you can configure a Customer Session in the Payment Element display the customer’s or account’s [existing payment methods](https://docs.stripe.com/payments/save-and-reuse.md?platform=web&ui=elements).
![Payment Element with one saved card](assets/stripe-payment-element-saved-card.png)

The Payment Element can only display the following saved payment method types:

- `card`
- `link`
- `us_bank_account`
- `acss_debit`
- `sepa_debit`
- `bacs_debit`
- `au_becs_debit`
- `nz_bank_account`
- `ideal`
- `sofort`
- `bancontact`

## Create PaymentIntent and CustomerSession [Server-side]

Create a [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md) and a [CustomerSession](https://docs.stripe.com/api/customer_sessions/create.md). Make sure to pass the existing `Customer` or `Account` ID and enable the `payment_method_redisplay` feature.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

app.post('/create-intent-and-customer-session', async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    amount: 1099,
    currency: 'usd',
    automatic_payment_methods: {enabled: true},
    customer_account: {{CUSTOMER_ACCOUNT_ID}},
  });
  const customerSession = await stripe.customerSessions.create({
    customer_account: {{CUSTOMER_ACCOUNT_ID}},
    components: {
      payment_element: {
        enabled: true,
        features: {
          payment_method_redisplay: 'enabled',
        },
      },
    },
  });
  res.json({
    client_secret: intent.client_secret,
    customer_session_client_secret: customerSession.client_secret
  });
});
```

#### Customers v1

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

app.post('/create-intent-and-customer-session', async (req, res) => {
  const intent = await stripe.paymentIntents.create({
    amount: 1099,
    currency: 'usd',
    // In the latest version of the API, specifying the `automatic_payment_methods` parameter
    // is optional because Stripe enables its functionality by default.
    automatic_payment_methods: {enabled: true},
    customer: {{CUSTOMER_ID}},
  });
  const customerSession = await stripe.customerSessions.create({
    customer: {{CUSTOMER_ID}},
    components: {
      payment_element: {
        enabled: true,
        features: {
          payment_method_redisplay: 'enabled',
        },
      },
    },
  });
  res.json({
    client_secret: intent.client_secret,
    customer_session_client_secret: customerSession.client_secret
  });
});
```

## Optional: Display additional saved payment methods [Server-side]

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. When rendering past payment methods to a customer for future purchases, make sure you’ve collected consent to save the payment method details for this specific future use.

By default, we only show payment methods set to [always allow redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay).

You can’t reuse Apple Pay and Google Pay during a Checkout Session, so these payment methods don’t appear in the list of saved options. You must display the Google Pay and Apple Pay UI, and the payment request button UI, each time the Checkout Session is active.

You can display other previously saved payment methods by including other redisplay values in the Checkout Session, or by updating a payment method’s `allow_redisplay` setting to `always`.

- Use the `payment_method_allow_redisplay_filters` [parameter](https://docs.stripe.com/api/customer_sessions/create.md#create_customer_session-components-payment_element-features-payment_method_allow_redisplay_filters) to specify which saved payment methods to show in the Payment Element. You can set any of the valid values: `limited`, `unspecified` and `always`.

  #### Accounts v2

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const customerSession = await stripe.customerSessions.create({
    customer_account: "{{CUSTOMERACCOUNT_ID}}",
    components: {
      payment_element: {
        enabled: true,
        features: {
          payment_method_redisplay: "enabled",
          payment_method_allow_redisplay_filters: [
            "always",
            "limited",
            "unspecified",
          ],
        },
      },
    },
  });
  ```

  #### Customers v1

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const customerSession = await stripe.customerSessions.create({
    customer: "{{CUSTOMER_ID}}",
    components: {
      payment_element: {
        enabled: true,
        features: {
          payment_method_redisplay: "enabled",
          payment_method_allow_redisplay_filters: [
            "always",
            "limited",
            "unspecified",
          ],
        },
      },
    },
  });
  ```

- [Update the Payment Method](https://docs.stripe.com/api/payment_methods/update.md) to set the `allow_redisplay` value on individual payment methods.

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const paymentMethod = await stripe.paymentMethods.update(
    "{{PAYMENTMETHOD_ID}}",
    {
      allow_redisplay: "always",
    },
  );
  ```

## Display the Payment Element [Client-side]

#### HTML + JS

### Set up Stripe.js

Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

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

Fetch the two `clients_secret` from the previous step to initialize the Element. Then create and mount the Payment Element.

```javascript
// Fetch the two `client_secret`
const response = await fetch("/create-intent-and-customer-session", {
  method: "POST",
});
const { client_secret, customer_session_client_secret } = await response.json();

// Initialize Elements
const elements = stripe.elements({
  clientSecret: client_secret,
  customerSessionClientSecret: customer_session_client_secret,
});

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

Fetch the two `clients_secret` from the previous step to initialize the [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Then render the CheckoutForm component that contains the payment form.

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";
import CheckoutForm from "./CheckoutForm";

// Make sure to call `loadStripe` outside of a component's render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

function App() {
  const [clientSecret, setClientSecret] = useState("");
  const [customerSessionClientSecret, setCustomerSessionClientSecret] =
    useState("");

  // Fetch the two `client_secret`
  useEffect(() => {
    fetch("/create-intent-and-customer-session", { method: "POST" })
      .then((res) => res.json())
      .then((data) => {
        setClientSecret(data.client_secret);
        setCustomerSessionClientSecret(data.customer_session_client_secret);
      });
  }, []);

  // Initialize the Element provider once we we received the two `client_secret`
  // And render the CheckoutForm
  return (
    <div>
      {clientSecret && customerSessionClientSecret && (
        <Elements
          stripe={stripePromise}
          options={{ clientSecret, customerSessionClientSecret }}
        >
          <CheckoutForm />
        </Elements>
      )}
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
```

### Add the Payment Element component

Use the `PaymentElement` component to display the payment form.

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

## Submit the payment to Stripe [Client-side]

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

## Handle post-payment events [Server-side]

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the [Dashboard webhook tool](https://dashboard.stripe.com/webhooks) or follow the [webhook guide](https://docs.stripe.com/webhooks/quickstart.md) to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events is what enables you to accept [different types of payment methods](https://stripe.com/payments/payment-methods-guide) with a single integration.

In addition to handling the `payment_intent.succeeded` event, we recommend handling these other events when collecting payments with the Payment Element:

| Event                                                                                                                           | Description                                                                                                                                                                                                                                                                         | Action                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.succeeded)           | Sent when a customer successfully completes a payment.                                                                                                                                                                                                                              | Send the customer an order confirmation and _fulfill_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) their order. |
| [payment_intent.processing](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.processing)         | Sent when a customer successfully initiates a payment, but the payment has yet to complete. This event is most commonly sent when the customer initiates a bank debit. It’s followed by either a `payment_intent.succeeded` or `payment_intent.payment_failed` event in the future. | Send the customer an order confirmation that indicates their payment is pending. For digital goods, you might want to fulfill the order before waiting for payment to complete.                  |
| [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.payment_failed) | Sent when a customer attempts a payment, but the payment fails.                                                                                                                                                                                                                     | If a payment transitions from `processing` to `payment_failed`, offer the customer another attempt to pay.                                                                                       |

# Direct API

> This is a Direct API for when platform is web and ui is direct-api. View the full page at https://docs.stripe.com/payments/existing-customers?platform=web&ui=direct-api.

To completely control how you display existing Payment Methods, use the Direct API implementation.

## Display Payment Methods [Client-side] [Server-side]

Call the [list Payment Method](https://docs.stripe.com/api/payment_methods/customer_list.md) endpoint with the `allow_redisplay` parameter to retrieve a the reusable payment methods associated with a customer.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer_account: "{{CUSTOMER_ACCOUNT_ID}}",
  allow_redisplay: "always",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.customers.listPaymentMethods(
  "{{CUSTOMER_ID}}",
  {
    allow_redisplay: "always",
  },
);
```

Use the API response data to display the Payment Methods in your own UI and let the customer select one.

## Optional: Display additional saved payment methods [Server-side]

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. When rendering past payment methods to a customer for future purchases, make sure you’ve collected consent to save the payment method details for this specific future use.

By default, we only show payment methods set to [always allow redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay).

You can’t reuse Apple Pay and Google Pay during a Checkout Session, so these payment methods don’t appear in the list of saved options. You must display the Google Pay and Apple Pay UI, and the payment request button UI, each time the Checkout Session is active.

You can display other previously saved payment methods by including other redisplay values in the Checkout Session, or by updating a payment method’s `allow_redisplay` setting to `always`.

- Use the `allow_redisplay` [parameter](https://docs.stripe.com/api/payment_methods/customer_list.md#list_customer_payment_methods-allow_redisplay) to specify which saved payment methods to show the customer. You can set any of the valid values: `limited`, `unspecified` and `always`.

  #### Accounts v2

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const paymentMethods = await stripe.paymentMethods.list({
    customer_account: "{{CUSTOMERACCOUNT_ID}}",
    allow_redisplay: "unspecified",
  });
  ```

  #### Customers v1

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const paymentMethods = await stripe.customers.listPaymentMethods(
    "{{CUSTOMER_ID}}",
    {
      allow_redisplay: "unspecified",
    },
  );
  ```

- [Update the Payment Method](https://docs.stripe.com/api/payment_methods/update.md) to set the `allow_redisplay` value on individual payment methods.

  ```node
  // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
  // Find your keys at https://dashboard.stripe.com/apikeys.
  const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

  const paymentMethod = await stripe.paymentMethods.update(
    "{{PAYMENTMETHOD_ID}}",
    {
      allow_redisplay: "always",
    },
  );
  ```

## Create PaymentIntent [Server-side]

Create a [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md) to try to charge the customer with the payment method they selected.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  customer_account: "{{CUSTOMER_ACCOUNT_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  confirm: true,
  return_url: "https://example.com/order/123/complete",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  confirm: true,
  return_url: "https://example.com/order/123/complete",
});
```

If the API call fails with a 402 response, it means the payment was declined. Ask the customer to try again or use a different payment method.

## Check PaymentIntent status [Client-side] [Server-side]

Assuming the PaymentIntent is successfully created, check its `status`:

- `succeeded` indicates the customer was charged as expected. Display a success message to your customer.
- `requires_action` indicates you must prompt additional action, such as authenticating with 3D Secure. Call [`handleNextAction`](https://docs.stripe.com/js/payment_intents/handle_next_action) on the frontend to trigger the action the customer needs to perform.

```javascript
const { error, paymentIntent } = await stripe.handleNextAction({
  clientSecret: "{{CLIENT_SECRET}}",
});

if (error) {
  // Show error from Stripe.js
} else {
  // Actions handled, show success message
}
```

## Handle post-payment events [Server-side]

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the [Dashboard webhook tool](https://dashboard.stripe.com/webhooks) or follow the [webhook guide](https://docs.stripe.com/webhooks/quickstart.md) to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events is what enables you to accept [different types of payment methods](https://stripe.com/payments/payment-methods-guide) with a single integration.

In addition to handling the `payment_intent.succeeded` event, we recommend handling these other events when collecting payments with the Payment Element:

| Event                                                                                                                           | Description                                                                                                                                                                                                                                                                         | Action                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.succeeded)           | Sent when a customer successfully completes a payment.                                                                                                                                                                                                                              | Send the customer an order confirmation and _fulfill_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) their order. |
| [payment_intent.processing](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.processing)         | Sent when a customer successfully initiates a payment, but the payment has yet to complete. This event is most commonly sent when the customer initiates a bank debit. It’s followed by either a `payment_intent.succeeded` or `payment_intent.payment_failed` event in the future. | Send the customer an order confirmation that indicates their payment is pending. For digital goods, you might want to fulfill the order before waiting for payment to complete.                  |
| [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.payment_failed) | Sent when a customer attempts a payment, but the payment fails.                                                                                                                                                                                                                     | If a payment transitions from `processing` to `payment_failed`, offer the customer another attempt to pay.                                                                                       |
