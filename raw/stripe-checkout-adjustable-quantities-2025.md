<!-- Source URL: https://docs.stripe.com/payments/checkout/adjustable-quantity -->
<!-- Fetched: 2026-04-21 -->

# Make line item quantities adjustable

Learn how to allow your customers to adjust the quantity of items during checkout.

The line items for each [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) keep track of what your customer is purchasing. You can configure the Checkout Session so customers can adjust line item quantities during checkout.

> #### Payment Intents API
>
> If you use the Payment Intents API, you must manually track line item updates and modify the payment amount, or by creating a new PaymentIntent with adjusted amounts.

## Enable adjustable quantities [Server-side]

> Other line item updates, such as adding new line items, aren’t supported for this integration.

Set [adjustable_quantity](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-adjustable_quantity) on your [line_items](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items) when creating a Checkout Session to allow your customers to update the quantity of an item during checkout.

```node
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

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
      adjustable_quantity: {
        enabled: true,
        maximum: 100,
        minimum: 0,
      },
    },
  ],
  mode: "payment",
  ui_mode: "elements",
  return_url: "{{RETURN_URL}}",
});
```

You can customize the default settings for the minimum and maximum quantities allowed by setting [adjustable_quantity.minimum](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-adjustable_quantity-minimum) and [adjustable_quantity.maximum](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-adjustable_quantity-maximum). By default, an item’s minimum adjustable quantity is 0 and the maximum adjustable quantity is 99. You can specify a value of up to 999999 for `adjustable_quantity.maximum`.

Checkout prevents the customer from removing an item if it’s the only item remaining.

## Update line item quantities [Client-side]

Use [updateLineItemQuantity](https://docs.stripe.com/js/custom_checkout/update_line_item_quantity) to change a line item’s quantity in response to customer interaction, such as a button to increment the quantity. Pass the [line item ID](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-lineItems-id) and the new quantity:

#### HTML + JS

```html
<button class="increment-quantity-button" data-line-item="{{line item ID}}">
  +
</button>
```

```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret });
const button = document.querySelector(".increment-quantity-button");
const lineItem = button.getAttribute("data-line-item");
checkout.loadActions().then((loadActionsResult) => {
  if (loadActionsResult.type === "success") {
    const { actions } = loadActionsResult;
    const session = loadActionsResult.getSession();
    const quantity = session.lineItems.find(
      (li) => li.id === lineItem,
    ).quantity;
    button.addEventListener("click", () => {
      actions.updateLineItemQuantity({
        lineItem,
        quantity: quantity + 1,
      });
    });
  } else {
    const { error } = loadActionsResult;
  }
});
```

#### React

```jsx
import React from "react";
import { useCheckout } from "@stripe/react-stripe-js/checkout";

const IncrementLineItemButton = (props) => {
  const checkoutState = useCheckout();
  if (checkoutState.type === "loading") {
    return <div>Loading...</div>;
  } else if (checkoutState.type === "error") {
    return <div>Error: {checkoutState.error.message}</div>;
  }
  const { updateLineItemQuantity } = checkoutState.checkout;

  const handleClick = () => {
    updateLineItemQuantity({
      lineItem: props.lineItem,
      quantity: props.quantity + 1,
    });
  };
  return <button onClick={handleClick}>+</button>;
};

export default IncrementLineItemButton;
```

## Handle completed transactions [Server-side]

After the payment completes, you can make a request for the finalized [line items](https://docs.stripe.com/api/checkout/sessions/line_items.md) and their quantities. If your customer removes a line item, it’s also removed from the line items response. See the [Fulfillment guide](https://docs.stripe.com/checkout/fulfillment.md) to learn how to create an event handler to handle completed Checkout Sessions.

> To test your event handler, [install the Stripe CLI](https://docs.stripe.com/stripe-cli.md) and use `stripe listen --forward-to localhost:4242/webhook` to [forward events to your local server](https://docs.stripe.com/webhooks.md#test-webhook).

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = "whsec_...";

// Using Express
const app = require("express")();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require("body-parser");

const fulfillOrder = (session, lineItems) => {
  // TODO: Remove error and implement...
  throw new Error(`
    Given the Checkout Session ${session.id}, load your internal order from the database here.
    Then you can reconcile your order's quantities with the final line item quantity purchased. You can use \`checkout_session.metadata\` and \`price.metadata\` to store and later reference your internal order and item ids.`);
};

app.post(
  "/webhook",
  bodyParser.raw({ type: "application/json" }),
  (request, response) => {
    const payload = request.body;
    const sig = request.headers["stripe-signature"];

    let event;

    try {
      event = stripe.webhooks.constructEvent(payload, sig, endpointSecret);
    } catch (err) {
      return response.status(400).send(`Webhook Error: ${err.message}`);
    }

    // Handle the checkout.session.completed event
    if (event.type === "checkout.session.completed") {
      const session = event.data.object;

      stripe.checkout.sessions.listLineItems(
        session.id,
        { limit: 100 },
        function (err, lineItems) {
          // Fulfill the purchase...
          try {
            fulfillOrder(session, lineItems);
          } catch (err) {
            return response
              .status(400)
              .send(`Fulfillment Error: ${err.message}`);
          }
        },
      );
    }

    response.status(200).end();
  },
);

app.listen(4242, () => console.log("Running on port 4242"));
```
