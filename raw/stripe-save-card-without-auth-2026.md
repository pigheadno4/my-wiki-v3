<!-- Source URL: https://docs.stripe.com/payments/save-card-without-authentication -->
<!-- Fetched: 2026-05-11 -->

# Save a card without bank authentication

Collect card details and charge your customer at a later time.

​​Stripe allows you to collect card details and charge your customer at a later time. ​​In some regions, banks require a second form of authentication such as entering a code sent to a phone. ​​The extra step decreases conversion if your customer isn’t actively using your website or application because they aren’t available to authenticate the purchase.

​​If you primarily do business in the US and Canada, banks don’t require authentication, so you can follow this simpler integration. This integration will be non-compliant in countries that require authentication for saving cards (for example, India) so building this integration means that expanding to other countries or adding other payment methods will require significant changes. Learn how to [save cards that require authentication](https://docs.stripe.com/payments/save-and-reuse.md).

> #### Compliance
>
> You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For instance, if you want to save their payment method for future use, such as charging them when they’re not actively using your website or app. Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in. If you want to charge them when they’re offline, make sure your terms include the following:
>
> - The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.

- The anticipated timing and frequency of payments (for example, if the charges are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.
  > Make sure you keep a record of your customer’s written agreement to these terms.

## Collect card details [Client-side]

Before starting this guide, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Build a checkout page to collect your customer’s card details. Use [Stripe Elements](https://docs.stripe.com/payments/elements.md), a UI library that helps you build custom payment forms. To get started with Elements, include the Stripe.js library with the following script on your checkout page.

```html
<script src="https://js.stripe.com/dahlia/stripe.js"></script>
```

Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

To best take advantage of the Stripe [advanced fraud functionality](https://docs.stripe.com/radar.md), include this script on every page on your site, not the checkout page only. Including the script on every page [allows Stripe to detect suspicious behavior](https://docs.stripe.com/disputes/prevention/advanced-fraud-detection.md) that might indicate fraud when users browse your website.

### Add Elements to your page

To securely collect card details from your customers, Elements creates UI components for you hosted by Stripe. They’re then placed into your payment form, rather than you creating them directly. To determine where to insert these components, create empty DOM elements (containers) with unique IDs within your payment form.

```html
<input id="cardholder-name" type="text" />
<!-- placeholder for Elements -->
<div id="card-element"></div>
<div id="card-result"></div>
<button id="card-button">Save Card</button>
```

Next, create an instance of the [Stripe object](https://docs.stripe.com/js.md#stripe-function), providing your publishable [API key](https://docs.stripe.com/keys.md) as the first parameter. After, create an instance of the [Elements object](https://docs.stripe.com/js.md#stripe-elements) and use it to mount a `card` element in the DOM.

The `card` Element simplifies the payment form and minimizes the number of required fields by inserting a single, flexible input field that securely collects all necessary card details.

Otherwise, combine `cardNumber`, `cardExpiry`, and `cardCvc` Elements for a flexible, multi-input card form.

> Always collect a postal code to increase card acceptance rates and reduce fraud.
>
> The [single line Card Element](https://docs.stripe.com/js/element/other_element?type=card) automatically collects and sends the customer’s postal code to Stripe. If you build your payment form with split Elements ([Card Number](https://docs.stripe.com/js/element/other_element?type=cardNumber), [Expiry](https://docs.stripe.com/js/element/other_element?type=cardExpiry), [CVC](https://docs.stripe.com/js/element/other_element?type=cardCvc)), add a separate input field for the customer’s postal code.

```javascript
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");

const elements = stripe.elements();
const cardElement = elements.create("card");
cardElement.mount("#card-element");
```

A Stripe Element contains an iframe that securely sends the payment information to Stripe over an HTTPS connection. The checkout page address must also start with `https://` rather than `http://` for your integration to work.

You can test your integration without using HTTPS. [Enable it](https://docs.stripe.com/security/guide.md#tls) when you’re ready to accept live payments.

```javascript
const cardholderName = document.getElementById("cardholder-name");
const cardButton = document.getElementById("card-button");
const resultContainer = document.getElementById("card-result");

cardButton.addEventListener("click", async (ev) => {
  const { paymentMethod, error } = await stripe.createPaymentMethod({
    type: "card",
    card: cardElement,
    billing_details: {
      name: cardholderName.value,
    },
  });

  if (error) {
    // Display error.message in your UI.
    resultContainer.textContent = error.message;
  } else {
    // You have successfully created a new PaymentMethod
    resultContainer.textContent = "Created payment method: " + paymentMethod.id;
  }
});
```

Send the resulting _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) ID to your server.

## Set up Stripe [Server-side]

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Save the card [Server-side]

Save the card by attaching the PaymentMethod to a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments). You can use the `Customer` object to store other information about your customer, such as shipping details and email address.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  payment_method: "{{PAYMENT_METHOD_ID}}",
});
```

If you have an existing Customer, you can attach the PaymentMethod to that object instead.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethod = await stripe.paymentMethods.attach(
  "{{PAYMENT_METHOD_ID}}",
  {
    customer: "{{CUSTOMER_ID}}",
  },
);
```

At this point, associate the Customer ID and the PaymentMethod ID with your own internal representation of a customer, if you have one.

## Charge the saved card [Server-side]

When you’re ready, fetch the PaymentMethod and Customer IDs to charge. You can do this by either storing the IDs of both in your database, or by using the Customer ID to look up all the customer’s available PaymentMethods.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  type: "card",
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethods = await stripe.paymentMethods.list({
  customer: "{{CUSTOMER_ID}}",
  type: "card",
});
```

Use the PaymentMethod ID and the Customer ID to create a new PaymentIntent. Set [error_on_requires_action](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-error_on_requires_action) to `true` to decline payments that require any actions from your customer, such as two-factor authentication.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  payment_method_types: ["card"],
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  error_on_requires_action: true,
  confirm: true,
});
```

When a payment attempt fails, the request also fails with a 402 HTTP status code and Stripe throws an error. You need to notify your customer to return to your application (for example, by sending an email) to complete the payment. Check the code of the [Error](https://docs.stripe.com/api/errors/handling.md) raised by the Stripe API library or check the [last_payment_error.decline_code](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-decline_code) on the PaymentIntent to inspect why the card issuer declined the payment.

## Handle any card errors

Notify your customer that the payment failed and direct them to the payment form you made in step 1 where they can enter new card details. Send that new PaymentMethod ID to your server to [attach](https://docs.stripe.com/api/payment_methods/attach.md) to the Customer object and make the payment again.

Alternatively, you can create a PaymentIntent and save a card in one API call if you already created a Customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  payment_method_types: ["card"],
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENT_METHOD_ID}}",
  error_on_requires_action: true,
  confirm: true,
  setup_future_usage: "on_session",
});
```

Setting [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) to `on_session` indicates to Stripe that you want to save the card for later, without triggering unnecessary authentication.

## Test the integration

Stripe provides [test cards](https://docs.stripe.com/testing.md) you can use in a sandbox to simulate the behavior of different cards. Use these cards with any CVC, postal code, and expiration date in the future.

| Number           | Description                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| 4242424242424242 | Succeeds and immediately processes the payment.                                                       |
| 4000000000009995 | Always fails with a decline code of `insufficient_funds`.                                             |
| 4000002500003155 | Requires authentication, which in this integration declines with a code of `authentication_required`. |

## Optional: Re-collect a CVC

When creating subsequent payments on a saved card, you might want to re-collect the CVC of the card as an additional fraud measure to verify the user.

Start by creating a PaymentIntent from your server with the amount and currency of the payment, and set the [Customer](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) to the ID of your customer. Then, [list](https://docs.stripe.com/api/payment_methods/list.md) the PaymentMethods associated with your customer to determine which PaymentMethods to show to your user for CVC re-collection.

After passing the PaymentIntent’s client secret to the browser, you’re ready to re-collect CVC information with Stripe Elements on your client. Use the `cardCvc` Element to re-collect a CVC value from your user, and then confirm the payment from your client using [stripe.confirmCardPayment](https://docs.stripe.com/js.md#stripe-confirm-card-payment). Set `payment_method` to your PaymentMethod ID, and `payment_method_options[card][cvc]` to your `cardCvc` Element.

```javascript
const result = await stripe.confirmCardPayment(clientSecret, {
  payment_method: "{{PAYMENT_METHOD_ID}}",
  payment_method_options: {
    card: {
      cvc: cardCvcElement,
    },
  },
});

if (result.error) {
  // Show error to your customer
  console.log(result.error.message);
} else {
  if (result.paymentIntent.status === "succeeded") {
    // Show a success message to your customer
    // There's a risk of the customer closing the window before callback
    // execution. Set up a webhook or plugin to listen for the
    // payment_intent.succeeded event that handles any business critical
    // post-payment actions.
  }
}
```

A payment might succeed even with a failed CVC check. To prevent this, configure your [Radar rules](https://docs.stripe.com/radar/rules.md#traditional-bank-checks) to block payments when CVC verification fails.

## Upgrade your integration to handle card authentication

This integration _declines cards that require authentication during payment_. If you start seeing many payments in the Dashboard listed as `Failed`, then it’s time to [upgrade your integration](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions.md). Stripe’s global integration handles these payments instead of automatically declining.
