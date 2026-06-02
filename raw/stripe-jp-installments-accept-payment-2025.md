<!-- Source URL: https://docs.stripe.com/payments/jp-installments/accept-a-payment -->
<!-- Fetched: 2026-05-01 -->

# Accept installment card payments

Learn how to accept credit card payments using installments across a variety of Stripe products.

Installments (分割払い) are a type of credit card payment in Japan that allows customers to split purchases over multiple billing statements. You receive the full amount as with standard card payments, and the customer’s card company provides credit and collects the funds over time.

Some restrictions apply to which transactions and cards can use installments. Review the [compatibility requirements](https://docs.stripe.com/payments/jp-installments.md#requirements).

You can enable installments across a variety of Stripe products. Choose the instructions below that match your implementation.

# Stripe-hosted page

> This is a Stripe-hosted page for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/jp-installments/accept-a-payment?payment-ui=checkout.

## Installments on Stripe Checkout

[Checkout](https://docs.stripe.com/payments/checkout.md) creates a secure, Stripe-hosted payment page that lets you collect payments quickly. It works across devices and can help increase your conversion. Checkout provides a low-code way to get started accepting payments.

Your customers use Checkout to pay with cards (with or without installments) and other payment methods that support Checkout.

## Review Checkout documentation

Stripe Checkout allows you to collect installment payments. For information about setting up Checkout, see the [quickstart](https://docs.stripe.com/checkout/quickstart.md).

## Create a new Checkout session

If you use [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md), installments appear automatically. If not, create a new Checkout session with installments enabled as shown in the example below. Substitute your own price object.

> Installments only works with `payment` mode, not `setup` or `subscription` mode.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  success_url: 'https://example.com/success',
  line_items: [
    {
      price: '{{PRICE_ID}}',
      quantity: 3,
    },
  ],
  mode: 'payment',
  payment_method_options: {
    card: {
      installments: {
        enabled: true,
      },
    },
  },
});
```

## Redirect to Checkout

After creating the session, redirect your customer to the URL for the Checkout page returned in the CheckoutSession.

## See also

- [Checkout integration guide](https://docs.stripe.com/checkout/quickstart.md)
- [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md)
- [Payment Intents](https://docs.stripe.com/api/payment_intents/object.md)

# Advanced integration

> This is a Advanced integration for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/jp-installments/accept-a-payment?payment-ui=elements.

## Installments on the Payment Element

The [Payment Element](https://docs.stripe.com/payments/payment-element.md) lets you embed a customizable payment form in your website.

Your customers use the Payment Element to pay with cards (with or without installments) and other payment methods that it supports.

## Review Payment Element documentation

The Payment Element allows you to collect installment payments. For information about setting up the Payment Element, see the [quickstart](https://docs.stripe.com/payments/quickstart.md?platform=web).

## Create a PaymentIntent

If you use [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md), installments appear automatically. If not, enable installments as shown in the example below when you create a PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 100000,
  currency: 'jpy',
  payment_method_options: {
    card: {
      installments: {
        enabled: true,
      },
    },
  },
});
```

After creating the PaymentIntent, return its [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) to the client.

> If you use dynamic payment methods, don’t set `payment_method_options[card][installments][enabled]`. If set to `false` when dynamic payment methods are enabled, you might encounter errors.

## Initialize Stripe Elements

Initializing Stripe Elements with the client secret lets the Payment Element know that installments are in use.

## Complete the payment

When your customer clicks the pay button, call [confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) with the Payment Element and pass a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to indicate where Stripe redirects the user after they complete the payment.

If you encounter a [`processing_error`](https://docs.stripe.com/declines/codes.md#processing_error) or [`transaction_not_allowed`](https://docs.stripe.com/declines/codes.md#transaction_not_allowed) decline, it might indicate that the selected plan isn’t supported by the card issuer. Instruct your customer to retry with a different plan or without installments.

## See also

- [Payment Element integration guide](https://docs.stripe.com/payments/quickstart.md)
- [Payment Element API reference](https://docs.stripe.com/js/element/payment_element)
- [Payment Intents](https://docs.stripe.com/api/payment_intents/object.md)

# Direct API

> This is a Direct API for when payment-ui is direct-api. View the full page at https://docs.stripe.com/payments/jp-installments/accept-a-payment?payment-ui=direct-api.

## Integrate with the Payment Intents API

You can accept installments using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md). It requires collecting payment details and installment plan information on the client and completing the payment on the server.
A diagram providing a high level overview of a payment integration that accepts installments using the Payment Intents API (See full diagram at https://docs.stripe.com/payments/jp-installments/accept-a-payment)

1. [Collect payment method details on the client](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md#collect-payment-method)
1. [Retrieve installment plans on the server](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md#retrieve-installment-plans)
1. [Select an installment plan on the client](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md#select-plan)
1. [Confirm the PaymentIntent on the server](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md#confirm-payment)

## Collect payment method details on the client

The Payment Intents API works with [Stripe.js & Elements](https://docs.stripe.com/payments/elements.md) to securely collect payment information (for example, credit card details) on the client side. To get started with Elements, include the following script on your pages. This script must always load directly from **js.stripe.com** to remain _PCI compliant_ (Any party involved in processing, transmitting, or storing credit card data must comply with the rules specified in the Payment Card Industry (PCI) Data Security Standards. PCI compliance is a shared responsibility and applies to both Stripe and your business)—you can’t include it in a bundle or host a copy of it yourself.

```html
<script src="https://js.stripe.com/dahlia/stripe.js"></script>
```

To securely collect card details from your customers, Elements creates Stripe-hosted UI components for you that we place into your payment form, rather than you creating them directly. To determine where to insert these components, create empty DOM elements (containers) with unique IDs within your payment form.

```html
<div id="details">
  <input id="cardholder-name" type="text" placeholder="Cardholder name" />
  <!-- placeholder for Elements -->
  <form id="payment-form">
    <div id="card-element"></div>
    <button id="card-button">Next</button>
  </form>
</div>
```

Next, create an instance of the [Stripe object](https://docs.stripe.com/js.md#stripe-function), providing your publishable [API key](https://docs.stripe.com/keys.md) as the first parameter, and then create an instance of the [Elements object](https://docs.stripe.com/js.md#stripe-elements). Use the newly created object to [mount](https://docs.stripe.com/js.md#element-mount) a Card element in the relevant placeholder in the page.

```javascript
const stripe = Stripe('<<YOUR_PUBLISHABLE_KEY>>');

const elements = stripe.elements();
const cardElement = elements.create('card');
cardElement.mount('#card-element');
```

Finally, use [stripe.createPaymentMethod](https://docs.stripe.com/js.md#stripe-create-payment-method) on your client to collect the card details and create a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) when the user clicks the submit button.

```javascript
const cardholderName = document.getElementById('cardholder-name');
const form = document.getElementById('payment-form');

form.addEventListener('submit', async (ev) => {
  ev.preventDefault();
  const {paymentMethod, error} = await stripe.createPaymentMethod(
    'card',
    cardElement,
    {billing_details: {name: cardholderName.value}},
  );
  if (error) {
    // Show error in payment form
  } else {
    // Send paymentMethod.id to your server (see Step 2)
    const response = await fetch('/collect_details', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({payment_method_id: paymentMethod.id}),
    });

    const json = await response.json();

    // Handle server response (see Step 3)
    handleInstallmentPlans(json);
  }
});
```

## Retrieve installment plans on the server

To retrieve available installment plans, set up an endpoint on your server to receive the request.

[Create a new PaymentIntent](https://docs.stripe.com/payments/payment-intents.md) with the ID of the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md) created on your client. Set `payment_method_options.card.installments.enabled=true` to allow this payment to use Installments. Send the available plans to the client so the customer can select which plan to pay with.

> Don’t _confirm_ (Confirming a PaymentIntent indicates that the customer intends to pay with the current or provided payment method. Upon confirmation, the PaymentIntent attempts to initiate a payment) the PaymentIntent here (that is, don’t set the [confirm](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-confirm) property) because we don’t know if the user wants to pay with installments yet.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');
// Using Express
const express = require('express');
const app = express();

app.use(express.json());

app.post('/collect_details', async (request, response) => {
  try {
    const intent = await stripe.paymentIntents.create({
      amount: 100000,
      currency: 'jpy',
      payment_method: request.body.payment_method_id,payment_method_options: {
        card: {
          installments: {
            enabled: true,
          },
        },
      },
    });

    // We could confirm without installments if no plans are available,
    // but let's give the user the chance to pick a different card
    // if installments are not available.
    return response.send({
      intent_id: intent.id,available_plans: intent.payment_method_options.card.installments.available_plans,
    });
  } catch (err) {
    // "err" contains a message explaining why the request failed
    return response.status(500).send({error: err.message});
  }
});

app.listen(3000, () => {
  console.log('Running on port 3000');
});
```

The PaymentIntent object lists the available installment plans for the PaymentMethod under `payment_method_options.card.installments.available_plans`.

```json
{
  "id": "pi_1FKDPTJXdud1yP2PpUXNgq0V",
  "object": "payment_intent",
  "amount": 100000,
...
  "payment_method_options": {
    "card": {
      "installments": {
        "enabled": true,
        "plan": null,
        "available_plans": [
          {
            "count": 3,
            "interval": "month",
            "type": "fixed_count"
          },
          {
            "count": 6,
            "interval": "month",
            "type": "fixed_count"
          },
          {
            "count": 9,
            "interval": "month",
            "type": "fixed_count"
          },
          {
            "count": 12,
            "interval": "month",
            "type": "fixed_count"
          },
          {
            "count": 18,
            "interval": "month",
            "type": "fixed_count"
          },
          {
            "count": 24,
            "interval": "month",
            "type": "fixed_count"
          }
      },
      "request_three_d_secure": "automatic"
    }
  },
  ...
}

```

## Select an installment plan on the client

Allow the customer to select the Installments plan they want to use.

```html
<div id="plans" hidden>
  <form id="installment-plan-form">
    <label
      ><input
        id="immediate-plan"
        type="radio"
        name="installment_plan"
        value="-1"
      />Immediate</label
    >
    <input id="payment-intent-id" type="hidden" />
  </form>
  <button id="confirm-button">Confirm Payment</button>
</div>

<div id="result" hidden>
  <p id="status-message"></p>
</div>
```

```javascript
const selectPlanForm = document.getElementById('installment-plan-form');
let availablePlans = [];

const handleInstallmentPlans = async (response) => {
  if (response.error) {
    // Show error from server on payment form
  } else {
    // Store the payment intent ID.
    document.getElementById('payment-intent-id').value = response.intent_id;
    availablePlans = response.available_plans;
// Show available installment options
    availablePlans.forEach((plan, idx) => {
      const newInput = document.getElementById('immediate-plan').cloneNode();
      newInput.setAttribute('value', idx);
      newInput.setAttribute('id', '');
      const label = document.createElement('label');
      label.appendChild(newInput);
      label.appendChild(
        document.createTextNode(`${plan.count} ${plan.interval}s`),
      );

      selectPlanForm.appendChild(label);
    });

    document.getElementById('details').hidden = true;
    document.getElementById('plans').hidden = false;
  }
};
```

Send the selected plan to your server.

```javascript
const confirmButton = document.getElementById('confirm-button');

confirmButton.addEventListener('click', async (ev) => {
  const selectedPlanIdx = selectPlanForm.installment_plan.value;
  const selectedPlan = availablePlans[selectedPlanIdx];
  const intentId = document.getElementById('payment-intent-id').value;
  const response = await fetch('/confirm_payment', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      payment_intent_id: intentId,
      selected_plan: selectedPlan,
    }),
  });

  const responseJson = await response.json();

  // Show success / error response.
  document.getElementById('plans').hidden = true;
  document.getElementById('result').hidden = false;

  var message;
  if (responseJson.status === "succeeded" && selectedPlan !== undefined) {
    message = `Success! You made a charge with this plan:${
      selectedPlan.count
    } ${selectedPlan.interval}`;
  } else if (responseJson.status === "succeeded") {
    message = "Success! You paid immediately!";
  } else {
    message = "Uh oh! Something went wrong";
  }

  document.getElementById("status-message").innerText = message;
});
```

## Confirm the PaymentIntent on the server

Using another server endpoint, confirm the PaymentIntent to finalize the payment and fulfill the order.

#### Node.js

```javascript
app.post('/confirm_payment', async (request, response) => {
  try {
    let confirmData = {};
    if (request.body.selected_plan !== undefined) {
      confirmData = {
        payment_method_options: {
          card: {
            installments: {
              plan: request.body.selected_plan,
            },
          },
        },
      };
    }

    const intent = await stripe.paymentIntents.confirm(
      request.body.payment_intent_id,
      confirmData,
    );

    return response.send({success: true, status: intent.status});
  } catch (err) {
    return response.status(500).send({error: err.message});
  }
});
```

The response from the server will indicate that you selected the plan on the PaymentIntent and also on the resulting charge.

```json
{
  "id": "pi_1FKDPFJXdud1yP2PMSXLlPbg",
  "object": "payment_intent",
  "amount": 100000,
...
  "charges": {
    "data": [
      {
        "id": "ch_1FKDPHJXdud1yP2P2u79mcIX",
        "object": "charge",
        "amount": 100000,
        "payment_method_details": {
          "card": {
            "installments": {
              "plan": {
                "count": 3,
                "interval": "month",
                "type": "fixed_count"
              }
            },
          },
          ...
        },
        ...
      }
    ],
  },
...
  "payment_method_options": {
    "card": {
      "installments": {
        "enabled": true,
        "plan": {
          "count": 3,
          "interval": "month",
          "type": "fixed_count"
        },
        "available_plans": [ ... ]
      }
    }
  }
}

```

## Manually remove installment plan

After an installment plan is set on a PaymentIntent, it remains until you remove it.

For example, consider the case where a customer’s card declines when trying to pay with installments on their first card, then enters a second card that doesn’t support installments. The PaymentIntent confirmation fails because the installments aren’t supported on the card.

You must explicitly unset `payment_method_options[card][installments][plan]` when confirming the PaymentIntent again to indicate the absence of an installment plan.

# Invoices

> This is a Invoices for when payment-ui is invoices. View the full page at https://docs.stripe.com/payments/jp-installments/accept-a-payment?payment-ui=invoices.

## Integrate with Invoicing

You can accept installments with [Invoicing](https://docs.stripe.com/invoicing.md).

Invoices provide an itemized list of goods and services rendered, which includes the cost, quantity, and taxes. You can also use them as a tool to collect payment.

Your customers can pay with Checkout using cards (with or without installments) and other payment methods that support Checkout.

## Enable installments for Invoicing

You can create an invoice that accepts a payment with installments with the Invoicing API or with the Stripe Dashboard.

If you want more customization, we recommend using the Invoicing API. If you want to set up Invoicing without writing any code, use the Stripe Dashboard.

> You can enable installments for individual invoices but not for subscriptions.

## Use the Invoicing API to set up an invoice that can be paid with installments

Stripe Invoicing allows you to collect payments with installments. You can use this [integration guide](https://docs.stripe.com/invoicing/integration.md) to set up invoices.

1. [Review Invoicing documentation](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md#review-invoicing-documentation)
1. [Create a new Invoice](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md#create-new-invoice)
1. [Select an Installment plan on the client](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md#select-plan)
1. [Retrieve the selected Installment plan](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md#retrieve-plan)

## Review Invoicing documentation

Review the [Invoicing API integration guide](https://docs.stripe.com/invoicing/integration.md) and Invoicing API docs to familiarize yourself with how to create and send a generic invoice.

## Create a new Invoice

Create a new invoice with a valid API key, a customer represented by either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md) or [Customer](https://docs.stripe.com/api/customers/object.md) object, and a [Price](https://docs.stripe.com/api/prices.md) object, as shown in the example below. You need to substitute your own valid API key and customer object.

> Installments only work with `collection_method` set to `send_invoice` mode, not `charge_automatically` mode.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoiceItem = await stripe.invoiceItems.create({
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  pricing: {
    price: '{{PRICE_ID}}',
  },
});
```

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoice = await stripe.invoices.create({
  customer_account: '{{CUSTOMERACCOUNT_ID}}',
  collection_method: 'send_invoice',
  days_until_due: 30,
  pending_invoice_items_behavior: 'include',
  payment_settings: {
    payment_method_options: {
      card: {
        installments: {
          enabled: true,
        },
      },
    },
  },
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoiceItem = await stripe.invoiceItems.create({
  customer: '{{CUSTOMER_ID}}',
  pricing: {
    price: '{{PRICE_ID}}',
  },
});
```

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoice = await stripe.invoices.create({
  customer: '{{CUSTOMER_ID}}',
  collection_method: 'send_invoice',
  days_until_due: 30,
  pending_invoice_items_behavior: 'include',
  payment_settings: {
    payment_method_options: {
      card: {
        installments: {
          enabled: true,
        },
      },
    },
  },
});
```

## Select an Installment plan on the client

The hosted invoice page displays the available installment options based on the credit card number provided by the customer.

If a customer clicks on **Pay in installments**, the installment plan option selected by default is the first plan on the list.

The customer can select their desired installment option in the hosted invoice interface.

In a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), you can use [test card numbers](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md#testing) to test different behaviors.

## Retrieve the selected Installment plan

The selected installment plan is available through both the Dashboard and API. In the Dashboard, click a payment and scroll down to **Payment details**. If it used installments, you see the length of the plan.

The selected installment plan is also available on the PaymentIntent. After the user has completed payment, get the ID of the PaymentIntent from the Invoice object (for example, “payment*intent”: “pi*…”), and use it to retrieve the PaymentIntent object to see which installment plan the customer selected.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const invoice = await stripe.invoices.retrieve('{{INVOICE_ID}}');
```

With the payment intent ID, retrieve the PaymentIntent object:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.retrieve('{{PAYMENTINTENT_ID}}');
```

The PaymentIntent object then shows the selected installment plan:

```json
{
  "id": "pi_...",
  "object": "payment_intent",
  "amount": 100000,
...
  "charges": {
    "data": [
      {
        "id": "ch_...",
        "object": "charge",
        "amount": 100000,
        "payment_method_details": {
          "card": {
            "installments": {
              "plan": {
                "count": 3,
                "interval": "month",
                "type": "fixed_count"
              }
            },
          },
          ...
        },
        ...
      }
    ],
  },
...
  "payment_method_options": {
    "card": {
      "installments": {
        "enabled": true,
        "plan": {
          "count": 3,
          "interval": "month",
          "type": "fixed_count"
        },
        "available_plans": []
      }
    }
  }
}
```

## Use the Stripe Dashboard to send an invoice that can be paid with installments

To configure installments for Invoicing, visit the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) payment methods settings page.

You can create an invoice with just a few clicks using the [Stripe Dashboard](https://dashboard.stripe.com/customers).

1. On the [Customers](https://dashboard.stripe.com/customers) page, click **Add customer** to create a new customer, and set the currency to **JPY - Japanese Yen**)

1. Click your newly created customer to view their information, including their Invoices.

1. On the customer’s overview page, click **Actions** and then select **Create invoice** to set up a new invoice for that customer.

1. On the Create invoice page, check the **Payment** section to make sure that cards are enabled, and that the option to **Allow payment with card installments** is also enabled.

1. Click **Find or add an item** under the **Items** section to add products to the invoice.

1. Click **Review invoice** in the top right corner of the Create invoice page to finalize the invoice and schedule it to get sent to your customer

1. You can see the status of your customer’s invoices in the **Invoices** section of the customer’s overview page.

Your customer receives their invoice in an email. The invoice contains the instructions for them to submit their payment to cover their purchase.

The invoice is available in three formats: directly in the body of the email, as a PDF attached to the email, and as a hosted invoice page.

You can view the status of a particular invoice at any time on the customer’s overview page.

# No code

> This is a No code for when payment-ui is payment-links. View the full page at https://docs.stripe.com/payments/jp-installments/accept-a-payment?payment-ui=payment-links.

## Integrate with Payment Links

You can accept installments with Payment Links.

With [Payment Links](https://stripe.com/payments/payment-links), you can create a payment page and share a link to it with your customers. It requires no coding and you can share the link as many times as you want on social media, in emails, or any other channel.

You can also [create payment links programmatically](https://docs.stripe.com/payment-links/create.md#api) by using the Payment Links API.

## Control installments in Payment Links

You can enable or disable installments for Payment Links from the payment methods settings page of the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Installments are enabled by default.

## Test the integration

You can use the following cards to test your integration.

### Testing successful payments

#### Card numbers

| Brand        | Number           |
| ------------ | ---------------- |
| Visa         | 4000003920000003 |
| Mastercard   | 5200003920000008 |
| JCB          | 3530111333300000 |
| Diner’s Club | 36000039200009   |

#### PaymentMethods

| Brand        | PaymentMethod           |
| ------------ | ----------------------- |
| Visa         | `pm_card_jp`            |
| Mastercard   | `pm_card_jp_mastercard` |
| JCB          | `pm_card_jcb`           |
| Diner’s Club | `pm_card_jp_diners`     |

### Testing payment failures

Sometimes a card might be a valid Japan-issued credit card, but the card issuer decides to decline the transaction. You can use the card number below to retrieve a list of supported installment plans, but the transaction fails with a `card_declined` error.

#### Card numbers

| Brand | Number           |
| ----- | ---------------- |
| Visa  | 4000003920000029 |

#### PaymentMethods

| Brand | Number                                 |
| ----- | -------------------------------------- |
| Visa  | `pm_card_jp_visa_installmentsDeclined` |
