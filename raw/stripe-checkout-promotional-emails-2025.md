<!-- Source: Stripe Checkout — Collect consent for promotional emails -->
<!-- Fetched: 2026-04-20 -->

# Collect consent for promotional emails

Learn how to collect permission from customers so that you can send them promotional emails.

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/promotional-emails-consent?payment-ui=stripe-hosted.

Promotional emails are often sent to inform customers of new products and to share coupons and discounts. For example, you can use them to subscribe customers to company newsletters or [send cart abandonment emails](https://docs.stripe.com/payments/checkout/abandoned-carts.md).
![Collect consent for promotional emails](assets/stripe-checkout-promotional-consent.png)

Collect consent from customers to send them promotional emails

To protect consumers from unwanted spam, customers must agree to receiving promotional emails before you can contact them. Checkout with a hosted page or embedded page helps you collect the necessary consent, where applicable, to send promotional emails. Learn more about [promotional email requirements](https://docs.stripe.com/payments/checkout/compliant-promotional-emails.md).

## Collect consent

You can collect promotional email consent with Stripe Checkout when you create the session.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  customer: "{{CUSTOMER_ID}}",
  mode: "payment",
  success_url: "https://example.com/success",
  consent_collection: {
    promotions: "auto",
  },
});
```

When `consent_collection.promotions='auto'`, Checkout dynamically displays a checkbox for collecting the customer’s consent to promotional content.

> When the checkbox is shown, the default state depends on the customer’s country and the country your business is based in. Data privacy laws vary by jurisdiction, so Checkout disables or limits this feature when local regulations prohibit it.

## Store consent and email address

The Checkout Session’s [consent](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-consent) attribute records whether or not the session collected promotional consent from the customer.

As customers complete purchases, keep track of which customers consent to promotional content. You can create or update an existing _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) handler to do this. Listen to the `checkout.session.completed` event, check for the `consent.promotions` status, and then store email addresses for customers who give consent.

#### Node.js

```javascript
// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = "whsec_...";

// Using Express
const app = require("express")();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require("body-parser");
const recordPromotionalEmailConsent = (email, promoConsent) => {
  // TODO: fill me in
  console.log("Recording promotional email consent", email, promoConsent);
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
    } // Handle the checkout.session.completed event
    if (event.type === "checkout.session.completed") {
      const session = event.data.object;
      const promoConsent = session.consent?.promotions;
      const email = session.customer_details.email;

      // Record whether or not the customer has agreed to receive promotional emails
      recordPromotionalEmailConsent(email, promoConsent);

      // Handle order fulfillment
    }
    response.status(200).end();
  },
);
```

After you’ve configured Checkout to collect consent for sending customers promotional content, you can [recover abandoned carts](https://docs.stripe.com/payments/checkout/abandoned-carts.md) by following up with leads for customers that left the checkout flow before completing payment.

# Embedded page

> This is a Embedded page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/promotional-emails-consent?payment-ui=embedded-form.

Promotional emails are often sent to inform customers of new products and to share coupons and discounts. For example, you can use them to subscribe customers to company newsletters or [send cart abandonment emails](https://docs.stripe.com/payments/checkout/abandoned-carts.md).
![Collect consent for promotional emails](assets/stripe-checkout-promotional-consent.png)

Collect consent from customers to send them promotional emails

To protect consumers from unwanted spam, customers must agree to receiving promotional emails before you can contact them. Checkout with a hosted page or embedded page helps you collect the necessary consent, where applicable, to send promotional emails. Learn more about [promotional email requirements](https://docs.stripe.com/payments/checkout/compliant-promotional-emails.md).

## Collect consent

You can collect promotional email consent with Stripe Checkout when you create the session.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  customer: "{{CUSTOMER_ID}}",
  mode: "payment",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
  consent_collection: {
    promotions: "auto",
  },
});
```

When `consent_collection.promotions='auto'`, Checkout dynamically displays a checkbox for collecting the customer’s consent to promotional content.

> When the checkbox is shown, the default state depends on the customer’s country and the country your business is based in. Data privacy laws vary by jurisdiction, so Checkout disables or limits this feature when local regulations prohibit it.

## Store consent and email address

The Checkout Session’s [consent](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-consent) attribute records whether or not the session collected promotional consent from the customer.

As customers complete purchases, keep track of which customers consent to promotional content. You can create or update an existing _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) handler to do this. Listen to the `checkout.session.completed` event, check for the `consent.promotions` status, and then store email addresses for customers who give consent.

#### Node.js

```javascript
// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = "whsec_...";

// Using Express
const app = require("express")();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require("body-parser");
const recordPromotionalEmailConsent = (email, promoConsent) => {
  // TODO: fill me in
  console.log("Recording promotional email consent", email, promoConsent);
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
    } // Handle the checkout.session.completed event
    if (event.type === "checkout.session.completed") {
      const session = event.data.object;
      const promoConsent = session.consent?.promotions;
      const email = session.customer_details.email;

      // Record whether or not the customer has agreed to receive promotional emails
      recordPromotionalEmailConsent(email, promoConsent);

      // Handle order fulfillment
    }
    response.status(200).end();
  },
);
```

After you’ve configured Checkout to collect consent for sending customers promotional content, you can [recover abandoned carts](https://docs.stripe.com/payments/checkout/abandoned-carts.md) by following up with leads for customers that left the checkout flow before completing payment.
