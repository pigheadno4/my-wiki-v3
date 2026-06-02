<!-- Source: Stripe Checkout — Manage limited inventory -->
<!-- Fetched: 2026-04-20 -->

# Manage limited inventory

Prevent customers from holding inventory in carts by expiring Checkout Sessions.

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/managing-limited-inventory?payment-ui=stripe-hosted.

For some types of limited-inventory businesses, it’s necessary to prevent customers from reserving items for a long time without completing the purchase. For example, an event ticket seller wants to allow customers only a few minutes to buy their selected tickets before canceling the sale and making those tickets available again. You can cancel a pending sale by expiring the _Checkout Session_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription).

Checkout supports both manual and timed session expiration. When a Checkout Session expires, its [status property](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-status) changes to `expired`.

## Manual expiration

To immediately expire an open Checkout Session and cancel any pending purchase, use the [expire](https://docs.stripe.com/api/checkout/sessions/expire.md) endpoint.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.expire("{{CHECKOUTSESSION_ID}}");
```

## Set an expiration time

When you create a Checkout Session, specify an expiration timestamp by setting the [expires_at](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-expires_at) parameter. The value must be between 30 minutes and 24 hours after the current time. If you don’t specify `expires_at`, the default value is 24 hours after the current time.

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

## Return items to your inventory

When a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) expires, Stripe sends the `checkout.session.expired` event. Configure your webhook endpoint to listen for this event so your webhook handler can return to inventory any items reserved in the expired session. For more information, see [Expire a Session](https://docs.stripe.com/api/checkout/sessions/expire.md).

# Embedded page

> This is a Embedded page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/managing-limited-inventory?payment-ui=embedded-form.

For some types of limited-inventory businesses, it’s necessary to prevent customers from reserving items for a long time without completing the purchase. For example, an event ticket seller wants to allow customers only a few minutes to buy their selected tickets before canceling the sale and making those tickets available again. You can cancel a pending sale by expiring the _Checkout Session_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription).

Checkout supports both manual and timed session expiration. When a Checkout Session expires, its [status property](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-status) changes to `expired`.

## Manual expiration

To immediately expire an open Checkout Session and cancel any pending purchase, use the [expire](https://docs.stripe.com/api/checkout/sessions/expire.md) endpoint.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.expire("{{CHECKOUTSESSION_ID}}");
```

## Set an expiration time

When you create a Checkout Session, specify an expiration timestamp by setting the [expires_at](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-expires_at) parameter. The value must be between 30 minutes and 24 hours after the current time. If you don’t specify `expires_at`, the default value is 24 hours after the current time.

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

## Return items to your inventory

When a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) expires, Stripe sends the `checkout.session.expired` event. Configure your webhook endpoint to listen for this event so your webhook handler can return to inventory any items reserved in the expired session. For more information, see [Expire a Session](https://docs.stripe.com/api/checkout/sessions/expire.md).
