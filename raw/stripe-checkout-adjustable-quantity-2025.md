<!-- Source: Stripe Checkout — Make line item quantities adjustable -->
<!-- Fetched: 2026-04-20 -->

# Make line item quantities adjustable

Enable your customers to adjust the quantity of items during checkout.

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/adjustable-quantity?payment-ui=stripe-hosted.

The line items for each [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) keep track of what your customer is purchasing. You can configure the Checkout Session so customers can adjust line item quantities during checkout.

## Create a Checkout Session with an adjustable quantity

Set `adjustable_quantity` on your `line_items` when creating a Checkout Session to enable your customers to update the quantity of an item during checkout.

You can customize the default settings for the minimum and maximum quantities allowed by setting `adjustable_quantity.minimum` and `adjustable_quantity.maximum`. By default, an item’s minimum adjustable quantity is `0` and the maximum adjustable quantity is `99`. You can specify a value of up to `999999` for `adjustable_quantity.maximum`.

When using adjustable quantities with a `line_items[].quantity` value greater than `99` (the default adjustable maximum), set `adjustable_quantity.maximum` to be greater than or equal to that item’s quantity.

If you use adjustable quantities, change your configuration so that it uses `adjustable_quantity.maximum` when creating the Checkout Session to reserve inventory quantity instead of the `line_items` quantity.

Checkout prevents the customer from removing an item if it’s the only item remaining.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
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
        tax_behavior: "exclusive",
      },
      adjustable_quantity: {
        enabled: true,
        minimum: 1,
        maximum: 10,
      },
      quantity: 1,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  mode: "payment",
  success_url: "https://example.com/success",
});
```

## Handle completed transactions

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

# Embedded page

> This is a Embedded page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/adjustable-quantity?payment-ui=embedded-form.

The line items for each [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) keep track of what your customer is purchasing. You can configure the Checkout Session so customers can adjust line item quantities during checkout.

## Create a Checkout Session with an adjustable quantity

Set `adjustable_quantity` on your `line_items` when creating a Checkout Session to enable your customers to update the quantity of an item during checkout.

You can customize the default settings for the minimum and maximum quantities allowed by setting `adjustable_quantity.minimum` and `adjustable_quantity.maximum`. By default, an item’s minimum adjustable quantity is `0` and the maximum adjustable quantity is `99`. You can specify a value of up to `999999` for `adjustable_quantity.maximum`.

When using adjustable quantities with a `line_items[].quantity` value greater than `99` (the default adjustable maximum), set `adjustable_quantity.maximum` to be greater than or equal to that item’s quantity.

If you use adjustable quantities, change your configuration so that it uses `adjustable_quantity.maximum` when creating the Checkout Session to reserve inventory quantity instead of the `line_items` quantity.

Checkout prevents the customer from removing an item if it’s the only item remaining.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
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
        tax_behavior: "exclusive",
      },
      adjustable_quantity: {
        enabled: true,
        minimum: 1,
        maximum: 10,
      },
      quantity: 1,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  mode: "payment",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
});
```

## Handle completed transactions

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
