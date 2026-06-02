<!-- Source: Stripe — Build a checkout page with Payment Intents API -->
<!-- Fetched: 2026-04-21 -->
<!-- URL: https://docs.stripe.com/payments/quickstart -->
<!-- Stack: React + Node.js (Payment Intents API) -->

# Build a checkout page with Payment Intents API

Learn how to embed a custom Stripe payment form in your website or application. The client- and server-side code builds a checkout form with Stripe's Web Elements to let you accept payments.

> **Interested in using Stripe Tax, discounts, shipping, or currency conversion?**
> Stripe has a Payment Element integration that manages tax, discounts, shipping, and currency conversion for you. See the build a checkout page (Checkout Sessions API) to learn more.

## Step 1: Set up the server

### Install the Stripe Node library

```bash
npm install --save stripe
```

### Create a PaymentIntent

Add an endpoint that creates a PaymentIntent. A PaymentIntent tracks the customer's payment lifecycle, keeping track of failed attempts and ensuring the customer is only charged once. Return the PaymentIntent's `client_secret` in the response.

### Configure payment methods

Stripe enables cards and other common payment methods by default with dynamic payment methods. You can update and configure payment methods from the Dashboard with no code required.

#### server.js (Node.js)

```javascript
const express = require("express");
const app = express();
const stripe = require("stripe")("sk_test_...");

app.use(express.static("public"));
app.use(express.json());

const calculateTax = async (items, currency) => {
  const taxCalculation = await stripe.tax.calculations.create({
    currency,
    customer_details: {
      address: {
        line1: "920 5th Ave",
        city: "Seattle",
        state: "WA",
        postal_code: "98104",
        country: "US",
      },
      address_source: "shipping",
    },
    line_items: items.map((item) => ({
      amount: item.amount, // Amount in cents
      reference: item.id,
    })),
  });
  return taxCalculation;
};

const calculateOrderAmount = (taxCalculation) => {
  return taxCalculation.amount_total;
};

const chargeCustomer = async (customerId) => {
  const paymentMethods = await stripe.paymentMethods.list({
    customer: customerId,
    type: "card",
  });
  try {
    await stripe.paymentIntents.create({
      amount: 1099,
      currency: "usd",
      customer: customerId,
      payment_method: paymentMethods.data[0].id,
      off_session: true,
      confirm: true,
    });
  } catch (err) {
    console.log("Error code is: ", err.code);
    const pi = await stripe.paymentIntents.retrieve(err.raw.payment_intent.id);
    console.log("PI retrieved: ", pi.id);
  }
};

app.post("/create-payment-intent", async (req, res) => {
  const { items } = req.body;
  const customer = await stripe.customers.create();

  // Create a Tax Calculation for the items being sold
  const taxCalculation = await calculateTax(items, "usd");
  const amount = calculateOrderAmount(taxCalculation);

  const paymentIntent = await stripe.paymentIntents.create({
    customer: customer.id,
    setup_future_usage: "off_session",
    amount,
    currency: "usd",
    automatic_payment_methods: { enabled: true },
    // Link tax calculation to PaymentIntent
    hooks: {
      inputs: {
        tax: { calculation: taxCalculation.id },
      },
    },
  });

  res.send({ clientSecret: paymentIntent.client_secret });
});

app.listen(4242, () => console.log("Node server listening on port 4242!"));
```

## Step 2: Build a checkout page on the client

### Add Stripe to your React app

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

### Load Stripe.js

Call `loadStripe()` with your publishable API key outside of any component render.

### Fetch a PaymentIntent

Immediately make a request on page load to create a new PaymentIntent. The `clientSecret` returned is used to complete the payment.

### Initialize Stripe Elements

Pass the promise from `loadStripe` to the `Elements` provider. Pass the `clientSecret` as an option.

### Store a reference to Stripe

Use `useStripe()` and `useElements()` hooks in your `CheckoutForm` component.

### Add the PaymentElement

`PaymentElement` embeds an iframe with a dynamic form collecting payment details for all supported payment methods. Pass `layout: 'accordion'` for accordion layout.

### (Optional) Style the Payment Element

Create an `Appearance` object and pass it to the `Elements` provider. Use `loader: 'auto'` for skeleton UI.

#### App.jsx

```jsx
import React, { useState, useEffect } from "react";
import { loadStripe } from "@stripe/stripe-js";
import { Elements } from "@stripe/react-stripe-js";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CheckoutForm from "./CheckoutForm";
import CompletePage from "./CompletePage";

const stripePromise = loadStripe("pk_test_...");

export default function App() {
  const [clientSecret, setClientSecret] = useState("");

  useEffect(() => {
    fetch("/create-payment-intent", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ items: [{ id: "xl-tshirt", amount: 1000 }] }),
    })
      .then((res) => res.json())
      .then((data) => setClientSecret(data.clientSecret));
  }, []);

  const appearance = { theme: "stripe" };
  const loader = "auto"; // skeleton loader

  return (
    <Router>
      <div className="App">
        {clientSecret && (
          <Elements options={{ clientSecret, appearance, loader }} stripe={stripePromise}>
            <Routes>
              <Route path="/checkout" element={<CheckoutForm />} />
              <Route path="/complete" element={<CompletePage />} />
            </Routes>
          </Elements>
        )}
      </div>
    </Router>
  );
}
```

## Step 3: Complete the payment on the client

### Complete the payment

Call `stripe.confirmPayment({ elements, confirmParams: { return_url, receipt_email } })`.

For bank auth methods, Stripe redirects to an intermediate page then to `return_url`. For card errors, Stripe.js returns an error immediately.

### Show a payment status message

On the return page, the `payment_intent_client_secret` query param is appended by Stripe.js. Use `stripe.retrievePaymentIntent(clientSecret)` to get the status.

| PaymentIntent status | Message |
| --- | --- |
| `succeeded` | Payment succeeded |
| `processing` | Your payment is processing |
| `requires_payment_method` | Payment not successful, please try again |

#### CheckoutForm.jsx

```jsx
import React, { useState } from "react";
import { PaymentElement, useStripe, useElements } from "@stripe/react-stripe-js";

export default function CheckoutForm() {
  const stripe = useStripe();
  const elements = useElements();
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!stripe || !elements) return;
    setIsLoading(true);

    const { error } = await stripe.confirmPayment({
      elements,
      confirmParams: {
        return_url: "http://localhost:3000/complete",
        receipt_email: email,
      },
    });

    if (error.type === "card_error" || error.type === "validation_error") {
      setMessage(error.message);
    } else {
      setMessage("An unexpected error occurred.");
    }
    setIsLoading(false);
  };

  return (
    <form id="payment-form" onSubmit={handleSubmit}>
      <input
        id="email"
        type="text"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Enter email address"
      />
      <PaymentElement id="payment-element" options={{ layout: "accordion" }} />
      <button disabled={isLoading || !stripe || !elements} id="submit">
        {isLoading ? <div className="spinner" /> : "Pay now"}
      </button>
      {message && <div id="payment-message">{message}</div>}
    </form>
  );
}
```

#### CompletePage.jsx

```jsx
import React, { useEffect, useState } from "react";
import { useStripe } from "@stripe/react-stripe-js";

const STATUS_CONTENT_MAP = {
  succeeded: { text: "Payment succeeded", iconColor: "#30B130" },
  processing: { text: "Your payment is processing.", iconColor: "#6D6E78" },
  requires_payment_method: {
    text: "Your payment was not successful, please try again.",
    iconColor: "#DF1B41",
  },
  default: { text: "Something went wrong, please try again.", iconColor: "#DF1B41" },
};

export default function CompletePage() {
  const stripe = useStripe();
  const [status, setStatus] = useState("default");
  const [intentId, setIntentId] = useState(null);

  useEffect(() => {
    if (!stripe) return;
    const clientSecret = new URLSearchParams(window.location.search).get(
      "payment_intent_client_secret"
    );
    if (!clientSecret) return;
    stripe.retrievePaymentIntent(clientSecret).then(({ paymentIntent }) => {
      if (!paymentIntent) return;
      setStatus(paymentIntent.status);
      setIntentId(paymentIntent.id);
    });
  }, [stripe]);

  return (
    <div id="payment-status">
      <h2 id="status-text">{STATUS_CONTENT_MAP[status].text}</h2>
      {intentId && (
        <table>
          <tbody>
            <tr><td>id</td><td>{intentId}</td></tr>
            <tr><td>status</td><td>{status}</td></tr>
          </tbody>
        </table>
      )}
      {intentId && (
        <a href={`https://dashboard.stripe.com/payments/${intentId}`} target="_blank" rel="noopener noreferrer">
          View details
        </a>
      )}
      <a id="retry-button" href="/checkout">Test another payment</a>
    </div>
  );
}
```

## Step 4: Handle post-payment events (webhook)

Stripe recommends handling: `payment_intent.succeeded`, `payment_intent.processing`, `payment_intent.payment_failed`.

Listen for these events server-side rather than waiting on client callbacks — clients can close the browser before callbacks execute, and malicious clients can manipulate responses.

## Step 5: Test

```bash
npm start
```

Visit `http://localhost:3000/checkout`. Test cards:

| Scenario | Card |
| --- | --- |
| Success | `4242 4242 4242 4242` |
| 3DS required | `4000 0025 0000 3155` |
| Declined | `4000 0000 0000 9995` |

## Optional: Stripe Tax

1. Activate Stripe Tax in Dashboard
2. `stripe.tax.calculations.create({ currency, customer_details, line_items })`
3. Use `taxCalculation.amount_total` as the PaymentIntent amount
4. Link to PaymentIntent: `hooks.inputs.tax.calculation = taxCalculation.id`

## Optional: Email receipts

Pass `receipt_email` in `confirmPayment.confirmParams`. Stripe sends email on success in live mode (not sandbox).

## Optional: Save payment method for future use

Set `setup_future_usage: 'off_session'` on PaymentIntent. To charge later:

```js
stripe.paymentIntents.create({
  customer: customerId,
  payment_method: paymentMethods.data[0].id,
  off_session: true,
  confirm: true,
  amount: 1099,
  currency: "usd",
})
```

## Key differences vs Checkout Elements

| | Payment Intents API | Checkout Elements (Sessions) |
| --- | --- | --- |
| Server creates | `PaymentIntent` | `Checkout Session` |
| Client provider | `Elements` from `@stripe/react-stripe-js` | `CheckoutElementsProvider` from `@stripe/react-stripe-js/checkout` |
| Client hooks | `useStripe()` + `useElements()` | `useCheckout()` |
| Confirm method | `stripe.confirmPayment()` | `checkout.confirm()` |
| Return page | `payment_intent_client_secret` URL param | `session_id` URL param |
| Built-in tax/shipping | Manual (Tax API) | Automatic (`automatic_tax`) |
| Effort | Most coding | Low coding |
