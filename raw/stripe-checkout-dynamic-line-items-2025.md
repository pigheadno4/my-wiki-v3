<!-- Source URL: https://docs.stripe.com/payments/checkout/dynamically-update-line-items -->
<!-- Fetched: 2026-04-21 -->

# Dynamically update line items

Learn how to modify pricing and the contents of a cart during checkout.

Learn how to dynamically add, remove, or update line items included in a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/object.md).

### Use cases

This guide demonstrates how to update line items to upsell a subscription, but you can also:

- **Check inventory**: Run inventory checks and holds when customers attempt to change item quantities.
- **Add new products**: Add a complimentary product if the order total exceeds a specific amount.
- **Update shipping rates**: If the order total changes, update shipping rates by combining the method described in this guide with what’s out on [Customize shipping options during checkout](https://docs.stripe.com/payments/checkout/custom-shipping-options.md).
- **Update tax rates**: If you’re not using [Stripe Tax](https://docs.stripe.com/tax/checkout.md), you can dynamically update [tax rates](https://docs.stripe.com/billing/taxes/collect-taxes.md?tax-calculation=tax-rates#adding-tax-rates-to-checkout) on line items based on the shipping address entered.

> #### Payment Intents API
>
> If you use the Payment Intents API, you must manually track line item updates and modify the payment amount, or by creating a new PaymentIntent with adjusted amounts.

## Set up the SDK [Server-side]

Use our official libraries to access the Stripe API from your application:

#### Ruby

```bash
gem install stripe -v 15.1.0
```

## Update the server SDK [Server-side]

To use this feature, ensure your SDK version is `2025-03-31.basil` or later.

#### Node

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  apiVersion: "2025-03-31.basil",
});
```

## Create a Checkout Session [Server-side]

```node
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  ui_mode: "elements",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  return_url: "https://example.com/return",
});
```

## Dynamically update line items [Server-side]

Create an endpoint on your server to update the line items on the Checkout Session. You’ll call this from the front end in a later step.

> Client-side code runs in an environment that’s controlled by the user. A malicious user can bypass your client-side validation, intercept and modify requests, or create new requests to your server.

When creating an endpoint, we recommend the following:

- Create endpoints for specific customer interactions instead of making them generic. For example, “add cross-sell items” instead of a general “update” action. Specific endpoints can help with writing and maintaining validation logic.
- Don’t pass [session data](https://docs.stripe.com/js/custom_checkout/session_object) directly from the client to your endpoint. Malicious clients can modify request data, making it an unreliable source for determining the Checkout Session state. Instead, pass the [session ID](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-id) to your server and use it to securely retrieve the data from the Stripe API.

#### Node

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  apiVersion: "2025-03-31.basil",
});

const express = require("express");
const bodyParser = require("body-parser");
const app = express();
app.use(bodyParser.json());

const MONTHLY_PRICE_ID = "{{MONTHLY_PRICE}}";
const YEARLY_PRICE_ID = "{{YEARLY_PRICE}}";

app.post("/change-subscription-interval", async (req, res) => {
  const { checkout_session_id, interval } = req.body;

  if (
    !checkout_session_id ||
    (interval !== "yearly" && interval !== "monthly")
  ) {
    return res.status(400).json({
      type: "error",
      message: "We couldn't process your request. Please try again later.",
    });
  }

  try {
    // 1. Create the new line items for the Checkout Session.
    const newPrice = interval === "yearly" ? YEARLY_PRICE_ID : MONTHLY_PRICE_ID;
    const lineItems = [
      {
        price: newPrice,
        quantity: 1,
      },
    ];

    // 2. Update the Checkout Session with the new line items.
    await stripe.checkout.sessions.update(checkout_session_id, {
      line_items: lineItems,
    });

    // 3. Return a success response.
    return res.json({ type: "success" });
  } catch (err) {
    if (err.type === "StripeInvalidRequestError") {
      // Handle Stripe errors with a generic error message
      return res.status(400).json({
        type: "error",
        message: "We couldn't process your request. Please try again later.",
      });
    }

    // Handle unexpected errors
    return res.status(500).json({
      type: "error",
      message: "Something went wrong on our end. Please try again later.",
    });
  }
});

app.listen(4242, () => console.log("Server is running on port 4242"));
```

When updating line items, you must retransmit the entire array of line items.

- To keep an existing line item, specify its `id`.
- To update an existing line item, specify its `id` along with the new values of the fields to update.
- To add a new line item, specify a `price` and `quantity` without an `id`.
- To remove an existing line item, omit the line item’s ID from the retransmitted array.
- To reorder a line item, specify its `id` at the desired position in the retransmitted array.

## Update the client SDK [Client-side]

#### HTML + JS

Initialize Stripe.js.

```javascript
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

#### React

Initialize the `stripe` instance.

```javascript
import { loadStripe } from "@stripe/stripe-js";
const stripe = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");
```

## Request server updates [Client-side]

#### HTML + JS

From your front end, create a function to send an update request to your server and wrap it in [runServerUpdate](https://docs.stripe.com/js/custom_checkout/run_server_update). A successful request updates the [Session](https://docs.stripe.com/js/custom_checkout/session_object) object with the new line items.

`runServerUpdate` enforces a 20-second timeout for your update function. If your function doesn’t resolve within 20 seconds, `runServerUpdate` returns an error. Wrap `runServerUpdate` calls in `try`/`catch` blocks to handle any errors, and record metrics to diagnose timeouts and other failures.

```html
<button id="change-subscription-interval" role="switch" aria-checked="false">
  Save with a yearly subscription
</button>
```

```javascript
document
  .getElementById("change-subscription-interval")
  .addEventListener("click", async (event) => {
    const button = event.target;
    const isCurrentSubscriptionMonthly =
      button.getAttribute("aria-checked") === "false";

    const updateCheckout = () => {
      return fetch("/change-subscription-interval", {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify({
          checkout_session_id: actions.getSession().id,
          interval: isCurrentSubscriptionMonthly ? "yearly" : "monthly",
        }),
      });
    };

    try {
      const response = await checkout.runServerUpdate(updateCheckout);
      if (!response.ok) {
        // Handle error state
        return;
      }
    } catch (error) {
      // Handle promise rejection (for example, timeouts)
      return;
    }

    // Update toggle state on success
    const isNewSubscriptionMonthly = !isCurrentSubscriptionMonthly;
    button.setAttribute("aria-checked", !isNewSubscriptionMonthly);
    button.textContent =
      isNewSubscriptionMonthly ?
        "Save with a yearly subscription"
      : "Use monthly subscription";
  });
```

#### React

From your front end, send an update request to your server and wrap it in [runServerUpdate](https://docs.stripe.com/js/custom_checkout/run_server_update). A successful request updates the [Session](https://docs.stripe.com/js/custom_checkout/session_object) object with the new line items.

`runServerUpdate` enforces a 20-second timeout for your update function. If your function doesn’t resolve within 20 seconds, `runServerUpdate` returns an error. Wrap `runServerUpdate` calls in `try`/`catch` blocks to handle any errors, and record metrics to diagnose timeouts and other failures.

```jsx
import React from "react";
import { useCheckout } from "@stripe/react-stripe-js/checkout";

const ChangeSubscriptionInterval = () => {
  const [isSubscriptionMonthly, setIsSubscriptionMonthly] =
    React.useState(false);
  const checkoutState = useCheckout();

  if (checkoutState.type === "loading") {
    return <div>Loading...</div>;
  } else if (checkoutState.type === "error") {
    return <div>Error: {checkoutState.error.message}</div>;
  }
  const { runServerUpdate, id } = checkoutState.checkout;

  const updateCheckout = () =>
    fetch("/change-subscription-interval", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify({
        checkout_session_id: id,
        interval: isSubscriptionMonthly ? "yearly" : "monthly",
      }),
    });

  const handleClick = async () => {
    try {
      const response = await runServerUpdate(updateCheckout);
      if (!response.ok) {
        // Handle error state
        return;
      }
    } catch (error) {
      // Handle promise rejection (for example, timeouts)
      return;
    }

    // Update toggle state on success
    setIsSubscriptionMonthly(!isSubscriptionMonthly);
  };
  return (
    <button
      onClick={handleClick}
      role="switch"
      aria-checked={!isSubscriptionMonthly}
    >
      {isSubscriptionMonthly ?
        "Save with a yearly subscription"
      : "Return to a monthly subscription"}
    </button>
  );
};
```
