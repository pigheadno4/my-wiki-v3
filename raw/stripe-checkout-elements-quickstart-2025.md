<!-- Source: Stripe — Build a checkout page with Checkout Sessions API (Checkout Elements) -->
<!-- Fetched: 2026-04-21 -->
<!-- URL: https://docs.stripe.com/payments/advanced/accept-a-payment -->
<!-- Stack: React + Node.js (ui_mode: 'elements') -->

# Build a checkout page with Checkout Sessions API

Build a checkout page on your website using Stripe Elements and the Checkout Sessions API, a front-end SDK that manages tax, discounts, shipping rates, and more.

## Step 1: Set up the server

### Install the Stripe Node library

```bash
npm install --save stripe
```

### Create a Checkout Session

Add an endpoint on your server that creates a Checkout Session, setting the `ui_mode` to `elements`.

The Checkout Session response includes a `client_secret`, which the client uses to complete the payment. Return the client secret in your response.

### Supply a return URL

Specify the URL of the return page in the `return_url` parameter. Include the `{CHECKOUT_SESSION_ID}` template variable in the URL — Checkout replaces it with the Checkout Session ID before redirecting.

### Define a product to sell

Use a predefined Price ID, or use `price_data` for dynamic prices.

### Handle different transaction types

Adjust the `mode` parameter:
- `payment` — one-time payments
- `subscription` — one or more recurring prices
- `setup` — save payment details without collecting payment

#### server.js (Node.js)

```javascript
const stripe = require("stripe")("sk_test_...");
const express = require("express");
const app = express();
app.use(express.static("public"));

const YOUR_DOMAIN = "http://localhost:3000";

app.post("/create-checkout-session", async (req, res) => {
  const session = await stripe.checkout.sessions.create({
    ui_mode: "elements",
    customer_email: "customer@example.com",
    billing_address_collection: "auto",
    shipping_address_collection: {
      allowed_countries: ["US", "CA"],
    },
    line_items: [
      {
        price: "{{PRICE_ID}}",
        quantity: 1,
      },
    ],
    mode: "payment",
    return_url: `${YOUR_DOMAIN}/complete?session_id={CHECKOUT_SESSION_ID}`,
    automatic_tax: { enabled: true },
  });

  res.send({ clientSecret: session.client_secret });
});

app.get("/session-status", async (req, res) => {
  const session = await stripe.checkout.sessions.retrieve(req.query.session_id, {
    expand: ["payment_intent"],
  });

  res.send({
    status: session.status,
    payment_status: session.payment_status,
    payment_intent_id: session.payment_intent.id,
    payment_intent_status: session.payment_intent.status,
  });
});

app.listen(4242, () => console.log("Running on port 4242"));
```

## Step 2: Build a checkout page on the client

### Add Stripe to your React app

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

### Load Stripe.js

Call `loadStripe()` with your publishable API key outside of any component render.

### Fetch a Checkout Session client secret

Make a request to your server to create a Checkout Session and retrieve the `client_secret`.

### Initialize Checkout

Render the `CheckoutElementsProvider`, passing `clientSecret`.

### Store a reference to Checkout

Use the `useCheckout()` hook to access the checkout object in your `CheckoutForm` component. It contains data from the Checkout Session and methods to update it.

### Collect the customer's email address

Provide a valid customer email when completing a Checkout Session. Use `updateEmail` from the Checkout object. Alternatively:
- Pass `customer_email` or `customer` when creating the session (Stripe validates emails this way)
- Pass an email you already validated on `confirm`

### Add the Payment Element

`PaymentElement` embeds an iframe with a dynamic form collecting payment details for all supported payment methods.

### (Optional) Style the Payment Element

Create an `Appearance` object and pass it as an option to `CheckoutElementsProvider`.

#### App.jsx

```jsx
import React, { useMemo } from "react";
import { loadStripe } from "@stripe/stripe-js";
import { CheckoutElementsProvider } from "@stripe/react-stripe-js/checkout";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import CheckoutForm from "./CheckoutForm";
import Complete from "./Complete";

const stripePromise = loadStripe("pk_test_...");

const App = () => {
  const clientSecret = useMemo(() => {
    return fetch("/create-checkout-session", { method: "POST" })
      .then((res) => res.json())
      .then((data) => data.clientSecret);
  }, []);

  const appearance = { theme: "stripe" };

  return (
    <div className="App">
      <Router>
        <CheckoutElementsProvider
          stripe={stripePromise}
          options={{
            clientSecret,
            elementsOptions: { appearance },
            adaptivePricing: { allowed: true },
          }}
        >
          <Routes>
            <Route path="/checkout" element={<CheckoutForm />} />
            <Route path="/complete" element={<Complete />} />
          </Routes>
        </CheckoutElementsProvider>
      </Router>
    </div>
  );
};

export default App;
```

## Step 3: Complete the payment on the client

### Handle the submit event + Complete the payment

Call `checkout.confirm()` when the customer clicks Pay.

### Handle errors

If there are immediate errors (card declined), Stripe.js returns an error — show it to the customer.

#### CheckoutForm.jsx

```jsx
import React, { useState } from "react";
import {
  PaymentElement,
  BillingAddressElement,
  ShippingAddressElement,
  CurrencySelectorElement,
  useCheckout,
} from "@stripe/react-stripe-js/checkout";

const CheckoutForm = () => {
  const [message, setMessage] = useState(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const checkoutState = useCheckout();

  if (checkoutState.type === "loading") return <div>Loading...</div>;
  if (checkoutState.type === "error")
    return <div>Error: {checkoutState.error.message}</div>;

  const handleSubmit = async (e) => {
    e.preventDefault();
    const { checkout } = checkoutState;
    setIsSubmitting(true);
    const confirmResult = await checkout.confirm();
    if (confirmResult.type === "error") {
      setMessage(confirmResult.error.message);
    }
    setIsSubmitting(false);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h4>Billing Address</h4>
      <BillingAddressElement />
      <h4>Shipping Address</h4>
      <ShippingAddressElement />
      <h4>Payment</h4>
      <CurrencySelectorElement />
      <PaymentElement id="payment-element" />
      <button
        disabled={!checkoutState.checkout.canConfirm || isSubmitting}
        id="submit"
      >
        {isSubmitting ? (
          <div className="spinner" />
        ) : (
          `Pay ${checkoutState.checkout.total.total.amount} now`
        )}
      </button>
      {message && <div id="payment-message">{message}</div>}
    </form>
  );
};

export default CheckoutForm;
```

## Step 4: Show a return page

### Create an endpoint to retrieve a Checkout Session

Already included in server.js above (`/session-status`).

### Handle session status

- `complete`: Payment succeeded — render success page
- `open`: Payment failed or canceled — remount Checkout

#### Complete.jsx

```jsx
import React, { useState, useEffect } from "react";

const Complete = () => {
  const [status, setStatus] = useState(null);
  const [paymentIntentId, setPaymentIntentId] = useState("");
  const [paymentStatus, setPaymentStatus] = useState("");
  const [paymentIntentStatus, setPaymentIntentStatus] = useState("");
  const [text, setText] = useState("");

  useEffect(() => {
    const sessionId = new URLSearchParams(window.location.search).get("session_id");
    fetch(`/session-status?session_id=${sessionId}`)
      .then((res) => res.json())
      .then((data) => {
        setStatus(data.status);
        setPaymentIntentId(data.payment_intent_id);
        setPaymentStatus(data.payment_status);
        setPaymentIntentStatus(data.payment_intent_status);
        setText(
          data.status === "complete"
            ? "Payment succeeded"
            : "Something went wrong, please try again."
        );
      });
  }, []);

  return (
    <div id="payment-status">
      <h2 id="status-text">{text}</h2>
      <table>
        <tbody>
          <tr><td>Payment Intent ID</td><td>{paymentIntentId}</td></tr>
          <tr><td>Status</td><td>{status}</td></tr>
          <tr><td>Payment Status</td><td>{paymentStatus}</td></tr>
          <tr><td>Payment Intent Status</td><td>{paymentIntentStatus}</td></tr>
        </tbody>
      </table>
      <a href={`https://dashboard.stripe.com/payments/${paymentIntentId}`} target="_blank" rel="noopener noreferrer">View details</a>
      <a id="retry-button" href="/checkout">Test another payment</a>
    </div>
  );
};

export default Complete;
```

## Step 5: Test your page

```bash
npm start
```

Visit `http://localhost:3000/checkout`. Test cards:

| Scenario | Card number |
| --- | --- |
| Payment succeeds | `4242 4242 4242 4242` |
| Requires 3DS auth | `4000 0025 0000 3155` |
| Payment declined | `4000 0000 0000 9995` |

## Additional features

### Prefill customer data

- `customer_email` — prefill email
- `customer` — prefill from stored Customer email (can't use `updateEmail` in this case)
- `customer_account` (Accounts v2) — prefill from Account's associated email

### Require billing and shipping details

- `billing_address_collection` (server-side)
- `shipping_address_collection.allowed_countries` (server-side)
- Use `BillingAddressElement` + `ShippingAddressElement` client-side

### Automatic tax (Stripe Tax)

- Activate in Dashboard
- Set `automatic_tax: { enabled: true }` on session
- Use `BillingAddressElement` to collect address for tax calculation

### Adaptive Pricing

- Enable in Dashboard settings
- Display localized amounts via `useCheckout` hook
- Mount `CurrencySelectorElement` for currency choice
- Set `adaptivePricing: { allowed: true }` in `CheckoutElementsProvider` options

## Key imports

```js
// Client — package: @stripe/react-stripe-js/checkout
import { CheckoutElementsProvider } from "@stripe/react-stripe-js/checkout";
import {
  PaymentElement,
  BillingAddressElement,
  ShippingAddressElement,
  CurrencySelectorElement,
  useCheckout,
} from "@stripe/react-stripe-js/checkout";
```

## Next steps

- Dynamically update line items
- Fulfill orders (webhook on `checkout.session.completed`)
- Receive payouts / refund payments
- Customer management (self-service portal)
- Express Checkout Element (one-click buttons)
