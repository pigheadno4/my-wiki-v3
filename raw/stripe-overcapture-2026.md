<!-- Source URL: https://docs.stripe.com/payments/overcapture -->
<!-- Fetched: 2026-05-11 -->

# Capture more than the authorized amount on a payment

Use overcapture to capture more than the authorized amount for a PaymentIntent.

# Stripe-hosted page

> This is a Stripe-hosted page for when platform is web and ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/overcapture?platform=web&ui=stripe-hosted.

Overcapture allows you to capture with an amount that’s higher than the authorized amount for a card payment. Unlike [incremental authorizations](https://docs.stripe.com/payments/incremental-authorization.md), overcapture doesn’t result in additional authorizations with the card networks. When you overcapture a PaymentIntent, your customer won’t see any immediate updates on their credit card statement. After the captured amount settles, the initial pending authorization gets updated with the final captured amount.

## Availability

When using overcapture, be aware of the following restrictions:

- Only available with Visa, Mastercard, American Express, or Discover.
- Only eligible for online card payments. For in-person card payments see how to [collect tips](https://docs.stripe.com/terminal/features/collecting-tips/overview.md).
- Card brands limit the amount that you can overcapture (generally calculated as a percentage of the authorized amount), and impose additional constraints, including country, card type, and merchant category restrictions (see below).

- [mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode) is set to `payment` and [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-capture_method) is set to `manual` on the [CheckoutSession](https://docs.stripe.com/api/checkout/sessions/.md)

> #### IC+ feature
>
> We offer overcapture to users on _IC+ pricing_ (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs). If you’re on standard Stripe pricing and want access to this feature, contact us using the form at [Stripe support](https://support.stripe.com).

### Availability by card network, merchant country, and merchant category

| Card brand           | Merchant country | Merchant category                                                                                                                                                     | Percent limit                                             |
| -------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Visa**\*           | Global           | Taxicabs and limousines; drinking places (alcoholic beverages); beauty and barber shops; health and beauty spas                                                       | +20%                                                      |
|                      | US               | Eating places and restaurants; fast food restaurants; caterers                                                                                                        | +30%                                                      |
|                      | Global           | Eating places and restaurants; fast food restaurants                                                                                                                  | +20%                                                      |
|                      | Global           | Car rentals                                                                                                                                                           | Greater of +15% or +75 USD (or local currency equivalent) |
|                      | Global           | Lodging; cruise lines                                                                                                                                                 | +15%                                                      |
|                      | Global\*\*       | All other merchant categories                                                                                                                                         | +15%                                                      |
| **Mastercard**       | US\*\*\*         | Eating places and restaurants; fast food restaurants                                                                                                                  | +30%                                                      |
| **American Express** | Global\*\*\*\*   | Eating places and restaurants; drinking places (alcoholic beverages); fast food restaurants                                                                           | +30%                                                      |
|                      | Global           | Taxicabs and limousines; beauty and barber shops; health and beauty spas                                                                                              | +20%                                                      |
|                      | Global           | Lodging; car rentals; truck and utility trailer rentals; motor home and recreational vehicle rentals; grocery stores; retail stores                                   | +15%                                                      |
| **Discover**         | Global           | Taxicabs and limousines; eating places and restaurants; drinking places (alcoholic beverages); fast food restaurants; beauty and barber shops; health and beauty spas | +20%                                                      |
|                      | Global           | Lodging; car rentals                                                                                                                                                  | +15%                                                      |

\* Excludes businesses in the European Economic Area (EEA)

\*\* For cardholder-initiated transactions

\*\*\* Card must also be issued in the United States

\*\*\*\* The percent limit for debit and prepaid card payments is 20%

### Networks with limited support (beta)

The following card networks have limited support for overcapture:

| Card brand      | Merchant country      | Merchant category                                                                                                                                                     | Percent limit |
| --------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Diners Club** | US (through Discover) | Taxicabs and limousines; eating places and restaurants; drinking places (alcoholic beverages); fast food restaurants; beauty and barber shops; health and beauty spas | +20%          |
|                 | US (through Discover) | Lodging; car rentals                                                                                                                                                  | +15%          |

### Overcapture with Strong Customer Authentication (SCA)

If you and the cardholder are in a country that has Strong Customer Authentication (SCA) requirements, keep in mind the limitations of overcapture availability.

- Under SCA requirements, you generally need to authenticate an amount that’s greater than or equal to the amount that you eventually capture. For this reason, you need to authenticate and authorize for the highest estimated amount that you plan to capture, rather than using overcapture as outlined elsewhere on this page. Subsequently, you can capture up to the full amount authenticated, depending on the total amount for the goods or services provided. If you find it necessary to capture an amount beyond the originally authorized and authenticated amount, you must cancel the original payment and create a new one with the correct amount. However, there are some exceptions to this requirement (see below).
- There are a number of [transaction exemptions](https://support.stripe.com/questions/transaction-exemptions-for-strong-customer-authentication-%28sca%29) for SCA where overcapture might be permissible. For example, merchant-initiated transactions (MIT) where the customer isn’t physically present during the checkout flow are potentially exempt. See [when to categorize a transaction as MIT](<https://support.stripe.com/questions/merchant-initiated-transactions-(mits)-when-to-categorize-a-transaction-as-mit>).

You need to familiarize yourself with the complete documentation to gain a comprehensive understanding of overcapture and SCA requirements. See our [SCA guide](https://stripe.com/guides/strong-customer-authentication) for more information.

You can use the [custom_text](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-custom_text) field when creating a new [CheckoutSession](https://docs.stripe.com/api/checkout_sessions.md) to display additional text on the checkout page to help meet compliance requirements.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when using overcapture. Make sure to review the rules for the card networks that you plan to use this feature with to make sure your sales comply with the applicable rules, which vary by network. For example, some card networks don’t allow overcapture for transactions where the final transaction amount should be known at the time of authorization.
>
> The information provided on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

## Create a Checkout Session

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

You must populate `success_url` with the URL of a page on your website that Checkout returns your customer to after they complete the payment.

> Checkout Sessions expire 24 hours after creation by default.

After creating a Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

To enable the overcapture feature, set [request_overcapture](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-card-request_overcapture) to `if_available`.

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
        request_overcapture: "if_available",
      },
    },
    mode: "payment",
    success_url: "http://localhost:4242/success",
  });

  res.redirect(303, session.url);
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));
```

After the customer completes checkout, look at the [overcapture.status](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-overcapture) field on the [latest_charge](https://docs.stripe.com/api/charges/object.md) in the [PaymentIntent](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_intent) to determine if overcapture is available for the payment based on [availability](https://docs.stripe.com/payments/overcapture.md#availability). If `available`, the [maximum_amount_capturable](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-overcapture-maximum_amount_capturable) field indicates the maximum amount capturable for the PaymentIntent. If `unavailable`, the maximum_amount_capturable is the amount authorized.

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
          "amount_authorized": 1000
          "overcapture": {"status": "available", // or "unavailable"
              "maximum_amount_capturable": 1200
          }
        }
      }
      ...
    }
  ...
}
```

## Capture the PaymentIntent

To capture more than the currently authorized amount on a PaymentIntent, use the [capture](https://docs.stripe.com/api/payment_intents/capture.md) endpoint and provide an [amount_to_capture](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-amount_to_capture) up to the [maximum_amount_capturable](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-overcapture).

If you need to capture an amount larger than the `maximum_amount_capturable`, perform an [incremental authorization](https://docs.stripe.com/payments/incremental-authorization.md) to increase the authorized amount, where available.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture("pi_xxx", {
  amount_to_capture: 1200,
  expand: ["latest_charge"],
});
```

The [amount_capturable](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_capturable) and [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received) fields update accordingly in the PaymentIntent capture response for a successful overcapture. The captured PaymentIntent that returns has an updated [amount](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount) to reflect the total monetary amount moved for this payment. Use the [amount_authorized](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-amount_authorized) field on the associated Charge to reference the initial amount authorized for a successfully overcaptured payment.

```json
// PaymentIntent response
{
  "id": "pi_xxx",
  "object": "payment_intent","amount": 1200,
  "amount_capturable": 0,
  "amount_received": 1200,
  "status": "succeeded",
  ...
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge",
      "payment_method_details": {
        "card": {
          "amount_authorized": 1000,
          "overcapture": {
              "maximum_amount_capturable": 1200,
              "status": "available" // or "unavailable"
          }
        }
      }
      ...
    }
  ...
}
```

# Full embedded page

> This is a Full embedded page for when platform is web and ui is embedded-page. View the full page at https://docs.stripe.com/payments/overcapture?platform=web&ui=embedded-page.

Overcapture allows you to capture with an amount that’s higher than the authorized amount for a card payment. Unlike [incremental authorizations](https://docs.stripe.com/payments/incremental-authorization.md), overcapture doesn’t result in additional authorizations with the card networks. When you overcapture a PaymentIntent, your customer won’t see any immediate updates on their credit card statement. After the captured amount settles, the initial pending authorization gets updated with the final captured amount.

## Availability

When using overcapture, be aware of the following restrictions:

- Only available with Visa, Mastercard, American Express, or Discover.
- Only eligible for online card payments. For in-person card payments see how to [collect tips](https://docs.stripe.com/terminal/features/collecting-tips/overview.md).
- Card brands limit the amount that you can overcapture (generally calculated as a percentage of the authorized amount), and impose additional constraints, including country, card type, and merchant category restrictions (see below).

- [mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode) is set to `payment` and [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-capture_method) is set to `manual` on the [CheckoutSession](https://docs.stripe.com/api/checkout/sessions/.md)

> #### IC+ feature
>
> We offer overcapture to users on _IC+ pricing_ (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs). If you’re on standard Stripe pricing and want access to this feature, contact us using the form at [Stripe support](https://support.stripe.com).

### Availability by card network, merchant country, and merchant category

| Card brand           | Merchant country | Merchant category                                                                                                                                                     | Percent limit                                             |
| -------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Visa**\*           | Global           | Taxicabs and limousines; drinking places (alcoholic beverages); beauty and barber shops; health and beauty spas                                                       | +20%                                                      |
|                      | US               | Eating places and restaurants; fast food restaurants; caterers                                                                                                        | +30%                                                      |
|                      | Global           | Eating places and restaurants; fast food restaurants                                                                                                                  | +20%                                                      |
|                      | Global           | Car rentals                                                                                                                                                           | Greater of +15% or +75 USD (or local currency equivalent) |
|                      | Global           | Lodging; cruise lines                                                                                                                                                 | +15%                                                      |
|                      | Global\*\*       | All other merchant categories                                                                                                                                         | +15%                                                      |
| **Mastercard**       | US\*\*\*         | Eating places and restaurants; fast food restaurants                                                                                                                  | +30%                                                      |
| **American Express** | Global\*\*\*\*   | Eating places and restaurants; drinking places (alcoholic beverages); fast food restaurants                                                                           | +30%                                                      |
|                      | Global           | Taxicabs and limousines; beauty and barber shops; health and beauty spas                                                                                              | +20%                                                      |
|                      | Global           | Lodging; car rentals; truck and utility trailer rentals; motor home and recreational vehicle rentals; grocery stores; retail stores                                   | +15%                                                      |
| **Discover**         | Global           | Taxicabs and limousines; eating places and restaurants; drinking places (alcoholic beverages); fast food restaurants; beauty and barber shops; health and beauty spas | +20%                                                      |
|                      | Global           | Lodging; car rentals                                                                                                                                                  | +15%                                                      |

\* Excludes businesses in the European Economic Area (EEA)

\*\* For cardholder-initiated transactions

\*\*\* Card must also be issued in the United States

\*\*\*\* The percent limit for debit and prepaid card payments is 20%

### Networks with limited support (beta)

The following card networks have limited support for overcapture:

| Card brand      | Merchant country      | Merchant category                                                                                                                                                     | Percent limit |
| --------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Diners Club** | US (through Discover) | Taxicabs and limousines; eating places and restaurants; drinking places (alcoholic beverages); fast food restaurants; beauty and barber shops; health and beauty spas | +20%          |
|                 | US (through Discover) | Lodging; car rentals                                                                                                                                                  | +15%          |

### Overcapture with Strong Customer Authentication (SCA)

If you and the cardholder are in a country that has Strong Customer Authentication (SCA) requirements, keep in mind the limitations of overcapture availability.

- Under SCA requirements, you generally need to authenticate an amount that’s greater than or equal to the amount that you eventually capture. For this reason, you need to authenticate and authorize for the highest estimated amount that you plan to capture, rather than using overcapture as outlined elsewhere on this page. Subsequently, you can capture up to the full amount authenticated, depending on the total amount for the goods or services provided. If you find it necessary to capture an amount beyond the originally authorized and authenticated amount, you must cancel the original payment and create a new one with the correct amount. However, there are some exceptions to this requirement (see below).
- There are a number of [transaction exemptions](https://support.stripe.com/questions/transaction-exemptions-for-strong-customer-authentication-%28sca%29) for SCA where overcapture might be permissible. For example, merchant-initiated transactions (MIT) where the customer isn’t physically present during the checkout flow are potentially exempt. See [when to categorize a transaction as MIT](<https://support.stripe.com/questions/merchant-initiated-transactions-(mits)-when-to-categorize-a-transaction-as-mit>).

You need to familiarize yourself with the complete documentation to gain a comprehensive understanding of overcapture and SCA requirements. See our [SCA guide](https://stripe.com/guides/strong-customer-authentication) for more information.

You can use the [custom_text](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-custom_text) field when creating a new [CheckoutSession](https://docs.stripe.com/api/checkout_sessions.md) to display additional text on the checkout page to help meet compliance requirements.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when using overcapture. Make sure to review the rules for the card networks that you plan to use this feature with to make sure your sales comply with the applicable rules, which vary by network. For example, some card networks don’t allow overcapture for transactions where the final transaction amount should be known at the time of authorization.
>
> The information provided on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

## Create a Checkout Session

From your server, create a _Checkout Session_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription) and set the [ui_mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-ui_mode) to `embedded_page`. You can configure the [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) with [line items](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items) to include, and options such as [currency](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-currency).

To return customers to a custom page that you host on your website, specify that page’s URL in the [return_url](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-return_url) parameter. Include the `{CHECKOUT_SESSION_ID}` template variable in the URL to retrieve the session’s status on the return page. Checkout automatically substitutes the variable with the Checkout Session ID before redirecting.

Read more about [configuring the return page](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=embedded-page#return-page) and other options for [customizing redirect behavior](https://docs.stripe.com/payments/checkout/custom-success-page.md?payment-ui=embedded-page).

After you create the Checkout Session, use the `client_secret` returned in the response to [mount Checkout](https://docs.stripe.com/payments/overcapture.md#mount-checkout).

To enable the overcapture feature, set [request_overcapture](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-card-request_overcapture) to `if_available`.

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
        request_overcapture: "if_available",
      },
    },
    return_url:
      "https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID}",
  });

  res.send({ clientSecret: session.client_secret });
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));
```

After the customer has completed checkout, look at the [overcapture.status](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-overcapture) field on the [latest_charge](https://docs.stripe.com/api/charges/object.md) in the [PaymentIntent](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_intent) to determine if overcapture is available for the payment based on [availability](https://docs.stripe.com/payments/overcapture.md#availability). If `available`, the [maximum_amount_capturable](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-overcapture-maximum_amount_capturable) field indicates the maximum amount capturable for the PaymentIntent. If `unavailable`, the maximum_amount_capturable is the amount authorized.

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
          "amount_authorized": 1000
          "overcapture": {"status": "available", // or "unavailable"
              "maximum_amount_capturable": 1200
          }
        }
      }
      ...
    }
  ...
}
```

## Capture the PaymentIntent

To capture more than the currently authorized amount on a PaymentIntent, use the [capture](https://docs.stripe.com/api/payment_intents/capture.md) endpoint and provide an [amount_to_capture](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-amount_to_capture) up to the [maximum_amount_capturable](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-overcapture).

If you need to capture an amount larger than the `maximum_amount_capturable`, perform an [incremental authorization](https://docs.stripe.com/payments/incremental-authorization.md) to increase the authorized amount, where available.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture("pi_xxx", {
  amount_to_capture: 1200,
  expand: ["latest_charge"],
});
```

The [amount_capturable](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_capturable) and [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received) fields update accordingly in the PaymentIntent capture response for a successful overcapture. The captured PaymentIntent that returns has an updated [amount](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount) to reflect the total monetary amount moved for this payment. Use the [amount_authorized](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-amount_authorized) field on the associated Charge to reference the initial amount authorized for a successfully overcaptured payment.

```json
// PaymentIntent response
{
  "id": "pi_xxx",
  "object": "payment_intent","amount": 1200,
  "amount_capturable": 0,
  "amount_received": 1200,
  "status": "succeeded",
  ...
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge",
      "payment_method_details": {
        "card": {
          "amount_authorized": 1000,
          "overcapture": {
              "maximum_amount_capturable": 1200,
              "status": "available" // or "unavailable"
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

# Advanced integration

> This is a Advanced integration for when platform is web and ui is elements. View the full page at https://docs.stripe.com/payments/overcapture?platform=web&ui=elements.

Overcapture allows you to capture with an amount that’s higher than the authorized amount for a card payment. Unlike [incremental authorizations](https://docs.stripe.com/payments/incremental-authorization.md), overcapture doesn’t result in additional authorizations with the card networks. When you overcapture a PaymentIntent, your customer won’t see any immediate updates on their credit card statement. After the captured amount settles, the initial pending authorization gets updated with the final captured amount.

## Availability

When using overcapture, be aware of the following restrictions:

- Only available with Visa, Mastercard, American Express, or Discover.
- Only eligible for online card payments. For in-person card payments see how to [collect tips](https://docs.stripe.com/terminal/features/collecting-tips/overview.md).
- Card brands limit the amount that you can overcapture (generally calculated as a percentage of the authorized amount), and impose additional constraints, including country, card type, and merchant category restrictions (see below).

> #### IC+ feature
>
> We offer overcapture to users on _IC+ pricing_ (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs). If you’re on standard Stripe pricing and want access to this feature, contact us using the form at [Stripe support](https://support.stripe.com).

### Availability by card network, merchant country, and merchant category

| Card brand           | Merchant country | Merchant category                                                                                                                                                     | Percent limit                                             |
| -------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Visa**\*           | Global           | Taxicabs and limousines; drinking places (alcoholic beverages); beauty and barber shops; health and beauty spas                                                       | +20%                                                      |
|                      | US               | Eating places and restaurants; fast food restaurants; caterers                                                                                                        | +30%                                                      |
|                      | Global           | Eating places and restaurants; fast food restaurants                                                                                                                  | +20%                                                      |
|                      | Global           | Car rentals                                                                                                                                                           | Greater of +15% or +75 USD (or local currency equivalent) |
|                      | Global           | Lodging; cruise lines                                                                                                                                                 | +15%                                                      |
|                      | Global\*\*       | All other merchant categories                                                                                                                                         | +15%                                                      |
| **Mastercard**       | US\*\*\*         | Eating places and restaurants; fast food restaurants                                                                                                                  | +30%                                                      |
| **American Express** | Global\*\*\*\*   | Eating places and restaurants; drinking places (alcoholic beverages); fast food restaurants                                                                           | +30%                                                      |
|                      | Global           | Taxicabs and limousines; beauty and barber shops; health and beauty spas                                                                                              | +20%                                                      |
|                      | Global           | Lodging; car rentals; truck and utility trailer rentals; motor home and recreational vehicle rentals; grocery stores; retail stores                                   | +15%                                                      |
| **Discover**         | Global           | Taxicabs and limousines; eating places and restaurants; drinking places (alcoholic beverages); fast food restaurants; beauty and barber shops; health and beauty spas | +20%                                                      |
|                      | Global           | Lodging; car rentals                                                                                                                                                  | +15%                                                      |

\* Excludes businesses in the European Economic Area (EEA)

\*\* For cardholder-initiated transactions

\*\*\* Card must also be issued in the United States

\*\*\*\* The percent limit for debit and prepaid card payments is 20%

### Networks with limited support (beta)

The following card networks have limited support for overcapture:

| Card brand      | Merchant country      | Merchant category                                                                                                                                                     | Percent limit |
| --------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Diners Club** | US (through Discover) | Taxicabs and limousines; eating places and restaurants; drinking places (alcoholic beverages); fast food restaurants; beauty and barber shops; health and beauty spas | +20%          |
|                 | US (through Discover) | Lodging; car rentals                                                                                                                                                  | +15%          |

### Overcapture with Strong Customer Authentication (SCA)

If you and the cardholder are in a country that has Strong Customer Authentication (SCA) requirements, keep in mind the limitations of overcapture availability.

- Under SCA requirements, you generally need to authenticate an amount that’s greater than or equal to the amount that you eventually capture. For this reason, you need to authenticate and authorize for the highest estimated amount that you plan to capture, rather than using overcapture as outlined elsewhere on this page. Subsequently, you can capture up to the full amount authenticated, depending on the total amount for the goods or services provided. If you find it necessary to capture an amount beyond the originally authorized and authenticated amount, you must cancel the original payment and create a new one with the correct amount. However, there are some exceptions to this requirement (see below).
- There are a number of [transaction exemptions](https://support.stripe.com/questions/transaction-exemptions-for-strong-customer-authentication-%28sca%29) for SCA where overcapture might be permissible. For example, merchant-initiated transactions (MIT) where the customer isn’t physically present during the checkout flow are potentially exempt. See [when to categorize a transaction as MIT](<https://support.stripe.com/questions/merchant-initiated-transactions-(mits)-when-to-categorize-a-transaction-as-mit>).

You need to familiarize yourself with the complete documentation to gain a comprehensive understanding of overcapture and SCA requirements. See our [SCA guide](https://stripe.com/guides/strong-customer-authentication) for more information.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when using overcapture. Make sure to review the rules for the card networks that you plan to use this feature with to make sure your sales comply with the applicable rules, which vary by network. For example, some card networks don’t allow overcapture for transactions where the final transaction amount should be known at the time of authorization.
>
> The information provided on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

## Create and confirm an uncaptured PaymentIntent

You can only perform overcapture on uncaptured payments after [PaymentIntent confirmation](https://docs.stripe.com/api/payment_intents/confirm.md). To indicate you want to separate the authorization and capture, specify the [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) as `manual` when creating the PaymentIntent. To learn more about separate authorization and capture, see [how to place a hold on a payment method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md).

You must specify the PaymentIntents you plan to overcapture by using `if_available` with the [request_overcapture](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-request_overcapture) parameter.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  payment_method_types: ["card"],
  payment_method: "pm_card_visa",
  confirm: true,
  capture_method: "manual",
  expand: ["latest_charge"],
  payment_method_options: {
    card: {
      request_overcapture: "if_available",
    },
  },
});
```

Look at the [overcapture.status](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-overcapture) field on the [latest_charge](https://docs.stripe.com/api/charges/object.md) in the PaymentIntent confirmation response to determine if overcapture is available for the payment based on [availability](https://docs.stripe.com/payments/overcapture.md#availability). If `available`, the [maximum_amount_capturable](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-overcapture-maximum_amount_capturable) field indicates the maximum amount capturable for the PaymentIntent. If `unavailable`, the maximum_amount_capturable is the amount authorized.

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
          "amount_authorized": 1000
          "overcapture": {"status": "available", // or "unavailable"
              "maximum_amount_capturable": 1200
          }
        }
      }
      ...
    }
  ...
}
```

## Capture the PaymentIntent

To capture more than the currently authorized amount on a PaymentIntent, use the [capture](https://docs.stripe.com/api/payment_intents/capture.md) endpoint and provide an [amount_to_capture](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-amount_to_capture) up to the [maximum_amount_capturable](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-overcapture).

If you need to capture an amount larger than the `maximum_amount_capturable`, perform an [incremental authorization](https://docs.stripe.com/payments/incremental-authorization.md) to increase the authorized amount, where available.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture("pi_xxx", {
  amount_to_capture: 1200,
  expand: ["latest_charge"],
});
```

The [amount_capturable](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_capturable) and [amount_received](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_received) fields update accordingly in the PaymentIntent capture response for a successful overcapture. The captured PaymentIntent that returns has an updated [amount](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount) to reflect the total monetary amount moved for this payment. Use the [amount_authorized](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-amount_authorized) field on the associated Charge to reference the initial amount authorized for a successfully overcaptured payment.

```json
// PaymentIntent response
{
  "id": "pi_xxx",
  "object": "payment_intent","amount": 1200,
  "amount_capturable": 0,
  "amount_received": 1200,
  "status": "succeeded",
  ...
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge",
      "payment_method_details": {
        "card": {
          "amount_authorized": 1000,
          "overcapture": {
              "maximum_amount_capturable": 1200,
              "status": "available" // or "unavailable"
          }
        }
      }
      ...
    }
  ...
}
```

## Test your integration

Use the Stripe test cards below with any CVC and future expiration date to request and perform overcaptures while testing. If overcapture is available on payments for a given network while testing, it’s also available on live payments.

| Number           | Payment method                                 | Description                                      |
| ---------------- | ---------------------------------------------- | ------------------------------------------------ |
| 4242424242424242 | `pm_card_visa`                                 | Visa test card that supports overcapture.        |
| 5555555555554444 | `pm_card_mastercard`                           | Mastercard test card that supports overcapture.  |
| 378282246310005  | `pm_card_amex`                                 | Amex test card that supports overcapture.        |
| 6011111111111117 | `pm_card_discover`                             | Discover test card that supports overcapture.    |
| 4000008400000076 | `pm_card_credit_disableEnterpriseCardFeatures` | Visa test card that doesn’t support overcapture. |
