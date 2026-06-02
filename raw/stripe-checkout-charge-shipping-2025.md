<!-- Source: Stripe Checkout — Charge for shipping -->
<!-- Fetched: 2026-04-20 -->

# Charge for shipping

Create different shipping rates for your customers.

Shipping rates let you display various shipping options—like standard, express, and overnight—with more accurate delivery estimates. Charge your customer for shipping using different Stripe products. Before you create a shipping rate, learn how to [collect billing and shipping addresses](https://docs.stripe.com/payments/collect-addresses.md).

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/during-payment/charge-shipping?payment-ui=stripe-hosted.

## Create a shipping rate [Dashboard] [Server-side]

Shipping rates only support fixed amount values for the entire order. You can’t adjust the shipping rate based on the number of items in the order.

#### Dashboard

To add a [shipping rate](https://dashboard.stripe.com/test/shipping-rates) using the Dashboard:

1. Click **Create shipping rate**.
1. Enter an amount, a description, and an optional delivery estimate.
1. Click **Save**, and copy the shipping rate ID (`shr_123456`).
   ![](assets/stripe-checkout-shipping-rate-dashboard.png)

Enter your shipping rate details

### Update a shipping rate

You can’t update an amount of a currency that’s already been set on a shipping rate. After you set a currency and amount on a shipping rate, it can only be updated to include new currencies. To update a shipping rate in the Dashboard, you must archive the shipping rate and then create a new one.

### Archive a shipping rate

To archive a shipping rate:

1. On the [Shipping rates](https://dashboard.stripe.com/test/shipping-rates) tab, select the applicable shipping rate.
1. Click the overflow menu ⋯, and select **Archive**.

To unarchive the shipping rate, click the overflow menu ⋯, and select **Unarchive shipping rate**.

#### API

> #### Interested in dynamic shipping rate updates?
>
> Checkout supports letting you dynamically update shipping rates based on the address your customer provides or the value of the order. See [Dynamically customize shipping options](https://docs.stripe.com/payments/checkout/custom-shipping-options.md) about this preview feature.

[Create a shipping rate](https://docs.stripe.com/api/shipping_rates.md), which at a minimum, requires the `type` and `display_name` parameters. The following code sample uses both of these parameters along with `fixed_amount` and `delivery_estimate` to create a shipping rate:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const shippingRate = await stripe.shippingRates.create({
  display_name: "Ground shipping",
  type: "fixed_amount",
  fixed_amount: {
    amount: 500,
    currency: "usd",
  },
  delivery_estimate: {
    minimum: {
      unit: "business_day",
      value: 5,
    },
    maximum: {
      unit: "business_day",
      value: 7,
    },
  },
});
```

### Update a shipping rate

To [update a shipping rate](https://docs.stripe.com/api/shipping_rates/update.md), call `Stripe::ShippingRate.update`, and update the parameters as needed.

## Create a Checkout Session [Server-side]

To create a Checkout Session that includes your shipping rate, pass in the generated shipping rate ID to the [shipping_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_options) parameter. If you want to create the shipping rate at the same time as a Checkout Session, use the `shipping_rate_data` parameter with `shipping_options`. Only Checkout Sessions in [payment mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode) support shipping options.

The following code sample adds two shipping options to the Checkout Session:

- Free shipping, with an estimated delivery of 5-7 business days.
- Next day air, at a cost of 15.00 USD, with an estimated delivery of exactly 1 business day.

In this example, the first option in the `shipping_options` array is pre-selected for the customer on the checkout page. However, customers can choose either option.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  shipping_address_collection: {
    allowed_countries: ["US", "CA"],
  },
  shipping_options: [
    {
      shipping_rate_data: {
        type: "fixed_amount",
        fixed_amount: {
          amount: 0,
          currency: "usd",
        },
        display_name: "Free shipping",
        delivery_estimate: {
          minimum: {
            unit: "business_day",
            value: 5,
          },
          maximum: {
            unit: "business_day",
            value: 7,
          },
        },
      },
    },
    {
      shipping_rate_data: {
        type: "fixed_amount",
        fixed_amount: {
          amount: 1500,
          currency: "usd",
        },
        display_name: "Next day air",
        delivery_estimate: {
          minimum: {
            unit: "business_day",
            value: 1,
          },
          maximum: {
            unit: "business_day",
            value: 1,
          },
        },
      },
    },
  ],
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
  success_url: "https://example.com/success",
});
```

If successful, the shipping selector appears in your checkout flow:
![The shipping selector in the checkout flow](assets/stripe-checkout-shipping-selector.jpg)

The shipping selector in the checkout flow

## Optional: Handle completed transactions

After the payment succeeds, you can retrieve the shipping amount in the [amount_total](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-amount_total) attribute of the [shipping_cost](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-shipping_cost). You can also retrieve the selected shipping rate using the `shipping_rate` attribute in `shipping_cost`. To access the `shipping_cost` property, you must [create an event handler](https://docs.stripe.com/checkout/fulfillment.md#create-payment-event-handler) to handle completed Checkout Sessions. You can test a handler by [installing the Stripe CLI](https://docs.stripe.com/stripe-cli.md) and using `stripe listen --forward-to localhost:4242/webhook` to [forward events to your local server](https://docs.stripe.com/webhooks.md#test-webhook). In the following code sample, the handler allows for the user to access the `shipping_property`:

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

const fulfillOrder = async (session) => {
  const selectedShippingRate = await stripe.shippingRates.retrieve(
    session.shipping_cost.shipping_rate,
  );
  const shippingTotal = session.shipping_cost.amount_total;

  // TODO: Remove error and implement...
  throw new Error(`
    Given the Checkout Session ${session.id}, load your internal order from the database then implement your own fulfillment logic.`);
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

      // Fulfill the purchase...
      fulfillOrder(session);
    }

    response.status(200).end();
  },
);

app.listen(4242, () => console.log("Running on port 4242"));
```

## Optional: Define a delivery estimate

You can configure shipping rates using a number of delivery estimate combinations. The following table contains some examples of plain English delivery estimates, and their corresponding `delivery_estimate.minimum` and `delivery_estimate.maximum` values:

| Delivery Estimate | Minimum | Maximum |
| ----------------- | ------- | ------- |
| 1 day             | ```es6  |

{
unit: 'day',
value: 1,
}
`         |`es6
{
unit: 'day',
value: 1,
}

````|
| 1 business day             | ```es6
{
  unit: 'business_day',
  value: 1,
}
``` | ```es6
{
  unit: 'business_day',
  value: 1,
}
``` |
| At least 2 business days   | ```es6
{
  unit: 'business_day',
  value: 2,
}
``` | ```es6
null
```                                          |
| 3 to 7 days                | ```es6
{
  unit: 'day',
  value: 3,
}
```          | ```es6
{
  unit: 'day',
  value: 7,
}
```          |
| 4 to 8 hours               | ```es6
{
  unit: 'hour',
  value: 4,
}
```         | ```es6
{
  unit: 'hour',
  value: 8,
}
```         |
| 4 hours to 2 business days | ```es6
{
  unit: 'hour',
  value: 4,
}

```      | ```es6
{
  unit: 'business_day',
  value: 2,
}
``` |

## Optional: Charge tax for shipping

You can use [Stripe Tax](https://docs.stripe.com/tax/checkout.md) to automatically calculate tax on shipping fees by setting a `tax_code` and `tax_behavior` on your shipping rate. Stripe Tax automatically determines whether shipping is taxable ([as taxability varies by state and country](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#shipping-tax-code)) and applies the correct tax rate if so.

When creating a shipping rate with `shipping_rate_data` or through [Create a Shipping Rate](https://docs.stripe.com/api/shipping_rates/create.md), you can add a `tax_behavior` and `tax_code` parameter to the shipping rate.

We recommend setting the `tax_code` to `Shipping` (`txcd_92010001`) to make sure that you always charge the correct tax. You can also set the shipping rate `tax_code` to `Nontaxable` (`txcd_00000000`) if you don’t want to charge tax.

For this example, we set the `tax_behavior` to `exclusive`, which is common in the US. Learn more about [tax behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#tax-behavior).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
billing_address_collection: 'required',
shipping_address_collection: {
  allowed_countries: ['US', 'CA'],
},
shipping_options: [
  {
    shipping_rate_data: {
      type: 'fixed_amount',
      fixed_amount: {
        amount: 0,
        currency: 'usd',
      },
      display_name: 'Free shipping',
      tax_behavior: 'exclusive',
      tax_code: 'txcd_92010001',
      delivery_estimate: {
        minimum: {
          unit: 'business_day',
          value: 5,
        },
        maximum: {
          unit: 'business_day',
          value: 7,
        },
      },
    },
  },
],
line_items: [
  {
    price_data: {
      currency: 'usd',
      product_data: {
        name: 'T-shirt',
      },
      unit_amount: 2000,
      tax_behavior: 'exclusive',
    },
    quantity: 1,
  },
],
automatic_tax: {
  enabled: true,
},
mode: 'payment',
success_url: 'https://example.com/success',
});
````

Your customer can see the calculated tax amount for the shipping rate factored into the total sales tax in your checkout flow:
![Calculated tax amount for the shipping rate on the checkout page](assets/stripe-checkout-taxed-shipping.jpg)

Calculated tax amount for the shipping rate in the checkout flow

# Embedded page

> This is a Embedded page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/during-payment/charge-shipping?payment-ui=embedded-form.

## Create a shipping rate [Dashboard] [Server-side]

Shipping rates only support fixed amount values for the entire order. You can’t adjust the shipping rate based on the number of items in the order.

#### Dashboard

To add a [shipping rate](https://dashboard.stripe.com/test/shipping-rates) using the Dashboard:

1. Click **Create shipping rate**.
1. Enter an amount, a description, and an optional delivery estimate.
1. Click **Save**, and copy the shipping rate ID (`shr_123456`).
   ![](assets/stripe-checkout-shipping-rate-dashboard.png)

Enter your shipping rate details

### Update a shipping rate

You can’t update an amount of a currency that’s already been set on a shipping rate. After you set a currency and amount on a shipping rate, it can only be updated to include new currencies. To update a shipping rate in the Dashboard, you must archive the shipping rate and then create a new one.

### Archive a shipping rate

To archive a shipping rate:

1. On the [Shipping rates](https://dashboard.stripe.com/test/shipping-rates) tab, select the applicable shipping rate.
1. Click the overflow menu ⋯, and select **Archive**.

To unarchive the shipping rate, click the overflow menu ⋯, and select **Unarchive shipping rate**.

#### API

> #### Interested in dynamic shipping rate updates?
>
> Checkout supports letting you dynamically update shipping rates based on the address your customer provides or the value of the order. See [Dynamically customize shipping options](https://docs.stripe.com/payments/checkout/custom-shipping-options.md) about this preview feature.

[Create a shipping rate](https://docs.stripe.com/api/shipping_rates.md), which at a minimum, requires the `type` and `display_name` parameters. The following code sample uses both of these parameters along with `fixed_amount` and `delivery_estimate` to create a shipping rate:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const shippingRate = await stripe.shippingRates.create({
  display_name: "Ground shipping",
  type: "fixed_amount",
  fixed_amount: {
    amount: 500,
    currency: "usd",
  },
  delivery_estimate: {
    minimum: {
      unit: "business_day",
      value: 5,
    },
    maximum: {
      unit: "business_day",
      value: 7,
    },
  },
});
```

### Update a shipping rate

To [update a shipping rate](https://docs.stripe.com/api/shipping_rates/update.md), call `Stripe::ShippingRate.update`, and update the parameters as needed.

## Create a Checkout Session [Server-side]

To create a Checkout Session that includes your shipping rate, pass in the generated shipping rate ID to the [shipping_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_options) parameter. If you want to create the shipping rate at the same time as a Checkout Session, use the `shipping_rate_data` parameter with `shipping_options`. Only Checkout Sessions in [payment mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode) support shipping options.

The following code sample adds two shipping options to the Checkout Session:

- Free shipping, with an estimated delivery of 5-7 business days.
- Next day air, at a cost of 15.00 USD, with an estimated delivery of exactly 1 business day.

In this example, the first option in the `shipping_options` array is pre-selected for the customer on the checkout page. However, customers can choose either option.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  billing_address_collection: "required",
  shipping_address_collection: {
    allowed_countries: ["US", "CA"],
  },
  shipping_options: [
    {
      shipping_rate_data: {
        type: "fixed_amount",
        fixed_amount: {
          amount: 0,
          currency: "usd",
        },
        display_name: "Free shipping",
        delivery_estimate: {
          minimum: {
            unit: "business_day",
            value: 5,
          },
          maximum: {
            unit: "business_day",
            value: 7,
          },
        },
      },
    },
    {
      shipping_rate_data: {
        type: "fixed_amount",
        fixed_amount: {
          amount: 1500,
          currency: "usd",
        },
        display_name: "Next day air",
        delivery_estimate: {
          minimum: {
            unit: "business_day",
            value: 1,
          },
          maximum: {
            unit: "business_day",
            value: 1,
          },
        },
      },
    },
  ],
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
  return_url: "https://example.com/return",
});
```

If successful, the shipping selector appears in your checkout flow:
![The shipping selector in the checkout flow](assets/stripe-checkout-shipping-selector.jpg)

The shipping selector in the checkout flow

## Optional: Handle completed transactions

After the payment succeeds, you can retrieve the shipping amount in the [amount_total](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-amount_total) attribute of the [shipping_cost](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-shipping_cost). You can also retrieve the selected shipping rate using the `shipping_rate` attribute in `shipping_cost`. To access the `shipping_cost` property, you must [create an event handler](https://docs.stripe.com/checkout/fulfillment.md#create-payment-event-handler) to handle completed Checkout Sessions. You can test a handler by [installing the Stripe CLI](https://docs.stripe.com/stripe-cli.md) and using `stripe listen --forward-to localhost:4242/webhook` to [forward events to your local server](https://docs.stripe.com/webhooks.md#test-webhook). In the following code sample, the handler allows for the user to access the `shipping_property`:

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

const fulfillOrder = async (session) => {
  const selectedShippingRate = await stripe.shippingRates.retrieve(
    session.shipping_cost.shipping_rate,
  );
  const shippingTotal = session.shipping_cost.amount_total;

  // TODO: Remove error and implement...
  throw new Error(`
    Given the Checkout Session ${session.id}, load your internal order from the database then implement your own fulfillment logic.`);
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

      // Fulfill the purchase...
      fulfillOrder(session);
    }

    response.status(200).end();
  },
);

app.listen(4242, () => console.log("Running on port 4242"));
```

## Optional: Define a delivery estimate

You can configure shipping rates using a number of delivery estimate combinations. The following table contains some examples of plain English delivery estimates, and their corresponding `delivery_estimate.minimum` and `delivery_estimate.maximum` values:

| Delivery Estimate | Minimum | Maximum |
| ----------------- | ------- | ------- |
| 1 day             | ```es6  |

{
unit: 'day',
value: 1,
}
`         |`es6
{
unit: 'day',
value: 1,
}

````|
| 1 business day             | ```es6
{
  unit: 'business_day',
  value: 1,
}
``` | ```es6
{
  unit: 'business_day',
  value: 1,
}
``` |
| At least 2 business days   | ```es6
{
  unit: 'business_day',
  value: 2,
}
``` | ```es6
null
```                                          |
| 3 to 7 days                | ```es6
{
  unit: 'day',
  value: 3,
}
```          | ```es6
{
  unit: 'day',
  value: 7,
}
```          |
| 4 to 8 hours               | ```es6
{
  unit: 'hour',
  value: 4,
}
```         | ```es6
{
  unit: 'hour',
  value: 8,
}
```         |
| 4 hours to 2 business days | ```es6
{
  unit: 'hour',
  value: 4,
}

```      | ```es6
{
  unit: 'business_day',
  value: 2,
}
``` |

## Optional: Charge tax for shipping

You can use [Stripe Tax](https://docs.stripe.com/tax/checkout.md) to automatically calculate tax on shipping fees by setting a `tax_code` and `tax_behavior` on your shipping rate. Stripe Tax automatically determines whether shipping is taxable ([as taxability varies by state and country](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#shipping-tax-code)) and applies the correct tax rate if so.

When creating a shipping rate with `shipping_rate_data` or through [Create a Shipping Rate](https://docs.stripe.com/api/shipping_rates/create.md), you can add a `tax_behavior` and `tax_code` parameter to the shipping rate.

We recommend setting the `tax_code` to `Shipping` (`txcd_92010001`) to make sure that you always charge the correct tax. You can also set the shipping rate `tax_code` to `Nontaxable` (`txcd_00000000`) if you don’t want to charge tax.

For this example, we set the `tax_behavior` to `exclusive`, which is common in the US. Learn more about [tax behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#tax-behavior).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
billing_address_collection: 'required',
shipping_address_collection: {
  allowed_countries: ['US', 'CA'],
},
shipping_options: [
  {
    shipping_rate_data: {
      type: 'fixed_amount',
      fixed_amount: {
        amount: 0,
        currency: 'usd',
      },
      display_name: 'Free shipping',
      tax_behavior: 'exclusive',
      tax_code: 'txcd_92010001',
      delivery_estimate: {
        minimum: {
          unit: 'business_day',
          value: 5,
        },
        maximum: {
          unit: 'business_day',
          value: 7,
        },
      },
    },
  },
],
line_items: [
  {
    price_data: {
      currency: 'usd',
      product_data: {
        name: 'T-shirt',
      },
      unit_amount: 2000,
      tax_behavior: 'exclusive',
    },
    quantity: 1,
  },
],
automatic_tax: {
  enabled: true,
},
mode: 'payment',
ui_mode: 'embedded_page',
return_url: 'https://example.com/return',
});
````

Your customer can see the calculated tax amount for the shipping rate factored into the total sales tax in your checkout flow:
![Calculated tax amount for the shipping rate on the checkout page](assets/stripe-checkout-taxed-shipping.jpg)

Calculated tax amount for the shipping rate in the checkout flow
