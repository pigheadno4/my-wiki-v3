<!-- Source URL: https://docs.stripe.com/checkout/quickstart -->
<!-- Fetched: 2026-04-20 -->

# Stripe Checkout Quickstart — Stripe-hosted page

Build a Checkout integration where customers click a button and get redirected to a payment page hosted by Stripe.

**Supported frontends**: HTML, React, Next.js
**Supported backends**: Ruby, Node.js, PHP, Python, Go, .NET, Java

## Step 1: Set up the server

### Install the Stripe Node library

```bash
npm install --save stripe
```

### Create a Checkout Session

Add an endpoint on your server that creates a Checkout Session. A Checkout Session controls what your customer sees on the payment page — line items, order amount, currency, and acceptable payment methods.

**Key parameters:**

- **`line_items`**: products to charge (use predefined `price` ID or inline `price_data`)
- **`mode`**: `payment` (one-time) | `subscription` (recurring) | `setup` (future payments)
- **`success_url`**: publicly accessible redirect URL after successful payment
- **`customer_email`**: prefills customer email
- **`submit_type`**: controls submit button copy — 4 options (e.g. `donate`)
- **`billing_address_collection`**: `auto` or `required`
- **`shipping_address_collection.allowed_countries`**: ISO country codes
- **`automatic_tax.enabled`**: true for Stripe Tax
- **`customer_creation`**: `always` to always create a Customer object
- **`customer`**: existing Customer ID to associate with the session

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require('stripe')('sk_test_...');
const express = require('express');
const app = express();
app.use(express.static('public'));

const YOUR_DOMAIN = 'http://localhost:4242';

app.post('/create-checkout-session', async (req, res) => {
  const session = await stripe.checkout.sessions.create({
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
    success_url: `${YOUR_DOMAIN}?success=true`,
    automatic_tax: { enabled: true },
    customer_creation: 'always',
    // customer: '{{CUSTOMER_ID}}'
  });

  res.redirect(303, session.url);
});

app.listen(4242, () => console.log('Running on port 4242'));
```

## Step 2: Build your checkout

### Add an order preview page

Add a page to show a preview of the customer's order before they're sent to Checkout. Once redirected to Checkout, the order is final and can't be modified without creating a new Checkout Session.

### Add a checkout button (React example)

```jsx
import React, { useState, useEffect } from "react";

const ProductDisplay = () => (
  <section>
    <div className="product">
      <img
        src="https://i.imgur.com/EHyR2nP.png"
        alt="The cover of Stubborn Attachments"
      />
      <div className="description">
        <h3>Stubborn Attachments</h3>
        <h5>$20.00</h5>
      </div>
    </div>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </section>
);

const Message = ({ message }) => (
  <section>
    <p>{message}</p>
  </section>
);

export default function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    // Check to see if this is a redirect back from Checkout
    const query = new URLSearchParams(window.location.search);

    if (query.get("success")) {
      setMessage("Order placed! You will receive an email confirmation.");
    }

    if (query.get("canceled")) {
      setMessage(
        "Order canceled -- continue to shop around and checkout when you're ready."
      );
    }
  }, []);

  return message ? <Message message={message} /> : <ProductDisplay />;
}
```

## Step 3: Test your page

Add `"proxy": "http://localhost:4242"` to `package.json` for local development.

Start server: `npm start` → go to `http://localhost:3000/checkout`

### Test cards

| Card number | Scenario |
| --- | --- |
| 4242 4242 4242 4242 | Payment succeeds |
| 4000 0025 0000 3155 | Requires 3DS authentication |
| 4000 0000 0000 9995 | Payment is declined |

## Customer handling

- By default, Checkout only creates `Customer` objects when required (e.g. subscriptions); otherwise uses guest customers
- `customer_creation: 'always'` — always creates a Customer
- Pass `customer: '{{CUSTOMER_ID}}'` to associate with an existing customer
- Accounts v2: pass `customer_account` field instead

## Next steps

- **Fulfill orders**: set up event destination for `checkout.session.completed`
- **Receive payouts**: move funds to bank account
- **Refunds**: via API or Dashboard
- **Customer management**: self-manage payment details, invoices, subscriptions
- **Adaptive Pricing**: auto-present prices in local currency
