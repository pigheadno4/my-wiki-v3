<!-- Source URL: https://docs.stripe.com/billing/quickstart -->
<!-- Fetched: 2026-05-12 -->
<!-- Note: Content formatted from structured UI quickstart (not raw markdown paste) -->
<!-- Frontend: HTML / React — Backend: Ruby / Node.js / PHP / Python / Go / .NET / Java -->

# Prebuilt subscription page with Stripe Checkout

Get started with our sample app to run a full, working subscription integration using Stripe Billing and Stripe Checkout.

The sample app demonstrates redirecting your customers from your site to a prebuilt payment page hosted on Stripe. The Stripe Billing APIs create and manage subscriptions, invoices, and recurring payments, while Checkout provides the prebuilt, secure, Stripe-hosted UI for collecting payment details.

You can model customers in your integration either as customer-configured Account objects using the Accounts v2 API (recommended in most cases) or as Customer objects using the Customers v1 API.

## Step 1: Set up products, pricing, and payment methods

### Add your products and prices

Create new Products and Prices to use in this sample.

### Add features to your product

Create features (such as an annual birthday gift) and associate them with your subscription to entitle new subscribers to them. Listen to the `active entitlements summary` events for your event destination, and use the list active entitlements API for a given customer to fulfill entitlements.

### (Optional) Enable payment methods

Use your Dashboard to enable supported payment methods in addition to cards. Checkout dynamically displays your enabled payment methods in order of relevance, based on the customer's location and other characteristics.

## Step 2: Build your subscription page

### Add a pricing preview page

Add a page that displays your product and allows customers to subscribe. Clicking Checkout redirects them to a Stripe-hosted Checkout page (prevents further modification).

Consider embedding a pricing table to dynamically display pricing information through the Dashboard.

### Add a checkout button

The button redirects the customer to the Stripe-hosted payment page and uses the product's `lookup_key` to retrieve the `price_id` from the server.

### Add a success page

Create a success page for order confirmation. Associate it with the Checkout Session `success_url`.

### Add a customer portal button and redirect

Add a button to redirect to the customer portal. Make a request to your server endpoint to redirect to a new customer portal session. Use `session_id` from Checkout to retrieve `customer_id`. In production, store this value alongside the authenticated user in your database.

## Step 3: Call the Stripe API

### Install the Stripe Node library

```bash
npm install --save stripe
```

### Create a Checkout Session

- Pass `lookup_key` to `stripe.prices.list()` to get the `price_id`
- Set `mode: 'subscription'`
- Set `success_url` with `{CHECKOUT_SESSION_ID}` template variable
- Optional: `subscription_data.trial_period_days`, `subscription_data.billing_cycle_anchor`, `automatic_tax: { enabled: true }`
- Redirect to `session.url` with HTTP 303

### Create a customer portal session

Use `stripe.checkout.sessions.retrieve(session_id)` to get `customer_id`, then create portal session and redirect.

### Fulfill the subscription (webhook)

Create a `/webhook` endpoint. Listen for subscription events:

- `customer.subscription.trial_will_end`
- `customer.subscription.deleted`
- `customer.subscription.created`
- `customer.subscription.updated`
- `entitlements.active_entitlement_summary.updated`

Use `stripe.webhooks.constructEvent(body, signature, endpointSecret)` for signature verification.

## Step 4: Test your page

```bash
npm start
# Opens http://localhost:3000/checkout
```

Test cards:
- Payment succeeds: `4242 4242 4242 4242`
- Requires 3DS: `4000 0025 0000 3155`
- Payment declined: `4000 0000 0000 9995`

## Optional customizations

- **Trial period**: `subscription_data.trial_period_days` (min 1); set `trial_settings[end_behavior][missing_payment_method]` to `pause` or `cancel` for free trials without payment method
- **Billing cycle anchor**: `subscription_data.billing_cycle_anchor` (Unix timestamp)
- **Automatic tax**: `automatic_tax: { enabled: true }` (activate Stripe Tax in Dashboard first)

## Client code (React)

```jsx
import React, { useState, useEffect } from 'react';
import './App.css';

const ProductDisplay = () => (
  <section>
    <div className="product">
      <Logo />
      <div className="description">
        <h3>Starter Plan</h3>
        <h5>$20.00 / month</h5>
      </div>
    </div>
    <form action="/create-checkout-session" method="POST">
      {/* Add a hidden field with the lookup_key of your Price */}
      <input type="hidden" name="lookup_key" value="{{PRICE_LOOKUP_KEY}}" />
      <button id="checkout-and-portal-button" type="submit">
        Checkout
      </button>
    </form>
  </section>
);

const SuccessDisplay = ({ sessionId }) => {
  return (
    <section>
      <div className="product Box-root">
        <Logo />
        <div className="description Box-root">
          <h3>Subscription to Starter Plan successful!</h3>
        </div>
      </div>
      <form action="/create-portal-session" method="POST">
        <input
          type="hidden"
          id="session-id"
          name="session_id"
          value={sessionId}
        />
        <button id="checkout-and-portal-button" type="submit">
          Manage your billing information
        </button>
      </form>
    </section>
  );
};

const Message = ({ message }) => (
  <section>
    <p>{message}</p>
  </section>
);

export default function App() {
  let [message, setMessage] = useState('');
  let [success, setSuccess] = useState(false);
  let [sessionId, setSessionId] = useState('');

  useEffect(() => {
    const query = new URLSearchParams(window.location.search);

    if (query.get('success')) {
      setSuccess(true);
      setSessionId(query.get('session_id'));
    }

    if (query.get('canceled')) {
      setSuccess(false);
      setMessage(
        "Order canceled -- continue to shop around and checkout when you're ready."
      );
    }
  }, [sessionId]);

  if (!success && message === '') {
    return <ProductDisplay />;
  } else if (success && sessionId !== '') {
    return <SuccessDisplay sessionId={sessionId} />;
  } else {
    return <Message message={message} />;
  }
}
```

## Server code (Node.js)

```javascript
// This is a public sample test API key.
// Don't submit any personally identifiable information in requests made with this key.
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('sk_test_Ou1w6LVt3zmVipDVJsvMeQsc');
const express = require('express');
const app = express();
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

const YOUR_DOMAIN = "http://localhost:3000";

app.post('/create-checkout-session', async (req, res) => {
  const prices = await stripe.prices.list({
    lookup_keys: [req.body.lookup_key],
    expand: ['data.product'],
  });
  const session = await stripe.checkout.sessions.create({
    billing_address_collection: 'auto',
    line_items: [
      {
        price: prices.data[0].id,
        quantity: 1,
      },
    ],
    mode: 'subscription',
    success_url: `${YOUR_DOMAIN}/?success=true&session_id={CHECKOUT_SESSION_ID}`,
    subscription_data: {
      trial_period_days: 7,
      billing_cycle_anchor: 1672531200,
    },
    automatic_tax: { enabled: true },
  });

  res.redirect(303, session.url);
});

app.post('/create-portal-session', async (req, res) => {
  const { session_id } = req.body;
  const checkoutSession = await stripe.checkout.sessions.retrieve(session_id);

  res.redirect(303, portalSession.url);
});

app.post(
  '/webhook',
  express.raw({ type: 'application/json' }),
  (request, response) => {
    let event = request.body;
    const endpointSecret = 'whsec_12345';
    if (endpointSecret) {
      const signature = request.headers['stripe-signature'];
      try {
        event = stripe.webhooks.constructEvent(
          request.body,
          signature,
          endpointSecret
        );
      } catch (err) {
        console.log(`⚠️  Webhook signature verification failed.`, err.message);
        return response.sendStatus(400);
      }
    }
    let subscription;
    let status;
    switch (event.type) {
      case 'customer.subscription.trial_will_end':
        subscription = event.data.object;
        status = subscription.status;
        console.log(`Subscription status is ${status}.`);
        break;
      case 'customer.subscription.deleted':
        subscription = event.data.object;
        status = subscription.status;
        console.log(`Subscription status is ${status}.`);
        break;
      case 'customer.subscription.created':
        subscription = event.data.object;
        status = subscription.status;
        console.log(`Subscription status is ${status}.`);
        break;
      case 'customer.subscription.updated':
        subscription = event.data.object;
        status = subscription.status;
        console.log(`Subscription status is ${status}.`);
        break;
      case 'entitlements.active_entitlement_summary.updated':
        subscription = event.data.object;
        console.log(`Active entitlement summary updated for ${subscription}.`);
        break;
      default:
        console.log(`Unhandled event type ${event.type}.`);
    }
    response.send();
  }
);

app.listen(4242, () => console.log('Running on port 4242'));
```
