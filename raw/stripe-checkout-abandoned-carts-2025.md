<!-- Source: Stripe Checkout — Recover abandoned carts -->
<!-- Fetched: 2026-04-20 -->

# Recover abandoned carts

Learn how to recover abandoned Checkout pages and boost revenue.

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/abandoned-carts?payment-ui=stripe-hosted.

In e-commerce, [cart abandonment](https://docs.stripe.com/payments/checkout/compliant-promotional-emails.md) is when customers leave the checkout flow before completing their purchase. To help bring customers back to Checkout, create a recovery flow where you follow up with customers over email to complete their purchases.

Cart abandonment emails fall into the broader category of _promotional emails_, which includes emails that inform customers of new products and that share coupons and discounts. Customers must agree to receive promotional emails before you can contact them. Checkout helps you:

1. Collect consent from customers to send them promotional emails.
1. Get notified when customers abandon Checkout so you can send cart abandonment emails.

## Collect promotional consent

Configure Checkout to [collect consent for promotional content](https://docs.stripe.com/payments/checkout/promotional-emails-consent.md). If you collect the customer’s email address and request consent for promotional content before redirecting to Checkout, you can skip using `consent_collection[promotions]`.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  mode: "payment",
  success_url: "https://example.com/success",
  consent_collection: {
    promotions: "auto",
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
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

## Configure recovery

A Checkout Session becomes abandoned when it reaches its [expires_at](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-expires_at) timestamp and the customer hasn’t completed checking out. When this occurs, the session is no longer accessible and Stripe fires the `checkout.session.expired` _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), which you can listen to and try to bring the customer back to a new Checkout Session to complete their purchase. To use this feature, enable `after_expiration.recovery` when you create the session.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "payment",
  success_url: "https://example.com/success",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  consent_collection: {
    promotions: "auto",
  },
  after_expiration: {
    recovery: {
      enabled: true,
      allow_promotion_codes: true,
    },
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "payment",
  success_url: "https://example.com/success",
  customer: "{{CUSTOMER_ID}}",
  consent_collection: {
    promotions: "auto",
  },
  after_expiration: {
    recovery: {
      enabled: true,
      allow_promotion_codes: true,
    },
  },
});
```

## Get notified of abandonment

Listen to the `checkout.session.expired` webhook to be notified when customers abandon Checkout and sessions expire. When the session expires with recovery enabled, the webhook payload contains [after_expiration](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-after_expiration-recovery), which includes a URL denoted by `after_expiration.recovery.url` that you can embed in cart abandonment emails. When the customer opens this URL, **it creates a new Checkout Session that’s a copy of the original expired session**. The customer uses this copied session to complete the purchase.

> For security purposes, the recovery URL for a session is usable for 30 days, denoted by the `after_expiration.recovery.expires_at` timestamp.

```json
{
  "id": "evt_123456789",
  "object": "event",
  "type": "checkout.session.expired",
  // ...other webhook attributes
  "data": {
    "object": {
      "id": "cs_12356789",
      "object": "checkout.session",
      // ...other Checkout Session attributes"consent_collection": {
        "promotions": "auto",
      },
      "consent": {
        "promotions": "opt_in"
      },
      "after_expiration": {
        "recovery": {
          "enabled": true,
          "url": "https://buy.stripe.com/r/live_asAb1724",
          "allow_promotion_code": true,
          "expires_at": 1622908282,
        }
      }
    }
  }
}
```

## Send recovery emails

To send recovery emails, create a webhook handler for expired sessions and send an email that embeds the session’s recovery URL. A customer might abandon multiple Checkout Sessions, each triggering its own `checkout.session.expired` event so make sure to record when you send recovery emails to customers and avoid spamming them.

#### Node.js

```javascript
// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = "whsec_...";

// Using Express
const app = require("express")();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require("body-parser");
const sendRecoveryEmail = (email, recoveryUrl) => {
  // TODO: fill me in
  console.log("Sending recovery email", email, recoveryUrl);
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
    } // Handle the checkout.session.expired event
    if (event.type === "checkout.session.expired") {
      const session = event.data.object;

      // When a Checkout Session expires, the customer's email isn't returned in
      // the webhook payload unless they give consent for promotional content
      const email = session.customer_details?.email;
      const recoveryUrl = session.after_expiration?.recovery?.url;

      // Do nothing if the Checkout Session has no email or recovery URL
      if (!email || !recoveryUrl) {
        return response.status(200).end();
      }

      // Check if the customer has consented to promotional emails and
      // avoid spamming people who abandon Checkout multiple times
      if (
        session.consent?.promotions === "opt_in" &&
        !hasSentRecoveryEmailToCustomer(email)
      ) {
        sendRecoveryEmail(email, recoveryUrl);
      }
    }
    response.status(200).end();
  },
);
```

## Optional: Adjust session expiration

By default, Checkout Sessions expire 24 hours after they’re created, but you can shorten the expiration time by setting `expires_at` to get notified of abandonment sooner. The minimum `expires_at` allowed is 30 minutes from when the session is created.

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer_account: "{{CUSTOMER_ACCOUNT_ID}}",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "payment",
  success_url: "https://example.com/success",
  expires_at: Math.floor(Date.now() / 1000) + 3600 * 2, // Configured to expire after 2 hours
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer: "{{CUSTOMER_ID}}",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "payment",
  success_url: "https://example.com/success",
  expires_at: Math.floor(Date.now() / 1000) + 3600 * 2, // Configured to expire after 2 hours
});
```

## Optional: Track conversion

When the customer opens the recovery URL for an expired Checkout Session, it creates a new Checkout Session that’s a copy of the abandoned session.

To verify whether a recovery email resulted in a successful conversion, check the [recovered_from](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-recovered_from) attribute in the `checkout.session.completed` webhook for the new Checkout Session. This attribute references the original session that expired.

#### Node.js

```javascript
// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = "whsec_...";

// Using Express
const app = require("express")();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require("body-parser");
const logRecoveredCart = (sessionId, recoveredFromSessionId) => {
  // TODO: fill me in
  console.log("Recording recovered session", sessionId, recoveredFromSessionId);
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

      const recoveryFromSessionId = session.recovered_from;
      if (recoveryFromSessionId) {
        // Log relationship between successfully completed session and abandoned session
        logRecoveredCart(session.id, recoveryFromSessionId);
      }

      // Handle order fulfillment
    }
    response.status(200).end();
  },
);
```

## Optional: Offer promotion codes in recovery emails

Offering [discounts](https://docs.stripe.com/payments/checkout/discounts.md) to customers who abandon their carts can incentivize them to complete their purchase. You can configure whether the Checkout Session created by the recovery URL has an option for promotion codes by setting `after_expiration.recovery.allow_promotion_code`.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "payment",
  success_url: "https://example.com/success",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  consent_collection: {
    promotions: "auto",
  },
  after_expiration: {
    recovery: {
      enabled: true,
      allow_promotion_codes: true,
    },
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "payment",
  success_url: "https://example.com/success",
  customer: "{{CUSTOMER_ID}}",
  consent_collection: {
    promotions: "auto",
  },
  after_expiration: {
    recovery: {
      enabled: true,
      allow_promotion_codes: true,
    },
  },
});
```

# Embedded page

> This is a Embedded page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/abandoned-carts?payment-ui=embedded-form.

In e-commerce, [cart abandonment](https://docs.stripe.com/payments/checkout/compliant-promotional-emails.md) is when customers leave the checkout flow before completing their purchase. To help bring customers back to Checkout, create a recovery flow where you follow up with customers over email to complete their purchases.

Cart abandonment emails fall into the broader category of _promotional emails_, which includes emails that inform customers of new products and that share coupons and discounts. Customers must agree to receive promotional emails before you can contact them. Checkout helps you:

1. Collect consent from customers to send them promotional emails.
1. Get notified when customers abandon Checkout so you can send cart abandonment emails.

## Collect promotional consent

Configure Checkout to [collect consent for promotional content](https://docs.stripe.com/payments/checkout/promotional-emails-consent.md). If you collect the customer’s email address and request consent for promotional content before they see the embedded form, you can skip using `consent_collection[promotions]`.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  mode: "payment",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
  consent_collection: {
    promotions: "auto",
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
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

## Configure recovery

A Checkout Session becomes abandoned when it reaches its [expires_at](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-expires_at) timestamp and the buyer hasn’t completed checking out. When this occurs, the session is no longer accessible and Stripe fires the `checkout.session.expired` _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), which you can listen to and try to bring the customer back to a new Checkout Session to complete their purchase. To use this feature, enable `after_expiration.recovery` when you create the session.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "payment",
  ui_mode: "embedded_page",
  return_url:
    "https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID}",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  consent_collection: {
    promotions: "auto",
  },
  after_expiration: {
    recovery: {
      enabled: true,
      allow_promotion_codes: true,
    },
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "payment",
  ui_mode: "embedded_page",
  return_url:
    "https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID}",
  customer: "{{CUSTOMER_ID}}",
  consent_collection: {
    promotions: "auto",
  },
  after_expiration: {
    recovery: {
      enabled: true,
      allow_promotion_codes: true,
    },
  },
});
```

## Get notified of abandonment

Listen to the `checkout.session.expired` webhook to be notified when customers abandon Checkout and sessions expire. When the session expires with recovery enabled, the webhook payload contains [after_expiration](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-after_expiration-recovery), which includes a URL denoted by `after_expiration.recovery.url` that you can embed in cart abandonment emails. When the customer opens this URL, **it creates a new Checkout Session that’s a copy of the original expired session**. The customer uses this copied session to complete the purchase.

> For security purposes, the recovery URL for a session is usable for 30 days, denoted by the `after_expiration.recovery.expires_at` timestamp.

```json
{
  "id": "evt_123456789",
  "object": "event",
  "type": "checkout.session.expired",
  // ...other webhook attributes
  "data": {
    "object": {
      "id": "cs_12356789",
      "object": "checkout.session",
      // ...other Checkout Session attributes"consent_collection": {
        "promotions": "auto",
      },
      "consent": {
        "promotions": "opt_in"
      },
      "after_expiration": {
        "recovery": {
          "enabled": true,
          "url": "https://buy.stripe.com/r/live_asAb1724",
          "allow_promotion_code": true,
          "expires_at": 1622908282,
        }
      }
    }
  }
}
```

## Send recovery emails

To send recovery emails, create a webhook handler for expired sessions and send an email that embeds the session’s recovery URL. A customer might abandon multiple Checkout Sessions, each triggering its own `checkout.session.expired` event so make sure to record when you send recovery emails to customers and avoid spamming them.

#### Node.js

```javascript
// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = "whsec_...";

// Using Express
const app = require("express")();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require("body-parser");
const sendRecoveryEmail = (email, recoveryUrl) => {
  // TODO: fill me in
  console.log("Sending recovery email", email, recoveryUrl);
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
    } // Handle the checkout.session.expired event
    if (event.type === "checkout.session.expired") {
      const session = event.data.object;

      // When a Checkout Session expires, the customer's email isn't returned in
      // the webhook payload unless they give consent for promotional content
      const email = session.customer_details?.email;
      const recoveryUrl = session.after_expiration?.recovery?.url;

      // Do nothing if the Checkout Session has no email or recovery URL
      if (!email || !recoveryUrl) {
        return response.status(200).end();
      }

      // Check if the customer has consented to promotional emails and
      // avoid spamming people who abandon Checkout multiple times
      if (
        session.consent?.promotions === "opt_in" &&
        !hasSentRecoveryEmailToCustomer(email)
      ) {
        sendRecoveryEmail(email, recoveryUrl);
      }
    }
    response.status(200).end();
  },
);
```

## Optional: Adjust session expiration

By default, Checkout Sessions expire 24 hours after they’re created, but you can shorten the expiration time by setting `expires_at` to get notified of abandonment sooner. The minimum `expires_at` allowed is 30 minutes from when the session is created.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  customer: "{{CUSTOMER_ID}}",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "payment",
  ui_mode: "embedded_page",
  return_url:
    "https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID}",
  expires_at: Math.floor(Date.now() / 1000) + 3600 * 2, // Configured to expire after 2 hours
});
```

## Optional: Track conversion

When the customer opens the recovery URL for an expired Checkout Session, it creates a new Checkout Session that’s a copy of the abandoned session.

To verify whether a recovery email resulted in a successful conversion, check the [recovered_from](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-recovered_from) attribute in the `checkout.session.completed` webhook for the new Checkout Session. This attribute references the original session that expired.

#### Node.js

```javascript
// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = "whsec_...";

// Using Express
const app = require("express")();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require("body-parser");
const logRecoveredCart = (sessionId, recoveredFromSessionId) => {
  // TODO: fill me in
  console.log("Recording recovered session", sessionId, recoveredFromSessionId);
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

      const recoveryFromSessionId = session.recovered_from;
      if (recoveryFromSessionId) {
        // Log relationship between successfully completed session and abandoned session
        logRecoveredCart(session.id, recoveryFromSessionId);
      }

      // Handle order fulfillment
    }
    response.status(200).end();
  },
);
```

## Optional: Offer promotion codes in recovery emails

Offering [discounts](https://docs.stripe.com/payments/checkout/discounts.md) to customers who abandon their carts can incentivize them to complete their purchase. You can configure whether the Checkout Session created by the recovery URL has an option for promotion codes by setting `after_expiration.recovery.allow_promotion_code`.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "payment",
  ui_mode: "embedded_page",
  return_url:
    "https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID}",
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  consent_collection: {
    promotions: "auto",
  },
  after_expiration: {
    recovery: {
      enabled: true,
      allow_promotion_codes: true,
    },
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  mode: "payment",
  ui_mode: "embedded_page",
  return_url:
    "https://example.com/checkout/return?session_id={CHECKOUT_SESSION_ID}",
  customer: "{{CUSTOMER_ID}}",
  consent_collection: {
    promotions: "auto",
  },
  after_expiration: {
    recovery: {
      enabled: true,
      allow_promotion_codes: true,
    },
  },
});
```
