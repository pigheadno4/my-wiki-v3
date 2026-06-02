<!-- Source URL: https://docs.stripe.com/billing/subscriptions/sepa-debit -->
<!-- Fetched: 2026-05-13 -->

# Set up a subscription with SEPA Direct Debit

Learn how to create and charge a subscription with SEPA Direct Debit.

# Full hosted page

> This is a Full hosted page for when platform is web and payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/billing/subscriptions/sepa-debit?platform=web&payment-ui=stripe-hosted.

Check out the [sample on GitHub](https://github.com/stripe-samples/checkout-single-subscription) or explore the [demo](https://checkout.stripe.dev/checkout).

A [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) represents the details of your customer’s intent to purchase. You create a Checkout Session when your customer wants to start a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis). After redirecting your customer to a Checkout Session, Stripe presents a payment form where your customer can complete their purchase. Once your customer has completed a purchase, they will be redirected back to your site.

## Set up Stripe [Server-side]

Install the Stripe client of your choice:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

Install the Stripe CLI (optional). The CLI provides [webhook testing](https://docs.stripe.com/webhooks.md#test-webhook), and you can run it to create your products and prices.
For additional install options, see [Get started with the Stripe CLI](https://docs.stripe.com/stripe-cli.md).

## Create the pricing model [Dashboard] [Stripe CLI]

[Recurring pricing models](https://docs.stripe.com/products-prices/pricing-models.md) represent the products or services you sell, how much they cost, what currency you accept for payments, and the service period for subscriptions. To build the pricing model, create [products](https://docs.stripe.com/api/products.md) (what you sell) and [prices](https://docs.stripe.com/api/prices.md) (how much and how often to charge for your products).

This example uses flat-rate pricing with two different service-level options: Basic and Premium. For each service-level option, you need to create a product and a recurring price. To add a one-time charge for something like a setup fee, create a third product with a one-time price.

Each product bills at monthly intervals. The price for the Basic product is 5 EUR. The price for the Premium product is 15 EUR. See the [flat rate pricing](https://docs.stripe.com/subscriptions/pricing-models/flat-rate-pricing.md) guide for an example with three tiers.

#### Dashboard

Go to the [Add a product](https://dashboard.stripe.com/test/products/create) page and create two products. Add one price for each product, each with a monthly recurring billing period:

- Premium product: Premium service with extra features
  - Price: Flat rate | 15 EUR

- Basic product: Basic service with minimum features
  - Price: Flat rate | 5 EUR

After you create the prices, record the price IDs so you can use them in other steps. Price IDs look like this: `price_G0FvDp6vZvdwRZ`.

When you’re ready, use the **Copy to live mode** button at the top right of the page to clone your product from [a sandbox to live mode](https://docs.stripe.com/keys.md#test-live-modes).

#### API

You can use the API to create the [Products](https://docs.stripe.com/api/products.md) and [Prices](https://docs.stripe.com/api/prices.md).

Create the Premium product:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Billing Guide: Premium Service",
  description: "Premium service with extra features",
});
```

Create the Basic product:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Billing Guide: Basic Service",
  description: "Basic service with minimum features",
});
```

Record the product ID for each product. They look like this:

```json
{
  "id": "prod_H94k5odtwJXMtQ",
  "object": "product",
  "active": true,
  "attributes": [],
  "created": 1587577341,
  "description": "Premium service with extra features",
  "images": [],
  "livemode": false,
  "metadata": {},
  "name": "Billing Guide: Premium Service",
  "statement_descriptor": null,
  "type": "service",
  "unit_label": null,
  "updated": 1587577341
}
```

Use the product IDs to create a price for each product. The [unit_amount](https://docs.stripe.com/api/prices/object.md#price_object-unit_amount) number is in cents, so `1500` = 15 EUR, for example.

Create the Premium price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{PREMIUM_PRODUCT_ID}}",
  unit_amount: 1500,
  currency: "usd",
  recurring: {
    interval: "month",
  },
});
```

Create the Basic price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  product: "{{BASIC_PRODUCT_ID}}",
  unit_amount: 500,
  currency: "usd",
  recurring: {
    interval: "month",
  },
});
```

Record the price ID for each price so you can use them in subsequent steps. They look like this:

```json
{
  "id": "price_HGd7M3DV3IMXkC",
  "object": "price",
  "product": "prod_HGd6W1VUqqXGvr",
  "type": "recurring",
  "currency": "eur",
  "recurring": {
    "interval": "month",
    "interval_count": 1,
    "trial_period_days": null,
    "usage_type": "licensed"
  },
  "active": true,
  "billing_scheme": "per_unit",
  "created": 1589319695,
  "livemode": false,
  "lookup_key": null,
  "metadata": {},
  "nickname": null,
  "unit_amount": 1500,
  "unit_amount_decimal": "1500",
  "tiers": null,
  "tiers_mode": null,
  "transform_quantity": null
}
```

For other pricing models, see [Billing examples](https://docs.stripe.com/products-prices/pricing-models.md).

## Create a Checkout Session [Client-side] [Server-side]

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

```html
<html>
  <head>
    <title>Checkout</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>
```

### Checkout Session parameters

See [Create a Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) for a complete list of parameters that can be used.

Create a Checkout Session with the ID of an existing _Price_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions). Ensure that mode is set to `subscription` and you pass at least one recurring price. You can add one-time prices in addition to recurring prices. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["sepa_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'sepa_debit', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});

// Record the session ID in your system
const session_id = session.id;

// 303 redirect to session.url
```

When your customer successfully completes their payment, they’re redirected to the `success_url`, a page on your website that informs the customer that their payment was successful. Make the Session ID available on your success page by including the `{CHECKOUT_SESSION_ID}` template variable in the `success_url` as in the above example.

When your customer clicks on your logo in a Checkout Session without completing a payment, Checkout redirects them back to your website that the customer viewed prior to redirecting to Checkout.

Checkout Sessions expire 24 hours after creation by default.

From your [Dashboard](https://dashboard.stripe.com/settings/payment_methods), enable the payment methods you want to accept from your customers. Checkout supports [several payment methods](https://docs.stripe.com/payments/payment-methods/payment-method-support.md#product-support).

> Don’t rely on the redirect to the `success_url` alone for detecting payment initiation, because:
>
> - Malicious users could directly access the `success_url` without paying and gain access to your goods or services.

- After a successful payment, customers might close their browser tab before they’re redirected to the `success_url`.

## Confirm the payment is successful

When your customer completes a payment, Stripe redirects them to the URL that you specified in the `success_url` parameter. Typically, this is a page on your website that informs your customer that their payment was successful.

However, SEPA Direct Debit is a delayed notification payment method, which means that funds aren’t immediately available. Because of this, delay order _fulfillment_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) until the funds are available. After the payment succeeds, the underlying _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) status changes from `processing` to `succeeded`.

You can confirm the payment is successful in several ways:

#### Dashboard

Successful payments display in the Dashboard’s [list of payments](https://dashboard.stripe.com/payments). When you click a payment, it takes you to the payment details page. The **Checkout summary** section contains billing information and the list of items purchased, which you can use to manually fulfill the order.
![](assets/stripe-ach-checkout-success.png)

> Stripe can help you keep up with incoming payments by sending you email notifications whenever a customer successfully completes one. Use the Dashboard to [configure email notifications](https://dashboard.stripe.com/settings/user).

#### Webhooks

We send the following Checkout events when the payment status changes:

| Event Name                                                                                                                                   | Description                                                                                 | Next steps                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed)                             | The customer has successfully authorized the debit payment by submitting the Checkout form. | Wait for the payment to succeed or fail.                                            |
| [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) | The delayed payment method eventually succeeded.                                            | Fulfill the goods or services that the customer purchased.                          |
| [checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_failed)       | The delayed payment method eventually failed.                                               | Email the customer and request that they attempt the payment again.                 |
| [invoice.paid](https://docs.stripe.com/api/events/types.md#event_types-invoice.paid)                                                         | The customer’s payment succeeded.                                                           | Fulfill the goods or services that the customer purchased.                          |
| [invoice.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-invoice.payment_failed)                                     | The customer’s payment was declined, or failed for some other reason.                       | Contact the customer through email and request that they attempt the payment again. |

Your webhook code needs to handle all of these Checkout events.

Each Checkout webhook payload includes the [Checkout Session object](https://docs.stripe.com/api/checkout/sessions.md) and invoice webhooks include the [Invoice](https://docs.stripe.com/api/invoices/object.md) object. Both contain information about the customer and _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods).

Stripe sends the `checkout.session.completed` webhook to your server before redirecting your customer. Your webhook acknowledgement (any `2xx` status code) triggers the customer’s redirect to the `success_url`. If Stripe doesn’t receive successful acknowledgement within 10 seconds of a successful payment, your customer automatically redirects to the `success_url` page.

We recommend [using webhooks](https://docs.stripe.com/webhooks.md) to confirm the payment has succeeded and fulfill the goods or services the customer purchased. Below is an example webhook endpoint that handles the success or failure of a payment:

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = "whsec_...";

// Using Express
const app = require("express")();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require("body-parser");

// Match the raw body to content type application/json
app.post(
  "/webhook",
  bodyParser.raw({ type: "application/json" }),
  (request, response) => {
    const sig = request.headers["stripe-signature"];

    let event;

    try {
      event = stripe.webhooks.constructEvent(request.body, sig, endpointSecret);
    } catch (err) {
      return response.status(400).send(`Webhook Error: ${err.message}`);
    }

    switch (event.type) {
      case "checkout.session.completed": {
        const session = event.data.object;
        const subscriptionId = session.subscription;

        // Find the subscription or save it to your database.
        // invoice.paid may have fired before this so there
        // could already be a subscription.
        findOrCreateSubscription(subscriptionId);

        break;
      }

      case "invoice.paid": {
        const invoice = event.data.object;
        const subscriptionId = invoice.parent.subscription_details.subscription;

        // Find the subscription or save it to your database.
        // checkout.session.completed may not have fired yet
        // so we may need to create the subscription.
        const subscription = findOrCreateSubscription(subscriptionId);

        // Fulfill the purchase
        fulfillOrder(invoice);

        // Record that the subscription has been paid for
        // this payment period. invoice.paid will fire every
        // time there is a payment made for this subscription.
        recordAsPaidForThisPeriod(subscription);

        break;
      }

      case "invoice.payment_failed": {
        const invoice = event.data.object;

        // Send an email to the customer asking them to retry their payment
        emailCustomerAboutFailedPayment(invoice);

        break;
      }
    }

    // Return a response to acknowledge receipt of the event
    response.json({ received: true });
  },
);
```

Get information about the customer, payment, or subscription by retrieving the objects referenced by the `customer` or `customer_account`, `payment_intent`, and `subscription` properties in the webhook payload.

### Retrieving line items from webhook

By default, Checkout webhooks don’t return `line_items`. To retrieve the items created with the Checkout Session, make an additional request with the Checkout Session id:

#### curl

```bash
curl https://api.stripe.com/v1/checkout/sessions/{{CHECKOUT_SESSION_ID}}/line_items \
  -u <<YOUR_SECRET_KEY>>:
```

#### Stripe CLI

```bash
stripe get /v1/checkout/sessions/{{CHECKOUT_SESSION_ID}}/line_items
```

### Testing webhooks locally

To test webhooks locally, you can use the [Stripe CLI](https://docs.stripe.com/stripe-cli.md). After you install it, you can forward events to your server:

```bash
stripe listen --forward-to localhost:4242/webhook
Ready! Your webhook signing secret is '{{WEBHOOK_SIGNING_SECRET}}' (^C to quit)
```

Learn more about [setting up webhooks](https://docs.stripe.com/webhooks.md).

#### Third-party plugins

You can use plugins such as [Zapier](https://stripe.com/works-with/zapier) to automate updating your purchase fulfillment systems with information from Stripe payments.

Some examples of automation supported by plugins include:

- Updating spreadsheets used for order tracking in response to successful payments
- Updating inventory management systems in response to successful payments
- Triggering notifications to internal customer service teams using email or chat applications

## Test the integration

You can test your integration using the IBANs below. The payment method details are successfully collected for each IBAN but exhibit different behavior when charged.

##### Test IBANs

Use these test IBANs with the Payment Element to test your SEPA Direct Debit integration. The Payment Element automatically validates the IBAN and displays the mandate when you enter one of these test values.

### AT

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| AT611904300234573201 | pm_success_at                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| AT321904300235473204 | pm_successDelayed_at                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| AT861904300235473202 | pm_failed_at                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| AT051904300235473205 | pm_failedDelayed_at                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| AT591904300235473203 | pm_disputed_at                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| AT981904300000343434 | pm_exceedsWeeklyVolumeLimit_at      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| AT601904300000121212 | pm_exceedsWeeklyTransactionLimit_at | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| AT981904300002222227 | pm_insufficientFunds_at             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### BE

| Account Number   | Token                               | Description                                                                                                                                          |
| ---------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| BE62510007547061 | pm_success_be                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| BE78510007547064 | pm_successDelayed_be                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| BE68539007547034 | pm_failed_be                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| BE51510007547065 | pm_failedDelayed_be                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| BE08510007547063 | pm_disputed_be                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| BE90510000343434 | pm_exceedsWeeklyVolumeLimit_be      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| BE52510000121212 | pm_exceedsWeeklyTransactionLimit_be | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| BE90510002222227 | pm_insufficientFunds_be             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### HR

| Account Number        | Token                               | Description                                                                                                                                          |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| HR7624020064583467589 | pm_success_hr                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| HR6323600002337876649 | pm_successDelayed_hr                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| HR2725000096983499248 | pm_failed_hr                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| HR6723600004878117427 | pm_failedDelayed_hr                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| HR8724840081455523553 | pm_disputed_hr                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| HR7424020060000343434 | pm_exceedsWeeklyVolumeLimit_hr      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| HR3624020060000121212 | pm_exceedsWeeklyTransactionLimit_hr | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| HR7424020060002222227 | pm_insufficientFunds_hr             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### EE

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| EE382200221020145685 | pm_success_ee                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| EE222200221020145682 | pm_successDelayed_ee                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| EE762200221020145680 | pm_failed_ee                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| EE922200221020145683 | pm_failedDelayed_ee                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| EE492200221020145681 | pm_disputed_ee                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| EE672200000000343434 | pm_exceedsWeeklyVolumeLimit_ee      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| EE292200000000121212 | pm_exceedsWeeklyTransactionLimit_ee | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| EE672200000002222227 | pm_insufficientFunds_ee             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### FI

| Account Number     | Token                               | Description                                                                                                                                          |
| ------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| FI2112345600000785 | pm_success_fi                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| FI3712345600000788 | pm_successDelayed_fi                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| FI9112345600000786 | pm_failed_fi                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| FI1012345600000789 | pm_failedDelayed_fi                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| FI6412345600000787 | pm_disputed_fi                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| FI6712345600343434 | pm_exceedsWeeklyVolumeLimit_fi      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| FI2912345600121212 | pm_exceedsWeeklyTransactionLimit_fi | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| FI6712345602222227 | pm_insufficientFunds_fi             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### FR

| Account Number              | Token                               | Description                                                                                                                                          |
| --------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| FR1420041010050500013M02606 | pm_success_fr                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| FR3020041010050500013M02609 | pm_successDelayed_fr                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| FR8420041010050500013M02607 | pm_failed_fr                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| FR7920041010050500013M02600 | pm_failedDelayed_fr                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| FR5720041010050500013M02608 | pm_disputed_fr                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| FR9720041010050000000343434 | pm_exceedsWeeklyVolumeLimit_fr      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| FR5920041010050000000121212 | pm_exceedsWeeklyTransactionLimit_fr | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| FR9720041010050000002222227 | pm_insufficientFunds_fr             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### DE

| Account Number         | Token                               | Description                                                                                                                                          |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| DE89370400440532013000 | pm_success_de                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| DE08370400440532013003 | pm_successDelayed_de                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| DE62370400440532013001 | pm_failed_de                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| DE78370400440532013004 | pm_failedDelayed_de                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| DE35370400440532013002 | pm_disputed_de                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| DE65370400440000343434 | pm_exceedsWeeklyVolumeLimit_de      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| DE27370400440000121212 | pm_exceedsWeeklyTransactionLimit_de | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| DE65370400440002222227 | pm_insufficientFunds_de             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### GI

| Account Number          | Token                               | Description                                                                                                                                          |
| ----------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| GI60MPFS599327643783385 | pm_success_gi                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| GI08RRNW626436291644533 | pm_successDelayed_gi                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| GI41SAFA461293238477751 | pm_failed_gi                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| GI50LROG772261344693297 | pm_failedDelayed_gi                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| GI26KJBC361883934534696 | pm_disputed_gi                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| GI14NWBK000000000343434 | pm_exceedsWeeklyVolumeLimit_gi      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| GI73NWBK000000000121212 | pm_exceedsWeeklyTransactionLimit_gi | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| GI14NWBK000000002222227 | pm_insufficientFunds_gi             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### IE

| Account Number         | Token                               | Description                                                                                                                                          |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| IE29AIBK93115212345678 | pm_success_ie                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| IE24AIBK93115212345671 | pm_successDelayed_ie                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| IE02AIBK93115212345679 | pm_failed_ie                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| IE94AIBK93115212345672 | pm_failedDelayed_ie                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| IE51AIBK93115212345670 | pm_disputed_ie                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| IE10AIBK93115200343434 | pm_exceedsWeeklyVolumeLimit_ie      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| IE69AIBK93115200121212 | pm_exceedsWeeklyTransactionLimit_ie | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| IE10AIBK93115202222227 | pm_insufficientFunds_ie             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### LI

| Account Number        | Token                               | Description                                                                                                                                          |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| LI0508800636123378777 | pm_success_li                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| LI4408800387787111369 | pm_successDelayed_li                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| LI1208800143823175626 | pm_failed_li                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| LI4908800356441975566 | pm_failedDelayed_li                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| LI7708800125525347723 | pm_disputed_li                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| LI2408800000000343434 | pm_exceedsWeeklyVolumeLimit_li      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| LI8308800000000121212 | pm_exceedsWeeklyTransactionLimit_li | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| LI2408800000002222227 | pm_insufficientFunds_li             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### LT

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| LT121000011101001000 | pm_success_lt                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| LT281000011101001003 | pm_successDelayed_lt                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| LT821000011101001001 | pm_failed_lt                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| LT981000011101001004 | pm_failedDelayed_lt                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| LT551000011101001002 | pm_disputed_lt                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| LT591000000000343434 | pm_exceedsWeeklyVolumeLimit_lt      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| LT211000000000121212 | pm_exceedsWeeklyTransactionLimit_lt | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| LT591000000002222227 | pm_insufficientFunds_lt             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### LU

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| LU280019400644750000 | pm_success_lu                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| LU440019400644750003 | pm_successDelayed_lu                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| LU980019400644750001 | pm_failed_lu                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| LU170019400644750004 | pm_failedDelayed_lu                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| LU710019400644750002 | pm_disputed_lu                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| LU900010000000343434 | pm_exceedsWeeklyVolumeLimit_lu      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| LU520010000000121212 | pm_exceedsWeeklyTransactionLimit_lu | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| LU900010000002222227 | pm_insufficientFunds_lu             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### NL

| Account Number     | Token                               | Description                                                                                                                                          |
| ------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| NL39RABO0300065264 | pm_success_nl                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| NL55RABO0300065267 | pm_successDelayed_nl                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| NL91ABNA0417164300 | pm_failed_nl                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| NL28RABO0300065268 | pm_failedDelayed_nl                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| NL82RABO0300065266 | pm_disputed_nl                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| NL27RABO0000343434 | pm_exceedsWeeklyVolumeLimit_nl      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| NL86RABO0000121212 | pm_exceedsWeeklyTransactionLimit_nl | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| NL55RABO0300065267 | pm_insufficientFunds_nl             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### NO

| Account Number  | Token                               | Description                                                                                                                                          |
| --------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| NO9386011117947 | pm_success_no                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| NO8886011117940 | pm_successDelayed_no                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| NO6686011117948 | pm_failed_no                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| NO6186011117941 | pm_failedDelayed_no                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| NO3986011117949 | pm_disputed_no                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| NO0586010343434 | pm_exceedsWeeklyVolumeLimit_no      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| NO0586010343434 | pm_exceedsWeeklyTransactionLimit_no | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| NO0586012222227 | pm_insufficientFunds_no             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### PT

| Account Number            | Token                               | Description                                                                                                                                          |
| ------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| PT50000201231234567890154 | pm_success_pt                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| PT66000201231234567890157 | pm_successDelayed_pt                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| PT23000201231234567890155 | pm_failed_pt                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| PT39000201231234567890158 | pm_failedDelayed_pt                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| PT93000201231234567890156 | pm_disputed_pt                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| PT05000201230000000343434 | pm_exceedsWeeklyVolumeLimit_pt      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| PT64000201230000000121212 | pm_exceedsWeeklyTransactionLimit_pt | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| PT05000201230000002222227 | pm_insufficientFunds_pt             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### ES

| Account Number           | Token                               | Description                                                                                                                                          |
| ------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| ES0700120345030000067890 | pm_success_es                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| ES2300120345030000067893 | pm_successDelayed_es                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| ES9121000418450200051332 | pm_failed_es                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| ES9300120345030000067894 | pm_failedDelayed_es                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| ES5000120345030000067892 | pm_disputed_es                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| ES1700120345000000343434 | pm_exceedsWeeklyVolumeLimit_es      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| ES7600120345000000121212 | pm_exceedsWeeklyTransactionLimit_es | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| ES1700120345000002222227 | pm_insufficientFunds_es             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### SE

| Account Number           | Token                               | Description                                                                                                                                          |
| ------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| SE3550000000054910000003 | pm_success_se                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| SE5150000000054910000006 | pm_successDelayed_se                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| SE0850000000054910000004 | pm_failed_se                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| SE2450000000054910000007 | pm_failedDelayed_se                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| SE7850000000054910000005 | pm_disputed_se                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| SE2850000000000000343434 | pm_exceedsWeeklyVolumeLimit_se      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| SE8750000000000000121212 | pm_exceedsWeeklyTransactionLimit_se | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| SE2850000000000002222227 | pm_insufficientFunds_se             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### CH

| Account Number        | Token                               | Description                                                                                                                                          |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| CH9300762011623852957 | pm_success_ch                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| CH8656663438253651553 | pm_successDelayed_ch                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| CH5362200119938136497 | pm_failed_ch                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| CH1843597160341964438 | pm_failedDelayed_ch                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| CH1260378413965193069 | pm_disputed_ch                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| CH1800762000000343434 | pm_exceedsWeeklyVolumeLimit_ch      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| CH7700762000000121212 | pm_exceedsWeeklyTransactionLimit_ch | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| CH1800762000002222227 | pm_insufficientFunds_ch             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### GB

| Account Number         | Token                               | Description                                                                                                                                          |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| GB82WEST12345698765432 | pm_success_gb                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| GB98WEST12345698765435 | pm_successDelayed_gb                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| GB55WEST12345698765433 | pm_failed_gb                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| GB71WEST12345698765436 | pm_failedDelayed_gb                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| GB28WEST12345698765434 | pm_disputed_gb                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| GB70WEST12345600343434 | pm_exceedsWeeklyVolumeLimit_gb      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| GB32WEST12345600121212 | pm_exceedsWeeklyTransactionLimit_gb | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| GB70WEST12345602222227 | pm_insufficientFunds_gb             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

## Optional: Adding a one-time setup fee [Server-side]

In addition to passing recurring prices, you can add one-time prices in `subscription` mode. These are only included on the initial _invoice_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) created by the subscription. This is useful for adding setup fees or other one-time fees associated with a subscription. You can add a one-time _price_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) to an existing product or create a new _product_ (Products represent items your customer can subscribe to with a Subscription. An associated Price object describes the pricing and other terms of the subscription) with a new price.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["sepa_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'sepa_debit', ...]
  line_items: [
    {
      price: "{{RECURRING_PRICE_ID}}",
      quantity: 1,
    },
    {
      price: "{{ONE_TIME_PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});
```

## Optional: Create prices and products inline [Server-side]

In addition to passing existing price IDs, you can create new prices at Checkout session creation. First, define a _Product_ (Products represent what your business sells—whether that's a good or a service) and then create a Checkout Session using the product ID. Make sure to pass [price_data](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-price_data) with the `unit_amount`, `currency`, and `recurring` details:

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({payment_method_types: ['sepa_debit'],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'sepa_debit', ...]line_items: [{
    price_data: {
      unit_amount: 5000,
      currency: 'eur',
      product: '{{PRODUCT_ID}}',
      recurring: {
        interval: 'month'
      },
    },
    quantity: 1
  }],
  mode: 'subscription',
  success_url: 'https://example.com/success?session_id={CHECKOUT_SESSION_ID}'
});
```

If you also need to create products inline, you can do so with [product_data](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-price_data-product_data):

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({payment_method_types: ['sepa_debit'],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'sepa_debit', ...]line_items: [{
    price_data: {
      currency: 'eur',
      product_data: {
        name: 'T-shirt'
      },
      unit_amount: 2000
    },
    quantity: 1
  }],
  mode: 'subscription',
  success_url: 'https://example.com/success?session_id={CHECKOUT_SESSION_ID}'
});
```

## Optional: Existing customers [Server-side]

#### Accounts v2

If you’ve previously created a customer-configured `Account` object to represent a customer, use the [customer_account](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_account) argument to pass their `Account` ID when creating a Checkout Session. This ensures that all objects created during the Session are associated with the correct `Account` object.

When you pass an `Account` ID, Stripe also uses the email stored on the `Account` object to prefill the email field on the Checkout page. If the customer changes their email on the Checkout page, it updates on the `Account` object after a successful payment.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer_account: "{{CUSTOMER_ACCOUNT_ID}}",
  payment_method_types: ["sepa_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'sepa_debit', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

#### Customers v1

If you’ve previously created a _`Customer`_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object to represent a customer, use the [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) argument to pass their `Customer` ID when creating a Checkout Session. This ensures that all objects created during the Session are associated with the correct `Customer` object.

When you pass a `Customer` ID, Stripe also uses the email stored on the `Customer` object to prefill the email field on the Checkout page. If the customer changes their email on the Checkout page, it will be updated on the `Customer` object after a successful payment.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method_types: ["sepa_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'sepa_debit', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

## Optional: Prefill customer data [Server-side]

If you’ve already collected your customer’s email and want to prefill it in the Checkout Session for them, pass [customer_email](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_email) when creating a Checkout Session.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer_email: "customer@example.com",
  payment_method_types: ["sepa_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'sepa_debit', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

## Optional: Handling trials [Server-side]

You can use [trial_end](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_end) or [trial_period_days](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_period_days) on the Checkout session to specify the duration of the trial period. In this example we use `trial_period_days` to create a Checkout session for a subscription with a 30 days trial.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["sepa_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'sepa_debit', ...]
  subscription_data: { trial_period_days: 30 },
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});
```

Checkout displays the following information automatically for subscriptions with trials:

- Trial period
- Frequency and amount of charges after trial expiration

For more information on compliance requirements, see the [Manage compliance requirements](https://docs.stripe.com/billing/subscriptions/trials/manage-trial-compliance.md) or [support](https://support.stripe.com/questions/2020-visa-trial-subscription-requirement-changes-guide) guides.

## Optional: Tax rates [Server-side]

You can specify [tax rates](https://docs.stripe.com/tax/tax-rates.md) (Sales, VAT, GST, and others) in Checkout Sessions to apply taxes to _subscriptions_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis).

- Use fixed tax rates when you know the exact tax rate to charge your customers before they start the checkout process (for example, you only sell to customers in the UK and always charge 20% VAT).
- With the _Prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) API, you can use dynamic tax rates when you require more information from your customer (for example, their billing or shipping address) before determining the tax rate to charge. With dynamic tax rates, you create tax rates for different regions (for example, a 20% VAT tax rate for customers in the UK and a 7.25% sales tax rate for customers in California, US) and Stripe attempts to match your customer’s location to one of those tax rates.

#### Fixed tax rates

Set [subscription_data.default_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-default_tax_rates) to apply a default tax rate to a subscription started with Checkout.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["sepa_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'sepa_debit', ...]
  subscription_data: { default_tax_rates: ["{{TAX_RATE_ID}}"] },
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

You can also specify [line_items.tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-tax_rates) or [subscription_data.items.tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-items-tax_rates) to apply tax rates to specific plans or invoice line items.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["sepa_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'sepa_debit', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
      tax_rates: ["{{TAX_RATE_ID}}"],
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

#### Dynamic tax rates

Pass an array of [tax rates](https://docs.stripe.com/api/tax_rates/object.md) to [line_items.dynamic_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates). Each tax rate must have a [supported](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates) `country`, and for the US, a `state`.

This list matches tax rates to your customer’s [shipping address](https://docs.stripe.com/payments/collect-addresses.md), billing address, or country. The shipping address takes precedence over the billing address for determining the tax rate to charge.

If you’re not collecting shipping or billing addresses, your customer’s country (and postal code where applicable) is used to determine the tax rate. If you haven’t passed a tax rate that matches your customer’s shipping address, billing address, or country, no tax rate is applied.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["sepa_debit"],
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
      dynamic_tax_rates: [
        "{{FIRST_TAX_RATE_ID}}",
        "{{SECOND_TAX_RATE_ID}}",
        // additional tax rates
      ],
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

> [subscription_data.default_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-default_tax_rates) and [line_items.tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-tax_rates) can’t be used in combination with [line_items.dynamic_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates).

You can use Stripe’s data exports to populate the periodic reports required for remittance. Visit [Tax reporting and remittance](https://docs.stripe.com/tax/tax-rates.md#remittance) for more information.

## Optional: Adding coupons [Server-side]

You can apply [coupons](https://docs.stripe.com/billing/subscriptions/coupons.md) to subscriptions in a Checkout Session by setting [discounts](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-discounts). This coupon overrides any coupon on the customer. If you’re creating a subscription with an [existing customer](https://docs.stripe.com/billing/subscriptions/sepa-debit.md#handling-existing-customers), any coupon associated with the customer is applied to the subscription’s _invoices_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice).

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["sepa_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'sepa_debit', ...]
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  discounts: [{ coupon: "{{COUPON_ID}}" }],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

### Adding customer-facing promotion codes

You can also enable user-redeemable [Promotion Codes](https://docs.stripe.com/billing/subscriptions/coupons.md#promotion-codes) using the [allow_promotion_codes](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-allow_promotion_codes) parameter in Checkout Sessions. When `allow_promotion_codes` is enabled on a Checkout Session, Checkout includes a promotion code redemption box for your customers to use. Create your [coupons](https://docs.stripe.com/billing/subscriptions/coupons.md) and promotion codes through the Dashboard or API in order for your customers to redeem them in Checkout.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  payment_method_types: ["sepa_debit"],

  // or you can take multiple payment methods with
  // payment_method_types: ['card', 'sepa_debit', ...]
  line_items: [
    {
      price_data: {
        currency: "eur",
        unit_amount: 2000,
        product: "{{PRODUCT_ID}}",
        recurring: {
          interval: "month",
        },
      },
      quantity: 1,
    },
  ],
  allow_promotion_codes: true,
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

## See also

- [Customize your integration](https://docs.stripe.com/payments/checkout/customization.md)
- [Manage subscriptions with the customer portal](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=checkout&ui=stripe-hosted)

# Advanced integration

> This is a Advanced integration for when platform is web and payment-ui is elements. View the full page at https://docs.stripe.com/billing/subscriptions/sepa-debit?platform=web&payment-ui=elements.

Learn how to create and charge for a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) with SEPA Direct Debit.

> If you’re a new user, use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) instead of using Stripe Elements as described in this guide. The Payment Element provides a low-code integration path with built-in conversion optimizations. For instructions, see [Build a subscription](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=elements).

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 EUR monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **EUR** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create a customer [Server-side]

To create a subscription, you need to add a customer to reuse payment methods and track recurring payments.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/create.md) when your customer creates an account with your business, or when saving a payment method. Associate the object’s ID with your own internal representation of a customer.

Create a new customer or retrieve an existing one to associate with this payment.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const account = await stripe.v2.core.accounts.create({
  contact_email: "jenny.rosen@example.com",
  display_name: "Jenny Rosen",
  configuration: {
    customer: {},
  },
  include: ["configuration.customer"],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  name: "Jenny Rosen",
  email: "jenny.rosen@example.com",
});
```

## Create the subscription [Server-side]

Create the _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) using the customer and price IDs. Return to the client side the `client_secret` from either the latest invoice’s [confirmation_secret.client_secret](https://docs.stripe.com/api/invoices/object.md#invoice_object-confirmation_secret) or, for subscriptions that don’t collect a payment up front, the [pending_setup_intent](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-pending_setup_intent). Additionally, set:

- [payment_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-payment_behavior) to `default_incomplete` to simplify collection of the SEPA Direct Debit mandate.
- [save_default_payment_method](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-payment_settings-save_default_payment_method) to `on_subscription` to save the payment method as the default for the subscription when the payment succeeds. Saving a default payment method increases the success rate of future subscription payments.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

app.post("/create-subscription", async (req, res) => {
  const customerId = req.cookies["customer"];
  const priceId = req.body.priceId;

  try {
    const subscription = await stripe.subscriptions.create({
      customer: customerId,
      items: [
        {
          price: priceId,
        },
      ],
      payment_behavior: "default_incomplete",
      payment_settings: { save_default_payment_method: "on_subscription" },
      expand: ["latest_invoice.confirmation_secret", "pending_setup_intent"],
    });

    if (subscription.pending_setup_intent !== null) {
      res.send({
        type: "setup",
        clientSecret: subscription.pending_setup_intent.client_secret,
      });
    } else {
      res.send({
        type: "payment",
        clientSecret:
          subscription.latest_invoice.confirmation_secret.client_secret,
      });
    }
  } catch (error) {
    return res.status(400).send({ error: { message: error.message } });
  }
});
```

## Collect payment method details and mandate acknowledgment [Client-side]

You’re ready to collect payment information on the client with [Stripe Elements](https://docs.stripe.com/payments/elements.md). Elements is a set of prebuilt UI components for collecting payment details.

A Stripe Element contains an iframe that securely sends the payment information to Stripe over an HTTPS connection. The checkout page address must also start with https:// rather than http:// for your integration to work.

You can test your integration without using HTTPS. [Enable it](https://docs.stripe.com/security/guide.md#tls) when you’re ready to accept live payments.

### Set up Stripe Elements

#### HTML + JS

Stripe Elements is automatically available as a feature of Stripe.js. Include the Stripe.js script on your payment page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<head>
  <title>Submit Payment</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Elements with the following JavaScript on your payment page. Pass the `mode` and `currency` to enable the Payment Element to collect SEPA Direct Debit payment details:

```javascript
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
const options = {
  mode: "setup",
  currency: "eur",
};
const elements = stripe.elements(options);
```

### Add the Payment Element

The Payment Element needs a place to live in your payment form. Create an empty DOM node (container) with a unique ID in your payment form. The Payment Element automatically displays the SEPA Direct Debit form and mandate acceptance text when SEPA Debit is enabled:

```html
<form action="/form" method="post" id="setup-form">
  <div id="payment-element">
    <!-- The Payment Element will be inserted here. -->
  </div>

  <!-- Add the client_secret from the SetupIntent as a data attribute   -->
  <button id="submit-button" data-secret="{CLIENT_SECRET}">
    Set up SEPA Direct Debit
  </button>

  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>
</form>
```

When the form loads, [create an instance](https://docs.stripe.com/js/elements_object/create_element?type=payment) of the Payment Element and mount it to the Element container. The Payment Element automatically collects the customer’s name, email, IBAN, and displays the mandate acceptance text:

```javascript
// Create and mount the Payment Element
const paymentElement = elements.create("payment");
paymentElement.mount("#payment-element");
```

#### React

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry:

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

Pass the setup details (`mode: 'setup'`, `currency`) to the [Elements Provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider):

```jsx
import React from "react";
import { loadStripe } from "@stripe/stripe-js";
import { Elements } from "@stripe/react-stripe-js";
import PaymentSetupForm from "./PaymentSetupForm";

// Make sure to call `loadStripe` outside of a component's render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

export default function App() {
  const options = {
    mode: "setup",
    currency: "eur",
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <PaymentSetupForm />
    </Elements>
  );
}
```

Create a setup form component that renders the [PaymentElement](https://docs.stripe.com/sdks/stripejs-react.md#element-components):

```jsx
import React from "react";
import { PaymentElement } from "@stripe/react-stripe-js";

export default function PaymentSetupForm() {
  return (
    <form id="setup-form">
      <PaymentElement />
      <button type="submit">Set up SEPA Direct Debit</button>
      <div id="error-message" role="alert"></div>
    </form>
  );
}
```

## Submit the payment method details to Stripe [Client-side]

Use [confirmSepaDebitPayment](https://docs.stripe.com/js/payment_intents/confirm_sepa_debit_payment#stripe_confirm_sepa_debit_payment-with_element) or, for subscriptions that don’t collect a payment up front, [confirmSepaDebitSetup](https://docs.stripe.com/js/setup_intents/confirm_sepa_debit_setup#stripe_confirm_sepa_debit_setup-with_element) to confirm the subscription and create a SEPA Direct Debit [PaymentMethod](https://docs.stripe.com/api/payment_methods.md). Include the customer’s name and email address in the `payment_method.billing_details` properties.

#### HTML + JS

```javascript
// Define stripe with your publishable key
var stripe = Stripe("pk_test_1234");

// Get the IBAN information from your element
var iban = document.getElementById("iban-element");

const form = document.getElementById("payment-form");
const accountholderName = document.getElementById("accountholder-name");
const email = document.getElementById("email");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  // Create the subscription
  const res = await fetch("/create-subscription", {
    method: "POST",
  });
  const { type, clientSecret } = await res.json();
  const confirmIntent =
    type === "setup" ?
      stripe.confirmSepaDebitSetup
    : stripe.confirmSepaDebitPayment;

  const { error } = await confirmIntent(clientSecret, {
    payment_method: {
      sepa_debit: iban,
      billing_details: {
        name: accountholderName.value,
        email: email.value,
      },
    },
  });
});
```

#### React

```jsx
import React, { useState } from "react";
import { useStripe, useElements, IbanElement } from "@stripe/react-stripe-js";
import IbanForm from "./IbanForm";

export default function PaymentSetupForm() {
  const stripe = useStripe();
  const elements = useElements();

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    const iban = elements.getElement(IbanElement);

    // For brevity, this example is using uncontrolled components for
    // the accountholder's name and email. In a real world app, you'd
    // probably want to use controlled components.
    // https://reactjs.org/docs/uncontrolled-components.html
    // https://reactjs.org/docs/forms.html#controlled-components

    const accountholderName = event.target["accountholder-name"];
    const email = event.target.email;

    // Create the subscription
    const res = await fetch("/create-subscription", {
      method: "POST",
    });
    const { type, clientSecret } = await res.json();
    const confirmIntent =
      type === "setup" ?
        stripe.confirmSepaDebitSetup
      : stripe.confirmSepaDebitPayment;

    const { error } = await confirmIntent(clientSecret, {
      payment_method: {
        sepa_debit: iban,
        billing_details: {
          name: accountholderName.value,
          email: email.value,
        },
      },
    });

    if (res.error) {
      // Show error to your customer
      console.log(res.error.message);
    } else {
      // Show a confirmation message to your customer
    }
  };

  return <IbanForm onSubmit={handleSubmit} disabled={!stripe} />;
}
```

## Set the default payment method [Server-side]

You need to add a stored payment method to the customer so future payments are successful. Set the payment method you collected at the top-level of the object representing the customer (either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md) or [Customer](https://docs.stripe.com/api/customers/object.md)) and as the [default payment method](https://docs.stripe.com/api/customers/update.md#update_customer-invoice_settings-default_payment_method) for _invoices_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice):

#### Accounts v2

If you use customer-configured Account objects to represent your customers, set [configuration.customer.billing.default_payment_method](https://docs.stripe.com/api/v2/core/accounts/update.md#v2_update_accounts-configuration-customer-billing-default_payment_method):

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const account = await stripe.v2.core.accounts.update("acct_Gk0uVzT2M4xOKD", {
  configuration: {
    customer: {
      billing: {
        default_payment_method: "pm_1F0c9v2eZvKYlo2CJDeTrB4n",
      },
    },
  },
});
```

#### Customers v1

If you use `Customer` objects to represent your customers, set [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/update.md#update_customer-invoice_settings-default_payment_method):

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.update("cus_Gk0uVzT2M4xOKD", {
  invoice_settings: {
    default_payment_method: "pm_1F0c9v2eZvKYlo2CJDeTrB4n",
  },
});
```

## Manage subscription status [Client-side]

When the initial payment succeeds, the status of the _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) is `active` and no further action is needed. When payments fail, the status is changed to the **Subscription status** configured in your [automatic collection settings](https://docs.stripe.com/invoicing/automatic-collection.md). Notify the customer after a failure and [charge them with a different payment method](https://docs.stripe.com/billing/subscriptions/overview.md#requires-payment-method).

## Test the integration

You can test your integration using the IBANs below. The payment method details are successfully collected for each IBAN but exhibit different behavior when charged.

##### Test IBANs

Use these test IBANs with the Payment Element to test your SEPA Direct Debit integration. The Payment Element automatically validates the IBAN and displays the mandate when you enter one of these test values.

### AT

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| AT611904300234573201 | pm_success_at                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| AT321904300235473204 | pm_successDelayed_at                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| AT861904300235473202 | pm_failed_at                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| AT051904300235473205 | pm_failedDelayed_at                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| AT591904300235473203 | pm_disputed_at                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| AT981904300000343434 | pm_exceedsWeeklyVolumeLimit_at      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| AT601904300000121212 | pm_exceedsWeeklyTransactionLimit_at | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| AT981904300002222227 | pm_insufficientFunds_at             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### BE

| Account Number   | Token                               | Description                                                                                                                                          |
| ---------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| BE62510007547061 | pm_success_be                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| BE78510007547064 | pm_successDelayed_be                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| BE68539007547034 | pm_failed_be                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| BE51510007547065 | pm_failedDelayed_be                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| BE08510007547063 | pm_disputed_be                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| BE90510000343434 | pm_exceedsWeeklyVolumeLimit_be      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| BE52510000121212 | pm_exceedsWeeklyTransactionLimit_be | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| BE90510002222227 | pm_insufficientFunds_be             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### HR

| Account Number        | Token                               | Description                                                                                                                                          |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| HR7624020064583467589 | pm_success_hr                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| HR6323600002337876649 | pm_successDelayed_hr                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| HR2725000096983499248 | pm_failed_hr                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| HR6723600004878117427 | pm_failedDelayed_hr                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| HR8724840081455523553 | pm_disputed_hr                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| HR7424020060000343434 | pm_exceedsWeeklyVolumeLimit_hr      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| HR3624020060000121212 | pm_exceedsWeeklyTransactionLimit_hr | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| HR7424020060002222227 | pm_insufficientFunds_hr             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### EE

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| EE382200221020145685 | pm_success_ee                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| EE222200221020145682 | pm_successDelayed_ee                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| EE762200221020145680 | pm_failed_ee                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| EE922200221020145683 | pm_failedDelayed_ee                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| EE492200221020145681 | pm_disputed_ee                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| EE672200000000343434 | pm_exceedsWeeklyVolumeLimit_ee      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| EE292200000000121212 | pm_exceedsWeeklyTransactionLimit_ee | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| EE672200000002222227 | pm_insufficientFunds_ee             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### FI

| Account Number     | Token                               | Description                                                                                                                                          |
| ------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| FI2112345600000785 | pm_success_fi                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| FI3712345600000788 | pm_successDelayed_fi                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| FI9112345600000786 | pm_failed_fi                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| FI1012345600000789 | pm_failedDelayed_fi                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| FI6412345600000787 | pm_disputed_fi                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| FI6712345600343434 | pm_exceedsWeeklyVolumeLimit_fi      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| FI2912345600121212 | pm_exceedsWeeklyTransactionLimit_fi | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| FI6712345602222227 | pm_insufficientFunds_fi             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### FR

| Account Number              | Token                               | Description                                                                                                                                          |
| --------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| FR1420041010050500013M02606 | pm_success_fr                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| FR3020041010050500013M02609 | pm_successDelayed_fr                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| FR8420041010050500013M02607 | pm_failed_fr                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| FR7920041010050500013M02600 | pm_failedDelayed_fr                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| FR5720041010050500013M02608 | pm_disputed_fr                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| FR9720041010050000000343434 | pm_exceedsWeeklyVolumeLimit_fr      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| FR5920041010050000000121212 | pm_exceedsWeeklyTransactionLimit_fr | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| FR9720041010050000002222227 | pm_insufficientFunds_fr             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### DE

| Account Number         | Token                               | Description                                                                                                                                          |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| DE89370400440532013000 | pm_success_de                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| DE08370400440532013003 | pm_successDelayed_de                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| DE62370400440532013001 | pm_failed_de                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| DE78370400440532013004 | pm_failedDelayed_de                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| DE35370400440532013002 | pm_disputed_de                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| DE65370400440000343434 | pm_exceedsWeeklyVolumeLimit_de      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| DE27370400440000121212 | pm_exceedsWeeklyTransactionLimit_de | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| DE65370400440002222227 | pm_insufficientFunds_de             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### GI

| Account Number          | Token                               | Description                                                                                                                                          |
| ----------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| GI60MPFS599327643783385 | pm_success_gi                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| GI08RRNW626436291644533 | pm_successDelayed_gi                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| GI41SAFA461293238477751 | pm_failed_gi                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| GI50LROG772261344693297 | pm_failedDelayed_gi                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| GI26KJBC361883934534696 | pm_disputed_gi                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| GI14NWBK000000000343434 | pm_exceedsWeeklyVolumeLimit_gi      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| GI73NWBK000000000121212 | pm_exceedsWeeklyTransactionLimit_gi | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| GI14NWBK000000002222227 | pm_insufficientFunds_gi             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### IE

| Account Number         | Token                               | Description                                                                                                                                          |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| IE29AIBK93115212345678 | pm_success_ie                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| IE24AIBK93115212345671 | pm_successDelayed_ie                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| IE02AIBK93115212345679 | pm_failed_ie                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| IE94AIBK93115212345672 | pm_failedDelayed_ie                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| IE51AIBK93115212345670 | pm_disputed_ie                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| IE10AIBK93115200343434 | pm_exceedsWeeklyVolumeLimit_ie      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| IE69AIBK93115200121212 | pm_exceedsWeeklyTransactionLimit_ie | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| IE10AIBK93115202222227 | pm_insufficientFunds_ie             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### LI

| Account Number        | Token                               | Description                                                                                                                                          |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| LI0508800636123378777 | pm_success_li                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| LI4408800387787111369 | pm_successDelayed_li                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| LI1208800143823175626 | pm_failed_li                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| LI4908800356441975566 | pm_failedDelayed_li                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| LI7708800125525347723 | pm_disputed_li                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| LI2408800000000343434 | pm_exceedsWeeklyVolumeLimit_li      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| LI8308800000000121212 | pm_exceedsWeeklyTransactionLimit_li | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| LI2408800000002222227 | pm_insufficientFunds_li             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### LT

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| LT121000011101001000 | pm_success_lt                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| LT281000011101001003 | pm_successDelayed_lt                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| LT821000011101001001 | pm_failed_lt                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| LT981000011101001004 | pm_failedDelayed_lt                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| LT551000011101001002 | pm_disputed_lt                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| LT591000000000343434 | pm_exceedsWeeklyVolumeLimit_lt      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| LT211000000000121212 | pm_exceedsWeeklyTransactionLimit_lt | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| LT591000000002222227 | pm_insufficientFunds_lt             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### LU

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| LU280019400644750000 | pm_success_lu                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| LU440019400644750003 | pm_successDelayed_lu                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| LU980019400644750001 | pm_failed_lu                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| LU170019400644750004 | pm_failedDelayed_lu                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| LU710019400644750002 | pm_disputed_lu                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| LU900010000000343434 | pm_exceedsWeeklyVolumeLimit_lu      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| LU520010000000121212 | pm_exceedsWeeklyTransactionLimit_lu | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| LU900010000002222227 | pm_insufficientFunds_lu             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### NL

| Account Number     | Token                               | Description                                                                                                                                          |
| ------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| NL39RABO0300065264 | pm_success_nl                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| NL55RABO0300065267 | pm_successDelayed_nl                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| NL91ABNA0417164300 | pm_failed_nl                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| NL28RABO0300065268 | pm_failedDelayed_nl                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| NL82RABO0300065266 | pm_disputed_nl                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| NL27RABO0000343434 | pm_exceedsWeeklyVolumeLimit_nl      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| NL86RABO0000121212 | pm_exceedsWeeklyTransactionLimit_nl | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| NL55RABO0300065267 | pm_insufficientFunds_nl             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### NO

| Account Number  | Token                               | Description                                                                                                                                          |
| --------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| NO9386011117947 | pm_success_no                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| NO8886011117940 | pm_successDelayed_no                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| NO6686011117948 | pm_failed_no                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| NO6186011117941 | pm_failedDelayed_no                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| NO3986011117949 | pm_disputed_no                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| NO0586010343434 | pm_exceedsWeeklyVolumeLimit_no      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| NO0586010343434 | pm_exceedsWeeklyTransactionLimit_no | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| NO0586012222227 | pm_insufficientFunds_no             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### PT

| Account Number            | Token                               | Description                                                                                                                                          |
| ------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| PT50000201231234567890154 | pm_success_pt                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| PT66000201231234567890157 | pm_successDelayed_pt                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| PT23000201231234567890155 | pm_failed_pt                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| PT39000201231234567890158 | pm_failedDelayed_pt                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| PT93000201231234567890156 | pm_disputed_pt                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| PT05000201230000000343434 | pm_exceedsWeeklyVolumeLimit_pt      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| PT64000201230000000121212 | pm_exceedsWeeklyTransactionLimit_pt | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| PT05000201230000002222227 | pm_insufficientFunds_pt             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### ES

| Account Number           | Token                               | Description                                                                                                                                          |
| ------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| ES0700120345030000067890 | pm_success_es                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| ES2300120345030000067893 | pm_successDelayed_es                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| ES9121000418450200051332 | pm_failed_es                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| ES9300120345030000067894 | pm_failedDelayed_es                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| ES5000120345030000067892 | pm_disputed_es                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| ES1700120345000000343434 | pm_exceedsWeeklyVolumeLimit_es      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| ES7600120345000000121212 | pm_exceedsWeeklyTransactionLimit_es | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| ES1700120345000002222227 | pm_insufficientFunds_es             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### SE

| Account Number           | Token                               | Description                                                                                                                                          |
| ------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| SE3550000000054910000003 | pm_success_se                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| SE5150000000054910000006 | pm_successDelayed_se                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| SE0850000000054910000004 | pm_failed_se                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| SE2450000000054910000007 | pm_failedDelayed_se                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| SE7850000000054910000005 | pm_disputed_se                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| SE2850000000000000343434 | pm_exceedsWeeklyVolumeLimit_se      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| SE8750000000000000121212 | pm_exceedsWeeklyTransactionLimit_se | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| SE2850000000000002222227 | pm_insufficientFunds_se             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### CH

| Account Number        | Token                               | Description                                                                                                                                          |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| CH9300762011623852957 | pm_success_ch                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| CH8656663438253651553 | pm_successDelayed_ch                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| CH5362200119938136497 | pm_failed_ch                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| CH1843597160341964438 | pm_failedDelayed_ch                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| CH1260378413965193069 | pm_disputed_ch                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| CH1800762000000343434 | pm_exceedsWeeklyVolumeLimit_ch      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| CH7700762000000121212 | pm_exceedsWeeklyTransactionLimit_ch | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| CH1800762000002222227 | pm_insufficientFunds_ch             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### GB

| Account Number         | Token                               | Description                                                                                                                                          |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| GB82WEST12345698765432 | pm_success_gb                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| GB98WEST12345698765435 | pm_successDelayed_gb                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| GB55WEST12345698765433 | pm_failed_gb                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| GB71WEST12345698765436 | pm_failedDelayed_gb                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| GB28WEST12345698765434 | pm_disputed_gb                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| GB70WEST12345600343434 | pm_exceedsWeeklyVolumeLimit_gb      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| GB32WEST12345600121212 | pm_exceedsWeeklyTransactionLimit_gb | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| GB70WEST12345602222227 | pm_insufficientFunds_gb             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

## Optional: Set the billing period

When you create a subscription, it automatically sets the billing cycle by default. For example, if a customer subscribes to a monthly plan on September 7, they’re billed on the 7th of every month after that. Some businesses prefer to set the billing cycle manually so that they can charge their customers at the same time each cycle. The [billing cycle anchor](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-billing_cycle_anchor) argument allows you to do this.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  billing_cycle_anchor: 1611008505,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  billing_cycle_anchor: 1611008505,
});
```

Setting the billing cycle manually automatically charges the customer a prorated amount for the time between the subscription being created and the billing cycle anchor. If you don’t want to charge customers for this time, you can set the [proration_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-proration_behavior) argument to `none`. You can also combine the billing cycle anchor with [trial periods](https://docs.stripe.com/billing/subscriptions/sepa-debit.md#trial-periods) to give users free access to your product and then charge them a prorated amount.

## Optional: Subscription trials

Free trials allow customers access to your product for a period of time for free. Using free trials is different from setting [proration_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-proration_behavior) to `none` because you can customize how long the free period lasts. Pass a timestamp in [trial end](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-trial_end) to set the trial period.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  trial_end: 1610403705,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  trial_end: 1610403705,
});
```

You can also combine a [billing cycle anchor](https://docs.stripe.com/billing/subscriptions/sepa-debit.md#billing-cycle) with a free trial. For example, say it’s September 15 and you want to give your customer a free trial for seven days and then start the normal billing cycle on October 1. You can set the free trial to end on September 22 and the billing cycle anchor to October 1. This gives the customer a free trial for seven days and then charges a prorated amount for the time between the trial ending and October 1. On October 1, you charge them the normal subscription amount for their first full billing cycle.

## Optional: Create SEPA Direct Debit payments using other payment methods

> This doc refers to a _Legacy_ (Technology that's no longer recommended) feature (the `idealBank` Element) that’s no longer available in the latest version of Stripe.js. We recommend you use the [Payment Element](https://docs.stripe.com/payments/payment-element.md), a UI component for the web that accepts 40+ payment methods, validates input, and handles errors.

You can create SEPA Direct Debit payments using other payment methods such as [Bancontact](https://docs.stripe.com/payments/bancontact/set-up-payment.md) and [iDEAL](https://docs.stripe.com/payments/ideal/set-up-payment.md). Using these payment methods requires a few additional steps. For iDEAL:

1. Use an [idealBank Element](https://docs.stripe.com/js/elements_object/create_element?type=idealBank) to collect payment information.
1. Confirm the subscription using [confirmIdealPayment](https://docs.stripe.com/js/payment_intents/confirm_ideal_payment) or, for subscriptions that don’t collect a payment up front, [confirmIdealSetup](https://docs.stripe.com/js/setup_intents/confirm_ideal_setup).
1. [List the customer’s payment methods](https://docs.stripe.com/api/payment_methods/customer_list.md), find the SEPA Direct Debit payment method, and set it as the customer’s [default payment method](https://docs.stripe.com/billing/subscriptions/sepa-debit.md#set-default-payment-method).

For Bancontact, substitute:

- `confirmIdealPayment` for [confirmBancontactPayment](https://docs.stripe.com/js/payment_intents/confirm_bancontact_payment)
- `confirmIdealSetup` for [confirmBancontactSetup](https://docs.stripe.com/js/setup_intents/confirm_bancontact_setup)
