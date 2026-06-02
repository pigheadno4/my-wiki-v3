<!-- Source URL: https://docs.stripe.com/payments/klarna/set-up-future-payments -->
<!-- Fetched: 2026-05-06 -->

# Set up future Klarna payments

Learn how to save Klarna details and charge your customers later.

You can save Klarna as a customer’s *payment method* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) and charge future payments to support:

- Automatic payment for *subscriptions* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis), with or without a [free trial](https://docs.stripe.com/billing/subscriptions/trials.md).
- Automatic payment for subscriptions for orders that also include non-subscription products.
- Saving Klarna to a wallet to streamline future *on-demand* (When a customer stores their payment method with a business, they can make on-demand future purchases without re-authenticating, such as ordering a ride in their ride-share app) purchases without requiring customer re-authentication.

This guide explains how to save Klarna as a payment method that you can charge immediately or later. This guide isn’t for integrations that use [Stripe Billing](https://docs.stripe.com/billing.md). If you use Stripe Billing, see [Klarna for subscriptions](https://docs.stripe.com/billing/subscriptions/klarna.md).

> #### Available Klarna payment options vary by use case and buyer country
>
> See which [payment options](https://docs.stripe.com/payments/klarna.md#payment-options) are available for your customers before you start your integration.

We recommend using [Stripe Checkout](https://docs.stripe.com/payments/checkout.md) to save Klarna as a payment method.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/klarna/set-up-future-payments?payment-ui=checkout.

The first part of this guide explains how to use [Stripe Checkout](https://docs.stripe.com/payments/checkout.md) to save Klarna as a payment method. The last step explains how to charge the saved payment method for a subscription or *on-demand* (When a customer stores their payment method with a business, they can make on-demand future purchases without re-authenticating, such as ordering a ride in their ride-share app) payment.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer before setup [Server-side]

To reuse a Klarna payment method for future payments, you must attach it to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a Customer object when your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a Checkout Session [Client-side] [Server-side]

Before you can accept Klarna payments, your customer must authorize you to use their Klarna account for future payments through Stripe Checkout.

Add an **Authorize** button to your site that calls a server-side endpoint to create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md).

```html
<html>
  <head>
    <title>Authorize</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Authorize</button>
    </form>
  </body>
</html>
```

#### Subscription

You should pass subscription details when you use Checkout to set up a subscription.

Passing in subscription details:

- Ensures your customers have access to all applicable [Klarna payment options](https://docs.stripe.com/payments/klarna.md#payment-options), including Pay in 3 or 4, which is only available for subscriptions that have specific lengths.
- Reduces support rates and customer dropouts due to unclear purchase details in the Klarna app, where Klarna renders subscription data for your customers.

Use the [payment_method_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-klarna) parameter to pass in subscription details. The subscription [reference](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-klarna-subscriptions-reference) is an arbitrary identifier you choose that isn’t visible to customers (for example, `GYM_ANNUAL_MEMBERSHIP` or `ID_123`).

> #### Use the same reference to charge the saved payment method
>
> When you charge the saved payment method, use the same subscription reference. The reference value needs to match the value of the `amount_details[line_items][payment_method_options][klarna][subscription_reference]` field, if you integration uses it later. If you don’t match the value, you receive an error.

The example below shows how to pass details for an annual subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "setup",
  customer: "{{CUSTOMER_ID}}",
  currency: "usd",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          name: "Customer-facing name for subscription",
          interval: "year",
          next_billing: {
            amount: 10000,
            date: "2026-01-01",
          },
        },
      ],
    },
  },
});
```

#### On-demand payments

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "setup",
  customer: "{{CUSTOMER_ID}}",
  currency: "usd",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});
```

After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

## Handle redirect back from Checkout [Client-side] [Server-side]

When your customer provides their payment method details, they’re redirected to the `success_url`, a page on your website that informs them that they saved their payment method successfully. Make the Session ID available on your success page by including the `{CHECKOUT_SESSION_ID}` template variable in the `success_url` as in the above example.

> Don’t rely on the redirect to the `success_url` alone for detecting payment initiation, because:
>
> - Malicious users could directly access the `success_url` without paying and gain access to your goods or services.

- After a successful payment, customers might close their browser tab before they’re redirected to the `success_url`.

## Retrieve the payment method [Server-side]

After a customer submits their payment details, retrieve the [PaymentMethod](https://docs.stripe.com/payments/payment-methods.md) object. A *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) stores the customer’s Klarna account information for future payments. You can retrieve the PaymentMethod synchronously using the `success_url` or asynchronously using *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests).

The decision to retrieve the PaymentMethod synchronously or asynchronously depends on your tolerance for dropoff, as customers might not always reach the `success_url` after a successful payment (for example, it’s possible for them to close their browser tab before the redirect occurs). Using webhooks prevents your integration from experiencing this form of dropoff.

#### Webhooks

Handle `checkout.session.completed` webhooks, which contain a Session object. To learn more, see [setting up webhooks](https://docs.stripe.com/webhooks.md). The following example is a `checkout.session.completed` response.

```json
{
  "id": "evt_1Ep24XHssDVaQm2PpwS19Yt0",
  "object": "event",
  "api_version": "2019-03-14",
  "created": 1561420781,
  "data": {
    "object": {
      "id": "cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k",
      "object": "checkout.session",
      "billing_address_collection": null,
      "client_reference_id": null,
      "customer": null,
      "customer_email": null,
      "display_items": [],
      "mode": "setup",
      "setup_intent": "seti_1EzVO3HssDVaQm2PJjXHmLlM",
      "submit_type": null,
      "subscription": null,
      "success_url": "https://example.com/success"
    }
  },
  "livemode": false,
  "pending_webhooks": 1,
  "request": {
    "id": null,
    "idempotency_key": null
  },
  "type": "checkout.session.completed"
}
```

Note the value of the `setup_intent` key, which is the ID for the SetupIntent created with the Checkout Session. A [SetupIntent](https://docs.stripe.com/payments/setup-intents.md) is an object used to set up the customer Klarna account information for future payments. [Retrieve](https://docs.stripe.com/api/setup_intents/retrieve.md) the SetupIntent object with the ID. The returned object contains the `payment_method` ID.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.retrieve(
  "seti_1EzVO3HssDVaQm2PJjXHmLlM",
);
```

#### Success URL

Obtain the `session_id` from the URL when a user redirects back to your site and [retrieve](https://docs.stripe.com/api/checkout/sessions/retrieve.md) the Session object.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.retrieve("{{SESSION_ID}}", {
  expand: ["setup_intent"],
});
```

> To ensure the `session_id` is available from the URL, include the `session_id={CHECKOUT_SESSION_ID}` template variable in the `success_url` when creating the Checkout Session.

Note the SetupIntent created during the Checkout Session. A [SetupIntent](https://docs.stripe.com/payments/setup-intents.md) is an object used to set up the customer Klarna account information for future payments. The returned object contains the `payment_method` ID.

## Handle post-setup events [Server-side]

Use a method such as [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm that the customer authorized the billing agreement. Don’t rely on your customer to return to the payment status page.

When a customer successfully authorizes the billing agreement, Stripe emits a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event and the Intent status transitions to `succeeded`. Store the resulting [payment_method](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method) ID to make payments using the saved PaymentMethod later.

If a customer doesn’t successfully authorize the billing agreement, Stripe emits a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event and the Intent status returns to `requires_payment_method`.

## Use the payment method for future payments [Server-side]

#### Subscription renewal

When you’re ready to charge your customer off-session, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during this payment attempt, which causes the PaymentIntent to throw an error if authentication is required.
- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the ID of the PaymentMethod and [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the Customer.
- Specify a [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) to indicate where Stripe needs to redirect the customer after they return from Klarna’s website.

Send subscription details and line items with each renewal. Use the same `reference` for your subscription as you did when setting up the payment method. If the subscription details have changed since you saved the payment method, send the new information with the same `reference`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  confirm: true,
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: true,
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription renewal",
        quantity: 1,
        unit_cost: 5000,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "year",
        },
      ],
    },
  },
});
```

#### On-demand payment

When you’re ready to charge your customer, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `false` to indicate that the customer is in a checkout flow during this payment attempt. If an error occurs, such as one that requires authentication, the customer is redirected to Klarna’s page to authenticate or resolve the issue.
- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the ID of the PaymentMethod and [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the Customer.

The example below includes optional details using [payment_method_options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options) to help improve Klarna underwriting and authorization rates. This includes details on how this saved Klarna payment method should be used in the future, such as expected future order amounts and frequency of payments.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  confirm: true,
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: false,
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription",
        quantity: 1,
        unit_cost: 1099,
        payment_method_options: {
          klarna: {
            subscription_reference: "{{SUBSCRIPTION_ID}}",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      on_demand: {
        average_amount: 1000,
        minimum_amount: 100,
        maximum_amount: 10000,
        interval: "year",
        interval_count: 1,
      },
    },
  },
});
```

## Handle reusable payment method revocation [Server-side]

You can revoke a reusable payment method in two ways:

- A customer can deactivate a reusable payment method in the Klarna mobile application. In this case, Stripe sends you a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) event. To handle this, subscribe to [webhook](https://docs.stripe.com/webhooks.md) events, and call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to deactivate it.
- A customer can also deactivate a reusable payment method on your UI, if supported. In this scenario, your server can call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to handle the deactivation.

In both cases, after you call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md), Stripe sends you a [payment_method.detached](https://docs.stripe.com/api/events/types.md#event_types-payment_method.detached) event.

## Test your integration

When testing your Checkout integration, select Klarna as the payment method and click the **Save** button. In a testing environment, you can then simulate different outcomes within Klarna’s redirect.

> Klarna uses cookies for session tracking. To test different customer locations, log out of the Klarna sandbox from the previous session and use the relevant triggers.

Below, we have specially selected test data for the currently supported customer countries. In a sandbox, Klarna approves or denies a transaction based on the supplied email address.

#### Australia

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 10-07-1970        | 03-05-1994               |
| First Name    | Test              | John                     |
| Last Name     | Person-au         | snow                     |
| Street        | Wharf St          | Silverwater Rd           |
| House number  | 4                 | 1-5                      |
| Postal Code   | 4877              | 2128                     |
| City          | Port Douglas      | Silverwater              |
| Region        | QLD               | NSW                      |
| Phone         | +61473752244      | +61473763254             |
| Email         | customer@email.au | customer+denied@email.au |

#### Austria

|               | Approved           | Denied                   |
| ------------- | ------------------ | ------------------------ |
| Date of Birth | 10-07-1970         | 10-07-1970               |
| First Name    | Test               | Test                     |
| Last Name     | Person-at          | Person-at                |
| Email         | customer@email.at  | customer+denied@email.at |
| Street        | Mariahilfer Straße | Mariahilfer Straße       |
| House number  | 47                 | 47                       |
| City          | Wien               | Wien                     |
| Postal code   | 1060               | 1060                     |
| Phone         | +4306762600456     | +4306762600745           |

#### Belgium

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 10-07-1970        | 10-07-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-be         | Person-be                |
| Email         | customer@email.be | customer+denied@email.be |
| Street        | Grote Markt       | Grote Markt              |
| House number  | 1                 | 1                        |
| City          | Brussel           | Brussel                  |
| Postal code   | 1000              | 1000                     |
| Phone         | +32485121291      | +32485212123             |

#### Canada

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 10-07-1970        | 10-07-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-ca         | Person-ca                |
| Street        | 2693 Byron Rd     | 2693 Byron Rd            |
| Postal Code   | V7H 1L9           | V7H 1L9                  |
| City          | North Vancouver   | North Vancouver          |
| Region        | BC                | BC                       |
| Phone         | +15197438620      | +15197308624             |
| Email         | customer@email.ca | customer+denied@email.ca |

#### Czechia

|               | Approved           | Denied                   |
| ------------- | ------------------ | ------------------------ |
| Date of Birth | 01-01-1970         | 27-06-1992               |
| First Name    | Test               | Test                     |
| Last Name     | Person-cz          | Person-cz                |
| Email         | customer@email.cz  | customer+denied@email.cz |
| Street        | Zazvorkova 1480/11 | Zázvorkova 1480/11       |
| Postal code   | 155 00             | 155 00                   |
| City          | Praha              | PRAHA 13                 |
| Phone         | +420771613715      | +420771623691            |

#### Denmark

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 01-01-1980        | 10-07-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-dk         | Person-dk                |
| Email         | customer@email.dk | customer+denied@email.dk |
| Street        | Dantes Plads      | Nygårdsvej               |
| House number  | 7                 | 65                       |
| City          | København Ø       | København Ø              |
| Postal code   | 1556              | 2100                     |
| Phone         | +4542555628       | +4552555348              |

#### Finland

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 01-01-1999        | 01-01-1999               |
| First Name    | Test              | Person FI                |
| Last Name     | Person-fi         | Test                     |
| Email         | customer@email.fi | customer+denied@email.fi |
| Street        | Mannerheimintie   | Mannerheimintie          |
| House number  | 34                | 34                       |
| City          | Helsinki          | Helsinki                 |
| Postal code   | 00100             | 00100                    |
| Phone         | +358401234567     | +358401234568            |

#### France

|                | Approved          | Denied                   |
| -------------- | ----------------- | ------------------------ |
| Date of Birth  | 10-07-1990        | 10-07-1990               |
| Place of Birth | Paris             | Paris                    |
| First Name     | Test              | Test                     |
| Last Name      | Person-fr         | Person-fr                |
| Email          | customer@email.fr | customer+denied@email.fr |
| Street         | rue La Fayette    | rue La Fayette           |
| House number   | 33                | 33                       |
| City           | Paris             | Paris                    |
| Postal code    | 75009             | 75009                    |
| Phone          | +33689854321      | +33687984322             |

#### Germany

|               | Approved              | Denied                   |
| ------------- | --------------------- | ------------------------ |
| Date of Birth | 10-07-1970            | 10-07-1970               |
| First Name    | Mock                  | Test                     |
| Last Name     | Mock                  | Person-de                |
| Email         | customer@email.de     | customer+denied@email.de |
| Street        | Neue Schönhauser Str. | Neue Schönhauser Str.    |
| House number  | 2                     | 2                        |
| City          | Berlin                | Berlin                   |
| Postal code   | 10178                 | 10178                    |
| Phone         | +49017614284340       | +49017610927312          |

#### Greece

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Tax number    | 090000045         | 090000045                |
| Date of Birth | 01-01-1960        | 11-11-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-gr         | Test-gr                  |
| Email         | customer@email.gr | customer+denied@email.gr |
| Street        | Kephisias         | Baralo                   |
| House number  | 37                | 56                       |
| Postal code   | 151 23            | 123 67                   |
| City          | Athina            | Athina                   |
| Phone         | +306945553624     | +306945553625            |

#### Ireland

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 10-07-1970        | 10-07-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-ie         | Person-ie                |
| Email         | customer@email.ie | customer+denied@email.ie |
| Street        | King Street South | King Street South        |
| House Number  | 30                | 30                       |
| City          | Dublin            | Dublin                   |
| EIR Code      | D02 C838          | D02 C838                 |
| Phone         | +353855351400     | +353855351401            |

#### Italy

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 01-01-1980        | 01-01-1980               |
| First Name    | Test              | Test                     |
| Last Name     | Person-it         | Person-it                |
| Email         | customer@email.it | customer+denied@email.it |
| Fiscal code   | RSSBNC80A41H501B  | RSSBNC80A41H501B         |
| Street        | Via Enrico Fermi  | Via Enrico Fermi         |
| House number  | 150               | 150                      |
| City          | Roma              | Roma                     |
| Postal code   | 00146             | 00146                    |
| Phone         | +393339741231     | +393312232389            |

#### Netherlands

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 10-07-1970        | 10-07-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-nl         | Person-nl                |
| Email         | customer@email.nl | customer+denied@email.nl |
| Street        | Osdorpplein       | Osdorpplein              |
| House number  | 137               | 137                      |
| City          | Amsterdam         | Amsterdam                |
| Postal code   | 1068 SR           | 1068 SR                  |
| Phone         | +31689124321      | +31632167678             |

#### New Zealand

|               | Approved                 | Denied                   |
| ------------- | ------------------------ | ------------------------ |
| Date of Birth | 10-07-1970               | 10-07-1970               |
| First Name    | Test                     | Test                     |
| Last Name     | Person-nz                | Person-nz                |
| Street        | Mount Wellington Highway | Mount Wellington Highway |
| House number  | 286                      | 286                      |
| Postal Code   | 6011                     | 6011                     |
| City          | Auckland                 | Wellington               |
| Phone         | +6427555290              | +642993007712            |
| Email         | customer@email.nz        | customer+denied@email.nz |

#### Norway

|                 | Approved            | Denied                   |
| --------------- | ------------------- | ------------------------ |
| Date of Birth   | 01-08-1970          | 01-08-1970               |
| First Name      | Jane                | Test                     |
| Last Name       | Test                | Person-no                |
| Email           | customer@email.no   | customer+denied@email.no |
| Personal number | NO1087000571        | NO1087000148             |
| Street          | Edvard Munchs Plass | Sæffleberggate           |
| House Number    | 1                   | 56                       |
| City            | Oslo                | Oslo                     |
| Postal code     | 0194                | 0563                     |
| Phone           | +4740123456         | +4740123457              |

#### Poland

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 05-05-1967        | 05-05-1967               |
| First Name    | Test              | Test                     |
| Last Name     | Person-pl         | Person-pl                |
| Street        | Ul. Górczewska    | Ul. Górczewska           |
| House number  | 124               | 124                      |
| Postal Code   | 01-460            | 01-460                   |
| City          | Warszawa          | Warszawa                 |
| Phone         | +48795222223      | +48795223325             |
| Email         | customer@email.pl | customer+denied@email.pl |

#### Portugal

|               | Approved            | Denied                   |
| ------------- | ------------------- | ------------------------ |
| Date of Birth | 10-07-1970          | 10-07-1970               |
| First Name    | Test                | Test                     |
| Last Name     | Person-pt           | Person-pt                |
| Street        | Avenida Dom João II | Avenida Dom João II      |
| House number  | 40                  | 40                       |
| Postal Code   | 1990-094            | 1990-094                 |
| City          | Lisboa              | Lisboa                   |
| Phone         | +351935556731       | +351915593837            |
| Email         | customer@email.pt   | customer+denied@email.pt |

#### Romania

|                                      | Approved          | Denied                   |
| ------------------------------------ | ----------------- | ------------------------ |
| Date of Birth                        | 25-12-1970        | 25-12-1970               |
| First Name                           | Test              | Test                     |
| Last Name                            | Person-ro         | Person-ro                |
| Email                                | customer@email.ro | customer+denied@email.ro |
| Street                               | Drumul Taberei    | Drumul Taberei           |
| House number                         | 35                | 35                       |
| City                                 | București         | București                |
| Sector                               | Sectorul 6        | Sectorul 6               |
| Postal code                          | 061357            | 061357                   |
| Phone                                | +40741209876      | +40707127444             |
| Personal Identification Number (CNP) | 1701225193558     |                          |

#### Spain

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| DNI/NIE       | 99999999R         | 99999999R                |
| Date of Birth | 10-07-1970        | 10-07-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-es         | Person-es                |
| Email         | customer@email.es | customer+denied@email.es |
| Street        | C. de Atocha      | C. de Atocha             |
| House number  | 27                | 27                       |
| City          | Madrid            | Madrid                   |
| Postal code   | 28012             | 28012                    |
| Phone         | +34672563009      | +34682425101             |

#### Sweden

|               | Approved                | Denied                   |
| ------------- | ----------------------- | ------------------------ |
| Date of Birth | 21-03-1941              | 28-10-1941               |
| First Name    | Alice                   | Test                     |
| Last Name     | Test                    | Person-se                |
| Email         | customer@email.se       | customer+denied@email.se |
| Street        | Södra Blasieholmshamnen | Karlaplan                |
| House number  | 2                       | 3                        |
| City          | Stockholm               | Stockholm                |
| Postal code   | 11 148                  | 11 460                   |
| Phone         | +46701740615            | +46701740620             |

#### Switzerland

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 01-01-1990        | 01-01-2000               |
| First Name    | Accepted          | Customer                 |
| Last Name     | Person-ch         | Person-ch                |
| Street        | Augustinergasse   | Bahnhofstrasse           |
| House number  | 2                 | 77                       |
| Postal Code   | 4051              | 8001                     |
| City          | Basel             | Zürich                   |
| Phone         | +41758680000      | +41758680001             |
| Email         | customer@email.ch | customer+denied@email.ch |

#### United Kingdom

|               | Approved              | Denied                   |
| ------------- | --------------------- | ------------------------ |
| Date of Birth | 10-07-1970            | 10-07-1970               |
| First Name    | Test                  | Test                     |
| Last Name     | Person-uk             | Person-uk                |
| Email         | customer@email.uk     | customer+denied@email.uk |
| Street        | New Burlington Street | New Burlington Street    |
| House number  | 10                    | 10                       |
| Apartment     | Apt 214               | Apt 214                  |
| Postal code   | W1S 3BE               | W1S 3BE                  |
| City          | London                | London                   |
| Phone         | +447755564318         | +447355505530            |

#### United States

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 07-10-1970        | 07-10-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-us         | Person-us                |
| Email         | customer@email.us | customer+denied@email.us |
| Street        | Amsterdam Ave     | Amsterdam Ave            |
| House number  | 509               | 509                      |
| City          | New York          | New York                 |
| State         | New York          | New York                 |
| Postal code   | 10024-3941        | 10024-3941               |
| Phone         | +13106683312      | +13106354386             |

### Two-step authentication

Any six digit number is a valid two-step authentication code. Use `999999` for authentication to fail.

### Repayment method

Inside the Klarna flow, you can use the following test values to try various repayment types:

| Type          | Value                         |
| ------------- | ----------------------------- |
| Direct Debit  | DE11520513735120710131        |
| Bank transfer | Demo Bank                     |
| Credit Card   | - Number: 4111 1111 1111 1111 |

- CVV: 123
- Expiration: any valid date in the future |
  | Debit Card | - Number: 4012 8888 8888 1881
- CVV: 123
- Expiration: any valid date in the future |

## Optional: Upgrade a saved payment method [Server-side]

Bringing the customer through the Klarna payment flow again if they upgrade their subscription. This ensures Klarna has the most accurate subscription information and optimizes authorization rates.

#### Upgrade and charge renewal

Create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) with the same structure as when you charge a saved payment method and include `setup_future_usage` to indicate that you want to upgrade the existing payment method. Pass the new subscription information and use the same `reference` as when you first saved the payment method.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  setup_future_usage: "off_session",
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription renewal",
        quantity: 1,
        unit_cost: 10000,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "year",
        },
      ],
    },
  },
});
```

The resulting PaymentIntent requires a redirect to Klarna to be completed. Learn [how to handle the redirect](https://docs.stripe.com/payments/klarna/set-up-future-payments.md?web-or-mobile=web&payment-ui=elements#web-redirect-customer).

#### Upgrade and charge later

Create a [SetupIntent](https://docs.stripe.com/api/payment_intents.md) and pass the existing saved payment method. Pass the new subscription information and use the same `reference` as when you first saved the payment method.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  return_url: "https://example.com/setup/complete",
  payment_method_options: {
    klarna: {
      currency: "usd",
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "annual",
          next_billing: {
            amount: 20000,
            date: "2026-01-01",
          },
        },
      ],
    },
  },
});
```

The resulting SetupIntent requires a redirect to Klarna to be completed. Learn how to [handle the redirect](https://docs.stripe.com/payments/klarna/set-up-future-payments.md?web-or-mobile=web&payment-ui=elements#web-redirect-customer).

## Optional: Remove a saved Klarna account [Server-side]

You can use the [detach](https://docs.stripe.com/api/payment_methods/detach.md) API to remove a customer’s saved Klarna account as a payment method. Remove a Klarna account when you know it won’t be used again, such as when the customer cancels their subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.detach(
  "{{PAYMENT_METHOD_ID}}",
);
```

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/klarna/set-up-future-payments?payment-ui=direct-api.

If you want to create a customized payments UI, use the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) with [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) or the [Setup Intents API](https://docs.stripe.com/api/setup_intents.md) to save Klarna payment method details and charge your customers later.

## Set up Stripe [Server-side] [Client-side]

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer before setup [Server-side]

To reuse a Klarna payment method for future payments, you must attach it to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a Customer object when your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a PaymentIntent or SetupIntent [Server-side]

Select the scenario below that best fits your use case.

#### Subscription with initial payment

If you’re setting up a subscription and charging the initial payment, use the Payment Intents API with [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). You should pass subscription details when you set up the subscription.

Passing in subscription details:

- Ensures your customers have access to all applicable [Klarna payment options](https://docs.stripe.com/payments/klarna.md#payment-options), including Pay in 3 or 4, which is only available for subscriptions that have specific lengths.
- Reduces support rates and customer dropouts due to unclear purchase details in the Klarna app, where Klarna renders subscription data for your customers.

Use the [payment_method_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-klarna) parameter to pass in subscription details. The subscription [reference](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-klarna-subscriptions-reference) is an arbitrary identifier you choose that isn’t visible to customers (for example, `GYM_ANNUAL_MEMBERSHIP` or `ID_123`).

> #### Use the same reference to charge the saved payment method
>
> When you charge the saved payment method, use the same subscription reference. The reference value needs to match the value of the `amount_details[line_items][payment_method_options][klarna][subscription_reference]` field, if you integration uses it later. If you don’t match the value, you receive an error.

The example below shows how to pass details for an annual subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription",
        quantity: 1,
        unit_cost: 5000,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "year",
        },
      ],
    },
  },
});
```

The resulting PaymentIntent contains a [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret). Pass the secret to the client side to redirect your buyer to Klarna and authorize the saved payment method.

#### Subscription and non-subscription products

If you’re charging for a one-off product and setting up a subscription at the same time, use the Payment Intents API with [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). You should pass subscription details when you set up the subscription.

Passing in subscription details:

- Ensures your customers have access to all applicable [Klarna payment options](https://docs.stripe.com/payments/klarna.md#payment-options), including Pay in 3 or 4, which is only available for subscriptions that have specific lengths.
- Reduces support rates and customer dropouts due to unclear purchase details in the Klarna app, where Klarna renders subscription data for your customers.

Use the [payment_method_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-klarna) parameter to pass in subscription details. The subscription [reference](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-klarna-subscriptions-reference) is an arbitrary identifier you choose that isn’t visible to customers (for example, `GYM_ANNUAL_MEMBERSHIP` or `ID_123`).

> #### Use the same reference to charge the saved payment method
>
> When you charge the saved payment method, use the same subscription reference. The reference value needs to match the value of the `amount_details[line_items][payment_method_options][klarna][subscription_reference]` field, if you integration uses it later. If you don’t match the value, you receive an error.

The example below shows how to pass details for an annual subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 100000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  amount_details: {
    line_items: [
      {
        product_name: "One-off product",
        unit_cost: 5000,
        quantity: 1,
      },
      {
        product_name: "Annual subscription",
        unit_cost: 5000,
        quantity: 1,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "annual",
        },
      ],
    },
  },
});
```

The resulting PaymentIntent contains a [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret). Pass the secret to the client side to redirect your buyer to Klarna and authorize the saved payment method.

#### Subscription with trial

If you’re setting up a subscription with a trial period, use the Setup Intents API. You should pass subscription details when you set up the subscription.

Passing in subscription details:

- Ensures your customers have access to all applicable [Klarna payment options](https://docs.stripe.com/payments/klarna.md#payment-options), including Pay in 3 or 4, which is only available for subscriptions that have specific lengths.
- Reduces support rates and customer dropouts due to unclear purchase details in the Klarna app, where Klarna renders subscription data for your customers.

Use the [payment_method_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-klarna) parameter to pass in subscription details. The subscription [reference](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-klarna-subscriptions-reference) is an arbitrary identifier you choose that isn’t visible to customers (for example, `GYM_ANNUAL_MEMBERSHIP` or `ID_123`).

> #### Use the same reference to charge the saved payment method
>
> When you charge the saved payment method, use the same subscription reference. The reference value needs to match the value of the `amount_details[line_items][payment_method_options][klarna][subscription_reference]` field, if you integration uses it later. If you don’t match the value, you receive an error.

The example below shows how to pass details on an annual subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  return_url: "https://example.com/setup/complete",
  payment_method_options: {
    klarna: {
      currency: "usd",
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "annual",
          next_billing: {
            amount: 10000,
            date: "2026-01-01",
          },
        },
      ],
    },
  },
});
```

The resulting SetupIntent contains a [client_secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret). Pass the secret to the client side to redirect your buyer to Klarna and authorize the saved payment method.

#### On-demand payments

For an *on-demand* (When a customer stores their payment method with a business, they can make on-demand future purchases without re-authenticating, such as ordering a ride in their ride-share app) use case, you can use either the Payment Intents API or the Setup Intents API.

If you want to process a payment and save the payment method at the same time, use the Payment Intents API.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  amount_details: {
    line_items: [
      {
        product_name: "Your product name",
        unit_cost: 5000,
        quantity: 1,
      },
    ],
  },
});
```

If you only need to save the payment method for later use and aren’t processing a payment, use the Setup Intents API.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  usage: "on_session",
});
```

## Redirect your customer [Client-side]

When a customer attempts to set up their Klarna account for future payments, use [Stripe.js](https://docs.stripe.com/js.md) to confirm the PaymentIntent or SetupIntent. Stripe.js is our foundational JavaScript library for building payment flows. It automatically handles functions such as the redirect described below, and enables you to extend your integration to other payment methods in the future.

### Set up Stripe.js

Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page.

```javascript
import { loadStripe } from "@stripe/stripe-js";

const stripe = await loadStripe("<<YOUR_PUBLISHABLE_KEY>>");
```

To confirm the setup on the client side, pass the client secret of the PaymentIntent or SetupIntent object that you created in step 3.

The client secret is different from your API keys that authenticate Stripe API requests. Handle it carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

### Confirm and redirect

Stripe.js automatically redirects your customer to Klarna when you confirm the PaymentIntent or SetupIntent. After the customer completes the process, Klarna redirects them back to the `return_url` you specify.

#### PaymentIntent

Pass the `client_secret` you received when creating your PaymentIntent in step 3. The client secret is different from your API keys that authenticate Stripe API requests. Handle it carefully, because it can complete the payment. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

```javascript
// Redirects away from the client
const { error } = await stripe.confirmKlarnaPayment(
  "{{PAYMENT_INTENT_CLIENT_SECRET}}",
  {
    payment_method: {
      billing_details: {
        email: "jenny@example.com",
        address: {
          country: "DE",
        },
      },
    },
    return_url: "https://example.com/setup/complete",
  },
);

if (error) {
  // Inform the customer that there was an error.
}
```

#### SetupIntent

Pass the `client_secret` you received when creating your SetupIntent in step 3. The client secret is different from your API keys that authenticate Stripe API requests. Handle it carefully, because it can complete the payment. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

```javascript
// Redirects away from the client
const { error } = await stripe.confirmKlarnaSetup(
  "{{SETUP_INTENT_CLIENT_SECRET}}",
  {
    payment_method: {
      billing_details: {
        email: "jenny@example.com",
        address: {
          country: "DE",
        },
      },
    },
    return_url: "https://example.com/setup/complete",
    mandate_data: {
      customer_acceptance: {
        type: "online",
        online: {
          infer_from_client: true,
        },
      },
    },
  },
);

if (error) {
  // Inform the customer that there was an error.
}
```

## Monitor webhooks [Server-side]

Use a method such as [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm that the customer authorized the billing agreement. Don’t rely on your customer to return to the payment status page.

When a customer successfully authorizes the billing agreement, Stripe emits a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event and the Intent status transitions to `succeeded`. Store the resulting [payment_method](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method) ID to make payments using the saved PaymentMethod later.

If a customer doesn’t successfully authorize the billing agreement, Stripe emits a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event and the Intent status returns to `requires_payment_method`.

## Charge a saved Klarna payment method [Server-side]

#### Subscription renewal

When you’re ready to charge your customer off-session, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during this payment attempt, which causes the PaymentIntent to throw an error if authentication is required.
- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the ID of the PaymentMethod and [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the Customer.
- Specify a [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) to indicate where Stripe needs to redirect the customer after they return from Klarna’s website.

Send subscription details and line items with each renewal. Use the same `reference` for your subscription as you did when setting up the payment method. If the subscription details have changed since you saved the payment method, send the new information with the same `reference`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  confirm: true,
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: true,
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription renewal",
        quantity: 1,
        unit_cost: 5000,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "year",
        },
      ],
    },
  },
});
```

#### On-demand payment

When you’re ready to charge your customer, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `false` to indicate that the customer is in a checkout flow during this payment attempt. If an error occurs, such as one that requires authentication, the customer is redirected to Klarna’s page to authenticate or resolve the issue.
- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the ID of the PaymentMethod and [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the Customer.

The example below includes optional details using [payment_method_options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options) to help improve Klarna underwriting and authorization rates. This includes details on how this saved Klarna payment method should be used in the future, such as expected future order amounts and frequency of payments.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  confirm: true,
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: false,
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription",
        quantity: 1,
        unit_cost: 1099,
        payment_method_options: {
          klarna: {
            subscription_reference: "{{SUBSCRIPTION_ID}}",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      on_demand: {
        average_amount: 1000,
        minimum_amount: 100,
        maximum_amount: 10000,
        interval: "year",
        interval_count: 1,
      },
    },
  },
});
```

## Handle reusable payment method revocation [Server-side]

You can revoke a reusable payment method in two ways:

- A customer can deactivate a reusable payment method in the Klarna mobile application. In this case, Stripe sends you a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) event. To handle this, subscribe to [webhook](https://docs.stripe.com/webhooks.md) events, and call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to deactivate it.
- A customer can also deactivate a reusable payment method on your UI, if supported. In this scenario, your server can call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to handle the deactivation.

In both cases, after you call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md), Stripe sends you a [payment_method.detached](https://docs.stripe.com/api/events/types.md#event_types-payment_method.detached) event.

## Test your integration

When testing your integration in a testing environment, you can simulate different outcomes within Klarna’s redirect.

> Klarna uses cookies for session tracking. To test different customer locations, log out of the Klarna sandbox from the previous session and use the relevant triggers.

Below, we have specially selected test data for the currently supported customer countries. In a sandbox, Klarna approves or denies a transaction based on the supplied email address.

#### Australia

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 10-07-1970        | 03-05-1994               |
| First Name    | Test              | John                     |
| Last Name     | Person-au         | snow                     |
| Street        | Wharf St          | Silverwater Rd           |
| House number  | 4                 | 1-5                      |
| Postal Code   | 4877              | 2128                     |
| City          | Port Douglas      | Silverwater              |
| Region        | QLD               | NSW                      |
| Phone         | +61473752244      | +61473763254             |
| Email         | customer@email.au | customer+denied@email.au |

#### Austria

|               | Approved           | Denied                   |
| ------------- | ------------------ | ------------------------ |
| Date of Birth | 10-07-1970         | 10-07-1970               |
| First Name    | Test               | Test                     |
| Last Name     | Person-at          | Person-at                |
| Email         | customer@email.at  | customer+denied@email.at |
| Street        | Mariahilfer Straße | Mariahilfer Straße       |
| House number  | 47                 | 47                       |
| City          | Wien               | Wien                     |
| Postal code   | 1060               | 1060                     |
| Phone         | +4306762600456     | +4306762600745           |

#### Belgium

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 10-07-1970        | 10-07-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-be         | Person-be                |
| Email         | customer@email.be | customer+denied@email.be |
| Street        | Grote Markt       | Grote Markt              |
| House number  | 1                 | 1                        |
| City          | Brussel           | Brussel                  |
| Postal code   | 1000              | 1000                     |
| Phone         | +32485121291      | +32485212123             |

#### Canada

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 10-07-1970        | 10-07-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-ca         | Person-ca                |
| Street        | 2693 Byron Rd     | 2693 Byron Rd            |
| Postal Code   | V7H 1L9           | V7H 1L9                  |
| City          | North Vancouver   | North Vancouver          |
| Region        | BC                | BC                       |
| Phone         | +15197438620      | +15197308624             |
| Email         | customer@email.ca | customer+denied@email.ca |

#### Czechia

|               | Approved           | Denied                   |
| ------------- | ------------------ | ------------------------ |
| Date of Birth | 01-01-1970         | 27-06-1992               |
| First Name    | Test               | Test                     |
| Last Name     | Person-cz          | Person-cz                |
| Email         | customer@email.cz  | customer+denied@email.cz |
| Street        | Zazvorkova 1480/11 | Zázvorkova 1480/11       |
| Postal code   | 155 00             | 155 00                   |
| City          | Praha              | PRAHA 13                 |
| Phone         | +420771613715      | +420771623691            |

#### Denmark

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 01-01-1980        | 10-07-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-dk         | Person-dk                |
| Email         | customer@email.dk | customer+denied@email.dk |
| Street        | Dantes Plads      | Nygårdsvej               |
| House number  | 7                 | 65                       |
| City          | København Ø       | København Ø              |
| Postal code   | 1556              | 2100                     |
| Phone         | +4542555628       | +4552555348              |

#### Finland

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 01-01-1999        | 01-01-1999               |
| First Name    | Test              | Person FI                |
| Last Name     | Person-fi         | Test                     |
| Email         | customer@email.fi | customer+denied@email.fi |
| Street        | Mannerheimintie   | Mannerheimintie          |
| House number  | 34                | 34                       |
| City          | Helsinki          | Helsinki                 |
| Postal code   | 00100             | 00100                    |
| Phone         | +358401234567     | +358401234568            |

#### France

|                | Approved          | Denied                   |
| -------------- | ----------------- | ------------------------ |
| Date of Birth  | 10-07-1990        | 10-07-1990               |
| Place of Birth | Paris             | Paris                    |
| First Name     | Test              | Test                     |
| Last Name      | Person-fr         | Person-fr                |
| Email          | customer@email.fr | customer+denied@email.fr |
| Street         | rue La Fayette    | rue La Fayette           |
| House number   | 33                | 33                       |
| City           | Paris             | Paris                    |
| Postal code    | 75009             | 75009                    |
| Phone          | +33689854321      | +33687984322             |

#### Germany

|               | Approved              | Denied                   |
| ------------- | --------------------- | ------------------------ |
| Date of Birth | 10-07-1970            | 10-07-1970               |
| First Name    | Mock                  | Test                     |
| Last Name     | Mock                  | Person-de                |
| Email         | customer@email.de     | customer+denied@email.de |
| Street        | Neue Schönhauser Str. | Neue Schönhauser Str.    |
| House number  | 2                     | 2                        |
| City          | Berlin                | Berlin                   |
| Postal code   | 10178                 | 10178                    |
| Phone         | +49017614284340       | +49017610927312          |

#### Greece

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Tax number    | 090000045         | 090000045                |
| Date of Birth | 01-01-1960        | 11-11-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-gr         | Test-gr                  |
| Email         | customer@email.gr | customer+denied@email.gr |
| Street        | Kephisias         | Baralo                   |
| House number  | 37                | 56                       |
| Postal code   | 151 23            | 123 67                   |
| City          | Athina            | Athina                   |
| Phone         | +306945553624     | +306945553625            |

#### Ireland

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 10-07-1970        | 10-07-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-ie         | Person-ie                |
| Email         | customer@email.ie | customer+denied@email.ie |
| Street        | King Street South | King Street South        |
| House Number  | 30                | 30                       |
| City          | Dublin            | Dublin                   |
| EIR Code      | D02 C838          | D02 C838                 |
| Phone         | +353855351400     | +353855351401            |

#### Italy

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 01-01-1980        | 01-01-1980               |
| First Name    | Test              | Test                     |
| Last Name     | Person-it         | Person-it                |
| Email         | customer@email.it | customer+denied@email.it |
| Fiscal code   | RSSBNC80A41H501B  | RSSBNC80A41H501B         |
| Street        | Via Enrico Fermi  | Via Enrico Fermi         |
| House number  | 150               | 150                      |
| City          | Roma              | Roma                     |
| Postal code   | 00146             | 00146                    |
| Phone         | +393339741231     | +393312232389            |

#### Netherlands

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 10-07-1970        | 10-07-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-nl         | Person-nl                |
| Email         | customer@email.nl | customer+denied@email.nl |
| Street        | Osdorpplein       | Osdorpplein              |
| House number  | 137               | 137                      |
| City          | Amsterdam         | Amsterdam                |
| Postal code   | 1068 SR           | 1068 SR                  |
| Phone         | +31689124321      | +31632167678             |

#### New Zealand

|               | Approved                 | Denied                   |
| ------------- | ------------------------ | ------------------------ |
| Date of Birth | 10-07-1970               | 10-07-1970               |
| First Name    | Test                     | Test                     |
| Last Name     | Person-nz                | Person-nz                |
| Street        | Mount Wellington Highway | Mount Wellington Highway |
| House number  | 286                      | 286                      |
| Postal Code   | 6011                     | 6011                     |
| City          | Auckland                 | Wellington               |
| Phone         | +6427555290              | +642993007712            |
| Email         | customer@email.nz        | customer+denied@email.nz |

#### Norway

|                 | Approved            | Denied                   |
| --------------- | ------------------- | ------------------------ |
| Date of Birth   | 01-08-1970          | 01-08-1970               |
| First Name      | Jane                | Test                     |
| Last Name       | Test                | Person-no                |
| Email           | customer@email.no   | customer+denied@email.no |
| Personal number | NO1087000571        | NO1087000148             |
| Street          | Edvard Munchs Plass | Sæffleberggate           |
| House Number    | 1                   | 56                       |
| City            | Oslo                | Oslo                     |
| Postal code     | 0194                | 0563                     |
| Phone           | +4740123456         | +4740123457              |

#### Poland

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 05-05-1967        | 05-05-1967               |
| First Name    | Test              | Test                     |
| Last Name     | Person-pl         | Person-pl                |
| Street        | Ul. Górczewska    | Ul. Górczewska           |
| House number  | 124               | 124                      |
| Postal Code   | 01-460            | 01-460                   |
| City          | Warszawa          | Warszawa                 |
| Phone         | +48795222223      | +48795223325             |
| Email         | customer@email.pl | customer+denied@email.pl |

#### Portugal

|               | Approved            | Denied                   |
| ------------- | ------------------- | ------------------------ |
| Date of Birth | 10-07-1970          | 10-07-1970               |
| First Name    | Test                | Test                     |
| Last Name     | Person-pt           | Person-pt                |
| Street        | Avenida Dom João II | Avenida Dom João II      |
| House number  | 40                  | 40                       |
| Postal Code   | 1990-094            | 1990-094                 |
| City          | Lisboa              | Lisboa                   |
| Phone         | +351935556731       | +351915593837            |
| Email         | customer@email.pt   | customer+denied@email.pt |

#### Romania

|                                      | Approved          | Denied                   |
| ------------------------------------ | ----------------- | ------------------------ |
| Date of Birth                        | 25-12-1970        | 25-12-1970               |
| First Name                           | Test              | Test                     |
| Last Name                            | Person-ro         | Person-ro                |
| Email                                | customer@email.ro | customer+denied@email.ro |
| Street                               | Drumul Taberei    | Drumul Taberei           |
| House number                         | 35                | 35                       |
| City                                 | București         | București                |
| Sector                               | Sectorul 6        | Sectorul 6               |
| Postal code                          | 061357            | 061357                   |
| Phone                                | +40741209876      | +40707127444             |
| Personal Identification Number (CNP) | 1701225193558     |                          |

#### Spain

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| DNI/NIE       | 99999999R         | 99999999R                |
| Date of Birth | 10-07-1970        | 10-07-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-es         | Person-es                |
| Email         | customer@email.es | customer+denied@email.es |
| Street        | C. de Atocha      | C. de Atocha             |
| House number  | 27                | 27                       |
| City          | Madrid            | Madrid                   |
| Postal code   | 28012             | 28012                    |
| Phone         | +34672563009      | +34682425101             |

#### Sweden

|               | Approved                | Denied                   |
| ------------- | ----------------------- | ------------------------ |
| Date of Birth | 21-03-1941              | 28-10-1941               |
| First Name    | Alice                   | Test                     |
| Last Name     | Test                    | Person-se                |
| Email         | customer@email.se       | customer+denied@email.se |
| Street        | Södra Blasieholmshamnen | Karlaplan                |
| House number  | 2                       | 3                        |
| City          | Stockholm               | Stockholm                |
| Postal code   | 11 148                  | 11 460                   |
| Phone         | +46701740615            | +46701740620             |

#### Switzerland

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 01-01-1990        | 01-01-2000               |
| First Name    | Accepted          | Customer                 |
| Last Name     | Person-ch         | Person-ch                |
| Street        | Augustinergasse   | Bahnhofstrasse           |
| House number  | 2                 | 77                       |
| Postal Code   | 4051              | 8001                     |
| City          | Basel             | Zürich                   |
| Phone         | +41758680000      | +41758680001             |
| Email         | customer@email.ch | customer+denied@email.ch |

#### United Kingdom

|               | Approved              | Denied                   |
| ------------- | --------------------- | ------------------------ |
| Date of Birth | 10-07-1970            | 10-07-1970               |
| First Name    | Test                  | Test                     |
| Last Name     | Person-uk             | Person-uk                |
| Email         | customer@email.uk     | customer+denied@email.uk |
| Street        | New Burlington Street | New Burlington Street    |
| House number  | 10                    | 10                       |
| Apartment     | Apt 214               | Apt 214                  |
| Postal code   | W1S 3BE               | W1S 3BE                  |
| City          | London                | London                   |
| Phone         | +447755564318         | +447355505530            |

#### United States

|               | Approved          | Denied                   |
| ------------- | ----------------- | ------------------------ |
| Date of Birth | 07-10-1970        | 07-10-1970               |
| First Name    | Test              | Test                     |
| Last Name     | Person-us         | Person-us                |
| Email         | customer@email.us | customer+denied@email.us |
| Street        | Amsterdam Ave     | Amsterdam Ave            |
| House number  | 509               | 509                      |
| City          | New York          | New York                 |
| State         | New York          | New York                 |
| Postal code   | 10024-3941        | 10024-3941               |
| Phone         | +13106683312      | +13106354386             |

### Two-step authentication

Any six digit number is a valid two-step authentication code. Use `999999` for authentication to fail.

### Repayment method

Inside the Klarna flow, you can use the following test values to try various repayment types:

| Type          | Value                         |
| ------------- | ----------------------------- |
| Direct Debit  | DE11520513735120710131        |
| Bank transfer | Demo Bank                     |
| Credit Card   | - Number: 4111 1111 1111 1111 |

- CVV: 123
- Expiration: any valid date in the future |
  | Debit Card | - Number: 4012 8888 8888 1881
- CVV: 123
- Expiration: any valid date in the future |

## Optional: Handle the Klarna redirect manually [Server-side]

We recommend relying on Stripe.js to handle Klarna redirects and billing authorizations on the client. Using the native SDK allows you to extend your integration to other payment methods. However, you can manually redirect your customers on your server using the following steps.

_Confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent or SetupIntent at creation time by including `confirm: true`. Provide a `return_url` to indicate where Stripe needs to redirect the user after they complete the setup on Klarna’s website or mobile application.

The Intent status is `requires_action` and the `next_action` type is `redirect_to_url`.

```json
{
  "id": "seti_1IQ9hjJJahOk1vSNevPWnhEN",
  "object": "setup_intent",
  "status": "requires_action",
  "next_action": {
    "type": "redirect_to_url",
    "redirect_to_url": {
      "url": "https://hooks.stripe.com/...",
      "return_url": "https://example.com/setup/complete"
    }
  },
  "application": null,
  "cancellation_reason": null,
  "client_secret": "seti_1IQ9hjJJahOk1vSNevPWnhEN_secret_J2EAlI0GQbQKV9tg7ITRcUWRBiAwvUV",
  "created": 1614597263,
  "customer": null,
  "description": null,
  "last_setup_error": null,
  "latest_attempt": "setatt_1IQ9hkJJahOk1vSN0rsCpnLI",
  "livemode": false,
  "mandate": null,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1IQ9hjJJahOk1vSNDc5lQWia",
  "payment_method_options": {},
  "payment_method_types": ["klarna"],
  "single_use_mandate": null,
  "usage": "off_session"
}
```

Redirect the customer to the URL provided in the `next_action.redirect_to_url.url` property.

## Optional: Upgrade a saved payment method [Server-side]

Bringing the customer through the Klarna payment flow again if they upgrade their subscription. This ensures Klarna has the most accurate subscription information and optimizes authorization rates.

#### Upgrade and charge renewal

Create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) with the same structure as when you charge a saved payment method and include `setup_future_usage` to indicate that you want to upgrade the existing payment method. Pass the new subscription information and use the same `reference` as when you first saved the payment method.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  setup_future_usage: "off_session",
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription renewal",
        quantity: 1,
        unit_cost: 10000,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "year",
        },
      ],
    },
  },
});
```

The resulting PaymentIntent requires a redirect to Klarna to be completed. Learn [how to handle the redirect](https://docs.stripe.com/payments/klarna/set-up-future-payments.md?web-or-mobile=web&payment-ui=elements#web-redirect-customer).

#### Upgrade and charge later

Create a [SetupIntent](https://docs.stripe.com/api/payment_intents.md) and pass the existing saved payment method. Pass the new subscription information and use the same `reference` as when you first saved the payment method.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  return_url: "https://example.com/setup/complete",
  payment_method_options: {
    klarna: {
      currency: "usd",
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "annual",
          next_billing: {
            amount: 20000,
            date: "2026-01-01",
          },
        },
      ],
    },
  },
});
```

The resulting SetupIntent requires a redirect to Klarna to be completed. Learn how to [handle the redirect](https://docs.stripe.com/payments/klarna/set-up-future-payments.md?web-or-mobile=web&payment-ui=elements#web-redirect-customer).

## Optional: Remove a saved Klarna account [Server-side]

You can use the [detach](https://docs.stripe.com/api/payment_methods/detach.md) API to remove a customer’s saved Klarna account as a payment method. Remove a Klarna account when you know it won’t be used again, such as when the customer cancels their subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.detach(
  "{{PAYMENT_METHOD_ID}}",
);
```

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/klarna/set-up-future-payments?payment-ui=mobile&platform=ios.

Use the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) with [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) or the [Setup Intents API](https://docs.stripe.com/api/setup_intents.md) to save Klarna payment method details.

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [Stripe iOS SDK](https://github.com/stripe/stripe-ios) is open source, [fully documented](https://stripe.dev/stripe-ios/index.html), and compatible with apps supporting iOS 13 or above.

#### Swift Package Manager

To install the SDK, follow these steps:

1. In Xcode, select **File** > **Add Package Dependencies…** and enter `https://github.com/stripe/stripe-ios-spm` as the repository URL.
1. Select the latest version number from our [releases page](https://github.com/stripe/stripe-ios/releases).
1. Add the **StripePaymentsUI** product to the [target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### CocoaPods

1. If you haven’t already, install the latest version of [CocoaPods](https://guides.cocoapods.org/using/getting-started.html).
1. If you don’t have an existing [Podfile](https://guides.cocoapods.org/syntax/podfile.html), run the following command to create one:
   ```bash
   pod init
   ```
1. Add this line to your `Podfile`:
   ```podfile
   pod 'StripePaymentsUI'
   ```
1. Run the following command:
   ```bash
   pod install
   ```
1. Don’t forget to use the `.xcworkspace` file to open your project in Xcode, instead of the `.xcodeproj` file, from here on out.
1. In the future, to update to the latest version of the SDK, run:
   ```bash
   pod update StripePaymentsUI
   ```

#### Carthage

1. If you haven’t already, install the latest version of [Carthage](https://github.com/Carthage/Carthage#installing-carthage).
1. Add this line to your `Cartfile`:
   ```cartfile
   github "stripe/stripe-ios"
   ```
1. Follow the [Carthage installation instructions](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos). Make sure to embed all of the required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentsUI/README.md#manual-linking).
1. In the future, to update to the latest version of the SDK, run the following command:
   ```bash
   carthage update stripe-ios --platform ios
   ```

#### Manual Framework

1. Head to our [GitHub releases page](https://github.com/stripe/stripe-ios/releases/latest) and download and unzip **Stripe.xcframework.zip**.
1. Drag **StripePaymentsUI.xcframework** to the **Embedded Binaries** section of the **General** settings in your Xcode project. Make sure to select **Copy items if needed**.
1. Repeat step 2 for all required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentsUI/README.md#manual-linking).
1. In the future, to update to the latest version of our SDK, repeat steps 1–3.

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-ios/releases) page on GitHub. To receive notifications when a new release is published, [watch releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository) for the repository.

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/test/apikeys) on app start. This enables your app to make requests to the Stripe API.

#### Swift

```swift
import UIKitimportStripePaymentsUI

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {StripeAPI.defaultPublishableKey = "<<YOUR_PUBLISHABLE_KEY>>"
        // do any other necessary launch configuration
        return true
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Create or retrieve a Customer [Server-side]

To reuse a Klarna payment method for future payments, you must attach it to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a Customer object when your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a PaymentIntent or SetupIntent [Server-side]

Select the scenario below that best fits your use case.

#### Subscription with initial payment

If you’re setting up a subscription and charging the initial payment, use the Payment Intents API with [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). You should pass subscription details when you set up the subscription.

Passing in subscription details:

- Ensures your customers have access to all applicable [Klarna payment options](https://docs.stripe.com/payments/klarna.md#payment-options), including Pay in 3 or 4, which is only available for subscriptions that have specific lengths.
- Reduces support rates and customer dropouts due to unclear purchase details in the Klarna app, where Klarna renders subscription data for your customers.

Use the [payment_method_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-klarna) parameter to pass in subscription details. The subscription [reference](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-klarna-subscriptions-reference) is an arbitrary identifier you choose that isn’t visible to customers (for example, `GYM_ANNUAL_MEMBERSHIP` or `ID_123`).

> #### Use the same reference to charge the saved payment method
>
> When you charge the saved payment method, use the same subscription reference. The reference value needs to match the value of the `amount_details[line_items][payment_method_options][klarna][subscription_reference]` field, if you integration uses it later. If you don’t match the value, you receive an error.

The example below shows how to pass details for an annual subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription",
        quantity: 1,
        unit_cost: 5000,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "year",
        },
      ],
    },
  },
});
```

The resulting PaymentIntent contains a [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret). Pass the secret to the client side to redirect your buyer to Klarna and authorize the saved payment method.

#### Subscription and non-subscription products

If you’re charging for a one-off product and setting up a subscription at the same time, use the Payment Intents API with [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). You should pass subscription details when you set up the subscription.

Passing in subscription details:

- Ensures your customers have access to all applicable [Klarna payment options](https://docs.stripe.com/payments/klarna.md#payment-options), including Pay in 3 or 4, which is only available for subscriptions that have specific lengths.
- Reduces support rates and customer dropouts due to unclear purchase details in the Klarna app, where Klarna renders subscription data for your customers.

Use the [payment_method_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-klarna) parameter to pass in subscription details. The subscription [reference](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-klarna-subscriptions-reference) is an arbitrary identifier you choose that isn’t visible to customers (for example, `GYM_ANNUAL_MEMBERSHIP` or `ID_123`).

> #### Use the same reference to charge the saved payment method
>
> When you charge the saved payment method, use the same subscription reference. The reference value needs to match the value of the `amount_details[line_items][payment_method_options][klarna][subscription_reference]` field, if you integration uses it later. If you don’t match the value, you receive an error.

The example below shows how to pass details for an annual subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 100000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  amount_details: {
    line_items: [
      {
        product_name: "One-off product",
        unit_cost: 5000,
        quantity: 1,
      },
      {
        product_name: "Annual subscription",
        unit_cost: 5000,
        quantity: 1,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "annual",
        },
      ],
    },
  },
});
```

The resulting PaymentIntent contains a [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret). Pass the secret to the client side to redirect your buyer to Klarna and authorize the saved payment method.

#### Subscription with trial

If you’re setting up a subscription with a trial period, use the Setup Intents API. You should pass subscription details when you set up the subscription.

Passing in subscription details:

- Ensures your customers have access to all applicable [Klarna payment options](https://docs.stripe.com/payments/klarna.md#payment-options), including Pay in 3 or 4, which is only available for subscriptions that have specific lengths.
- Reduces support rates and customer dropouts due to unclear purchase details in the Klarna app, where Klarna renders subscription data for your customers.

Use the [payment_method_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-klarna) parameter to pass in subscription details. The subscription [reference](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-klarna-subscriptions-reference) is an arbitrary identifier you choose that isn’t visible to customers (for example, `GYM_ANNUAL_MEMBERSHIP` or `ID_123`).

> #### Use the same reference to charge the saved payment method
>
> When you charge the saved payment method, use the same subscription reference. The reference value needs to match the value of the `amount_details[line_items][payment_method_options][klarna][subscription_reference]` field, if you integration uses it later. If you don’t match the value, you receive an error.

The example below shows how to pass details on an annual subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  return_url: "https://example.com/setup/complete",
  payment_method_options: {
    klarna: {
      currency: "usd",
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "annual",
          next_billing: {
            amount: 10000,
            date: "2026-01-01",
          },
        },
      ],
    },
  },
});
```

The resulting SetupIntent contains a [client_secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret). Pass the secret to the client side to redirect your buyer to Klarna and authorize the saved payment method.

#### On-demand payments

For an *on-demand* (When a customer stores their payment method with a business, they can make on-demand future purchases without re-authenticating, such as ordering a ride in their ride-share app) use case, you can use either the Payment Intents API or the Setup Intents API.

If you want to process a payment and save the payment method at the same time, use the Payment Intents API.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  amount_details: {
    line_items: [
      {
        product_name: "Your product name",
        unit_cost: 5000,
        quantity: 1,
      },
    ],
  },
});
```

If you only need to save the payment method for later use and aren’t processing a payment, use the Setup Intents API.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  usage: "on_session",
});
```

## Collect payment method details [Client-side]

#### Swift

```swift
// Klarna doesn't require additional parameters so we only need to pass the initialized
// STPPaymentMethodKlarnaParams instance to STPPaymentMethodParams
let klarnaParams = STPPaymentMethodKlarnaParams()
let paymentMethodParams = STPPaymentMethodParams(klarna: klarnaParams, billingDetails: nil, metadata: nil)
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the intent you created and call [confirmPaymentIntent](<https://stripe.dev/stripe-ios/stripepayments/documentation/stripepayments/stppaymenthandler/confirmpayment(_:with:completion:)>) or [confirmSetupIntent](<https://stripe.dev/stripe-ios/stripepayments/documentation/stripepayments/stppaymenthandler/confirmsetupintent(_:with:completion:)>). This presents a webview where the customer can complete the payment in Klarna. Afterwards, the completion block is called with the result of the payment.

#### PaymentIntent

#### Swift

```swift
let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)
paymentIntentParams.paymentMethodParams = paymentMethodParams
paymentIntentParams.returnURL = "payments-example://stripe-redirect"

STPPaymentHandler.shared().confirmPayment(withParams: paymentIntentParams, authenticationContext: self) { (handlerStatus, paymentIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // Payment succeeded

    case .canceled:
        // Payment was canceled

    case .failed:
        // Payment failed

    @unknown default:
        fatalError()
    }
}
```

#### SetupIntent

#### Swift

```swift
let setupIntentParams = STPSetupIntentConfirmParams(clientSecret: setupIntentClientSecret)
setupIntentParams.paymentMethodParams = paymentMethodParams
setupIntentParams.returnURL = "payments-example://stripe-redirect"

STPPaymentHandler.shared().confirmSetupIntent(withParams: setupIntentParams, authenticationContext: self) { (handlerStatus, setupIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // Setup succeeded

    case .canceled:
        // Setup was canceled

    case .failed:
        // Setup failed

    @unknown default:
        fatalError()
    }
}
```

## Monitor webhooks [Server-side]

Use a method such as [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm that the customer authorized the billing agreement. Don’t rely on your customer to return to the payment status page.

When a customer successfully authorizes the billing agreement, Stripe emits a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event and the Intent status transitions to `succeeded`. Store the resulting [payment_method](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method) ID to make payments using the saved PaymentMethod later.

If a customer doesn’t successfully authorize the billing agreement, Stripe emits a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event and the Intent status returns to `requires_payment_method`.

## Charge a saved Klarna payment method [Server-side]

#### Subscription renewal

When you’re ready to charge your customer off-session, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during this payment attempt, which causes the PaymentIntent to throw an error if authentication is required.
- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the ID of the PaymentMethod and [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the Customer.
- Specify a [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) to indicate where Stripe needs to redirect the customer after they return from Klarna’s website.

Send subscription details and line items with each renewal. Use the same `reference` for your subscription as you did when setting up the payment method. If the subscription details have changed since you saved the payment method, send the new information with the same `reference`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  confirm: true,
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: true,
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription renewal",
        quantity: 1,
        unit_cost: 5000,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "year",
        },
      ],
    },
  },
});
```

#### On-demand payment

When you’re ready to charge your customer, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `false` to indicate that the customer is in a checkout flow during this payment attempt. If an error occurs, such as one that requires authentication, the customer is redirected to Klarna’s page to authenticate or resolve the issue.
- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the ID of the PaymentMethod and [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the Customer.

The example below includes optional details using [payment_method_options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options) to help improve Klarna underwriting and authorization rates. This includes details on how this saved Klarna payment method should be used in the future, such as expected future order amounts and frequency of payments.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  confirm: true,
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: false,
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription",
        quantity: 1,
        unit_cost: 1099,
        payment_method_options: {
          klarna: {
            subscription_reference: "{{SUBSCRIPTION_ID}}",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      on_demand: {
        average_amount: 1000,
        minimum_amount: 100,
        maximum_amount: 10000,
        interval: "year",
        interval_count: 1,
      },
    },
  },
});
```

## Handle reusable payment method revocation [Server-side]

You can revoke a reusable payment method in two ways:

- A customer can deactivate a reusable payment method in the Klarna mobile application. In this case, Stripe sends you a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) event. To handle this, subscribe to [webhook](https://docs.stripe.com/webhooks.md) events, and call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to deactivate it.
- A customer can also deactivate a reusable payment method on your UI, if supported. In this scenario, your server can call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to handle the deactivation.

In both cases, after you call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md), Stripe sends you a [payment_method.detached](https://docs.stripe.com/api/events/types.md#event_types-payment_method.detached) event.

## Optional: Handle the Klarna redirect manually [Server-side]

We recommend relying on the iOS SDK to handle Klarna redirects and billing authorizations on the client. Using the native SDK allows you to extend your integration to other payment methods. However, you can manually redirect your customers on your server using the following steps.

_Confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent or SetupIntent at creation time by including `confirm: true`. Provide a `return_url` to indicate where Stripe needs to redirect the user after they complete the setup on Klarna’s website or mobile application.

After creation, the Intent status is `requires_action` and the `next_action` type is `redirect_to_url`.

```json
{
  "id": "seti_1IQ9hjJJahOk1vSNevPWnhEN",
  "object": "setup_intent",
  "status": "requires_action",
  "next_action": {
    "type": "redirect_to_url",
    "redirect_to_url": {
      "url": "https://hooks.stripe.com/...",
      "return_url": "https://example.com/setup/complete"
    }
  },
  "application": null,
  "cancellation_reason": null,
  "client_secret": "seti_1IQ9hjJJahOk1vSNevPWnhEN_secret_J2EAlI0GQbQKV9tg7ITRcUWRBiAwvUV",
  "created": 1614597263,
  "customer": null,
  "description": null,
  "last_setup_error": null,
  "latest_attempt": "setatt_1IQ9hkJJahOk1vSN0rsCpnLI",
  "livemode": false,
  "mandate": null,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1IQ9hjJJahOk1vSNDc5lQWia",
  "payment_method_options": {},
  "payment_method_types": ["klarna"],
  "single_use_mandate": null,
  "usage": "off_session"
}
```

Redirect the customer to the URL provided in the `next_action.redirect_to_url.url` property.

## Optional: Upgrade a saved payment method [Server-side]

Bring the customer through the Klarna payment flow again if they upgrade their subscription. This ensures Klarna has the most accurate subscription information and optimizes authorization rates.

#### Upgrade and charge renewal

Create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) with the same structure as when you charge a saved payment method and include `setup_future_usage` to indicate that you want to upgrade the existing payment method. Pass the new subscription information and use the same `reference` as when you first saved the payment method.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  setup_future_usage: "off_session",
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription renewal",
        quantity: 1,
        unit_cost: 10000,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "year",
        },
      ],
    },
  },
});
```

The resulting PaymentIntent requires a redirect to Klarna to be completed. Learn how to [handle the redirect](https://docs.stripe.com/payments/klarna/set-up-future-payments.md#ios-submit-payment).

#### Upgrade and charge later

Create a [SetupIntent](https://docs.stripe.com/api/payment_intents.md) and pass the existing saved payment method. Pass the new subscription information and use the same `reference` as when you first saved the payment method.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  return_url: "https://example.com/setup/complete",
  payment_method_options: {
    klarna: {
      currency: "usd",
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "annual",
          next_billing: {
            amount: 20000,
            date: "2026-01-01",
          },
        },
      ],
    },
  },
});
```

The resulting SetupIntent requires a redirect to Klarna to be completed. Learn how to [handle the redirect](https://docs.stripe.com/payments/klarna/set-up-future-payments.md#ios-submit-payment).

## Optional: Remove a saved Klarna account [Server-side]

You can use the [detach](https://docs.stripe.com/api/payment_methods/detach.md) API to remove a customer’s saved Klarna account as a payment method. Remove a Klarna account when you know it won’t be used again, such as when the customer cancels their subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.detach(
  "{{PAYMENT_METHOD_ID}}",
);
```

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/klarna/set-up-future-payments?payment-ui=mobile&platform=android.

Use the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) with [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) or the [Setup Intents API](https://docs.stripe.com/api/setup_intents.md) to save Klarna payment method details.

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [Stripe Android SDK](https://github.com/stripe/stripe-android) is open source and [fully documented](https://stripe.dev/stripe-android/).

To install the SDK, add `stripe-android` to the `dependencies` block of your [app/build.gradle](https://developer.android.com/studio/build/dependencies) file:

#### Kotlin

```kotlin
plugins {
    id("com.android.application")
}

android { ... }

dependencies {
  // ...

  // Stripe Android SDK
  implementation("com.stripe:stripe-android:23.7.0")
  // Include the financial connections SDK to support US bank account as a payment method
  implementation("com.stripe:financial-connections:23.7.0")
}
```

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-android/releases) page on GitHub. To receive notifications when a new release is published, [watch releases for the repository](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository).

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/apikeys) so that it can make requests to the Stripe API, such as in your `Application` subclass:

#### Kotlin

```kotlin
import com.stripe.android.PaymentConfiguration

class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        PaymentConfiguration.init(
            applicationContext,
            "<<YOUR_PUBLISHABLE_KEY>>"
        )
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

Stripe samples also use [OkHttp](https://github.com/square/okhttp) and [GSON](https://github.com/google/gson) to make HTTP requests to a server.

## Create or retrieve a Customer [Server-side]

To reuse a Klarna payment method for future payments, you must attach it to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a Customer object when your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a PaymentIntent or SetupIntent [Server-side]

Select the scenario below that best fits your use case.

#### Subscription with initial payment

If you’re setting up a subscription and charging the initial payment, use the Payment Intents API with [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). You should pass subscription details when you set up the subscription.

Passing in subscription details:

- Ensures your customers have access to all applicable [Klarna payment options](https://docs.stripe.com/payments/klarna.md#payment-options), including Pay in 3 or 4, which is only available for subscriptions that have specific lengths.
- Reduces support rates and customer dropouts due to unclear purchase details in the Klarna app, where Klarna renders subscription data for your customers.

Use the [payment_method_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-klarna) parameter to pass in subscription details. The subscription [reference](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-klarna-subscriptions-reference) is an arbitrary identifier you choose that isn’t visible to customers (for example, `GYM_ANNUAL_MEMBERSHIP` or `ID_123`).

> #### Use the same reference to charge the saved payment method
>
> When you charge the saved payment method, use the same subscription reference. The reference value needs to match the value of the `amount_details[line_items][payment_method_options][klarna][subscription_reference]` field, if you integration uses it later. If you don’t match the value, you receive an error.

The example below shows how to pass details for an annual subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription",
        quantity: 1,
        unit_cost: 5000,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "year",
        },
      ],
    },
  },
});
```

The resulting PaymentIntent contains a [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret). Pass the secret to the client side to redirect your buyer to Klarna and authorize the saved payment method.

#### Subscription and non-subscription products

If you’re charging for a one-off product and setting up a subscription at the same time, use the Payment Intents API with [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). You should pass subscription details when you set up the subscription.

Passing in subscription details:

- Ensures your customers have access to all applicable [Klarna payment options](https://docs.stripe.com/payments/klarna.md#payment-options), including Pay in 3 or 4, which is only available for subscriptions that have specific lengths.
- Reduces support rates and customer dropouts due to unclear purchase details in the Klarna app, where Klarna renders subscription data for your customers.

Use the [payment_method_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-klarna) parameter to pass in subscription details. The subscription [reference](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-klarna-subscriptions-reference) is an arbitrary identifier you choose that isn’t visible to customers (for example, `GYM_ANNUAL_MEMBERSHIP` or `ID_123`).

> #### Use the same reference to charge the saved payment method
>
> When you charge the saved payment method, use the same subscription reference. The reference value needs to match the value of the `amount_details[line_items][payment_method_options][klarna][subscription_reference]` field, if you integration uses it later. If you don’t match the value, you receive an error.

The example below shows how to pass details for an annual subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 100000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  amount_details: {
    line_items: [
      {
        product_name: "One-off product",
        unit_cost: 5000,
        quantity: 1,
      },
      {
        product_name: "Annual subscription",
        unit_cost: 5000,
        quantity: 1,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "annual",
        },
      ],
    },
  },
});
```

The resulting PaymentIntent contains a [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret). Pass the secret to the client side to redirect your buyer to Klarna and authorize the saved payment method.

#### Subscription with trial

If you’re setting up a subscription with a trial period, use the Setup Intents API. You should pass subscription details when you set up the subscription.

Passing in subscription details:

- Ensures your customers have access to all applicable [Klarna payment options](https://docs.stripe.com/payments/klarna.md#payment-options), including Pay in 3 or 4, which is only available for subscriptions that have specific lengths.
- Reduces support rates and customer dropouts due to unclear purchase details in the Klarna app, where Klarna renders subscription data for your customers.

Use the [payment_method_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-klarna) parameter to pass in subscription details. The subscription [reference](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-klarna-subscriptions-reference) is an arbitrary identifier you choose that isn’t visible to customers (for example, `GYM_ANNUAL_MEMBERSHIP` or `ID_123`).

> #### Use the same reference to charge the saved payment method
>
> When you charge the saved payment method, use the same subscription reference. The reference value needs to match the value of the `amount_details[line_items][payment_method_options][klarna][subscription_reference]` field, if you integration uses it later. If you don’t match the value, you receive an error.

The example below shows how to pass details on an annual subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  return_url: "https://example.com/setup/complete",
  payment_method_options: {
    klarna: {
      currency: "usd",
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "annual",
          next_billing: {
            amount: 10000,
            date: "2026-01-01",
          },
        },
      ],
    },
  },
});
```

The resulting SetupIntent contains a [client_secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret). Pass the secret to the client side to redirect your buyer to Klarna and authorize the saved payment method.

#### On-demand payments

For an *on-demand* (When a customer stores their payment method with a business, they can make on-demand future purchases without re-authenticating, such as ordering a ride in their ride-share app) use case, you can use either the Payment Intents API or the Setup Intents API.

If you want to process a payment and save the payment method at the same time, use the Payment Intents API.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  amount_details: {
    line_items: [
      {
        product_name: "Your product name",
        unit_cost: 5000,
        quantity: 1,
      },
    ],
  },
});
```

If you only need to save the payment method for later use and aren’t processing a payment, use the Setup Intents API.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  usage: "on_session",
});
```

## Collect payment method details [Client-side]

#### Kotlin

```swift
// Klarna doesn't require additional parameters so we only need to pass the initialized
// STPPaymentMethodKlarnaParams instance to STPPaymentMethodParams
val klarnaParams = STPPaymentMethodKlarnaParams()
val paymentMethodParams = STPPaymentMethodParams.paramsWithKlarna(klarnaParams, null, null)
```

## Submit the payment method details to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent or SetupIntent you created and call [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/confirm.html). This presents a webview where the customer can complete the checkout with Klarna. Upon completion, the provided `PaymentResultCallback` is called with the result of the payment.

#### PaymentIntent

#### Kotlin

```kotlin
class KlarnaPaymentActivity : AppCompatActivity() {

    // ...

    private val paymentLauncher: PaymentLauncher by lazy {
        val paymentConfiguration = PaymentConfiguration.getInstance(this)
        PaymentLauncher.create(
            activity = this,
            publishableKey = paymentConfiguration.publishableKey,
            stripeAccountId = paymentConfiguration.stripeAccountId,
            callback = ::onPaymentResult,
        )
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        // …
        startCheckout()
    }

    private fun startCheckout() {
        // Create a PaymentIntent on your backend and return the client_secret here
        val paymentIntentClientSecret = // …

        val klarnaParams = PaymentMethodCreateParams.createKlarna()

        val confirmParams = ConfirmPaymentIntentParams.create(
            paymentMethodCreateParams = klarnaParams,
            clientSecret = paymentIntentClientSecret,
        )

        paymentLauncher.confirm(confirmParams)
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        // Handle the setup result…
    }
}
```

#### SetupIntent

#### Kotlin

```kotlin
class KlarnaSetupActivity : AppCompatActivity() {

    // ...

    private val paymentLauncher: PaymentLauncher by lazy {
        val paymentConfiguration = PaymentConfiguration.getInstance(this)
        PaymentLauncher.create(
            activity = this,
            publishableKey = paymentConfiguration.publishableKey,
            stripeAccountId = paymentConfiguration.stripeAccountId,
            callback = ::onPaymentResult,
        )
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        // …
        startCheckout()
    }

    private fun startCheckout() {
        // Create a SetupIntent on your backend and return the client_secret here
        val setupIntentClientSecret = // …

        val klarnaParams = PaymentMethodCreateParams.createKlarna()

        val confirmParams = ConfirmSetupIntentParams.create(
            paymentMethodCreateParams = klarnaParams,
            clientSecret = setupIntentClientSecret,
            // Add a mandate ID or MandateDataParams…
        )

        paymentLauncher.confirm(confirmParams)
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        // Handle the setup result…
    }
}
```

## Monitor webhooks [Server-side]

Use a method such as [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm that the customer authorized the billing agreement. Don’t rely on your customer to return to the payment status page.

When a customer successfully authorizes the billing agreement, Stripe emits a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event and the Intent status transitions to `succeeded`. Store the resulting [payment_method](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method) ID to make payments using the saved PaymentMethod later.

If a customer doesn’t successfully authorize the billing agreement, Stripe emits a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event and the Intent status returns to `requires_payment_method`.

## Charge a saved Klarna payment method [Server-side]

#### Subscription renewal

When you’re ready to charge your customer off-session, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during this payment attempt, which causes the PaymentIntent to throw an error if authentication is required.
- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the ID of the PaymentMethod and [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the Customer.
- Specify a [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) to indicate where Stripe needs to redirect the customer after they return from Klarna’s website.

Send subscription details and line items with each renewal. Use the same `reference` for your subscription as you did when setting up the payment method. If the subscription details have changed since you saved the payment method, send the new information with the same `reference`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  confirm: true,
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: true,
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription renewal",
        quantity: 1,
        unit_cost: 5000,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "year",
        },
      ],
    },
  },
});
```

#### On-demand payment

When you’re ready to charge your customer, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `false` to indicate that the customer is in a checkout flow during this payment attempt. If an error occurs, such as one that requires authentication, the customer is redirected to Klarna’s page to authenticate or resolve the issue.
- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the ID of the PaymentMethod and [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the Customer.

The example below includes optional details using [payment_method_options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options) to help improve Klarna underwriting and authorization rates. This includes details on how this saved Klarna payment method should be used in the future, such as expected future order amounts and frequency of payments.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  confirm: true,
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: false,
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription",
        quantity: 1,
        unit_cost: 1099,
        payment_method_options: {
          klarna: {
            subscription_reference: "{{SUBSCRIPTION_ID}}",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      on_demand: {
        average_amount: 1000,
        minimum_amount: 100,
        maximum_amount: 10000,
        interval: "year",
        interval_count: 1,
      },
    },
  },
});
```

## Handle reusable payment method revocation [Server-side]

You can revoke a reusable payment method in two ways:

- A customer can deactivate a reusable payment method in the Klarna mobile application. In this case, Stripe sends you a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) event. To handle this, subscribe to [webhook](https://docs.stripe.com/webhooks.md) events, and call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to deactivate it.
- A customer can also deactivate a reusable payment method on your UI, if supported. In this scenario, your server can call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to handle the deactivation.

In both cases, after you call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md), Stripe sends you a [payment_method.detached](https://docs.stripe.com/api/events/types.md#event_types-payment_method.detached) event.

## Optional: Handle the Klarna redirect manually [Server-side]

We recommend relying on the native SDK to handle Klarna redirects and billing authorizations on the client. Using the native SDK allows you to extend your integration to other payment methods. However, you can manually redirect your customers on your server using the following steps.

_Confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the PaymentIntent or SetupIntent at creation time by including `confirm: true`. Provide a `return_url` to indicate where Stripe needs to redirect the user after they complete the setup on Klarna’s website or mobile application.

Verify that the Intent status is `requires_action` and the `next_action` type is `redirect_to_url`.

```json
{
  "id": "seti_1IQ9hjJJahOk1vSNevPWnhEN",
  "object": "setup_intent",
  "status": "requires_action",
  "next_action": {
    "type": "redirect_to_url",
    "redirect_to_url": {
      "url": "https://hooks.stripe.com/...",
      "return_url": "https://example.com/setup/complete"
    }
  },
  "application": null,
  "cancellation_reason": null,
  "client_secret": "seti_1IQ9hjJJahOk1vSNevPWnhEN_secret_J2EAlI0GQbQKV9tg7ITRcUWRBiAwvUV",
  "created": 1614597263,
  "customer": null,
  "description": null,
  "last_setup_error": null,
  "latest_attempt": "setatt_1IQ9hkJJahOk1vSN0rsCpnLI",
  "livemode": false,
  "mandate": null,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1IQ9hjJJahOk1vSNDc5lQWia",
  "payment_method_options": {},
  "payment_method_types": ["klarna"],
  "single_use_mandate": null,
  "usage": "off_session"
}
```

Redirect the customer to the URL provided in the `next_action.redirect_to_url.url` property.

## Optional: Upgrade a saved payment method [Server-side]

Bring the customer through the Klarna payment flow again if they upgrade their subscription. This ensures Klarna has the most accurate subscription information and optimizes authorization rates.

#### Upgrade and charge renewal

Create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) with the same structure as when you charge a saved payment method and include `setup_future_usage` to indicate that you want to upgrade the existing payment method. Pass the new subscription information and use the same `reference` as when you first saved the payment method.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  setup_future_usage: "off_session",
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription renewal",
        quantity: 1,
        unit_cost: 10000,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "year",
        },
      ],
    },
  },
});
```

The resulting PaymentIntent requires a redirect to Klarna to be completed. Learn how to [handle the redirect](https://docs.stripe.com/payments/klarna/set-up-future-payments.md#submit-payment).

#### Upgrade and charge later

Create a [SetupIntent](https://docs.stripe.com/api/payment_intents.md) and pass the existing saved payment method. Pass the new subscription information and use the same `reference` as when you first saved the payment method.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  return_url: "https://example.com/setup/complete",
  payment_method_options: {
    klarna: {
      currency: "usd",
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "annual",
          next_billing: {
            amount: 20000,
            date: "2026-01-01",
          },
        },
      ],
    },
  },
});
```

The resulting SetupIntent requires a redirect to Klarna to be completed. Learn how to [handle the redirect](https://docs.stripe.com/payments/klarna/set-up-future-payments.md#submit-payment).

## Optional: Remove a saved Klarna account [Server-side]

You can use the [detach](https://docs.stripe.com/api/payment_methods/detach.md) API to remove a customer’s saved Klarna account as a payment method. Remove a Klarna account when you know it won’t be used again, such as when the customer cancels their subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.detach(
  "{{PAYMENT_METHOD_ID}}",
);
```

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/klarna/set-up-future-payments?payment-ui=mobile&platform=react-native.

Use the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) with [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) or the [Setup Intents API](https://docs.stripe.com/api/setup_intents.md) to save Klarna payment method details.

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that communicate to the Stripe API. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [React Native SDK](https://github.com/stripe/stripe-react-native) is open source and fully documented. Internally, it uses the [native iOS](https://github.com/stripe/stripe-ios) and [Android](https://github.com/stripe/stripe-android) SDKs. To install Stripe’s React Native SDK, run one of the following commands in your project’s directory (depending on which package manager you use):

#### yarn

```bash
yarn add @stripe/stripe-react-native
```

#### npm

```bash
npm install @stripe/stripe-react-native
```

Next, install some other necessary dependencies:

- For iOS, go to the **ios** directory and run `pod install` to ensure that you also install the required native dependencies.
- For Android, there are no more dependencies to install.

> We recommend following the [official TypeScript guide](https://reactnative.dev/docs/typescript#adding-typescript-to-an-existing-project) to add TypeScript support.

### Stripe initialization

To initialize Stripe in your React Native app, either wrap your payment screen with the `StripeProvider` component, or use the `initStripe` initialization method. Only the API [publishable key](https://docs.stripe.com/keys.md#obtain-api-keys) in `publishableKey` is required. The following example shows how to initialize Stripe using the `StripeProvider` component.

```jsx
import { useState, useEffect } from "react";
import { StripeProvider } from "@stripe/stripe-react-native";

function App() {
  const [publishableKey, setPublishableKey] = useState("");

  const fetchPublishableKey = async () => {
    const key = await fetchKey(); // fetch key from your server here
    setPublishableKey(key);
  };

  useEffect(() => {
    fetchPublishableKey();
  }, []);

  return (
    <StripeProvider
      publishableKey={publishableKey}
      merchantIdentifier="merchant.identifier" // required for Apple Pay
      urlScheme="your-url-scheme" // required for 3D Secure and bank redirects
    >
      {/* Your app code here */}
    </StripeProvider>
  );
}
```

> Use your API [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Set up a return URL (iOS only) [Client-side]

When a customer exits your app (for example to authenticate in Safari or their banking app), provide a way for them to automatically return to your app. Many payment method types _require_ a return URL. If you don’t provide one, we can’t present payment methods that require a return URL to your users, even if you’ve enabled them.

To provide a return URL:

1. [Register](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app#Register-your-URL-scheme) a custom URL. Universal links aren’t supported.
1. [Configure](https://reactnative.dev/docs/linking) your custom URL.
1. Set up your root component to forward the URL to the Stripe SDK as shown below.

> If you’re using Expo, [set your scheme](https://docs.expo.io/guides/linking/#in-a-standalone-app) in the `app.json` file.

```jsx
import { useEffect, useCallback } from 'react';
import { Linking } from 'react-native';
import { useStripe } from '@stripe/stripe-react-native';

export default function MyApp() {
  const { handleURLCallback } = useStripe();

  const handleDeepLink = useCallback(
    async (url: string | null) => {
      if (url) {
        const stripeHandled = await handleURLCallback(url);
        if (stripeHandled) {
          // This was a Stripe URL - you can return or add extra handling here as you see fit
        } else {
          // This was NOT a Stripe URL – handle as you normally would
        }
      }
    },
    [handleURLCallback]
  );

  useEffect(() => {
    const getUrlAsync = async () => {
      const initialUrl = await Linking.getInitialURL();
      handleDeepLink(initialUrl);
    };

    getUrlAsync();

    const deepLinkListener = Linking.addEventListener(
      'url',
      (event: { url: string }) => {
        handleDeepLink(event.url);
      }
    );

    return () => deepLinkListener.remove();
  }, [handleDeepLink]);

  return (
    <View>
      <AwesomeAppComponent />
    </View>
  );
}
```

For more information on native URL schemes, refer to the [Android](https://developer.android.com/training/app-links/deep-linking) and [iOS](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app) docs.

## Create or retrieve a Customer before setup [Server-side]

To reuse a Klarna payment method for future payments, you must attach it to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a Customer object when your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. If your customer hasn’t created an account yet, you can create a Customer object and associate it with your internal representation of the customer’s account at a later time.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create();
```

## Create a PaymentIntent or SetupIntent [Server-side]

Select the scenario below that best fits your use case.

#### Subscription with initial payment

If you’re setting up a subscription and charging the initial payment, use the Payment Intents API with [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). You should pass subscription details when you set up the subscription.

Passing in subscription details:

- Ensures your customers have access to all applicable [Klarna payment options](https://docs.stripe.com/payments/klarna.md#payment-options), including Pay in 3 or 4, which is only available for subscriptions that have specific lengths.
- Reduces support rates and customer dropouts due to unclear purchase details in the Klarna app, where Klarna renders subscription data for your customers.

Use the [payment_method_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-klarna) parameter to pass in subscription details. The subscription [reference](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-klarna-subscriptions-reference) is an arbitrary identifier you choose that isn’t visible to customers (for example, `GYM_ANNUAL_MEMBERSHIP` or `ID_123`).

> #### Use the same reference to charge the saved payment method
>
> When you charge the saved payment method, use the same subscription reference. The reference value needs to match the value of the `amount_details[line_items][payment_method_options][klarna][subscription_reference]` field, if you integration uses it later. If you don’t match the value, you receive an error.

The example below shows how to pass details for an annual subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription",
        quantity: 1,
        unit_cost: 5000,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "year",
        },
      ],
    },
  },
});
```

The resulting PaymentIntent contains a [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret). Pass the secret to the client side to redirect your buyer to Klarna and authorize the saved payment method.

#### Subscription and non-subscription products

If you’re charging for a one-off product and setting up a subscription at the same time, use the Payment Intents API with [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage). You should pass subscription details when you set up the subscription.

Passing in subscription details:

- Ensures your customers have access to all applicable [Klarna payment options](https://docs.stripe.com/payments/klarna.md#payment-options), including Pay in 3 or 4, which is only available for subscriptions that have specific lengths.
- Reduces support rates and customer dropouts due to unclear purchase details in the Klarna app, where Klarna renders subscription data for your customers.

Use the [payment_method_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-klarna) parameter to pass in subscription details. The subscription [reference](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-klarna-subscriptions-reference) is an arbitrary identifier you choose that isn’t visible to customers (for example, `GYM_ANNUAL_MEMBERSHIP` or `ID_123`).

> #### Use the same reference to charge the saved payment method
>
> When you charge the saved payment method, use the same subscription reference. The reference value needs to match the value of the `amount_details[line_items][payment_method_options][klarna][subscription_reference]` field, if you integration uses it later. If you don’t match the value, you receive an error.

The example below shows how to pass details for an annual subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 100000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  amount_details: {
    line_items: [
      {
        product_name: "One-off product",
        unit_cost: 5000,
        quantity: 1,
      },
      {
        product_name: "Annual subscription",
        unit_cost: 5000,
        quantity: 1,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "annual",
        },
      ],
    },
  },
});
```

The resulting PaymentIntent contains a [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret). Pass the secret to the client side to redirect your buyer to Klarna and authorize the saved payment method.

#### Subscription with trial

If you’re setting up a subscription with a trial period, use the Setup Intents API. You should pass subscription details when you set up the subscription.

Passing in subscription details:

- Ensures your customers have access to all applicable [Klarna payment options](https://docs.stripe.com/payments/klarna.md#payment-options), including Pay in 3 or 4, which is only available for subscriptions that have specific lengths.
- Reduces support rates and customer dropouts due to unclear purchase details in the Klarna app, where Klarna renders subscription data for your customers.

Use the [payment_method_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_options-klarna) parameter to pass in subscription details. The subscription [reference](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-klarna-subscriptions-reference) is an arbitrary identifier you choose that isn’t visible to customers (for example, `GYM_ANNUAL_MEMBERSHIP` or `ID_123`).

> #### Use the same reference to charge the saved payment method
>
> When you charge the saved payment method, use the same subscription reference. The reference value needs to match the value of the `amount_details[line_items][payment_method_options][klarna][subscription_reference]` field, if you integration uses it later. If you don’t match the value, you receive an error.

The example below shows how to pass details on an annual subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  return_url: "https://example.com/setup/complete",
  payment_method_options: {
    klarna: {
      currency: "usd",
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "annual",
          next_billing: {
            amount: 10000,
            date: "2026-01-01",
          },
        },
      ],
    },
  },
});
```

The resulting SetupIntent contains a [client_secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret). Pass the secret to the client side to redirect your buyer to Klarna and authorize the saved payment method.

#### On-demand payments

For an *on-demand* (When a customer stores their payment method with a business, they can make on-demand future purchases without re-authenticating, such as ordering a ride in their ride-share app) use case, you can use either the Payment Intents API or the Setup Intents API.

If you want to process a payment and save the payment method at the same time, use the Payment Intents API.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  setup_future_usage: "off_session",
  amount_details: {
    line_items: [
      {
        product_name: "Your product name",
        unit_cost: 5000,
        quantity: 1,
      },
    ],
  },
});
```

If you only need to save the payment method for later use and aren’t processing a payment, use the Setup Intents API.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  usage: "on_session",
});
```

## Redirect your customer [Client-side]

Use the Stripe React Native SDK to confirm the PaymentIntent or SetupIntent. It automatically handles functions such as the redirect described below, and enables you to extend your integration to other payment methods in the future.

Your customer is redirected to a Klarna billing agreement page, where they must authorize you to use their Klarna account for future payments before being redirected back to your app.

#### PaymentIntent

```js
import { confirmPayment } from "@stripe/stripe-react-native";

// In your component...
const { error, paymentIntent } = await confirmPayment(
  "{{PAYMENT_INTENT_CLIENT_SECRET}}",
  {
    paymentMethodType: "Klarna",
    paymentMethodData: {
      billingDetails: {
        email: "jenny@example.com",
        address: {
          country: "DE",
        },
      },
      mandateData: {
        // Add mandate data...
      },
    },
  },
);

if (error) {
  // Something went wrong
}
```

#### SetupIntent

```js
import { confirmSetupIntent } from "@stripe/stripe-react-native";

// In your component...
const { error, setupIntent } = await confirmSetupIntent(
  "{{SETUP_INTENT_CLIENT_SECRET}}",
  {
    paymentMethodType: "Klarna",
    paymentMethodData: {
      billingDetails: {
        email: "jenny@example.com",
        address: {
          country: "DE",
        },
      },
      mandateData: {
        // Add mandate data...
      },
    },
  },
);

if (error) {
  // Something went wrong
}
```

## Monitor webhooks [Server-side]

Use a method such as [webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to confirm that the customer authorized the billing agreement. Don’t rely on your customer to return to the payment status page.

When a customer successfully authorizes the billing agreement, Stripe emits a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) or [setup_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.succeeded) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event and the Intent status transitions to `succeeded`. Store the resulting [payment_method](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method) ID to make payments using the saved PaymentMethod later.

If a customer doesn’t successfully authorize the billing agreement, Stripe emits a [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) or [setup_intent.setup_failed](https://docs.stripe.com/api/events/types.md#event_types-setup_intent.setup_failed) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event and the Intent status returns to `requires_payment_method`.

## Charge a saved Klarna payment method [Server-side]

#### Subscription renewal

When you’re ready to charge your customer off-session, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `true` to indicate that the customer isn’t in your checkout flow during this payment attempt, which causes the PaymentIntent to throw an error if authentication is required.
- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the ID of the PaymentMethod and [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the Customer.
- Specify a [return_url](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-return_url) to indicate where Stripe needs to redirect the customer after they return from Klarna’s website.

Send subscription details and line items with each renewal. Use the same `reference` for your subscription as you did when setting up the payment method. If the subscription details have changed since you saved the payment method, send the new information with the same `reference`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: "usd",
  confirm: true,
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: true,
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription renewal",
        quantity: 1,
        unit_cost: 5000,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "year",
        },
      ],
    },
  },
});
```

#### On-demand payment

When you’re ready to charge your customer, use the *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) IDs to create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). Set a few other parameters to make the *off-session payment* (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information):

- Set [off_session](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to `false` to indicate that the customer is in a checkout flow during this payment attempt. If an error occurs, such as one that requires authentication, the customer is redirected to Klarna’s page to authenticate or resolve the issue.
- Set the value of the PaymentIntent’s [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property to `true`, which causes confirmation to occur immediately when the PaymentIntent is created.
- Set [payment_method](https://docs.stripe.com/api.md#create_payment_intent-payment_method) to the ID of the PaymentMethod and [customer](https://docs.stripe.com/api.md#create_payment_intent-customer) to the ID of the Customer.

The example below includes optional details using [payment_method_options](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options) to help improve Klarna underwriting and authorization rates. This includes details on how this saved Klarna payment method should be used in the future, such as expected future order amounts and frequency of payments.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  confirm: true,
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  off_session: false,
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription",
        quantity: 1,
        unit_cost: 1099,
        payment_method_options: {
          klarna: {
            subscription_reference: "{{SUBSCRIPTION_ID}}",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      on_demand: {
        average_amount: 1000,
        minimum_amount: 100,
        maximum_amount: 10000,
        interval: "year",
        interval_count: 1,
      },
    },
  },
});
```

## Handle reusable payment method revocation [Server-side]

You can revoke a reusable payment method in two ways:

- A customer can deactivate a reusable payment method in the Klarna mobile application. In this case, Stripe sends you a [mandate.updated](https://docs.stripe.com/api/events/types.md#event_types-mandate.updated) event. To handle this, subscribe to [webhook](https://docs.stripe.com/webhooks.md) events, and call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to deactivate it.
- A customer can also deactivate a reusable payment method on your UI, if supported. In this scenario, your server can call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to handle the deactivation.

In both cases, after you call [detach PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md), Stripe sends you a [payment_method.detached](https://docs.stripe.com/api/events/types.md#event_types-payment_method.detached) event.

## Optional: Handle the Klarna redirect manually [Server-side]

We recommend relying on the Stripe React Native SDK to handle Klarna redirects and billing authorizations on the client side with `confirmSetupIntent`. Using the native SDK allows you to extend your integration to other payment methods. However, you can manually redirect your customers on your server using the following steps.

_Confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the SetupIntent at creation time by setting `confirm: true`. You must provide a `return_url` when you confirm a SetupIntent to indicate where Stripe needs to redirect the user to after they complete the setup on Klarna’s website or mobile application.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method_options: {
    klarna: {
      currency: "usd",
    },
  },
  payment_method_types: ["klarna"],
  payment_method_data: {
    type: "klarna",
    billing_details: {
      email: "jenny@example.com",
      address: {
        country: "DE",
      },
    },
  },
  usage: "off_session",
  confirm: true,
  return_url: "https://example.com/setup/complete",
});
```

Verify that the SetupIntent status is `requires_action` and the `next_action` type is `redirect_to_url`.

```json
{
  "id": "seti_1IQ9hjJJahOk1vSNevPWnhEN",
  "object": "setup_intent",
  "status": "requires_action",
  "next_action": {
    "type": "redirect_to_url",
    "redirect_to_url": {
      "url": "https://hooks.stripe.com/...",
      "return_url": "https://example.com/setup/complete"
    }
  },
  "application": null,
  "cancellation_reason": null,
  "client_secret": "seti_1IQ9hjJJahOk1vSNevPWnhEN_secret_J2EAlI0GQbQKV9tg7ITRcUWRBiAwvUV",
  "created": 1614597263,
  "customer": null,
  "description": null,
  "last_setup_error": null,
  "latest_attempt": "setatt_1IQ9hkJJahOk1vSN0rsCpnLI",
  "livemode": false,
  "mandate": null,
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1IQ9hjJJahOk1vSNDc5lQWia",
  "payment_method_options": {},
  "payment_method_types": ["klarna"],
  "single_use_mandate": null,
  "usage": "off_session"
}
```

Redirect the customer to the URL provided in the `next_action.redirect_to_url.url` property.

## Optional: Upgrade a saved payment method [Server-side]

Bring the customer through the Klarna payment flow again if they upgrade their subscription. This ensures Klarna has the most accurate subscription information and optimizes authorization rates.

#### Upgrade and charge renewal

Create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) with the same structure as when you charge a saved payment method and include `setup_future_usage` to indicate that you want to upgrade the existing payment method. Pass the new subscription information and use the same `reference` as when you first saved the payment method.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 10000,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  setup_future_usage: "off_session",
  return_url: "https://example.com/setup/complete",
  amount_details: {
    line_items: [
      {
        product_name: "Annual subscription renewal",
        quantity: 1,
        unit_cost: 10000,
        payment_method_options: {
          klarna: {
            subscription_reference: "EXAMPLE_REFERENCE",
          },
        },
      },
    ],
  },
  payment_method_options: {
    klarna: {
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "year",
        },
      ],
    },
  },
});
```

The resulting PaymentIntent requires a redirect to Klarna to be completed. Learn how to [handle the redirect](https://docs.stripe.com/payments/klarna/set-up-future-payments.md#react-native-redirect-customer).

#### Upgrade and charge later

Create a [SetupIntent](https://docs.stripe.com/api/payment_intents.md) and pass the existing saved payment method. Pass the new subscription information and use the same `reference` as when you first saved the payment method.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  return_url: "https://example.com/setup/complete",
  payment_method_options: {
    klarna: {
      currency: "usd",
      subscriptions: [
        {
          reference: "EXAMPLE_REFERENCE",
          interval: "annual",
          next_billing: {
            amount: 20000,
            date: "2026-01-01",
          },
        },
      ],
    },
  },
});
```

The resulting SetupIntent requires a redirect to Klarna to be completed. Learn how to [handle the redirect](https://docs.stripe.com/payments/klarna/set-up-future-payments.md#react-native-redirect-customer).

## Optional: Remove a saved Klarna account [Server-side]

You can use the [detach](https://docs.stripe.com/api/payment_methods/detach.md) API to remove a customer’s saved Klarna account as a payment method. Remove a Klarna account when you know it won’t be used again, such as when the customer cancels their subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.detach(
  "{{PAYMENT_METHOD_ID}}",
);
```
