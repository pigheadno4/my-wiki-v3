<!-- Source URL: https://docs.stripe.com/payments/incremental-authorization -->
<!-- Fetched: 2026-05-11 -->

# Increment an authorization

Increase an existing authorization on a confirmed PaymentIntent before you capture it.

# Stripe-hosted page

> This is a Stripe-hosted page for when platform is web and ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/incremental-authorization?platform=web&ui=stripe-hosted.

Incremental authorization allows you to increase the authorized amount on a confirmed PaymentIntent before you capture it. Before capture, each incremental authorization appears on the credit card statement as an additional pending entry (for example, a 10 USD authorization incremented to 15 USD appears as separate 10 USD and 5 USD pending entries). After capture, the pending authorizations are removed, and the total captured amount appears as one final entry.

## Availability

When using incremental authorizations, be aware of the following restrictions:

- It’s only available with Visa, Mastercard, American Express, or Discover.
- Certain card brands have merchant category restrictions (see below).
- [mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode) is set to `payment` and [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-capture_method) is set to `manual` on the [CheckoutSession](https://docs.stripe.com/api/checkout/sessions/.md).

To learn more about incremental authorization and in-person payments made using Terminal, see [Incremental Authorizations](https://docs.stripe.com/terminal/features/incremental-authorizations.md).

> #### IC+ feature
>
> We offer incremental authorizations to users on _IC+_ (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs) pricing. If you’re on standard Stripe pricing and want access to this feature, contact us using the form at [Stripe support](https://support.stripe.com).

### Availability by card network and merchant category

Use incremental authorizations on payments that fulfill the criteria below. You can find your user category in the [Dashboard](https://dashboard.stripe.com/settings/update/company/update).

Attempting to perform an incremental authorization on a payment that doesn’t fulfill the below criteria results in an error.

| Card brand           | Merchant country | Payment type               | Merchant category                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------- | ---------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Visa**             | Global           | All card payment types     | All user categories                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Mastercard**       | Global\*         | All card payment types     | All user categories                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **American Express** | Global           | All card payment types\*\* | All user categories                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Discover**         | Global           | All card payment types     | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified) |
| **Discover**         | Global           | Card not present           | Taxicabs and limousines                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

\* Excludes MX users and JPY transactions for JP users

\*\* Some American Express issuers don’t support incremental authorizations. When the feature is requested for these cards, the returned [status](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-incremental_authorization_supported) is `unavailable`.

### Networks with limited support (beta)

The following card networks have limited support for incremental authorization:

| Card brand      | Merchant country              | Payment type     | Merchant category                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------- | ----------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Diners Club** | US, CA, UK (through Discover) | Card present     | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified)                      |
| **Diners Club** | Global (through Discover)     | Card not present | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, taxicabs/limousines, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified) |
| **UnionPay**    | Global (through Discover)     | Card not present | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, taxicabs/limousines, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified) |
| **JCB**         | Global (through Discover)     | Card not present | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, taxicabs/limousines, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified) |

### Incremental authorizations with Strong Customer Authentication (SCA)

If you and the cardholder are in a [country with SCA requirements](<https://support.stripe.com/questions/countries-in-the-european-economic-area-(eea)-impacted-by-strong-customer-authentication-(sca)-regulation>), there are important considerations to keep in mind when using incremental authorization.

When you request the incremental authorization feature during the initial authorization, Stripe automatically configures the payment method for future off-session usage. Although this requires 3D Secure (3DS) for the initial authorization, subsequent incremental authorizations on this payment is considered merchant-initiated, potentially exempting any additional SCA. Clearly indicate to your customer during the initial transaction that their payment will be saved for future off-session usage with the incremental authorizations.

With some 3DS transactions, the [liability for fraudulent chargebacks (stolen or counterfeit cards) shifts from you to the card issuer](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#disputed-payments). You don’t benefit from liability shift when submitting merchant-initiated transactions.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For instance, if you want to save their payment method for future use, such as charging them when they’re not actively using your website or app. Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in.
>
> If you want to charge them when they’re offline, make sure your terms include the following:
>
> - The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.

- The anticipated timing and frequency of payments (for example, if the charges are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.
  > Make sure you keep a record of your customer’s written agreement to these terms.

## Best practices

When using incremental authorization, proactively notify your end customer with the details of any authorizations for estimated amounts, which might be followed by incremental authorizations that increase those amounts. Here are some best practices for doing so:

- Disclose that an authorization is for an estimated amount and that subsequent authorization requests might follow at the time of checkout, before purchase.
- Base estimated amounts on a genuine estimate of what the total transaction amount will be.

You can use the [custom_text](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-custom_text) field when creating a new [CheckoutSession](https://docs.stripe.com/api/checkout_sessions.md) to display additional text on the checkout page to help meet compliance requirements.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when using incremental authorization. Consult the network rules for the card networks that you plan to use this feature with to make sure your sales comply with applicable rules, which vary by network. For example, most card networks restrict how you can calculate estimated amounts included in the initial authorization, and prohibit the use of incremental authorizations for transactions where the transaction amount should be known at the time of authorization (for example, charges for recurring subscriptions).
>
> The information provided on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

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

Lastly, set [request_incremental_authorization](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-card-request_incremental_authorization) as `if_available` to enable the incremental authorization feature.

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
        request_incremental_authorization: "if_available",
      },
    },
    mode: "payment",
    success_url: "http://localhost:4242/success",
  });

  res.redirect(303, session.url);
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));
```

After the customer has completed checkout, the [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details) field on the [latest_charge](https://docs.stripe.com/api/charges/object.md) in the [PaymentIntent](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_intent) contains `available` or `unavailable` based on the customer’s payment method and [the availability criteria mentioned above](https://docs.stripe.com/payments/incremental-authorization.md#availability), which determines whether a PaymentIntent is eligible for incremental authorization or not. (If you didn’t request incremental authorization when creating the CheckoutSession, it will be `unavailable`.)

```json
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  ...
  // if latest_charge is expanded
  {
    "latest_charge": {
        "amount": 1000,
        "payment_method_details": {
          "card": {
            "incremental_authorization": {"status": "available" // or "unavailable"
            }
          }
        }
        ...
      }
  }

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

## Perform an incremental authorization

To increase the authorized amount on a PaymentIntent, use the [increment_authorization](https://docs.stripe.com/api/payment_intents/increment_authorization.md) endpoint and provide the updated total [authorization amount](https://docs.stripe.com/api/payment_intents/increment_authorization.md#increment_authorization-amount) to increment to, which must be greater than the original authorized amount. This attempts to authorize for a higher amount on your customer’s card. A single PaymentIntent can call this endpoint multiple times to further increase the authorized amount.

You have a maximum of 10 incremental authorization attempts per PaymentIntent.

#### curl

```bash
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/increment_authorization \
  -u <<YOUR_SECRET_KEY>>: \
  -d "amount"=1500
```

If the incremental authorization succeeds, it returns the PaymentIntent object with the updated amount. If the authorization fails, it returns a [card_declined](https://docs.stripe.com/error-codes.md#card-declined) error instead. The PaymentIntent object remains capturable for the previously authorized amount. Any potential updates to other PaymentIntent fields (for example, [application_fee_amount](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-application_fee_amount), [transfer_data](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-transfer_data), [metadata](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-metadata), [description](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-description), and [statement_descriptor](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-statement_descriptor)) aren’t saved if the incremental authorization fails.

Incremental authorization has a maximum cap of either 500 USD (or local equivalent) over, or 500% over the previously authorized amount (whichever is higher) for each individual increment.

## Capture the PaymentIntent

Whether you increase the authorized amount on a PaymentIntent with an incremental authorization or not, you need to capture the funds before the initial authorization expires–incremental authorizations don’t extend [the validity period](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md). To capture the authorized amount on a PaymentIntent with prior incremental authorizations, use the [capture endpoint](https://docs.stripe.com/api/payment_intents/capture.md) as usual.

#### curl

```bash
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/capture \
  -u <<YOUR_SECRET_KEY>>:
```

If the incremental authorization succeeds, it returns the captured PaymentIntent object with the updated amount. If the authorization fails, it returns a [card_declined error](https://docs.stripe.com/error-codes.md#card-declined) instead. The PaymentIntent isn’t captured, but it remains capturable for the previously authorized amount. Any potential updates to other PaymentIntent fields (for example, [application_fee_amount](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-application_fee_amount), [transfer_data](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-transfer_data), [metadata](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-metadata), [description](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-description) and [statement_descriptor](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-statement_descriptor)) aren’t saved if the incremental authorization fails.

## Test your integration

Use a Stripe test card with any CVC, postal code, and future expiration date to trigger incremental authorizations while testing:

1. Create the CheckoutSession using the test card in the [create a CheckoutSession step](https://docs.stripe.com/payments/incremental-authorization.md#create-and-confirm).

1. Perform the incremental authorization with the parameters specified in the [perform an incremental authorization step](https://docs.stripe.com/payments/incremental-authorization.md#increment-authorization). Use the following test cards to simulate incremental authorization success or failure.

| Number           | Payment Method                                 | Description                                                               |
| ---------------- | ---------------------------------------------- | ------------------------------------------------------------------------- |
| 4000058400000063 | `pm_card_debit_incrementalAuthAuthorized`      | Increases the authorization amount to the amount provided in the request. |
| 4000008400000076 | `pm_card_credit_disableEnterpriseCardFeatures` | Declines the increased authorization request.                             |

# Full embedded page

> This is a Full embedded page for when platform is web and ui is embedded-page. View the full page at https://docs.stripe.com/payments/incremental-authorization?platform=web&ui=embedded-page.

Incremental authorization allows you to increase the authorized amount on a confirmed PaymentIntent before you capture it. Before capture, each incremental authorization appears on the credit card statement as an additional pending entry (for example, a 10 USD authorization incremented to 15 USD appears as separate 10 USD and 5 USD pending entries). After capture, the pending authorizations are removed, and the total captured amount appears as one final entry.

## Availability

When using incremental authorizations, be aware of the following restrictions:

- It’s only available with Visa, Mastercard, American Express, or Discover.
- Certain card brands have merchant category restrictions (see below).
- [mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode) is set to `payment` and [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-capture_method) is set to `manual` on the [CheckoutSession](https://docs.stripe.com/api/checkout/sessions/.md).

To learn more about incremental authorization and in-person payments made using Terminal, see [Incremental Authorizations](https://docs.stripe.com/terminal/features/incremental-authorizations.md).

> #### IC+ feature
>
> We offer incremental authorizations to users on _IC+_ (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs) pricing. If you’re on standard Stripe pricing and want access to this feature, contact us using the form at [Stripe support](https://support.stripe.com).

### Availability by card network and merchant category

Use incremental authorizations on payments that fulfill the criteria below. You can find your user category in the [Dashboard](https://dashboard.stripe.com/settings/update/company/update).

Attempting to perform an incremental authorization on a payment that doesn’t fulfill the below criteria results in an error.

| Card brand           | Merchant country | Payment type               | Merchant category                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------- | ---------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Visa**             | Global           | All card payment types     | All user categories                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Mastercard**       | Global\*         | All card payment types     | All user categories                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **American Express** | Global           | All card payment types\*\* | All user categories                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Discover**         | Global           | All card payment types     | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified) |
| **Discover**         | Global           | Card not present           | Taxicabs and limousines                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

\* Excludes MX users and JPY transactions for JP users

\*\* Some American Express issuers don’t support incremental authorizations. When the feature is requested for these cards, the returned [status](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-incremental_authorization_supported) is `unavailable`.

### Networks with limited support (beta)

The following card networks have limited support for incremental authorization:

| Card brand      | Merchant country              | Payment type     | Merchant category                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------- | ----------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Diners Club** | US, CA, UK (through Discover) | Card present     | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified)                      |
| **Diners Club** | Global (through Discover)     | Card not present | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, taxicabs/limousines, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified) |
| **UnionPay**    | Global (through Discover)     | Card not present | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, taxicabs/limousines, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified) |
| **JCB**         | Global (through Discover)     | Card not present | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, taxicabs/limousines, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified) |

### Incremental authorizations with Strong Customer Authentication (SCA)

If you and the cardholder are in a [country with SCA requirements](<https://support.stripe.com/questions/countries-in-the-european-economic-area-(eea)-impacted-by-strong-customer-authentication-(sca)-regulation>), there are important considerations to keep in mind when using incremental authorization.

When you request the incremental authorization feature during the initial authorization, Stripe automatically configures the payment method for future off-session usage. Although this requires 3D Secure (3DS) for the initial authorization, subsequent incremental authorizations on this payment is considered merchant-initiated, potentially exempting any additional SCA. Clearly indicate to your customer during the initial transaction that their payment will be saved for future off-session usage with the incremental authorizations.

With some 3DS transactions, the [liability for fraudulent chargebacks (stolen or counterfeit cards) shifts from you to the card issuer](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#disputed-payments). You don’t benefit from liability shift when submitting merchant-initiated transactions.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For instance, if you want to save their payment method for future use, such as charging them when they’re not actively using your website or app. Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in.
>
> If you want to charge them when they’re offline, make sure your terms include the following:
>
> - The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.

- The anticipated timing and frequency of payments (for example, if the charges are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.
  > Make sure you keep a record of your customer’s written agreement to these terms.

## Best practices

When using incremental authorization, proactively notify your end customer with the details of any authorizations for estimated amounts, which might be followed by incremental authorizations that increase those amounts. Here are some best practices for doing so:

- Disclose that an authorization is for an estimated amount and that subsequent authorization requests might follow at the time of checkout, before purchase.
- Base estimated amounts on a genuine estimate of what the total transaction amount will be.

You can use the [custom_text](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-custom_text) field when creating a new [CheckoutSession](https://docs.stripe.com/api/checkout_sessions.md) to display additional text on the checkout page to help meet compliance requirements.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when using incremental authorization. Consult the network rules for the card networks that you plan to use this feature with to make sure your sales comply with applicable rules, which vary by network. For example, most card networks restrict how you can calculate estimated amounts included in the initial authorization, and prohibit the use of incremental authorizations for transactions where the transaction amount should be known at the time of authorization (for example, charges for recurring subscriptions).
>
> The information provided on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

## Create a CheckoutSession

From your server, create a _Checkout Session_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription) and set the [ui_mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-ui_mode) to `embedded_page`. You can configure the [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) with [line items](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items) to include, and options such as [currency](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-currency).

To return customers to a custom page that you host on your website, specify that page’s URL in the [return_url](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-return_url) parameter. Include the `{CHECKOUT_SESSION_ID}` template variable in the URL to retrieve the session’s status on the return page. Checkout automatically substitutes the variable with the Checkout Session ID before redirecting.

Read more about [configuring the return page](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=embedded-page#return-page) and other options for [customizing redirect behavior](https://docs.stripe.com/payments/checkout/custom-success-page.md?payment-ui=embedded-page).

After you create the Checkout Session, use the `client_secret` returned in the response to [mount Checkout](https://docs.stripe.com/payments/incremental-authorization.md#mount-checkout).

To enable the incremental authorization feature, set [request_incremental_authorization](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-card-request_incremental_authorization) to `if_available`.

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
        request_incremental_authorization: "if_available",
      },
    },
    return_url:
      "https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID}",
  });

  res.send({ clientSecret: session.client_secret });
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));
```

After the customer has completed checkout, the [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details) field on the [latest_charge](https://docs.stripe.com/api/charges/object.md) in the [PaymentIntent](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_intent) contains `available` or `unavailable` based on the customer’s payment method and [the availability criteria mentioned above](https://docs.stripe.com/payments/incremental-authorization.md#availability), which determines whether a PaymentIntent is eligible for incremental authorization or not. (If you didn’t request incremental authorization when creating the CheckoutSession, it will be `unavailable`.)

```json
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  ...
  // if latest_charge is expanded
  {
    "latest_charge": {
        "amount": 1000,
        "payment_method_details": {
          "card": {
            "incremental_authorization": {"status": "available" // or "unavailable"
            }
          }
        }
        ...
      }
  }

}
```

## Perform an incremental authorization

To increase the authorized amount on a PaymentIntent, use the [increment_authorization](https://docs.stripe.com/api/payment_intents/increment_authorization.md) endpoint and provide the updated total [authorization amount](https://docs.stripe.com/api/payment_intents/increment_authorization.md#increment_authorization-amount) to increment to, which must be greater than the original authorized amount. This attempts to authorize for a higher amount on your customer’s card. A single PaymentIntent can call this endpoint multiple times to further increase the authorized amount.

You have a maximum of 10 incremental authorization attempts per PaymentIntent.

#### curl

```bash
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/increment_authorization \
  -u <<YOUR_SECRET_KEY>>: \
  -d "amount"=1500
```

If the incremental authorization succeeds, it returns the PaymentIntent object with the updated amount. If the authorization fails, it returns a [card_declined](https://docs.stripe.com/error-codes.md#card-declined) error instead. The PaymentIntent object remains capturable for the previously authorized amount. Any potential updates to other PaymentIntent fields (for example, [application_fee_amount](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-application_fee_amount), [transfer_data](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-transfer_data), [metadata](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-metadata), [description](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-description), and [statement_descriptor](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-statement_descriptor)) aren’t saved if the incremental authorization fails.

Incremental authorization has a maximum cap of either 500 USD (or local equivalent) over, or 500% over the previously authorized amount (whichever is higher) for each individual increment.

## Capture the PaymentIntent

Whether you increase the authorized amount on a PaymentIntent with an incremental authorization or not, you need to capture the funds before the initial authorization expires–incremental authorizations don’t extend [the validity period](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md). To capture the authorized amount on a PaymentIntent with prior incremental authorizations, use the [capture endpoint](https://docs.stripe.com/api/payment_intents/capture.md) as usual.

#### curl

```bash
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/capture \
  -u <<YOUR_SECRET_KEY>>:
```

If the incremental authorization succeeds, it returns the captured PaymentIntent object with the updated amount. If the authorization fails, it returns a [card_declined error](https://docs.stripe.com/error-codes.md#card-declined) instead. The PaymentIntent isn’t captured, but it remains capturable for the previously authorized amount. Any potential updates to other PaymentIntent fields (for example, [application_fee_amount](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-application_fee_amount), [transfer_data](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-transfer_data), [metadata](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-metadata), [description](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-description) and [statement_descriptor](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-statement_descriptor)) aren’t saved if the incremental authorization fails.

## Test your integration

Use a Stripe test card with any CVC, postal code, and future expiration date to trigger incremental authorizations while testing:

1. Create the CheckoutSession using the test card in the [create a CheckoutSession step](https://docs.stripe.com/payments/incremental-authorization.md#create-and-confirm).

1. Perform the incremental authorization with the parameters specified in the [perform an incremental authorization step](https://docs.stripe.com/payments/incremental-authorization.md#increment-authorization). Use the following test cards to simulate incremental authorization success or failure.

| Number           | Payment Method                                 | Description                                                               |
| ---------------- | ---------------------------------------------- | ------------------------------------------------------------------------- |
| 4000058400000063 | `pm_card_debit_incrementalAuthAuthorized`      | Increases the authorization amount to the amount provided in the request. |
| 4000008400000076 | `pm_card_credit_disableEnterpriseCardFeatures` | Declines the increased authorization request.                             |

# Advanced integration

> This is a Advanced integration for when platform is web and ui is elements. View the full page at https://docs.stripe.com/payments/incremental-authorization?platform=web&ui=elements.

Incremental authorization allows you to increase the authorized amount on a confirmed PaymentIntent before you capture it. Before capture, each incremental authorization appears on the credit card statement as an additional pending entry (for example, a 10 USD authorization incremented to 15 USD appears as separate 10 USD and 5 USD pending entries). After capture, the pending authorizations are removed, and the total captured amount appears as one final entry.

## Availability

When using incremental authorizations, be aware of the following restrictions:

- It’s only available with Visa, Mastercard, American Express, or Discover.
- Certain card brands have merchant category restrictions (see below).

To learn more about incremental authorization and in-person payments made using Terminal, see [Incremental Authorizations](https://docs.stripe.com/terminal/features/incremental-authorizations.md).

> #### IC+ feature
>
> We offer incremental authorizations to users on _IC+_ (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs) pricing. If you’re on standard Stripe pricing and want access to this feature, contact us using the form at [Stripe support](https://support.stripe.com).

### Availability by card network and merchant category

Use incremental authorizations on payments that fulfill the criteria below. You can find your user category in the [Dashboard](https://dashboard.stripe.com/settings/update/company/update).

Attempting to perform an incremental authorization on a payment that doesn’t fulfill the below criteria results in an error.

| Card brand           | Merchant country | Payment type               | Merchant category                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------- | ---------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Visa**             | Global           | All card payment types     | All user categories                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Mastercard**       | Global\*         | All card payment types     | All user categories                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **American Express** | Global           | All card payment types\*\* | All user categories                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Discover**         | Global           | All card payment types     | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified) |
| **Discover**         | Global           | Card not present           | Taxicabs and limousines                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

\* Excludes MX users and JPY transactions for JP users

\*\* Some American Express issuers don’t support incremental authorizations. When the feature is requested for these cards, the returned [status](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-incremental_authorization_supported) is `unavailable`.

### Networks with limited support (beta)

The following card networks have limited support for incremental authorization:

| Card brand      | Merchant country              | Payment type     | Merchant category                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------- | ----------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Diners Club** | US, CA, UK (through Discover) | Card present     | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified)                      |
| **Diners Club** | Global (through Discover)     | Card not present | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, taxicabs/limousines, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified) |
| **UnionPay**    | Global (through Discover)     | Card not present | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, taxicabs/limousines, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified) |
| **JCB**         | Global (through Discover)     | Card not present | Car rental, hotels, local/suburban commuter, passenger transportation, including ferries, passenger railways, taxicabs/limousines, bus lines-charter, tour, steamship/cruise lines, boat rentals & lease, grocery stores and supermarkets, electric vehicle charging, eating places and restaurants, drinking places (alcoholic beverages), hotels, motels, resorts, trailer parks & campgrounds, equip/tool/furn/appl rental & leasing, automobile rental agency, truck and utility trailer rentals, motor home and rec vehicle rentals, parking lots, parking meters, and garages, amusement parks, circuses, fortune tell, recreation services (not classified) |

### Incremental authorizations with Strong Customer Authentication (SCA)

If you and the cardholder are in a [country with SCA requirements](<https://support.stripe.com/questions/countries-in-the-european-economic-area-(eea)-impacted-by-strong-customer-authentication-(sca)-regulation>), there are important considerations to keep in mind when using incremental authorization.

When you request the incremental authorization feature during the initial authorization, Stripe automatically configures the payment method for future off-session usage. Although this requires 3D Secure (3DS) for the initial authorization, subsequent incremental authorizations on this payment is considered merchant-initiated, potentially exempting any additional SCA. Clearly indicate to your customer during the initial transaction that their payment will be saved for future off-session usage with the incremental authorizations.

With some 3DS transactions, the [liability for fraudulent chargebacks (stolen or counterfeit cards) shifts from you to the card issuer](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#disputed-payments). You don’t benefit from liability shift when submitting merchant-initiated transactions.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For instance, if you want to save their payment method for future use, such as charging them when they’re not actively using your website or app. Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in.
>
> If you want to charge them when they’re offline, make sure your terms include the following:
>
> - The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.

- The anticipated timing and frequency of payments (for example, if the charges are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.
  > Make sure you keep a record of your customer’s written agreement to these terms.

## Best practices

When using incremental authorization, proactively notify your end customer with the details of any authorizations for estimated amounts, which might be followed by incremental authorizations that increase those amounts. Here are some best practices for doing so:

- Disclose that an authorization is for an estimated amount and that subsequent authorization requests might follow at the time of checkout, before purchase.
- Base estimated amounts on a genuine estimate of what the total transaction amount will be.

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when using incremental authorization. Consult the network rules for the card networks that you plan to use this feature with to make sure your sales comply with applicable rules, which vary by network. For example, most card networks restrict how you can calculate estimated amounts included in the initial authorization, and prohibit the use of incremental authorizations for transactions where the transaction amount should be known at the time of authorization (for example, charges for recurring subscriptions).
>
> The information provided on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

## Create and confirm an uncaptured PaymentIntent

You can use the `request_incremental_authorization` parameter to specify the PaymentIntents you plan to increment.

Use the `if_available` or `never` parameters to determine when to start incrementing a PaymentIntent:

- `if_available`: The created PaymentIntent allows for future increments based on [incremental authorization support availability](https://docs.stripe.com/payments/incremental-authorization.md#availability).

- `never`: The created PaymentIntent doesn’t allow for future increments.

You can only perform incremental authorizations on uncaptured payments after [PaymentIntent confirmation](https://docs.stripe.com/api/payment_intents/confirm.md). To adjust the amount of a payment before confirmation, use [update method](https://docs.stripe.com/api/payment_intents/update.md) instead.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  payment_method_types: ["card"],
  payment_method: "pm_card_debit_incrementalAuthAuthorized",
  confirm: true,
  capture_method: "manual",
  expand: ["latest_charge"],
  payment_method_options: {
    card: {
      request_incremental_authorization: "if_available",
    },
  },
});
```

In the PaymentIntent confirmation response, the [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details) field on the [latest_charge](https://docs.stripe.com/api/charges/object.md) contains `available` or `unavailable` based on the customer’s payment method and [the availability criteria mentioned above](https://docs.stripe.com/payments/incremental-authorization.md#availability), which determines whether a PaymentIntent is eligible for incremental authorization or not. (If you didn’t request incremental authorization in your PaymentIntent confirmation request, it will be `unavailable`.)

```json
// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  ...
  // if latest_charge is expanded
  {
    "latest_charge": {
        "amount": 1000,
        "payment_method_details": {
          "card": {
            "incremental_authorization": {"status": "available" // or "unavailable"
            }
          }
        }
        ...
      }
  }

}
```

## Perform an incremental authorization

To increase the authorized amount on a PaymentIntent, use the [increment_authorization](https://docs.stripe.com/api/payment_intents/increment_authorization.md) endpoint and provide the updated total [authorization amount](https://docs.stripe.com/api/payment_intents/increment_authorization.md#increment_authorization-amount) to increment to, which must be greater than the original authorized amount. This attempts to authorize for a higher amount on your customer’s card. A single PaymentIntent can call this endpoint multiple times to further increase the authorized amount.

You have a maximum of 10 incremental authorization attempts per PaymentIntent.

#### curl

```bash
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/increment_authorization \
  -u <<YOUR_SECRET_KEY>>: \
  -d "amount"=1500
```

If the incremental authorization succeeds, it returns the PaymentIntent object with the updated amount. If the authorization fails, it returns a [card_declined](https://docs.stripe.com/error-codes.md#card-declined) error instead. The PaymentIntent object remains capturable for the previously authorized amount. Any potential updates to other PaymentIntent fields (for example, [application_fee_amount](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-application_fee_amount), [transfer_data](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-transfer_data), [metadata](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-metadata), [description](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-description), and [statement_descriptor](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-statement_descriptor)) aren’t saved if the incremental authorization fails.

Incremental authorization has a maximum cap of either 500 USD (or local equivalent) over, or 500% over the previously authorized amount (whichever is higher) for each individual increment.

## Capture the PaymentIntent

Whether you increase the authorized amount on a PaymentIntent with an incremental authorization or not, you need to capture the funds before the initial authorization expires–incremental authorizations don’t extend [the validity period](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md). To capture the authorized amount on a PaymentIntent with prior incremental authorizations, use the [capture endpoint](https://docs.stripe.com/api/payment_intents/capture.md) as usual.

#### curl

```bash
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/capture \
  -u <<YOUR_SECRET_KEY>>:
```

If the incremental authorization succeeds, it returns the captured PaymentIntent object with the updated amount. If the authorization fails, it returns a [card_declined error](https://docs.stripe.com/error-codes.md#card-declined) instead. The PaymentIntent isn’t captured, but it remains capturable for the previously authorized amount. Any potential updates to other PaymentIntent fields (for example, [application_fee_amount](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-application_fee_amount), [transfer_data](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-transfer_data), [metadata](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-metadata), [description](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-description) and [statement_descriptor](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-statement_descriptor)) aren’t saved if the incremental authorization fails.

## Test your integration

Use a Stripe test card with any CVC, postal code, and future expiration date to trigger incremental authorizations while testing:

1. Create the PaymentIntent using the test card in the [create and confirm PaymentIntent step](https://docs.stripe.com/payments/incremental-authorization.md#create-and-confirm).

1. Perform the incremental authorization with the parameters specified in the [perform an incremental authorization step](https://docs.stripe.com/payments/incremental-authorization.md#increment-authorization). Use the following test cards to simulate incremental authorization success or failure.

| Number           | Payment Method                                 | Description                                                               |
| ---------------- | ---------------------------------------------- | ------------------------------------------------------------------------- |
| 4000058400000063 | `pm_card_debit_incrementalAuthAuthorized`      | Increases the authorization amount to the amount provided in the request. |
| 4000008400000076 | `pm_card_credit_disableEnterpriseCardFeatures` | Declines the increased authorization request.                             |
