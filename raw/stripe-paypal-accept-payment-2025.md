# Accept a PayPal payment

Learn how to accept PayPal payment, a digital wallet popular with businesses in Europe.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/paypal/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Stripe Checkout shows PayPal either as a standard payment method or as a standalone button, depending on which option is more likely to increase the conversion rate.

## Determine compatibility

**Supported business locations**: Europe, GB, EEA

**Supported currencies**: `eur, gbp, usd, chf, czk, dkk, nok, pln, sek, aud, cad, hkd, nzd, sgd`

**Presentment currencies**: `eur, gbp, usd, chf, czk, dkk, nok, pln, sek, aud, cad, hkd, nzd, sgd`

**Payment mode**: Yes

**Setup mode**: Yes

**Subscription mode**: Yes

A Checkout Session must satisfy all of the following conditions to support PayPal payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.

## Accept a payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

This guides you through enabling PayPal and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable PayPal as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), do the following:

1. Add `paypal` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the same currency.

#### Stripe-hosted page

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
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "paypal"],
  success_url: "https://example.com/success",
});
```

#### Full embedded page

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
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "paypal"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

You don’t need to connect your PayPal business account to test the integration. However, make sure to connect your PayPal and Stripe accounts when you’re ready to [activate live mode payments](https://docs.stripe.com/payments/paypal/activate.md).

When Checkout shows the **PayPal** button, you need a [personal PayPal Sandbox account](https://developer.paypal.com/tools/sandbox/accounts/) to complete the test payment. If Checkout lists PayPal as a payment method instead, select **PayPal** and click **Pay**—no PayPal Sandbox account is required.

To simulate the most common integration and failure scenarios for PayPal payments, pass `email` values that match the patterns described in these [test scenarios](https://docs.stripe.com/payments/paypal/accept-a-payment.md?platform=web&ui=stripe-hosted#test-scenarios).

### Test scenarios

| Email pattern                   | Scenario                                 | Explanation                                                                                                                                                                                                                          |
| ------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `.*payee_account_restricted@.*` | Merchant account restricted              | Capturing or authorizing a payment fails with a `payment_method_unexpected_state` error if your merchant account is restricted by PayPal. Provide an email matching this pattern at time of authorization to fail the authorization. |
| `.*transaction_refused@.*`      | Transaction refused                      | Capturing a payment fails with a `payment_method_provider_decline` error if the transaction is refused by PayPal.                                                                                                                    |
| `.*instrument_declined@.*`      | Payment instrument declined              | Capturing a payment fails with a `payment_method_provider_decline` error if the instrument presented was either declined by the processor or bank, or it can’t be used for this payment.                                             |
| `.*authorization_expired@.*`    | Manually capturing an authorized payment | Capturing an authorized payment fails with a `capture_charge_authorization_expired` error if the authorization has already expired.                                                                                                  |

## Handle refunds and disputes

Learn more about PayPal [disputes](https://docs.stripe.com/payments/paypal.md#disputed-payments) and [refunds](https://docs.stripe.com/payments/paypal.md#refunds).

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/paypal/accept-a-payment?payment-ui=direct-api.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

Stripe uses a payment object, called a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md), to track and handle all the states of the payment until it’s completed. Create a `PaymentIntent` on your server, specifying the amount to collect and the currency. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `paypal` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["paypal"],
});
```

Included in the returned PaymentIntent is a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which is used to securely complete the payment process instead of passing the entire PaymentIntent object. Send the client secret back to the client so you can use it in later steps.

#### Include a custom description

By default, the order details on the PayPal users purchase activity page displays the order amount. You can change this by providing a custom description in the `description` property.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  description: "A sample description",
  payment_method_types: ["paypal"],
});
```

#### Customize the preferred locale

By default, the PayPal authorization page is localized based on variables such as the business’s country. You can set this to your customer’s preferred locale using the `preferred_locale` property. The value must be a two-character lowercased language code, followed by a hyphen (`-`), followed by a two-character uppercased country code. For example, the value for a French-language user in Belgium would be `fr-BE`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["paypal"],
  payment_method_options: {
    paypal: {
      preferred_locale: "fr-BE",
    },
  },
});
```

You can set the PayPal authorization page to your customer’s preferred locale through the [preferred_locale](https://docs.stripe.com/payments/paypal/accept-a-payment.md#customize-the-preferred-locale) property. See the following table for supported locales:

| Value | Locale     | Country                  |
| ----- | ---------- | ------------------------ |
| cs-CZ | Czech      | The Czech Republic       |
| da-DK | Danish     | Denmark                  |
| de-AT | German     | Austria                  |
| de-DE | German     | Germany                  |
| de-LU | German     | Luxembourg               |
| el-GR | Greek      | Greece                   |
| en-GB | English    | United Kingdom           |
| en-US | English    | United States of America |
| es-ES | Spanish    | Spain                    |
| fi-FI | Finnish    | Finland                  |
| fr-BE | French     | Belgium                  |
| fr-FR | French     | France                   |
| fr-LU | French     | Luxembourg               |
| hu-HU | Hungarian  | Hungary                  |
| it-IT | Italian    | Italy                    |
| nl-BE | Dutch      | Belgium                  |
| nl-NL | Dutch      | Netherlands              |
| pl-PL | Polish     | Poland                   |
| pt-PT | Portuguese | Portugal                 |
| sk-SK | Slovak     | Slovakia                 |
| sv-SE | Swedish    | Sweden                   |

#### Statement descriptors with PayPal

The descriptor that appears on the buyer’s bank statement is set by PayPal, and by default is `PAYPAL *YOUR_BUSINESS_NAME`. If you set the `statement_descriptor` field when creating the `PaymentIntent`, its value is appended to the one set by PayPal, up to a total limit of 22 characters.

For example, if your business name in PayPal is `BUSINESS` and you set `statement_descriptor` to `order_id_1234`, buyers see `PAYPAL *BUSINESS order` on their bank account statement.

## Submit the payment to Stripe [Client-side]

When a customer clicks to pay with PayPal, use Stripe.js to submit the payment to Stripe. [Stripe.js](https://docs.stripe.com/payments/elements.md) is the foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and enables you to extend your integration to other payment methods. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout page.

```javascript
// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

To create a payment on the client side, pass the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object that you created in [Step 2](https://docs.stripe.com/payments/paypal/accept-a-payment.md#create-payment-intent). The client secret is different from your API keys that authenticate Stripe API requests. Handle this carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

### Confirm PayPal payment

Call [stripe.confirmPayPalPayment](https://docs.stripe.com/js/payment_intents/confirm_paypal_payment) to redirect your customer to PayPal to complete the payment. You must add a `return_url` to specify where Stripe will redirect your customer after they complete the payment. You can also add the `return_url` for new PayPal payment methods, but it’s not required when using a previously set up PayPal payment method with SetupIntent or a PaymentIntent that includes `setup_future_usage`.

```javascript
// Redirects away from the client
const { error } = await stripe.confirmPayPalPayment(
  "{{PAYMENT_INTENT_CLIENT_SECRET}}",
  {
    return_url: "https://example.com/checkout/complete",
  },
);

if (error) {
  // Inform the customer that there was an error.
}
```

If you settle your PayPal funds with PayPal, the [balance transaction](https://docs.stripe.com/api.md#balance_transaction_object) linked to the payment has an amount of zero regardless of the payment amount, because the transaction represents money moved into and out of your Stripe balance. However, for PayPal, funds settle in your PayPal balance, and no money goes to your Stripe balance. The balance transaction in this case also includes fees associated with it. Learn about other important details related to the [settlement preference](https://docs.stripe.com/payments/paypal/choose-settlement-preference.md).

### Handling the redirect

The following URL query parameters are provided when Stripe redirects the customer to the `return_url`.

| Parameter                      | Description                                                                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. |

You can also append your own query parameters when providing the `return_url`. They persist throughout the redirect process. The `return_url` should correspond to a page on your website that provides the status of the payment. You should verify the status of the `PaymentIntent` when rendering the return page. You can do so by using the `retrievePaymentIntent` function from Stripe.js and passing in the `payment_intent_client_secret`.

```javascript
(async () => {
  const url = new URL(window.location);
  const clientSecret = url.searchParams.get("payment_intent_client_secret");

  const { paymentIntent, error } =
    await stripe.retrievePaymentIntent(clientSecret);
  if (error) {
    // Handle error
  } else if (paymentIntent && paymentIntent.status === "succeeded") {
    // Handle successful payment
  }
})();
```

You can find the payment owner’s name, email, payer ID, and transaction ID in the [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-paypal) property.

| Field            | Value                                                   |
| ---------------- | ------------------------------------------------------- |
| `payer_email`    | The email address of the payer on their PayPal account. |
| `payer_name`     | The name of the payer on their PayPal account.          |
| `payer_id`       | A unique ID of the payer’s PayPal account.              |
| `transaction_id` | A unique transaction ID generated by PayPal.            |

#### Json

```json
{
  "charges": {
    "data": [
      {
        "payment_method_details": {
          "paypal": {
            "payer_id": "H54KFE9XXVVYJ",
            "payer_email": "jenny@example.com",
            "payer_name": "Jenny Rosen",
            "transaction_id": "89W40396MK104212M"
          },
          "type": "paypal"
        },
        "id": "src_16xhynE8WzK49JbAs9M21jaR",
        "object": "source",
        "amount": 1099,
        "client_secret": "src_client_secret_UfwvW2WHpZ0s3QEn9g5x7waU",
        "created": 1445277809,
        "currency": "eur",
        "flow": "redirect",
        "livemode": true,
        "statement_descriptor": null,
        "status": "pending",
        "type": "paypal",
        "usage": "single_use"
      }
    ],
    "object": "list",
    "has_more": false,
    "url": "/v1/charges?payment_intent=pi_1G1sgdKi6xqXeNtkldRRE6HT"
  },
  "payment_method_options": {
    "paypal": {}
  },
  "payment_method_types": ["paypal"],
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  "amount": 1099,
  "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
  "confirmation_method": "automatic",
  "created": 1579259303,
  "currency": "eur",
  "livemode": true,
  "next_action": null
}
```

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

There are a few options for receiving and running business actions.

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Handle the PayPal redirect manually

Stripe.js helps you extend your integration to other payment methods. However, you can manually redirect your customers on your server.

1. Create and *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) a PaymentIntent of type `paypal`. By specifying `payment_method_data`, a PaymentMethod is created and immediately used with the PaymentIntent.

You must also provide the URL where your customer is redirected to after they complete their payment in the `return_url` field. You can provide your own query parameters in this URL. These parameters are included in the final URL upon completing the redirect flow.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["paypal"],
  payment_method_data: {
    type: "paypal",
  },
  return_url: "https://example.com/checkout/complete",
  confirm: true,
});
```

1. Check that the `PaymentIntent` has a status of `requires_action` and the type for `next_action` is `redirect_to_url`.

#### Json

```json
{"status": "requires_action",
  "next_action": {
    "type": "redirect_to_url",
    "redirect_to_url": {
      "url": "https://hooks.stripe.com/...",
      "return_url": "https://example.com/checkout/complete"
    }
  },
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  ...
}
```

1. Redirect the customer to the URL provided in the `next_action.redirect_to_url.url` property. This code example is approximate—the redirect method might be different in your web framework.

#### Node.js

```javascript
if (
  paymentIntent.status === "requires_action" &&
  paymentIntent.next_action.type === "redirect_to_url"
) {
  const url = paymentIntent.next_action.redirect_to_url.url;
  res.redirect(url);
}
```

Your customer is redirected to the `return_url` when they complete the payment process. The `payment_intent` and `payment_intent_client_secret` URL query parameters are included along with any of your own query parameters. Stripe recommends setting up a [webhook endpoint](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to programmatically confirm the status of a payment.

## Optional: Authorize a payment and then capture later

PayPal supports [separate authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md). If you’ve opted for [settlement to Stripe](https://docs.stripe.com/payments/paypal/choose-settlement-preference.md), your authorizations are valid for 10 days. Stripe automatically reauthorizes the payment to extend the authorization period by another 10 days. This results in a total of 20 days. If the reauthorization doesn’t work, Stripe makes the payment expire right after 10 days. Listen to the [charge.expired](https://docs.stripe.com/api/events/types.md#event_types-charge.expired) webhook to know when the authorization period ends.

If you’ve opted for [settlement to PayPal](https://docs.stripe.com/payments/paypal/choose-settlement-preference.md), your authorizations remain valid for 3 days. Stripe tries to extend the authorization period by another 3 days. For an extended guaranteed authorization period of up to 10 days, referred to as *honor period* on PayPal, contact [PayPal support](https://www.paypal.com/nu/cshelp/business).

### Tell Stripe to authorize only

To indicate that you want separate authorization and capture, set [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) to `manual` when creating the PaymentIntent. This parameter instructs Stripe to only authorize the amount on the customer’s PayPal account.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  capture_method: "manual",
  payment_method_types: ["paypal"],
  payment_method_data: {
    type: "paypal",
  },
  confirm: true,
  return_url: "http://example.com",
});
```

Upon authorization success, Stripe sends a [payment_intent.amount_capturable_updated](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.amount_capturable_updated) event. Read our [Events guide](https://docs.stripe.com/api/events.md) to learn more.

### Capture the funds

After the authorization succeeds, the PaymentIntent [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) transitions to `requires_capture`. To capture the authorized funds, make a PaymentIntent [capture](https://docs.stripe.com/api/payment_intents/capture.md) request. The total authorized amount is captured by default—you can’t capture more than this, but you can capture less.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "{{PAYMENT_INTENT_ID}}",
  {
    amount_to_capture: 750,
  },
);
```

### (Optional) Cancel the authorization

If you need to cancel an authorization, you can [cancel the PaymentIntent](https://docs.stripe.com/refunds.md#cancel-payment).

## Optional: Turn on asynchronous payment methods on PayPal

By default, Stripe only allows synchronous payment methods on PayPal. This guarantees that you receive an [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) for the success or the failure of each payment. If you allow asynchronous payment methods, you might encounter [delayed notifications](https://docs.stripe.com/payments/payment-methods.md#payment-notification) for some payments. As a result, you must rely on [webhook endpoints](https://docs.stripe.com/payments/payment-methods.md#webhooks) to receive notifications about the success or failure of certain payments.

To enable asynchronous payments on PayPal, contact [Stripe support](https://support.stripe.com/contact).

## Optional: Error codes

These are the common error codes and corresponding details while integrating with PayPal. If a PayPal API request returned the error, it includes a PayPal issue code and the associated Debug ID for the request. You can use the Debug ID when contacting [PayPal support](https://www.paypal-support.com/) to get help with your issue.

| Error Code                        | Details                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `country_code_invalid`            | The specified country code in the shipping address is invalid.                                                                                                                                                                                                                                                                                                                   |
| `incorrect_address`               | The specified shipping address is invalid. This error is also thrown if the specified country additionally requires either a city or a postal code. For further information, please check the error message and contact [PayPal support](https://www.paypal-support.com/) with the `Debug ID` and `PayPal issue`.                                                                |
| `payment_method_not_available`    | The `paypal` payment method is currently not available. This error might be caused by a timeout or server issue when connecting to PayPal API.                                                                                                                                                                                                                                   |
| `payment_method_provider_decline` | The transaction is declined by PayPal. This is commonly caused by the business’s fraud protection settings on PayPal, a compliance violation, or the payer being unable to pay with the chosen funding instrument. For further information, please check the error message and contact [PayPal support](https://www.paypal-support.com/) with the `Debug ID` and `PayPal issue`. |
| `payment_method_provider_timeout` | The request timed out on PayPal. In most cases, this is a transient error and you can retry the request after a few moments.                                                                                                                                                                                                                                                     |
| `payment_method_unactivated`      | The `paypal` payment method isn’t activated for your Stripe account.                                                                                                                                                                                                                                                                                                             |
| `payment_method_unexpected_state` | The request failed on PayPal. This can occur if the merchant’s business account is locked, restricted, or closed by PayPal, or if the payer’s PayPal account is restricted. For further information, please check the error message and contact [PayPal support](https://www.paypal-support.com/) with the `Debug ID` and `PayPal issue`.                                        |

## Optional: Test PayPal integration

To test a successful payment on your PayPal integration, use your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) and view the redirect page. This page shows you the options to **Authorize** or **Fail** the user authentication as test scenarios. When you select **Authorize test payment**, the PaymentIntent transitions from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click **Fail test payment**. The PaymentIntent then transitions from `requires_action` to `requires_payment_method`.

To simulate the most common integration and failure scenarios for PayPal payments, pass `email` values that match the patterns described in [Test Scenarios](https://docs.stripe.com/payments/paypal/accept-a-payment.md?platform=web#test-scenarios) when you create the PaymentIntent as part of the [billing details](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_data-billing_details). For example, when confirming the PaymentIntent server-side, a request simulating a transaction refused by PayPal would look like:

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1099 \
  -d currency=eur \
  -d "payment_method_types[]=paypal" \
  -d "payment_method_data[type]=paypal" \
  --data-urlencode "payment_method_data[billing_details][email]=transaction_refused@example.com"
```

### Test scenarios

| Email pattern                   | Scenario                                 | Explanation                                                                                                                                                                                                                          |
| ------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `.*payee_account_restricted@.*` | Merchant account restricted              | Capturing or authorizing a payment fails with a `payment_method_unexpected_state` error if your merchant account is restricted by PayPal. Provide an email matching this pattern at time of authorization to fail the authorization. |
| `.*transaction_refused@.*`      | Transaction refused                      | Capturing a payment fails with a `payment_method_provider_decline` error if the transaction is refused by PayPal.                                                                                                                    |
| `.*instrument_declined@.*`      | Payment instrument declined              | Capturing a payment fails with a `payment_method_provider_decline` error if the instrument presented was either declined by the processor or bank, or it can’t be used for this payment.                                             |
| `.*authorization_expired@.*`    | Manually capturing an authorized payment | Capturing an authorized payment fails with a `capture_charge_authorization_expired` error if the authorization has already expired.                                                                                                  |

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/paypal/accept-a-payment?payment-ui=mobile&platform=ios.

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

## Create a PaymentIntent [Server-side] [Client-side]

### Server-side

Stripe uses a payment object, called a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md), to track and handle all the states of the payment until it’s completed. Create a `PaymentIntent` on your server, specifying the amount to collect and the currency. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `paypal` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["paypal"],
});
```

Included in the returned PaymentIntent is a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which is used to securely complete the payment process instead of passing the entire PaymentIntent object. Send the client secret back to the client so you can use it in later steps.

#### Include a custom description

By default, the order details on the PayPal users purchase activity page displays the order amount. You can change this by providing a custom description in the `description` property.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  description: "A sample description",
  payment_method_types: ["paypal"],
});
```

#### Customize the preferred locale

By default, the PayPal authorization page is localized based on variables such as the business’s country. You can set this to your customer’s preferred locale using the `preferred_locale` property. The value must be a two-character lowercased language code, followed by a hyphen (`-`), followed by a two-character uppercased country code. For example, the value for a French-language user in Belgium would be `fr-BE`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["paypal"],
  payment_method_options: {
    paypal: {
      preferred_locale: "fr-BE",
    },
  },
});
```

You can set the PayPal authorization page to your customer’s preferred locale through the [preferred_locale](https://docs.stripe.com/payments/paypal/accept-a-payment.md#customize-the-preferred-locale) property. See the following table for supported locales:

| Value | Locale     | Country                  |
| ----- | ---------- | ------------------------ |
| cs-CZ | Czech      | The Czech Republic       |
| da-DK | Danish     | Denmark                  |
| de-AT | German     | Austria                  |
| de-DE | German     | Germany                  |
| de-LU | German     | Luxembourg               |
| el-GR | Greek      | Greece                   |
| en-GB | English    | United Kingdom           |
| en-US | English    | United States of America |
| es-ES | Spanish    | Spain                    |
| fi-FI | Finnish    | Finland                  |
| fr-BE | French     | Belgium                  |
| fr-FR | French     | France                   |
| fr-LU | French     | Luxembourg               |
| hu-HU | Hungarian  | Hungary                  |
| it-IT | Italian    | Italy                    |
| nl-BE | Dutch      | Belgium                  |
| nl-NL | Dutch      | Netherlands              |
| pl-PL | Polish     | Poland                   |
| pt-PT | Portuguese | Portugal                 |
| sk-SK | Slovak     | Slovakia                 |
| sv-SE | Swedish    | Sweden                   |

#### Statement descriptors with PayPal

The descriptor that appears on the buyer’s bank statement is set by PayPal, and by default is `PAYPAL *YOUR_BUSINESS_NAME`. If you set the `statement_descriptor` field when creating the `PaymentIntent`, its value is appended to the one set by PayPal, up to a total limit of 22 characters.

For example, if your business name in PayPal is `BUSINESS` and you set `statement_descriptor` to `order_id_1234`, buyers see `PAYPAL *BUSINESS order` on their bank account statement.

### Client-side

On the client, request a PaymentIntent from your server and store its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)).

#### Swift

```swift
class CheckoutViewController: UIViewController {
    var paymentIntentClientSecret: String?

    // ...continued from previous step

    override func viewDidLoad() {
        // ...continued from previous step
        startCheckout()
    }

    func startCheckout() {
        // Request a PaymentIntent from your server and store its client secret
        // Click View full sample to see a complete implementation
    }
}
```

## Submit the payment to Stripe [Client-side]

When a customer taps to pay with PayPal, confirm the `PaymentIntent` to complete the payment. Configure an `STPPaymentIntentParams` object with the `PaymentIntent` [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret).

The client secret is different from your API keys that authenticate Stripe API requests. Handle this carefully as it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

### Set up a return URL

The iOS SDK presents a webview in your app to complete the PayPal payment. When authentication is finished, the webview can automatically dismiss itself instead of having your customer close it. To enable this behavior, configure a custom URL scheme or universal link and set up your app delegate to forward the URL to the SDK.

#### Swift

```swift
// This method handles opening custom URL schemes (for example, "your-app://stripe-redirect")
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool {
    let stripeHandled = StripeAPI.handleURLCallback(with: url)
    if (stripeHandled) {
        return true
    } else {
        // This was not a Stripe url – handle the URL normally as you would
    }
    return false
}

// This method handles opening universal link URLs (for example, "https://example.com/stripe_ios_callback")
func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    if userActivity.activityType == NSUserActivityTypeBrowsingWeb {
        if let url = userActivity.webpageURL {
            let stripeHandled = StripeAPI.handleURLCallback(with: url)
            if (stripeHandled) {
                return true
            } else {
                // This was not a Stripe url – handle the URL normally as you would
            }
        }
    }
    return false
}
```

Pass the URL as the `return_url` when you confirm the PaymentIntent. After webview-based authentication is finished, Stripe redirects the user to the `return_url`.

### Confirm PayPal payment

Complete the payment by calling `STPPaymentHandler confirmPayment`. This presents a webview where the customer can complete the payment with PayPal. Upon completion, the completion block is called with the result of the payment.

#### Swift

```swift
let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)

// PayPal doesn't require additional parameters so we only need to pass the initialized
// STPPaymentMethodPayPalParams instance to STPPaymentMethodParams
let payPal = STPPaymentMethodPayPalParams()
let paymentMethodParams = STPPaymentMethodParams(payPal: payPal, billingDetails: nil, metadata: nil)

paymentIntentParams.paymentMethodParams = paymentMethodParams

STPPaymentHandler.shared().confirmPayment(paymentIntentParams,
                                          with: self)
{ (handlerStatus, paymentIntent, error) in
    switch handlerStatus {
    case .succeeded:
        // Payment succeeded
        // ...

    case .canceled:
        // Payment canceled
        // ...

    case .failed:
        // Payment failed
        // ...

    @unknown default:
        fatalError()
    }
}
```

You can find the payment owner’s name, email, payer ID, and transaction ID in the [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-paypal) property.

| Field            | Value                                                   |
| ---------------- | ------------------------------------------------------- |
| `payer_email`    | The email address of the payer on their PayPal account. |
| `payer_name`     | The name of the payer on their PayPal account.          |
| `payer_id`       | A unique ID of the payer’s PayPal account.              |
| `transaction_id` | A unique transaction ID generated by PayPal.            |

#### Json

```json
{
  "charges": {
    "data": [
      {
        "payment_method_details": {
          "paypal": {
            "payer_id": "H54KFE9XXVVYJ",
            "payer_email": "jenny@example.com",
            "payer_name": "Jenny Rosen",
            "transaction_id": "89W40396MK104212M"
          },
          "type": "paypal"
        },
        "id": "src_16xhynE8WzK49JbAs9M21jaR",
        "object": "source",
        "amount": 1099,
        "client_secret": "src_client_secret_UfwvW2WHpZ0s3QEn9g5x7waU",
        "created": 1445277809,
        "currency": "eur",
        "flow": "redirect",
        "livemode": true,
        "statement_descriptor": null,
        "status": "pending",
        "type": "paypal",
        "usage": "single_use"
      }
    ],
    "object": "list",
    "has_more": false,
    "url": "/v1/charges?payment_intent=pi_1G1sgdKi6xqXeNtkldRRE6HT"
  },
  "payment_method_options": {
    "paypal": {}
  },
  "payment_method_types": ["paypal"],
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  "amount": 1099,
  "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
  "confirmation_method": "automatic",
  "created": 1579259303,
  "currency": "eur",
  "livemode": true,
  "next_action": null
}
```

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

There are a few options for receiving and running business actions.

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/paypal/accept-a-payment?payment-ui=mobile&platform=android.

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

## Create a PaymentIntent [Server-side] [Client-side]

### Server-side

Stripe uses a payment object, called a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md), to track and handle all the states of the payment until it’s completed. Create a `PaymentIntent` on your server, specifying the amount to collect and the currency. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `paypal` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["paypal"],
});
```

Included in the returned PaymentIntent is a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which is used to securely complete the payment process instead of passing the entire PaymentIntent object. Send the client secret back to the client so you can use it in later steps.

#### Include a custom description

By default, the order details on the PayPal users purchase activity page displays the order amount. You can change this by providing a custom description in the `description` property.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  description: "A sample description",
  payment_method_types: ["paypal"],
});
```

#### Customize the preferred locale

By default, the PayPal authorization page is localized based on variables such as the business’s country. You can set this to your customer’s preferred locale using the `preferred_locale` property. The value must be a two-character lowercased language code, followed by a hyphen (`-`), followed by a two-character uppercased country code. For example, the value for a French-language user in Belgium would be `fr-BE`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["paypal"],
  payment_method_options: {
    paypal: {
      preferred_locale: "fr-BE",
    },
  },
});
```

You can set the PayPal authorization page to your customer’s preferred locale through the [preferred_locale](https://docs.stripe.com/payments/paypal/accept-a-payment.md#customize-the-preferred-locale) property. See the following table for supported locales:

| Value | Locale     | Country                  |
| ----- | ---------- | ------------------------ |
| cs-CZ | Czech      | The Czech Republic       |
| da-DK | Danish     | Denmark                  |
| de-AT | German     | Austria                  |
| de-DE | German     | Germany                  |
| de-LU | German     | Luxembourg               |
| el-GR | Greek      | Greece                   |
| en-GB | English    | United Kingdom           |
| en-US | English    | United States of America |
| es-ES | Spanish    | Spain                    |
| fi-FI | Finnish    | Finland                  |
| fr-BE | French     | Belgium                  |
| fr-FR | French     | France                   |
| fr-LU | French     | Luxembourg               |
| hu-HU | Hungarian  | Hungary                  |
| it-IT | Italian    | Italy                    |
| nl-BE | Dutch      | Belgium                  |
| nl-NL | Dutch      | Netherlands              |
| pl-PL | Polish     | Poland                   |
| pt-PT | Portuguese | Portugal                 |
| sk-SK | Slovak     | Slovakia                 |
| sv-SE | Swedish    | Sweden                   |

#### Statement descriptors with PayPal

The descriptor that appears on the buyer’s bank statement is set by PayPal, and by default is `PAYPAL *YOUR_BUSINESS_NAME`. If you set the `statement_descriptor` field when creating the `PaymentIntent`, its value is appended to the one set by PayPal, up to a total limit of 22 characters.

For example, if your business name in PayPal is `BUSINESS` and you set `statement_descriptor` to `order_id_1234`, buyers see `PAYPAL *BUSINESS order` on their bank account statement.

### Client-side

On the client, request a PaymentIntent from your server and store its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)).

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {

  private lateinit var paymentIntentClientSecret: String

  override fun onCreate(savedInstanceState: Bundle?) {
      super.onCreate(savedInstanceState)
      // ...
      startCheckout()
  }

  private fun startCheckout() {
      // Request a PaymentIntent from your server and store its client secret in paymentIntentClientSecret
      // Click View full sample to see a complete implementation
  }
}
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the SetupIntent you created and call [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/index.html#74063765%2FFunctions%2F-1622557690). This presents a webview where the customer can complete the setup on their bank’s website or app. Afterwards, `onPaymentResult` is called with the result of the payment.

#### Kotlin

```kotlin
class CheckoutActivity : AppCompatActivity() {
    // ...
    private lateinit var paymentIntentClientSecret: String
    private val paymentLauncher: PaymentLauncher by lazy {
        PaymentLauncher.Companion.create(
            this,
            PaymentConfiguration.getInstance(applicationContext).publishableKey,
            PaymentConfiguration.getInstance(applicationContext).stripeAccountId,
            ::onPaymentResult
        )
    }

    private fun startCheckout() {
        // ...

        val confirmParams = ConfirmPaymentIntentParams
            .createWithPaymentMethodCreateParams(
                paymentMethodCreateParams = PaymentMethodCreateParams.createPayPal(),
                clientSecret = paymentIntentClientSecret
            )
        paymentLauncher.confirm(confirmParams)
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        val message = when (paymentResult) {
            is PaymentResult.Completed -> {
                "Completed!"
            }
            is PaymentResult.Canceled -> {
                "Canceled!"
            }
            is PaymentResult.Failed -> {
                // This string comes from the PaymentIntent's error message.
                // See here: https://stripe.com/docs/api/payment_intents/object#payment_intent_object-last_payment_error-message
                "Failed: " + paymentResult.throwable.message
            }
        }
    }
}
```

You can find the payment owner’s name, email, payer ID, and transaction ID in the [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-paypal) property.

| Field            | Value                                                   |
| ---------------- | ------------------------------------------------------- |
| `payer_email`    | The email address of the payer on their PayPal account. |
| `payer_name`     | The name of the payer on their PayPal account.          |
| `payer_id`       | A unique ID of the payer’s PayPal account.              |
| `transaction_id` | A unique transaction ID generated by PayPal.            |

#### Json

```json
{
  "charges": {
    "data": [
      {
        "payment_method_details": {
          "paypal": {
            "payer_id": "H54KFE9XXVVYJ",
            "payer_email": "jenny@example.com",
            "payer_name": "Jenny Rosen",
            "transaction_id": "89W40396MK104212M"
          },
          "type": "paypal"
        },
        "id": "src_16xhynE8WzK49JbAs9M21jaR",
        "object": "source",
        "amount": 1099,
        "client_secret": "src_client_secret_UfwvW2WHpZ0s3QEn9g5x7waU",
        "created": 1445277809,
        "currency": "eur",
        "flow": "redirect",
        "livemode": true,
        "statement_descriptor": null,
        "status": "pending",
        "type": "paypal",
        "usage": "single_use"
      }
    ],
    "object": "list",
    "has_more": false,
    "url": "/v1/charges?payment_intent=pi_1G1sgdKi6xqXeNtkldRRE6HT"
  },
  "payment_method_options": {
    "paypal": {}
  },
  "payment_method_types": ["paypal"],
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  "amount": 1099,
  "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
  "confirmation_method": "automatic",
  "created": 1579259303,
  "currency": "eur",
  "livemode": true,
  "next_action": null
}
```

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

There are a few options for receiving and running business actions.

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/paypal/accept-a-payment?payment-ui=mobile&platform=react-native.

## Set up Stripe [Server-side] [Client-side]

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries for access to the Stripe API from your server:

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

## Create a PaymentIntent [Server-side] [Client-side]

### Server-side

Stripe uses a payment object, called a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md), to track and handle all the states of the payment until it’s completed. Create a `PaymentIntent` on your server, specifying the amount to collect and the currency. If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `paypal` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["paypal"],
});
```

Included in the returned PaymentIntent is a *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)), which is used to securely complete the payment process instead of passing the entire PaymentIntent object. Send the client secret back to the client so you can use it in later steps.

#### Include a custom description

By default, the order details on the PayPal users purchase activity page displays the order amount. You can change this by providing a custom description in the `description` property.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  description: "A sample description",
  payment_method_types: ["paypal"],
});
```

#### Customize the preferred locale

By default, the PayPal authorization page is localized based on variables such as the business’s country. You can set this to your customer’s preferred locale using the `preferred_locale` property. The value must be a two-character lowercased language code, followed by a hyphen (`-`), followed by a two-character uppercased country code. For example, the value for a French-language user in Belgium would be `fr-BE`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "eur",
  payment_method_types: ["paypal"],
  payment_method_options: {
    paypal: {
      preferred_locale: "fr-BE",
    },
  },
});
```

You can set the PayPal authorization page to your customer’s preferred locale through the [preferred_locale](https://docs.stripe.com/payments/paypal/accept-a-payment.md#customize-the-preferred-locale) property. See the following table for supported locales:

| Value | Locale     | Country                  |
| ----- | ---------- | ------------------------ |
| cs-CZ | Czech      | The Czech Republic       |
| da-DK | Danish     | Denmark                  |
| de-AT | German     | Austria                  |
| de-DE | German     | Germany                  |
| de-LU | German     | Luxembourg               |
| el-GR | Greek      | Greece                   |
| en-GB | English    | United Kingdom           |
| en-US | English    | United States of America |
| es-ES | Spanish    | Spain                    |
| fi-FI | Finnish    | Finland                  |
| fr-BE | French     | Belgium                  |
| fr-FR | French     | France                   |
| fr-LU | French     | Luxembourg               |
| hu-HU | Hungarian  | Hungary                  |
| it-IT | Italian    | Italy                    |
| nl-BE | Dutch      | Belgium                  |
| nl-NL | Dutch      | Netherlands              |
| pl-PL | Polish     | Poland                   |
| pt-PT | Portuguese | Portugal                 |
| sk-SK | Slovak     | Slovakia                 |
| sv-SE | Swedish    | Sweden                   |

#### Statement descriptors with PayPal

The descriptor that appears on the buyer’s bank statement is set by PayPal, and by default is `PAYPAL *YOUR_BUSINESS_NAME`. If you set the `statement_descriptor` field when creating the `PaymentIntent`, its value is appended to the one set by PayPal, up to a total limit of 22 characters.

For example, if your business name in PayPal is `BUSINESS` and you set `statement_descriptor` to `order_id_1234`, buyers see `PAYPAL *BUSINESS order` on their bank account statement.

### Client-side

On the client, request a PaymentIntent from your server and store its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)):

```javascript
function PaymentScreen() {
  const fetchPaymentIntentClientSecret = async () => {
    const response = await fetch(`${API_URL}/create-payment-intent`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        currency: "eur",
      }),
    });
    const { clientSecret } = await response.json();

    return clientSecret;
  };

  const handlePayPress = async () => {
    // See below
  };

  return (
    <View>
      <Button onPress={handlePayPress} title="Pay" />
    </View>
  );
}
```

The client secret is different from your API keys that authenticate Stripe API requests. Handle it carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

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

## Submit the payment to Stripe [Client-side]

When a customer taps to pay with PayPal, complete the payment by calling `confirmPayment`. This presents a webview where the customer can complete the payment with PayPal. Upon completion, the promise resolves with either a `paymentIntent` object, or an `error` object if an error occurred with the payment.

```javascript
import { useConfirmPayment } from "@stripe/stripe-react-native";

function PaymentScreen() {
  const { confirmPayment, loading } = useConfirmPayment();

  const fetchPaymentIntentClientSecret = async () => {
    // See above
  };

  const handlePayPress = async () => {
    // Fetch the client secret from the backend.
    const clientSecret = await fetchPaymentIntentClientSecret();

    const { error, paymentIntent } = await confirmPayment(clientSecret, {
      paymentMethodType: "PayPal",
    });

    if (error) {
      console.log("Payment confirmation error: ", error);
    } else if (paymentIntent) {
      console.log("Successfully confirmed payment: ", paymentIntent);
    }
  };

  return (
    <View>
      <Button onPress={handlePayPress} title="Pay" disabled={loading} />
    </View>
  );
}
```

You can find the payment owner’s name, email, payer ID, and transaction ID in the [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-paypal) property.

| Field            | Value                                                   |
| ---------------- | ------------------------------------------------------- |
| `payer_email`    | The email address of the payer on their PayPal account. |
| `payer_name`     | The name of the payer on their PayPal account.          |
| `payer_id`       | A unique ID of the payer’s PayPal account.              |
| `transaction_id` | A unique transaction ID generated by PayPal.            |

#### Json

```json
{
  "charges": {
    "data": [
      {
        "payment_method_details": {
          "paypal": {
            "payer_id": "H54KFE9XXVVYJ",
            "payer_email": "jenny@example.com",
            "payer_name": "Jenny Rosen",
            "transaction_id": "89W40396MK104212M"
          },
          "type": "paypal"
        },
        "id": "src_16xhynE8WzK49JbAs9M21jaR",
        "object": "source",
        "amount": 1099,
        "client_secret": "src_client_secret_UfwvW2WHpZ0s3QEn9g5x7waU",
        "created": 1445277809,
        "currency": "eur",
        "flow": "redirect",
        "livemode": true,
        "statement_descriptor": null,
        "status": "pending",
        "type": "paypal",
        "usage": "single_use"
      }
    ],
    "object": "list",
    "has_more": false,
    "url": "/v1/charges?payment_intent=pi_1G1sgdKi6xqXeNtkldRRE6HT"
  },
  "payment_method_options": {
    "paypal": {}
  },
  "payment_method_types": ["paypal"],
  "id": "pi_1G1sgdKi6xqXeNtkldRRE6HT",
  "object": "payment_intent",
  "amount": 1099,
  "client_secret": "pi_1G1sgdKi6xqXeNtkldRRE6HT_secret_h9B56ObhTN72fQiBAuzcVPb2E",
  "confirmation_method": "automatic",
  "created": 1579259303,
  "currency": "eur",
  "livemode": true,
  "next_action": null
}
```

## Optional: Handle post-payment events

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

### Receive events and run business actions

There are a few options for receiving and running business actions.

#### Manually

Use the Stripe Dashboard to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

- [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments)

#### Custom code

Build a webhook handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook)

#### Prebuilt apps

Handle common business events, like [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.
