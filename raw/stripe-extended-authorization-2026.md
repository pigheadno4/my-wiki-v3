<!-- Source URL: https://docs.stripe.com/payments/extended-authorization -->
<!-- Fetched: 2026-05-11 -->

# Place an extended hold on an online card payment

Learn how to use extended authorizations to capture online card payments up to 30 days after authorization.

# Full hosted page

> This is a Full hosted page for when platform is web and ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/extended-authorization?platform=web&ui=stripe-hosted.

Extended authorizations have a longer authorization validity period, which allows you to hold customer funds for longer than standard authorization validity windows. For most card networks, the default authorization validity period is 7 days for online payments and 2 days for in-person [Terminal](https://docs.stripe.com/terminal.md) payments, whereas extended validity periods can go up to 30 days depending on the card network. For more information about authorization validity windows, see [place a hold on a payment method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md).

## Availability

When you use extended authorizations, there are no regional restrictions. However, be aware of the following limitations:

- They’re only available with Visa, Mastercard, American Express, and Discover.
- Certain card brands have merchant category restrictions. Refer to the network availability table below.
- This page describes extended authorizations for online card payments. For in-person card payments using extended authorizations, refer to the [Terminal documentation](https://docs.stripe.com/terminal/features/extended-authorizations.md).

- [mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode) is set to `payment` and [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-capture_method) is set to `manual` on the [CheckoutSession](https://docs.stripe.com/api/checkout/sessions/.md).

> #### IC+ Feature
>
> We offer extended authorizations to users on _IC+_ (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs) pricing. If you’re on blended Stripe pricing and want access to this feature, contact us using the form at [Stripe support](https://support.stripe.com).

### Availability by card network and merchant category

Every card network has different rules that determine which payments have extended authorizations available, and how long they’re valid. The following table shows the validity windows and transaction types that extended authorization is available for using Visa, Mastercard, American Express, and Discover. However, we recommend that you rely on the [capture_before field](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-capture_before) to confirm the validity window for any given payment because these rules can change without prior notice.

| Card brand | Merchant category                               | Extended authorization validity window |
| ---------- | ----------------------------------------------- | -------------------------------------- |
| **Visa**   | Hotel, lodging, vehicle rental, and cruise line |

All other merchant categories\* | 30 days** |
| **Mastercard** (not including Maestro and Cirrus cards) | All merchant categories | 30 days |
| **American Express** | Lodging and vehicle rental | 30 days\*** |
| **Discover** | Airline, bus charter/tour, car rental, cruise line, local/suburban commuter, passenger transportation including ferries, hotel, lodging, and passenger railway | 30 days |

\* For other merchant categories, Stripe charges an additional 0.08% fee per transaction. The extended window only applies to [Customer-Initiated Transactions](https://docs.stripe.com/payments/cits-and-mits.md) and doesn’t apply to transactions with businesses in Japan or transactions related to healthcare, bill payment, or debt repayment. \*\* The exact extended authorization window for Visa is 29 days and 18 hours, to allow time for clearing processes.\*\*\* Although your validity window is extended to 30 days, you must capture the authorized funds no later than the end of your customer’s stay or rental.

### Networks with limited support (beta)

The following card networks have limited support for extended authorization:

| Card brand      | Merchant country                 | Merchant category                                                                                                                                              | Extended authorization validity window |
| --------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **Diners Club** | US (through Discover)            | All merchant categories                                                                                                                                        | 30 days                                |
| **UnionPay**    | Global, excluding US and Canada  | All merchant categories                                                                                                                                        | 27 to 29 days                          |
|                 | US and Canada (through Discover) | Airline, bus charter/tour, car rental, cruise line, local/suburban commuter, passenger transportation including ferries, hotel, lodging, and passenger railway | 30 days                                |

### Recent changes to availability

- **September 2023**: Extended authorizations on Discover are no longer available for the following merchant categories due to information provided by the network: eating and drinking places, boat rental, motor home and RV rental, truck rental, timeshares, taxicabs/limousines, trailer parks/campgrounds, equipment/furniture/appliance rental, amusement parks, circuses, fortune tellers, recreational services.
- **September 2023**: The authorization validity period for Visa was reduced from 31 to 30 days to avoid non-compliance network fees. To make sure we clear transactions within that window, we added a buffer of 6 hours, making the effective authorization window 29 days and 18 hours.

## Best Practices

Customers see their funds held longer when you use extended authorizations. Use clear [statement descriptors](https://docs.stripe.com/get-started/account/statement-descriptors.md) to avoid increased disputes from unrecognized payments.

You can use the [custom_text](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-custom_text) field when creating a new [CheckoutSession](https://docs.stripe.com/api/checkout_sessions.md) to display additional text on the checkout page to help meet compliance requirements.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when using extended authorization. Consult the network specifications for the card networks that you plan to accept using this feature with to make sure your sales are compliant with the applicable rules, which vary by network. For instance, for many networks extended validity windows are only for cases where you don’t know the final amount that you’ll capture at the time of authorization.
>
> The information provided on this page relating to your compliance with these requirements is for your general guidance, and is not legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

## Create a CheckoutSession

Add a checkout button to your website that calls a server-side endpoint to create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md).

```html
<html>
  <head>
    <title>Buy cool new product</title>
  </head>
  <body>
    <!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
```

A Checkout Session is the programmatic representation of what your customer sees when they’re redirected to the payment form. You can configure it with options such as:

- [Line items](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items) to charge
- Currencies to use

You must populate `success_url` with the URL value of a page on your website that Checkout returns your customer to after they complete the payment.

> Checkout Sessions expire 24 hours after creation by default.

After creating a Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

To enable the extended authorization feature, set [request_extended_authorization](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-card-request_extended_authorization) to `if_available`.

#### Node.js

```javascript
// This example sets up an endpoint using the Express framework.

const express = require("express");
const app = express();
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

app.post("/create-checkout-session", async (req, res) => {
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
    payment_method_options: {
      card: {
        request_extended_authorization: "if_available",
      },
    },
    mode: "payment",
    success_url: "http://localhost:4242/success",
  });

  res.redirect(303, session.url);
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));
```

Rely on the [capture_before field](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-capture_before) to confirm the validity window for a given payment. The validity window won’t change after the CheckoutSession is complete. To determine if the authorization is extended after the CheckoutSession is complete, look at the [extended_authorization.status field](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-extended_authorization-status) on the associated charge.

```json
{
  "id": "pi_xxx",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  "status": "requires_capture",
  ...
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge",
      "payment_method_details": {
        "card": {
          "amount_authorized": 1000,"capture_before": 1696524701,
          "extended_authorization": {
              "status": "enabled", // or "disabled"
          }
        }
      }
      ...
    }
  ...
}
```

## Test your integration

Use the Stripe test cards below with any CVC and future expiration date to request extended authorizations while testing. If extended authorizations are available on payments for a given network while testing, they’re also available for live payments.

| Card brand | Number           | Payment method       |
| ---------- | ---------------- | -------------------- |
| Visa       | 4242424242424242 | `pm_card_visa`       |
| Mastercard | 5555555555554444 | `pm_card_mastercard` |
| Amex       | 378282246310005  | `pm_card_amex`       |
| Discover   | 6011111111111117 | `pm_card_discover`   |

# Full embedded page

> This is a Full embedded page for when platform is web and ui is embedded-page. View the full page at https://docs.stripe.com/payments/extended-authorization?platform=web&ui=embedded-page.

Extended authorizations have a longer authorization validity period, which allows you to hold customer funds for longer than standard authorization validity windows. For most card networks, the default authorization validity period is 7 days for online payments and 2 days for in-person [Terminal](https://docs.stripe.com/terminal.md) payments, whereas extended validity periods can go up to 30 days depending on the card network. For more information about authorization validity windows, see [place a hold on a payment method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md).

## Availability

When you use extended authorizations, there are no regional restrictions. However, be aware of the following limitations:

- They’re only available with Visa, Mastercard, American Express, and Discover.
- Certain card brands have merchant category restrictions. Refer to the network availability table below.
- This page describes extended authorizations for online card payments. For in-person card payments using extended authorizations, refer to the [Terminal documentation](https://docs.stripe.com/terminal/features/extended-authorizations.md).

- [mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode) is set to `payment` and [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-capture_method) is set to `manual` on the [CheckoutSession](https://docs.stripe.com/api/checkout/sessions/.md).

> #### IC+ Feature
>
> We offer extended authorizations to users on _IC+_ (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs) pricing. If you’re on blended Stripe pricing and want access to this feature, contact us using the form at [Stripe support](https://support.stripe.com).

### Availability by card network and merchant category

Every card network has different rules that determine which payments have extended authorizations available, and how long they’re valid. The following table shows the validity windows and transaction types that extended authorization is available for using Visa, Mastercard, American Express, and Discover. However, we recommend that you rely on the [capture_before field](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-capture_before) to confirm the validity window for any given payment because these rules can change without prior notice.

| Card brand | Merchant category                               | Extended authorization validity window |
| ---------- | ----------------------------------------------- | -------------------------------------- |
| **Visa**   | Hotel, lodging, vehicle rental, and cruise line |

All other merchant categories\* | 30 days** |
| **Mastercard** (not including Maestro and Cirrus cards) | All merchant categories | 30 days |
| **American Express** | Lodging and vehicle rental | 30 days\*** |
| **Discover** | Airline, bus charter/tour, car rental, cruise line, local/suburban commuter, passenger transportation including ferries, hotel, lodging, and passenger railway | 30 days |

\* For other merchant categories, Stripe charges an additional 0.08% fee per transaction. The extended window only applies to [Customer-Initiated Transactions](https://docs.stripe.com/payments/cits-and-mits.md) and doesn’t apply to transactions with businesses in Japan or transactions related to healthcare, bill payment, or debt repayment. \*\* The exact extended authorization window for Visa is 29 days and 18 hours, to allow time for clearing processes.\*\*\* Although your validity window is extended to 30 days, you must capture the authorized funds no later than the end of your customer’s stay or rental.

### Networks with limited support (beta)

The following card networks have limited support for extended authorization:

| Card brand      | Merchant country                 | Merchant category                                                                                                                                              | Extended authorization validity window |
| --------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **Diners Club** | US (through Discover)            | All merchant categories                                                                                                                                        | 30 days                                |
| **UnionPay**    | Global, excluding US and Canada  | All merchant categories                                                                                                                                        | 27 to 29 days                          |
|                 | US and Canada (through Discover) | Airline, bus charter/tour, car rental, cruise line, local/suburban commuter, passenger transportation including ferries, hotel, lodging, and passenger railway | 30 days                                |

### Recent changes to availability

- **September 2023**: Extended authorizations on Discover are no longer available for the following merchant categories due to information provided by the network: eating and drinking places, boat rental, motor home and RV rental, truck rental, timeshares, taxicabs/limousines, trailer parks/campgrounds, equipment/furniture/appliance rental, amusement parks, circuses, fortune tellers, recreational services.
- **September 2023**: The authorization validity period for Visa was reduced from 31 to 30 days to avoid non-compliance network fees. To make sure we clear transactions within that window, we added a buffer of 6 hours, making the effective authorization window 29 days and 18 hours.

## Best Practices

Customers see their funds held longer when you use extended authorizations. Use clear [statement descriptors](https://docs.stripe.com/get-started/account/statement-descriptors.md) to avoid increased disputes from unrecognized payments.

You can use the [custom_text](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-custom_text) field when creating a new [CheckoutSession](https://docs.stripe.com/api/checkout_sessions.md) to display additional text on the checkout page to help meet compliance requirements.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when using extended authorization. Consult the network specifications for the card networks that you plan to accept using this feature with to make sure your sales are compliant with the applicable rules, which vary by network. For instance, for many networks extended validity windows are only for cases where you don’t know the final amount that you’ll capture at the time of authorization.
>
> The information provided on this page relating to your compliance with these requirements is for your general guidance, and is not legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

## Create a CheckoutSession

From your server, create a _Checkout Session_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription) and set the [ui_mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-ui_mode) to `embedded_page`. You can configure the [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) with [line items](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items) to include, and options such as [currency](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-currency).

To return customers to a custom page that you host on your website, specify that page’s URL in the [return_url](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-return_url) parameter. Include the `{CHECKOUT_SESSION_ID}` template variable in the URL to retrieve the session’s status on the return page. Checkout automatically substitutes the variable with the Checkout Session ID before redirecting.

Read more about [configuring the return page](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=embedded-page#return-page) and other options for [customizing redirect behavior](https://docs.stripe.com/payments/checkout/custom-success-page.md?payment-ui=embedded-page).

After you create the Checkout Session, use the `client_secret` returned in the response to [mount Checkout](https://docs.stripe.com/payments/extended-authorization.md#mount-checkout).

To enable the extended authorization feature, set [request_extended_authorization](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-card-request_extended_authorization) to `if_available`.

#### Node.js

```javascript
// This example sets up an endpoint using the Express framework.
const express = require("express");
const app = express();

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

app.post("/create-checkout-session", async (req, res) => {
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
    ui_mode: "embedded_page",
    payment_method_options: {
      card: {
        request_extended_authorization: "if_available",
      },
    },
    return_url:
      "https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID}",
  });

  res.send({ clientSecret: session.client_secret });
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));
```

Rely on the [capture_before field](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-capture_before) to confirm the validity window for a given payment. The validity window won’t change after the CheckoutSession is complete. To determine if the authorization is extended after the CheckoutSession is complete, look at the [extended_authorization.status field](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-extended_authorization-status) on the associated Charge.

```json
{
  "id": "pi_xxx",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  "status": "requires_capture",
  ...
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge",
      "payment_method_details": {
        "card": {
          "amount_authorized": 1000,"capture_before": 1696524701,
          "extended_authorization": {
              "status": "enabled", // or "disabled"
          }
        }
      }
      ...
    }
  ...
}
```

## Mount Checkout

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

## Show a return page

After your customer attempts payment, Stripe redirects them to a return page that you host on your site. When you created the Checkout Session, you specified the URL of the return page in the [return_url](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-return_url) parameter. Read more about other options for [customizing redirect behavior](https://docs.stripe.com/payments/checkout/custom-success-page.md?payment-ui=embedded-page).

When rendering your return page, retrieve the Checkout Session status using the Checkout Session ID in the URL. Handle the result according to the session status as follows:

- `complete`: The payment succeeded. Use the information from the Checkout Session to render a success page.
- `open`: The payment failed or was canceled. Remount Checkout so that your customer can try again.

#### Node.js

```javascript
app.get("/session_status", async (req, res) => {
  const session = await stripe.checkout.sessions.retrieve(req.query.session_id);

  res.send({
    status: session.status,
    payment_status: session.payment_status,
    customer_email: session.customer_details.email,
  });
});
```

```javascript
const session = await fetch(`/session_status?session_id=${session_id}`);
if (session.status == "open") {
  // Remount embedded Checkout
} else if (session.status == "complete") {
  // Show success page
  // Optionally use session.payment_status or session.customer_email
  // to customize the success page
}
```

#### Redirect-based payment methods

During payment, some payment methods redirect the customer to an intermediate page, such as a bank authorization page. When they complete that page, Stripe redirects them to your return page.

Learn more about [redirect-based payment methods and redirect behavior](https://docs.stripe.com/payments/checkout/custom-success-page.md?payment-ui=embedded-page#redirect-based-payment-methods).

## Test your integration

Use the Stripe test cards below with any CVC and future expiration date to request extended authorizations while testing. If extended authorizations are available on payments for a given network while testing, they’re also available for live payments.

| Card brand | Number           | Payment method       |
| ---------- | ---------------- | -------------------- |
| Visa       | 4242424242424242 | `pm_card_visa`       |
| Mastercard | 5555555555554444 | `pm_card_mastercard` |
| Amex       | 378282246310005  | `pm_card_amex`       |
| Discover   | 6011111111111117 | `pm_card_discover`   |

# Advanced integration

> This is a Advanced integration for when platform is web and ui is elements. View the full page at https://docs.stripe.com/payments/extended-authorization?platform=web&ui=elements.

Extended authorizations have a longer authorization validity period, which allows you to hold customer funds for longer than standard authorization validity windows. For most card networks, the default authorization validity period is 7 days for online payments and 2 days for in-person [Terminal](https://docs.stripe.com/terminal.md) payments, whereas extended validity periods can go up to 30 days depending on the card network. For more information about authorization validity windows, see [place a hold on a payment method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md).

## Availability

When you use extended authorizations, there are no regional restrictions. However, be aware of the following limitations:

- They’re only available with Visa, Mastercard, American Express, and Discover.
- Certain card brands have merchant category restrictions. Refer to the network availability table below.
- This page describes extended authorizations for online card payments. For in-person card payments using extended authorizations, refer to the [Terminal documentation](https://docs.stripe.com/terminal/features/extended-authorizations.md).

- [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) is set to `manual` on the [PaymentIntent](https://docs.stripe.com/api/payment_intents/.md).

> #### IC+ Feature
>
> We offer extended authorizations to users on _IC+_ (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs) pricing. If you’re on blended Stripe pricing and want access to this feature, contact us using the form at [Stripe support](https://support.stripe.com).

### Availability by card network and merchant category

Every card network has different rules that determine which payments have extended authorizations available, and how long they’re valid. The following table shows the validity windows and transaction types that extended authorization is available for using Visa, Mastercard, American Express, and Discover. However, we recommend that you rely on the [capture_before field](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-capture_before) to confirm the validity window for any given payment because these rules can change without prior notice.

| Card brand | Merchant category                               | Extended authorization validity window |
| ---------- | ----------------------------------------------- | -------------------------------------- |
| **Visa**   | Hotel, lodging, vehicle rental, and cruise line |

All other merchant categories\* | 30 days** |
| **Mastercard** (not including Maestro and Cirrus cards) | All merchant categories | 30 days |
| **American Express** | Lodging and vehicle rental | 30 days\*** |
| **Discover** | Airline, bus charter/tour, car rental, cruise line, local/suburban commuter, passenger transportation including ferries, hotel, lodging, and passenger railway | 30 days |

\* For other merchant categories, Stripe charges an additional 0.08% fee per transaction. The extended window only applies to [Customer-Initiated Transactions](https://docs.stripe.com/payments/cits-and-mits.md) and doesn’t apply to transactions with businesses in Japan or transactions related to healthcare, bill payment, or debt repayment. \*\* The exact extended authorization window for Visa is 29 days and 18 hours, to allow time for clearing processes.\*\*\* Although your validity window is extended to 30 days, you must capture the authorized funds no later than the end of your customer’s stay or rental.

### Networks with limited support (beta)

The following card networks have limited support for extended authorization:

| Card brand      | Merchant country                 | Merchant category                                                                                                                                              | Extended authorization validity window |
| --------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **Diners Club** | US (through Discover)            | All merchant categories                                                                                                                                        | 30 days                                |
| **UnionPay**    | Global, excluding US and Canada  | All merchant categories                                                                                                                                        | 27 to 29 days                          |
|                 | US and Canada (through Discover) | Airline, bus charter/tour, car rental, cruise line, local/suburban commuter, passenger transportation including ferries, hotel, lodging, and passenger railway | 30 days                                |

### Recent changes to availability

- **September 2023**: Extended authorizations on Discover are no longer available for the following merchant categories due to information provided by the network: eating and drinking places, boat rental, motor home and RV rental, truck rental, timeshares, taxicabs/limousines, trailer parks/campgrounds, equipment/furniture/appliance rental, amusement parks, circuses, fortune tellers, recreational services.
- **September 2023**: The authorization validity period for Visa was reduced from 31 to 30 days to avoid non-compliance network fees. To make sure we clear transactions within that window, we added a buffer of 6 hours, making the effective authorization window 29 days and 18 hours.

## Best Practices

Customers see their funds held longer when you use extended authorizations. Use clear [statement descriptors](https://docs.stripe.com/get-started/account/statement-descriptors.md) to avoid increased disputes from unrecognized payments.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when using extended authorization. Consult the network specifications for the card networks that you plan to accept using this feature with to make sure your sales are compliant with the applicable rules, which vary by network. For instance, for many networks extended validity windows are only for cases where you don’t know the final amount that you’ll capture at the time of authorization.
>
> The information provided on this page relating to your compliance with these requirements is for your general guidance, and is not legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

## Create and confirm an uncaptured PaymentIntent

By default, an authorization for an online card payment is valid for 7 days for most card networks. To increase the validity period, you can request an extended authorization by using `if_available` with the [request_extended_authorization](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-request_extended_authorization) parameter.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  payment_method: "pm_card_visa",
  confirm: true,
  capture_method: "manual",
  expand: ["latest_charge"],
  payment_method_options: {
    card: {
      request_extended_authorization: "if_available",
    },
  },
});
```

Rely on the [capture_before field](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-capture_before) to confirm the validity window for a given payment. The validity window won’t change after the PaymentIntent is confirmed. To determine if the authorization is extended after confirming the PaymentIntent, look at the [extended_authorization.status field](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-extended_authorization-status) on the associated Charge.

```json
// PaymentIntent response
{
  "id": "pi_xxx",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  "status": "requires_capture",
  ...
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge",
      "payment_method_details": {
        "card": {
          "amount_authorized": 1000,"capture_before": 1696524701,
          "extended_authorization": {
              "status": "enabled", // or "disabled"
          }
        }
      }
      ...
    }
  ...
}
```

## Test your integration

Use the Stripe test cards below with any CVC and future expiration date to request extended authorizations while testing. If extended authorizations are available on payments for a given network while testing, they’re also available for live payments.

| Card brand | Number           | Payment method       |
| ---------- | ---------------- | -------------------- |
| Visa       | 4242424242424242 | `pm_card_visa`       |
| Mastercard | 5555555555554444 | `pm_card_mastercard` |
| Amex       | 378282246310005  | `pm_card_amex`       |
| Discover   | 6011111111111117 | `pm_card_discover`   |

## See also

- [Place a hold on a payment method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md)
