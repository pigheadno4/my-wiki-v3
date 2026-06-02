<!-- Source URL: https://docs.stripe.com/checkout/quickstart?ui=embedded-form -->
<!-- Fetched: 2026-04-20 -->

# Stripe Checkout Quickstart — Embedded page

Build a Checkout integration where customers pay through an embedded form on your website. An embeddable UI component displays the checkout page on your site.

**Supported frontends**: HTML, React, Next.js
**Supported backends**: Ruby, Node.js, PHP, Python, Go, .NET, Java

## Key Difference from Hosted Page

| | Hosted page | Embedded page |
| --- | --- | --- |
| `ui_mode` | *(default)* | `embedded_page` |
| Redirect | Customer leaves your site | Stays on your site |
| Return URL | `success_url` | `return_url` with `{CHECKOUT_SESSION_ID}` template |
| Client secret | Not needed client-side | Returned from server; used to mount Checkout |
| Return handling | Simple redirect page | Check session status via API; remount on failure |

## Step 1: Set up the server

### Install Stripe

```bash
npm install --save stripe
```

### Create a Checkout Session

Set `ui_mode: 'embedded_page'` and return `client_secret` (not a redirect).

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('sk_test_...');
const express = require('express');
const app = express();
app.use(express.static('public'));

const YOUR_DOMAIN = 'http://localhost:3000';

app.post('/create-checkout-session', async (req, res) => {
  const session = await stripe.checkout.sessions.create({
    ui_mode: 'embedded_page',
    customer_email: 'customer@example.com',
    submit_type: 'donate',
    billing_address_collection: 'auto',
    shipping_address_collection: {
      allowed_countries: ['US', 'CA'],
    },
    line_items: [
      {
        price: '{{PRICE_ID}}',
        quantity: 1,
      },
    ],
    mode: 'payment',
    return_url: `${YOUR_DOMAIN}/return?session_id={CHECKOUT_SESSION_ID}`,
    automatic_tax: { enabled: true },
    customer_creation: 'always',
    // customer: '{{CUSTOMER_ID}}'
  });

  res.send({ clientSecret: session.client_secret });
});

// Endpoint to retrieve session status for return page
app.get('/session-status', async (req, res) => {
  const session = await stripe.checkout.sessions.retrieve(req.query.session_id);

  res.send({
    status: session.status,
    customer_email: session.customer_details.email,
  });
});

app.listen(4242, () => console.log('Running on port 4242'));
```

## Step 2: Mount Checkout (React)

Install React Stripe.js for PCI compliance — payment details go directly to Stripe:

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

```jsx
import React, { useCallback } from "react";
import { loadStripe } from '@stripe/stripe-js';
import {
  EmbeddedCheckoutProvider,
  EmbeddedCheckout
} from '@stripe/react-stripe-js';

// Call loadStripe outside component render to avoid recreating Stripe object
const stripePromise = loadStripe("pk_test_...");

const CheckoutForm = () => {
  const fetchClientSecret = useCallback(() => {
    return fetch("/create-checkout-session", { method: "POST" })
      .then((res) => res.json())
      .then((data) => data.clientSecret);
  }, []);

  return (
    <div id="checkout">
      <EmbeddedCheckoutProvider stripe={stripePromise} options={{ fetchClientSecret }}>
        <EmbeddedCheckout />
      </EmbeddedCheckoutProvider>
    </div>
  );
};
```

## Step 3: Show a return page

Handle session status on the return page:

- **`complete`**: payment succeeded → show success
- **`open`**: payment failed/canceled → redirect back to `/checkout` to remount

```jsx
import React, { useState, useEffect } from "react";
import { Navigate } from "react-router-dom";

const Return = () => {
  const [status, setStatus] = useState(null);
  const [customerEmail, setCustomerEmail] = useState('');

  useEffect(() => {
    const sessionId = new URLSearchParams(window.location.search).get('session_id');

    fetch(`/session-status?session_id=${sessionId}`)
      .then((res) => res.json())
      .then((data) => {
        setStatus(data.status);
        setCustomerEmail(data.customer_email);
      });
  }, []);

  if (status === 'open') return <Navigate to="/checkout" />;

  if (status === 'complete') {
    return (
      <section id="success">
        <p>
          We appreciate your business! A confirmation email will be sent to {customerEmail}.
        </p>
      </section>
    );
  }

  return null;
};
```

## Step 4: Test

Start server: `npm start` → go to `http://localhost:3000/checkout`

### Test cards

| Card | Scenario |
| --- | --- |
| 4242 4242 4242 4242 | Payment succeeds |
| 4000 0025 0000 3155 | Requires 3DS authentication |
| 4000 0000 0000 9995 | Payment is declined |

## Key Parameters (same as hosted page, plus)

- `ui_mode: 'embedded_page'` — renders embedded form instead of redirecting
- `return_url` — use `{CHECKOUT_SESSION_ID}` template variable; Stripe replaces before redirect
- Server returns `clientSecret` (not a redirect URL)
- `/session-status` endpoint required to check `session.status` and `session.customer_details.email`

## Next Steps

- Fulfill orders via `checkout.session.completed` webhook (most reliable)
- Receive payouts to bank account
- Refunds via API or Dashboard
- Customer self-management portal
