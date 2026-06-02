<!-- Source URL: https://docs.stripe.com/billing/subscriptions/klarna -->
<!-- Fetched: 2026-05-13 -->

# Set up a subscription with Klarna

Learn how to create and charge for a subscription with Klarna.

Use this guide to set up a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) using [Klarna](https://docs.stripe.com/payments/klarna.md) as a payment method.

> #### Available Klarna payment options vary by use case and buyer country
>
> See which [payment options](https://docs.stripe.com/payments/klarna.md#payment-options) are available for your customers before you start your integration.

We recommend using [Stripe Checkout](https://docs.stripe.com/payments/checkout.md) to save Klarna as a payment method.

# Stripe-hosted page

> This is a Stripe-hosted page for when api-integration is checkout. View the full page at https://docs.stripe.com/billing/subscriptions/klarna?api-integration=checkout.

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 USD monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **USD** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

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

Create a Checkout Session with the ID of an existing [Price](https://docs.stripe.com/api/prices.md). Set the mode to `subscription` and pass at least one recurring price. You can add one-time prices in addition to recurring prices. After creating the Checkout Session, redirect your customer to the [URL](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-url) returned in the response.

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
  mode: "subscription",
  success_url: "https://example.com/success?session_id={CHECKOUT_SESSION_ID}",
});
```

When your customer successfully completes their payment, Stripe redirects them to the `success_url`, a page on your website that informs the customer that their payment was successful. Make the Session ID available on your success page by including the `{CHECKOUT_SESSION_ID}` template variable in the `success_url` as in the above example.

Checkout Sessions expire 24 hours after creation.

> Don’t rely on the redirect to the `success_url` alone for detecting payment initiation, because:
>
> - Malicious users could directly access the `success_url` without paying and gain access to your goods or services.

- After a successful payment, customers might close their browser tab before they’re redirected to the `success_url`.

### Set up a trial

You can create free trials in a Checkout Session by using the [subscription_data](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data) parameter to provide information about the length, end date, and other trial settings.

Learn how to [configure free trials to cancel or pause when they end without a payment method](https://docs.stripe.com/billing/subscriptions/trials/free-trials.md?how=checkout#create-free-trials-without-payment).

## Retrieve the subscription [Server-side]

After a customer submits their payment details, Stripe automatically creates a Subscription. You can retrieve the Subscription synchronously using the `success_url` or asynchronously using _webhooks_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests).

The decision to retrieve the subscription synchronously or asynchronously depends on your tolerance for drop-off because customers might not always reach the `success_url` after a successful payment (for example, it’s possible for them to close their browser tab before the redirect occurs). Using webhooks prevents your integration from encountering this form of drop-off.

#### Webhooks

Handle `checkout.session.completed` webhooks, which contain a Session object. Learn how to [set up webhooks](https://docs.stripe.com/webhooks.md).

The following example is a `checkout.session.completed` response.

```json
{
  "id": "evt_1Ep24XHssDVaQm2PpwS19Yt0",
  "object": "event",
  "api_version": "2019-03-14",
  "created": 1561420781,
  "data": {
    "object": {
      "id": "cs_test_a1h2mO4eLbjemY0JWW9rCz5dcglwr3M5ldjLOvpGxWD37i1Oi5SeFhSup1",
      "object": "checkout.session",
      "billing_address_collection": null,
      "client_reference_id": null,
      "customer": null,
      "customer_email": null,
      "display_items": [],
      "mode": "setup",
      "subscription": "sub_1Op9VFCvDOElLqwO6fs7Na4P",
      "submit_type": null,
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

Keep a record of the value of the `subscription` key, which is the ID for the [Subscription](https://docs.stripe.com/api/subscriptions.md) created from the Checkout Session.

#### Success URL

Obtain the `session_id` from the URL when a user redirects back to your site and [retrieve](https://docs.stripe.com/api/checkout/sessions/retrieve.md) the Session object.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.retrieve("{{SESSION_ID}}", {
  expand: ["subscription"],
});
```

> To make sure that the `session_id` is available from the URL, include the `session_id={CHECKOUT_SESSION_ID}` template variable in the `success_url` when you create the Checkout Session.

The response contains the created [Subscription](https://docs.stripe.com/api/subscriptions.md) under the [subscription](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-subscription) key.

## Test your integration

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

# Advanced integration

> This is a Advanced integration for when api-integration is elements. View the full page at https://docs.stripe.com/billing/subscriptions/klarna?api-integration=elements.

If you want to create a customized payments UI with the [Payment Element](https://docs.stripe.com/payments/payment-element.md), use the [Subscriptions API](https://docs.stripe.com/api/subscriptions.md) to create a subscription.

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 USD monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **USD** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create a subscription [Server-side]

Create a [subscription](https://docs.stripe.com/api/subscriptions.md) that has a price and customer with status of `incomplete` by providing the [payment_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-payment_behavior) parameter with a value of `default_incomplete`. Set the `payment_settings.save_default_payment_method=on_subscription` parameter to save a payment method when a subscription is activated.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  payment_behavior: "default_incomplete",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  payment_settings: {
    save_default_payment_method: "on_subscription",
  },
  expand: ["latest_invoice.payments", "latest_invoice.confirmation_secret"],
});
```

The response includes the _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis)’s first [Invoice](https://docs.stripe.com/api/invoices.md). This contains the invoice’s payments, which includes a default PaymentIntent that Stripe generated for this invoice and the confirmation secret which you can use on the client side to securely complete the payment process instead of passing the entire PaymentIntent object. Get the PaymentIntent ID that you must use to confirm a payment from `latest_invoice.payments`. Return the `latest_invoice.confirmation_secret.client_secret` to the front end to complete payment.

### Set up a trial

You can set up subscriptions with free trials. Learn how to [delay payments on active subscriptions with trial periods](https://docs.stripe.com/billing/subscriptions/trials.md).

## Collect payment information [Client-side]

### Set up Stripe Elements

The Payment Element is automatically available as a feature of Stripe.js. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
<body>
  <!-- content here -->
</body>
```

Create an instance of Stripe with the following JavaScript on your checkout page:

```javascript
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

### Add the Payment Element to your page

The Payment Element needs a place to live on your payment page. Create an empty DOM node (container) with a unique ID in your payment form.

```html
<form id="payment-form">
  <div id="payment-element">
    <!-- Elements will create form elements here -->
  </div>
  <button id="submit">Subscribe</button>
  <div id="error-message">
    <!-- Display error message to your customers here -->
  </div>
</form>
```

When the form above has loaded, create an instance of the Payment Element and mount it to the container DOM node. In the [create the subscription](https://docs.stripe.com/billing/subscriptions/klarna.md#pi-create-subscription) step, you passed the `client_secret` value to the frontend. Pass this value as an option when creating an instance of Elements.

```javascript
const options = {
  clientSecret: "{{CLIENT_SECRET}}",
};

// Set up Stripe.js and Elements to use in checkout form, passing the client secret obtained in step 5
const elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: "accordion" };
const paymentElement = elements.create("payment", paymentElementOptions);
paymentElement.mount("#payment-element");
```

The Payment Element renders a dynamic form that allows your customer to select a payment method. The form automatically collects all necessary payments details for the payment method that they select.

### Complete payment

Use `stripe.confirmPayment` to complete the payment using details from the Payment Element and activate the subscription. This creates a PaymentMethod and confirms the incomplete Subscription’s first PaymentIntent, causing a charge to be made.

Stripe redirects the customer to Klarna to complete the first payment and future payments. Provide a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to indicate where the user should be redirect after completing the checkout on Klarna.

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const { error } = await stripe.confirmPayment({
    //`Elements` instance that was used to create the Payment Element
    elements,
    confirmParams: {
      return_url: "https://example.com/order/123/complete",
      mandate_data: {
        customer_acceptance: {
          type: "online",
          online: {
            infer_from_client: true,
          },
        },
      },
    },
  });

  if (error) {
    // This point will only be reached if there is an immediate error when
    // confirming the payment. Show error to your customer (for example, payment
    // details incomplete)
    const messageContainer = document.querySelector("#error-message");
    messageContainer.textContent = error.message;
  }
});
```

After the user has been redirected, query the PaymentIntent to check its status. If the status is `succeeded`, the payment was successful and your subscription is now active.

## Test your integration

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
