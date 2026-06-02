<!-- Source: Stripe Checkout — Collect customer names -->
<!-- Fetched: 2026-04-20 -->

# Collect customer names

Collect business and individual names as first-class fields on Checkout.

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/name-collection?payment-ui=stripe-hosted.

You can enable name collection on the payment form to collect business or individual names from your customers. The information is available after the session is complete.

These _first-class_ (First-class fields are prominent input fields that appear at the top level of the payment form and API, rather than being grouped within other sections such as billing or shipping details) names are separate from the names collected within billing and shipping information, and always appear as top-level name fields on the payment form if enabled.
![First-class name fields in the Checkout form](assets/stripe-checkout-name-fields.png)

Checkout adds top-level name fields to the payment form within contact details.

## Enable name collection

Create a Checkout Session while specifying name collection settings. To enable name collection, configure the [name_collection](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-name_collection) object when creating a Checkout Session. You can collect business names, individual names, or both, and set each field as either required or optional based on your needs.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  success_url: "https://example.com/success",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  name_collection: {
    business: {
      enabled: true,
    },
    individual: {
      enabled: true,
      optional: true,
    },
  },
});
```

> When you set business name collection to required, express checkout and one-click buttons, such as Apple Pay, move to the bottom of the payment form or are disabled.

## Retrieve the collected names

After the session, you can retrieve customers’ business or individual names from the resulting _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments), or _Checkout Session_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription) objects:

### On the Customer

Checkout saves collected names onto their respective [business_name](https://docs.stripe.com/api/customers/object.md#customer_object-business_name) or [individual_name](https://docs.stripe.com/api/customers/object.md#customer_object-individual_name) properties of the Customer object, which you can access programmatically by either fetching the Customer object directly with the [API](https://docs.stripe.com/api/customers/retrieve.md), or by listening for the [customer.created](https://docs.stripe.com/api/events/types.md#event_types-customer.created) event in a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests).

The Customer object’s [name](https://docs.stripe.com/api/customers/object.md#customer_object-name) will also be set to the business_name or individual_name, in that order.

```json
{
  "object": {
    "id": "cus_HQmikpKnGHkNwW",
    "object": "customer",
    ...
    "name": "Stripe, Inc.""business_name": "Stripe, Inc."
    ..."individual_name": "Jenny Rosen"
    ...
  }
}
```

You can also view the customer names in the [Dashboard](https://dashboard.stripe.com/customers).

### On the Checkout Session

The customer’s names are also saved in the `collected_information` and `customer_details` hash of the Checkout Session object, under:

- [collected_information.business_name](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-collected_information-business_name) and [collected_information.individual_name](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-collected_information-individual_name)
- [customer_details.business_name](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-customer_details-business_name) and [customer_details.individual_name](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-customer_details-individual_name)

```json
{
  "object": {
    "id": "cs_test_a1dJwt0TCJTBsDkbK7RcoyJ91vJxe2Y",
    "object": "checkout.session",
    ...
    "collected_information": {"business_name": "Stripe, Inc.",
      "individual_name": "Jenny Rosen"
    },
    ...
    "customer": "cus_id_of_new_customer",
    "customer_details": {
      ..."business_name": "Stripe, Inc.",
      "individual_name": "Jenny Rosen",
      "name": "Stripe, Inc."
    },
    ...
  }
}
```

After each successful Checkout Session, Stripe sends the [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) event containing the Checkout Session object and collected values, which you can listen for in a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests).

# Embedded Page

> This is a Embedded Page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/name-collection?payment-ui=embedded-form.

You can enable name collection on the payment form to collect business or individual names from your customers. The information is available after the session is complete.

These _first-class_ (First-class fields are prominent input fields that appear at the top level of the payment form and API, rather than being grouped within other sections such as billing or shipping details) names are separate from the names collected within billing and shipping information, and always appear as top-level name fields on the payment form if enabled.
![First-class name fields in the Checkout form](assets/stripe-checkout-name-fields.png)

Checkout adds top-level name fields to the payment form within contact details.

## Enable name collection

Create a Checkout Session while specifying name collection settings. To enable name collection, configure the [name_collection](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-name_collection) object when creating a Checkout Session. You can collect business names, individual names, or both, and set each field as either required or optional based on your needs.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  name_collection: {
    business: {
      enabled: true,
    },
    individual: {
      enabled: true,
      optional: true,
    },
  },
});
```

> When you set business name collection to required, express checkout and one-click buttons, such as Apple Pay, move to the bottom of the payment form or are disabled.

## Retrieve the collected names

After the session, you can retrieve customers’ business or individual names from the resulting _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments), or _Checkout Session_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription) objects:

### On the Customer

Checkout saves collected names onto their respective [business_name](https://docs.stripe.com/api/customers/object.md#customer_object-business_name) or [individual_name](https://docs.stripe.com/api/customers/object.md#customer_object-individual_name) properties of the Customer object, which you can access programmatically by either fetching the Customer object directly with the [API](https://docs.stripe.com/api/customers/retrieve.md), or by listening for the [customer.created](https://docs.stripe.com/api/events/types.md#event_types-customer.created) event in a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests).

The Customer object’s [name](https://docs.stripe.com/api/customers/object.md#customer_object-name) will also be set to the business_name or individual_name, in that order.

```json
{
  "object": {
    "id": "cus_HQmikpKnGHkNwW",
    "object": "customer",
    ...
    "name": "Stripe, Inc.""business_name": "Stripe, Inc."
    ..."individual_name": "Jenny Rosen"
    ...
  }
}
```

You can also view the customer names in the [Dashboard](https://dashboard.stripe.com/customers).

### On the Checkout Session

The customer’s names are also saved in the `collected_information` and `customer_details` hash of the Checkout Session object, under:

- [collected_information.business_name](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-collected_information-business_name) and [collected_information.individual_name](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-collected_information-individual_name)
- [customer_details.business_name](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-customer_details-business_name) and [customer_details.individual_name](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-customer_details-individual_name)

```json
{
  "object": {
    "id": "cs_test_a1dJwt0TCJTBsDkbK7RcoyJ91vJxe2Y",
    "object": "checkout.session",
    ...
    "collected_information": {"business_name": "Stripe, Inc.",
      "individual_name": "Jenny Rosen"
    },
    ...
    "customer": "cus_id_of_new_customer",
    "customer_details": {
      ..."business_name": "Stripe, Inc.",
      "individual_name": "Jenny Rosen",
      "name": "Stripe, Inc."
    },
    ...
  }
}
```

After each successful Checkout Session, Stripe sends the [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) event containing the Checkout Session object and collected values, which you can listen for in a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests).
