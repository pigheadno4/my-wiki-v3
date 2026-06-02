<!-- Source URL: https://docs.stripe.com/payments/fpx/accept-a-payment -->
<!-- Fetched: 2026-05-03 -->

# Accept an FPX payment

Learn how to accept FPX, a common payment method in Malaysia.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/fpx/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

FPX is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method. Customers pay with FPX by redirecting from your website, sending you payment, then returning to your website where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

## Determine compatibility

**Customer Geography**: Malaysia

**Supported currencies**: `myr`

**Presentment currencies**: `myr`

**Payment mode**: Yes

**Setup mode**: No

**Subscription mode**: No

A Checkout Session must satisfy all of the following conditions to support FPX payments:

- *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.
- You can only use one-time line items (recurring *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) plans aren’t supported).

## Accept a payment

> Build an integration to [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?integration=checkout) with Checkout before using this guide.

This guides you through enabling FPX and shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable FPX as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `fpx` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the `myr` currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: "myr",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "fpx"],
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
        currency: "myr",
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  payment_method_types: ["card", "fpx"],
  return_url: "https://example.com/return",
  ui_mode: "embedded_page",
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

### Confirmation page

FPX requires showing your customer their transaction information after they’ve completed their payment. Follow the [custom success page](https://docs.stripe.com/payments/checkout/custom-success-page.md) guide to learn how to customize your success page.

When customizing, you’ll need to retrieve the Charge object directly from the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) object using the PaymentIntent ID from your Checkout Session and display the following information on your `success_url` page.

| Information             | Source of information                                                   |
| ----------------------- | ----------------------------------------------------------------------- |
| Transaction Date & Time | `created` from the `Charge` object.                                     |
| Amount                  | `amount` from the `Charge` object.                                      |
| Seller Order No.        | `statement_descriptor` from the `Charge` object.                        |
| FPX Transaction ID      | `payment_method_details[fpx][transaction_id]` from the `Charge` object. |
| Buyer Bank Name         | `payment_method_details[fpx][bank]` from the `Charge` object            |
| Transaction Status      | `status` from the `Charge` object                                       |

## Test your integration

When testing your Checkout integration, select FPX as the payment method and click the **Pay** button.

## Handle refunds and disputes

The refund period for FPX is up to 60 days after the original payment.

There is no dispute process—customers authenticate with their bank.

## See also

- [More about FPX](https://docs.stripe.com/payments/fpx.md)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment.md)
- [Customizing Checkout](https://docs.stripe.com/payments/checkout/customization.md)

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/fpx/accept-a-payment?payment-ui=elements.

> The content of this section refers to a *Legacy* (Technology that's no longer recommended) product. You should use the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide for the most recent integration path instead. While Stripe still supports this product, this support might end if the product is deprecated.

FPX is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method. Customers pay with FPX by redirecting from your website, sending you payment, then returning to your website where you get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.

To enable FPX payments:

1. Go to the [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard. If you haven’t already, [set up your Stripe account](https://docs.stripe.com/get-started/account/set-up.md).
1. Find FPX under **Bank redirects** and select **Turn on**.
1. Accept the FPX terms of service.

FPX is only available to businesses based in Malaysia. See [payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md) for more information about countries, currencies, and payment methods compatible with Stripe products.

> FPX is a single-use payment method and can’t be used for recurring or additional payments. It’s currently not supported with [Stripe Billing](https://stripe.com/billing). Support for FPX payments for [Custom accounts](https://docs.stripe.com/connect/custom-accounts.md) is in beta. Contact [Stripe support](https://support.stripe.com/contact) for any support queries.

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) represents your intent to collect payment from a customer, tracking the lifecycle of the payment process through [each stage](https://docs.stripe.com/payments/paymentintents/lifecycle.md). Create a PaymentIntent as soon as you know the amount (for example, the beginning of the checkout process). You need the following values to create the PaymentIntent:

| Parameter              | Value                                                                                                                                                                                                                                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_method_types` | **fpx**                                                                                                                                                                                                                                                                                           |
| `amount`               | A positive integer in the [smallest currency unit](https://docs.stripe.com/currencies.md#zero-decimal) that represents the amount to charge the customer (for example, **1099** for a RM10.99 payment). Stripe supports a minimum amount of RM2 and a maximum amount of RM30,000 per transaction. |
| `currency`             | **myr** (FPX must always use Ringgit).                                                                                                                                                                                                                                                            |

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["fpx"],
  amount: 1099,
  currency: "myr",
});
```

You can also [update](https://docs.stripe.com/api.md#update_payment_intent) the [amount](https://docs.stripe.com/api.md#payment_intent_object-amount) if it changes later (for example, when calculating shipping fees and taxes):

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.update(
  "pi_1DRuHnHgsMRlo4MtwuIAUe6u",
  {
    amount: 1499,
  },
);
```

## Collect payment method details [Client-side]

[Stripe Elements](https://docs.stripe.com/payments/elements.md) is a set of prebuilt UI components for collecting payment details. Elements is automatically available as a feature of Stripe.js. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Elements with the following JavaScript on your checkout page.

```javascript
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
const elements = stripe.elements();
```

Elements needs a place to live in your payment form. Create empty DOM nodes (containers) with unique IDs in your payment form and then pass those IDs to Elements.

```html
<form id="payment-form">
  <div class="form-row">
    <div>
      <label for="fpx-bank-element"> FPX Bank </label>
      <div id="fpx-bank-element">
        <!-- A Stripe Element will be inserted here. -->
      </div>
    </div>
  </div>

  <button id="fpx-button" data-secret="{{ CLIENT_SECRET }}">
    Submit Payment
  </button>

  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>
</form>
```

> This doc refers to a *Legacy* (Technology that's no longer recommended) feature that’s no longer available in the latest version of Stripe.js. We recommend you use the [Payment Element](https://docs.stripe.com/payments/payment-element.md), a UI component for the web that accepts 40+ payment methods, validates input, and handles errors.

When the form above has loaded, [create an instance](https://docs.stripe.com/js/elements_object/create_element?type=fpxBank) of an `fpxBank` Element and mount it to the Element container created above.

```javascript
const style = {
  base: {
    // Add your base input styles here. For example:
    padding: "10px 12px",
    color: "#32325d",
    fontSize: "16px",
  },
};

// Create an instance of the fpxBank Element.
const fpxBank = elements.create("fpxBank", {
  style: style,
  accountHolderType: "individual",
});

// Add an instance of the fpxBank Element into the container with id `fpx-bank-element`.
fpxBank.mount("#fpx-bank-element");
```

## Submit the payment to Stripe [Client-side]

To create a payment on the client side, pass the [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object that you created in Step 1.

Use [stripe.confirmFpxPayment](https://docs.stripe.com/js.md#stripe-confirm-fpx-payment) to handle the redirect away from your page and to complete the payment. Add a `return_url` to this function to indicate where Stripe should redirect the user after they complete the payment on their bank’s website or mobile application.

```javascript
const form = document.getElementById("payment-form");

form.addEventListener("submit", async function (event) {
  event.preventDefault();
  const fpxButton = document.getElementById("fpx-button");
  const clientSecret = fpxButton.dataset.secret;

  const result = await stripe.confirmFpxPayment(clientSecret, {
    payment_method: {
      fpx: fpxBank,
    },
    // Return URL where the customer should be redirected after the authorization
    return_url: `${window.location.href}`,
  });

  if (result.error) {
    // Inform the customer that there was an error.
    const errorElement = document.getElementById("error-message");
    errorElement.textContent = result.error.message;
  }
});
```

When your customer submits a payment, Stripe redirects them to the `return_url` and includes the following URL query parameters. The return page can use them to get the status of the PaymentIntent so it can display the payment status to the customer.

When you specify the `return_url`, you can also append your own query parameters for use on the return page.

| Parameter                      | Description                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_intent`               | The unique identifier for the `PaymentIntent`.                                                                                                                                                                                                                                                                                                             |
| `payment_intent_client_secret` | The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent` object. For subscription integrations, this client_secret is also exposed on the `Invoice` object through [`confirmation_secret`](https://docs.stripe.com/api/invoices/object.md#invoice_object-confirmation_secret) |

When the customer is redirected back to your site, you can use the `payment_intent_client_secret` to query for the PaymentIntent and display the transaction status to your customer.

## Test your integration

#### Authentication success and failure cases

Test your FPX integration by selecting any bank with your test API keys and viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from `requires_action` to `succeeded`.

To test the case where the user fails to authenticate, select any bank with your test API keys. On the redirect page, click **Fail test payment**. The PaymentIntent will transition from `requires_action` to `requires_payment_method`.

#### Confirmation error cases

Other error cases you might encounter are connecting to banks that are offline and processing errors during confirmation. To trigger these errors, set the `fpx[bank]` value on confirm to one of the test error bank values below. The PaymentIntent state will be `requires_confirmation`. Learn more about these [error codes](https://docs.stripe.com/payments/fpx/accept-a-payment.md#error-codes).

| Parameter   | Value                   | Error code                                  |
| ----------- | ----------------------- | ------------------------------------------- |
| `fpx[bank]` | `test_offline_bank`     | `offline_bank`                              |
| `fpx[bank]` | `test_processing_error` | `payment_method_processing_error_transient` |

## Handle post-payment events [Server-side]

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the Dashboard, a custom *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), or a partner solution to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events also helps you accept more payment methods in the future. Learn about the [differences between all supported payment methods](https://stripe.com/payments/payment-methods-guide).

- **Handle events manually in the Dashboard**

  Use the Dashboard to [View your test payments in the Dashboard](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.

- **Build a custom webhook**

  [Build a custom webhook](https://docs.stripe.com/webhooks/handling-payment-events.md#build-your-own-webhook) handler to listen for events and build custom asynchronous payment flows. Test and debug your webhook integration locally with the Stripe CLI.

- **Integrate a prebuilt app**

  Handle common business events, such as [automation](https://stripe.partners/?f_category=automation) or [marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## Optional: Handle FPX bank element events

You can update the configuration options (for example, the `style`) of the `fpxBank` Element using [.update(options)](https://docs.stripe.com/js.md#other-methods).

The FPX Bank Element outputs the customer’s selected bank as it changes. To perform additional logic with the bank value (for example, requiring the field for form validation), you can listen to the change event:

```javascript
fpxBank.on("change", function (event) {
  var bank = event.value;
  // Perform any additional logic here...
});
```

The change event contains other helpful parameters:

| Parameter     | Description                                                                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `elementType` | The name of the element. The default value is `fpxBank`.                                                                                                                                |
| `empty`       | If `true`, the value is empty.                                                                                                                                                          |
| `complete`    | If `true`, the customer has selected the value. You can use this parameter to progressively disclose the rest of your form or to enable form submission.                                |
| `value`       | The FPX bank that the customer selected from the Element. The [FPX guide](https://docs.stripe.com/payments/fpx/accept-a-payment.md#bank-reference) contains the complete list of banks. |

## Optional: Handle FPX redirect manually

We recommend relying on Stripe.js to handle FPX redirects and payments with `confirmFpxPayment`. However, you can also manually redirect your customers by:

1. Providing the URL where your customers will be redirected after they complete their payment.

   ```node
   // Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
   // Find your keys at https://dashboard.stripe.com/apikeys.
   const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

   const paymentIntent = await stripe.paymentIntents.confirm(
     "pi_1DRuHnHgsMRlo4MtwuIAUe6u",
     {
       payment_method: "pm_1EnPf7AfTbPYpBIFLxIc8SD9",
       return_url: "https://shop.example.com/crtA6B28E1",
     },
   );
   ```

   At this point, Stripe checks if the selected bank is online and available to authenticate. If the bank isn’t available, Stripe returns the following error code and error message:

| |
| |
| `error_code` | offline_bank |
| `error_message` | %{bank} is currently offline. Try using a different bank. |

You should then advise your customer to either select a different bank or payment method to complete the transaction.

**Testing an offline bank** You can test the `offline_bank` error above by creating a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) in Step 2 using the following value, and then attaching it to the PaymentIntent as shown above.

| Parameter   | Value               |
| ----------- | ------------------- |
| `fpx[bank]` | `test_offline_bank` |

1. Confirming the `PaymentIntent` has a status of `requires_action`. The type for the `next_action` will be `redirect_to_url`.

   ```json
   "next_action": {
     "type": "redirect_to_url",
     "redirect_to_url": {
       "url": "https://hooks.stripe.com/...",
       "return_url": "https://example.com/checkout/complete"
     }
   }
   ```

1. Redirecting the customer to the URL provided in the `next_action` property.

   ```javascript
   const action = intent.next_action;
   if (action && action.type === "redirect_to_url") {
     window.location = action.redirect_to_url.url;
   }
   ```

When the customer finishes the payment process, they’re sent to the `return_url` destination. The `payment_intent` and `payment_intent_client_secret` URL query parameters are included and you can pass through your own query parameters, as described above.

## Checkout and payment confirmation requirements

You must adhere to the following requirements on your checkout page:

| Requirement                                                  | Detail                                                                                                                                                             |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Display the FPX logo.                                        | Download the [FPX logo](https://exchange.fpx.prod.inet.paynet.my/files/FPX%20Logo.zip).                                                                            |
| Create FPX Buyer Bank’s selection in a dropdown list.        | Bank names must match the names in the [bank reference](https://docs.stripe.com/payments/fpx/accept-a-payment.md#bank-reference).                                  |
| Present the FPX Terms & Conditions standard wording and URL. | **Standard wording:** By clicking on the **Proceed** button, you agree to FPX’s [Terms and Conditions](https://www.mepsfpx.com.my/FPXMain/termsAndConditions.jsp). |

The following information must be displayed on the payment confirmation page that your customer returns to after completing their bank authentication.

| Information             | Source of information                                                   |
| ----------------------- | ----------------------------------------------------------------------- |
| Transaction Date & Time | `created` from the `Charge` object.                                     |
| Amount                  | `amount` from the `Charge` object.                                      |
| Seller Order No.        | `statement_descriptor` from the `Charge` object.                        |
| FPX Transaction ID      | `payment_method_details[fpx][transaction_id]` from the `Charge` object. |
| Buyer Bank Name         | `payment_method_details[fpx][bank]` from the `Charge` object            |
| Transaction Status      | `status` from the `Charge` object                                       |

You can access this information on the [Charge](https://docs.stripe.com/api/charges/object.md) by retrieving it from the `payment_intent.succeeded` event.

Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older: You can access this information on the [Charge](https://docs.stripe.com/api/charges/object.md) by retrieving it from the `payment_intent.succeeded` event or directly from the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-charges-data).

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const intent = await stripe.paymentIntents.retrieve("{{PAYMENT_INTENT_ID}}");
const charges = intent.charges.data;
```

## Bank reference

| Bank name          | Value              |
| ------------------ | ------------------ |
| Affin Bank         | affin_bank         |
| Alliance Bank      | alliance_bank      |
| AmBank             | ambank             |
| Bank Islam         | bank_islam         |
| Bank Muamalat      | bank_muamalat      |
| Bank Rakyat        | bank_rakyat        |
| BSN                | bsn                |
| CIMB Clicks        | cimb               |
| Hong Leong Bank    | hong_leong_bank    |
| HSBC Bank          | hsbc               |
| KFH                | kfh                |
| Maybank2E          | maybank2e          |
| Maybank2U          | maybank2u          |
| OCBC Bank          | ocbc               |
| Public Bank        | public_bank        |
| RHB Bank           | rhb                |
| Standard Chartered | standard_chartered |
| UOB Bank           | uob                |

## Error codes

These are the common error codes and corresponding recommended actions:

| Error Code                                  | Recommended Action                                                                                                                                                                |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `invalid_amount`                            | FPX transactions must be greater than RM2 and less than RM30,000.                                                                                                                 |
| `invalid_bank`                              | The provided bank isn’t supported by FPX. Please use one of the options from the [Bank Reference](https://docs.stripe.com/payments/fpx/accept-a-payment.md#bank-reference) above. |
| `invalid_currency`                          | FPX only supports MYR transactions.                                                                                                                                               |
| `missing_parameter`                         | A required parameter is missing. Please check the `error_message` for more information about which parameter is required.                                                         |
| `offline_bank`                              | The provided bank is currently offline. Please try using a different bank or payment method type.                                                                                 |
| `payment_method_not_available`              | The payment method is currently not available. You should invite your customer to fallback to another payment method to proceed.                                                  |
| `payment_method_processing_error_transient` | An unexpected error occurred preventing us from confirming the payment intent. The payment intent confirmation should be retried.                                                 |

## Payouts and transfers

For compliance reasons, your FPX funds settle in a separate `fpx` balance on your account. This means that you might receive two separate automatic *payouts* (A payout is the transfer of funds to an external account, usually a bank account, in the form of a deposit) in a single day, one for your FPX funds and another for all other funds. For [Connect platforms](https://docs.stripe.com/connect.md), you can [create a payout](https://docs.stripe.com/api/payouts/create.md) or [transfer](https://docs.stripe.com/api/transfers/create.md) from your `fpx` balance by specifying `fpx` as the `source_type`:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const payout = await stripe.payouts.create({
  amount: 5000,
  currency: "myr",
  source_type: "fpx",
});
```

You can also [retrieve](https://docs.stripe.com/api/balance/balance_retrieve.md) your balance to see a breakdown of your `available` and `pending` Stripe balances by `source_type`.

FPX is a [single-use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method available only in Malaysia. Customers are redirected from your app to complete the payment using FPX, send you payment, then return to your app where you receive an [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) stating if the payment succeeded or failed.

To enable FPX payments:

1. Go to the [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard. If you haven’t already, [set up your Stripe account](https://docs.stripe.com/get-started/account/set-up.md).
1. Find FPX under **Bank redirects** and select **Turn on**.
1. Accept the FPX terms of service.

FPX is only available to businesses based in Malaysia. See [payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md) for more information about countries, currencies, and payment methods compatible with Stripe products.

After you enable FPX payments, integrate with the [Mobile Payment Element](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=android) to start accepting online payments. You can choose between Android, iOS, and React Native.
