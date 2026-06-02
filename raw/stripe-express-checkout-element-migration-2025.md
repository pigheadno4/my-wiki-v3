<!-- Source URL: https://docs.stripe.com/elements/express-checkout-element/migration -->
<!-- Fetched: 2026-04-21 -->

# Migrate to the Express Checkout Element

Migrate your existing integration with the Payment Request Button Element to the Express Checkout Element.

The [Payment Request Button Element](https://docs.stripe.com/stripe-js/elements/payment-request-button.md) allows you to accept card payments through [Apple Pay](https://docs.stripe.com/apple-pay.md), [Google Pay](https://docs.stripe.com/google-pay.md), or [Link](https://docs.stripe.com/payments/link.md). When you migrate to the [Express Checkout Element](https://docs.stripe.com/elements/express-checkout-element.md), you can accept card or [wallet](https://docs.stripe.com/payments/wallets.md) payments through one or more payment buttons, including [PayPal](https://docs.stripe.com/payments/paypal.md).

| If your existing integration uses                                                                                                        | Do the following                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [Payment Intents](https://docs.stripe.com/api/payment_intents.md) API to create and track payments or save card details during a payment | Follow the steps in this guide to use the Express Checkout Element.                                                        |
| [Charges](https://docs.stripe.com/api/charges.md) API with tokens                                                                        | Migrate to the [Payment Intents API](https://docs.stripe.com/payments/payment-intents/migration.md#web) before proceeding. |

## Enable payment methods

Enable the payment methods you want to support in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods). You must enable at least one payment method.

By default, Stripe enables cards and other common payment methods. You can enable additional payment methods that are relevant for your business and customers. See the [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md) for product and payment method support and our [pricing page](https://stripe.com/pricing/local-payment-methods) for fees.

## Update Elements instance [Client-side]

Next, update your client-side code to pass the mode (payment), amount, and currency. These values determine which payment methods to show to your customers.

For example, if you pass the `eur` currency on the `PaymentIntent` and enable OXXO in the Dashboard, your customer won’t see OXXO because OXXO doesn’t support `eur` payments.

Stripe evaluates the currency, payment method restrictions, and other parameters to determine the list of supported payment methods. We prioritize payment methods that increase conversion and are most relevant to the currency and customer location.

#### HTML + JS

### Before

```javascript
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
const elements = stripe.elements();
```

### After

```javascript
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
const options = {
  mode: "payment",
  amount: 1099,
  currency: "usd",
};
const elements = stripe.elements(options);
```

#### React

### Before

```jsx
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

function App() {
  return (
    <Elements stripe={stripePromise}>
      <CheckoutForm />
    </Elements>
  );
}
```

### After

```jsx
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

const options = {
  mode: "payment",
  amount: 1099,
  currency: "usd",
};

function App() {
  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm />
    </Elements>
  );
}
```

## Optional: Save payment details during a payment

If your existing integration saves card details during payment, use the `setup_future_usage` option when creating the Elements instance, instead of passing it at the confirm payment stage with `stripe.confirmCardPayment`.

You can’t save certain payment methods during payment. You can still enable these [payment methods](https://docs.stripe.com/payments/payment-methods/integration-options.md) for other use cases, but customers won’t see them when they set up future payments.

#### HTML + JS

```javascript
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
const options = {
  mode: "payment",
  amount: 1099,
  currency: "usd",
  setup_future_usage: "off_session",
};
const elements = stripe.elements(options);
```

#### React

```jsx
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

const options = {
  mode: "payment",
  amount: 1099,
  currency: "usd",
  setup_future_usage: "off_session",
};

function App() {
  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm />
    </Elements>
  );
}
```

## Update your PaymentIntent creation call [Server-side]

The `PaymentIntent` includes the payment methods shown to customers during checkout. You can manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

#### Node.js

```javascript
const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd", // In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
  automatic_payment_methods: {
    enabled: true,
  },
});
```

If your existing integration supports multiple payment methods or you want to accept payment methods other than cards, you can [enable more payment methods](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard.

## Add the Express Checkout Element [Client-side]

If you use [React Stripe.js](https://github.com/stripe/react-stripe-js), update to the latest package to use the Express Checkout Element.

Replace the Payment Request Button Element with the Express Checkout Element. The examples below demonstrate how to replace `PaymentRequestButtonElement` with `ExpressCheckoutElement`.

You no longer need to create a `paymentRequest` object. Instead, pass the options when creating the `ExpressCheckoutElement`.

#### HTML + JS

### Before

```html
<div id="payment-request-button"></div>
```

### After

```html
<div id="express-checkout-element">
  <!-- Mount the Express Checkout Element here -->
</div>
```

### Before

```javascript
const paymentRequest = stripe.paymentRequest({
  country: "US",
  currency: "usd",
  total: {
    label: "Demo total",
    amount: 1099,
  },
  requestPayerName: true,
  requestPayerEmail: true,
});
const paymentRequestButton = elements.create("paymentRequestButton", {
  paymentRequest: paymentRequest,
});
paymentRequestButton.mount("#payment-request-button");
paymentRequest.canMakePayment().then(function (result) {
  if (result) {
    paymentRequestButton.mount("#payment-request-button");
  } else {
    document.getElementById("payment-request-button").style.display = "none";
  }
});
```

### After

```javascript
const expressCheckoutElement = elements.create("expressCheckout", {
  emailRequired: true,
});
expressCheckoutElement.mount("#express-checkout-element");
```

#### React

### Before

```jsx
import React, { useState, useEffect } from "react";
import {
  PaymentRequestButtonElement,
  useStripe,
} from "@stripe/react-stripe-js";

const CheckoutForm = () => {
  const stripe = useStripe();
  const [paymentRequest, setPaymentRequest] = useState(null);

  useEffect(() => {
    if (stripe) {
      const pr = stripe.paymentRequest({
        country: "US",
        currency: "usd",
        total: {
          label: "Demo total",
          amount: 1099,
        },
        requestPayerName: true,
        requestPayerEmail: true,
      });

      pr.canMakePayment().then((result) => {
        if (result) {
          setPaymentRequest(pr);
        }
      });
    }
  }, [stripe]);

  return (
    paymentRequest && (
      <PaymentRequestButtonElement options={{ paymentRequest }} />
    )
  );
};
```

### After

```jsx
import React from "react";
import { ExpressCheckoutElement } from "@stripe/react-stripe-js";

const CheckoutPage = () => {
  const options = {
    emailRequired: true,
  };

  return (
    <div id="checkout-page">
      <ExpressCheckoutElement options={options} onConfirm={onConfirm} />
    </div>
  );
};
```

## Optional: Request an Apple Pay merchant token (MPAN)

The Express Checkout Element supports Apple Pay merchant tokens, which we recommend over device tokens to enable merchant initiated transactions (MIT) such as recurring and deferred payments and automatic reloads. Merchant tokens (MPANs) connect your business with your customer’s Apple Wallet payment method, so they work across multiple devices and keep payment information active in a new device even when its removed from a lost or stolen device. See [ApplePay merchant tokens](https://docs.stripe.com/apple-pay/merchant-tokens.md?pay-element=ece) for integration details.

## Optional: Listen to the ready event

After mounting, the Express Checkout Element won’t show any buttons for a brief period. You might want to animate in the Element when buttons appear. To do so, listen to the [ready event](https://docs.stripe.com/js/element/events/on_ready) and inspect the value of `availablePaymentMethods` to determine which buttons, if any, show up in the Express Checkout Element.

#### HTML + JS

```javascript
// Optional: If you're doing custom animations, hide the Element
const expressCheckoutDiv = document.getElementById("express-checkout-element");
expressCheckoutDiv.style.visibility = "hidden";

expressCheckoutElement.on("ready", ({ availablePaymentMethods }) => {
  if (!availablePaymentMethods) {
    // No buttons will show
  } else {
    // Optional: Animate in the Element
    expressCheckoutDiv.style.visibility = "initial";
  }
});
```

#### React

```jsx
import React, { useState } from "react";
import { ExpressCheckoutElement } from "@stripe/react-stripe-js";
import { onConfirm } from "./confirmHandler";

const CheckoutPage = () => {
  // Optional: If you're doing custom animations, hide the Element
  const [visibility, setVisibility] = useState("hidden");
  const onReady = ({ availablePaymentMethods }) => {
    if (!availablePaymentMethods) {
      // No buttons will show
    } else {
      // Optional: Animate in the Element
      setVisibility("initial");
    }
  };

  return (
    <div id="checkout-page">
      <div id="express-checkout-element" style={{ visibility }}>
        <ExpressCheckoutElement onConfirm={onConfirm} onReady={onReady} />
      </div>
    </div>
  );
};
```

## Optional: Style the Express Checkout Element

You can [style](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-buttonTheme) each payment method button—for example, [Google Pay](https://developers.google.com/pay/api/web/guides/resources/customize) or [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/buttons-and-marks/)—to have different themes and types.

You can also use the `borderRadius` variable in the [Appearance](https://docs.stripe.com/elements/appearance-api.md?platform=web#commonly-used-variables) API.

#### HTML + JS

### Before

```javascript
elements.create("paymentRequestButton", {
  paymentRequest,
  style: {
    paymentRequestButton: {
      type: "book",
      theme: "dark",
      height: "55px",
    },
  },
});
```

### After

```javascript
const appearance = {
  variables: {
    // This controls the border-radius of the rendered Express Checkout Element.
    borderRadius: "4px",
  },
};
const options = {
  mode: "payment",
  amount: 1099,
  currency: "usd",
  appearance,
};
// Pass the appearance object to the Elements instance.
const elements = stripe.elements(options);
elements.create("expressCheckout", {
  layout: "auto",
  buttonType: {
    googlePay: "book",
    applePay: "book",
    paypal: "buynow",
  },
  buttonTheme: {
    applePay: "black",
  },
  buttonHeight: 55,
});
```

#### React

### Before

```jsx
import React, { useState, useEffect } from "react";
import {
  PaymentRequestButtonElement,
  useStripe,
} from "@stripe/react-stripe-js";

const CheckoutForm = () => {
  const options = {
    paymentRequest,
    style: {
      paymentRequestButton: {
        type: "book",
        theme: "dark",
        height: "55px",
      },
    },
  };

  return <PaymentRequestButtonElement options={options} />;
};
```

### After

```jsx
import React from 'react';
import {ExpressCheckoutElement} from '@stripe/react-stripe-js';

const CheckoutPage = () => {
  const options = {
    layout: 'auto',
    buttonType: {
      googlePay: 'book',
      applePay: 'book',
      paypal: 'buynow',
    },
    buttonTheme: {
      applePay: 'black'
    },
    buttonHeight: 55
  }

  return (
    <ExpressCheckoutElementoptions={options}
      onConfirm={onConfirm}
    />
  );
};
```

## Update the confirm payment method [Client-side]

Listen to the [confirm](https://docs.stripe.com/js/elements_object/express_checkout_element_confirm_event) event to handle confirmation. To collect and submit payment information to Stripe, use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) instead of individual confirmation methods like `stripe.confirmCardPayment`.

Instead of a PaymentMethod ID, `stripe.confirmPayment` uses the Elements instance from the Express Checkout Element and the client secret from the created `PaymentIntent`.

When called, `stripe.confirmPayment` attempts to complete any required actions, such as authenticating your customers by displaying a 3DS dialog or redirecting them to a bank authorization page. After confirmation completes, users are directed to the [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) that you configured, which corresponds to a page on your website that provides the payment status.

If you want the checkout flow for card payments to redirect only for payment methods that require it, you can set [redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect) to `if_required`. This doesn’t apply to the Express Checkout Element.

The example below replaces `stripe.confirmCardPayment` with `stripe.confirmPayment`.

#### HTML + JS

### Before

```javascript
paymentRequest.on("paymentmethod", function (ev) {
  stripe
    .confirmCardPayment(
      "{{CLIENT_SECRET}}",
      { payment_method: ev.paymentMethod.id },
      { handleActions: false },
    )
    .then(function (confirmResult) {
      if (confirmResult.error) {
        ev.complete("fail");
      } else {
        ev.complete("success");
        if (confirmResult.paymentIntent.status === "requires_action") {
          stripe.confirmCardPayment(clientSecret).then(function (result) {
            if (result.error) {
              // The payment failed -- ask your customer for a new payment method.
            } else {
              // The payment succeeded.
            }
          });
        } else {
          // The payment succeeded.
        }
      }
    });
});
```

### After

```javascript
expressCheckoutElement.on("confirm", async (event) => {
  const { error } = await stripe.confirmPayment({
    // `Elements` instance that's used to create the Express Checkout Element.
    elements,
    // `clientSecret` from the created PaymentIntent
    clientSecret,
    confirmParams: {
      return_url: "https://example.com/order/123/complete",
    },
    // Uncomment below if you only want redirect for redirect-based payments.
    // redirect: 'if_required',
  });

  if (error) {
    // This point is reached only if there's an immediate error when confirming the payment. Show the error to your customer (for example, payment details incomplete).
  } else {
    // Your customer will be redirected to your `return_url`.
  }
});
```

#### React

### Before

```javascript
paymentRequest.on("paymentmethod", function (ev) {
  stripe
    .confirmCardPayment(
      "{{CLIENT_SECRET}}",
      { payment_method: ev.paymentMethod.id },
      { handleActions: false },
    )
    .then(function (confirmResult) {
      if (confirmResult.error) {
        ev.complete("fail");
      } else {
        ev.complete("success");
        if (confirmResult.paymentIntent.status === "requires_action") {
          stripe.confirmCardPayment(clientSecret).then(function (result) {
            if (result.error) {
              // The payment failed -- ask your customer for a new payment method.
            } else {
              // The payment succeeded.
            }
          });
        } else {
          // The payment succeeded.
        }
      }
    });
});
```

### After

```jsx
import React from 'react';
import {ExpressCheckoutElement} from '@stripe/react-stripe-js';

const CheckoutPage = () => {
  const onConfirm = async () => {
    const {error} = await stripe.confirmPayment({
      // `Elements` instance that's used to create the Express Checkout Element.
      elements,
      // `clientSecret` from the created PaymentIntent
      clientSecret,
      confirmParams: {
        return_url: 'https://example.com/order/123/complete',
      },
      // Uncomment below if you only want redirect for redirect-based payments.
      // redirect: 'if_required',
    });

    if (error) {
      // This point is reached only if there's an immediate error when confirming the payment. Show the error to your customer (for example, payment details incomplete).
    } else {
      // Your customer will be redirected to your `return_url`.
    }
  };

  return (
    <div id="checkout-page">
      <ExpressCheckoutElementonConfirm={onConfirm}
      />
    </div>
  );
};
```

## Handle post-payment events [Server-side]

Stripe sends a [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event when the payment completes. Use the [Dashboard webhook tool](https://dashboard.stripe.com/webhooks) or follow the [webhook guide](https://docs.stripe.com/webhooks/quickstart.md) to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events is what enables you to accept [different types of payment methods](https://stripe.com/payments/payment-methods-guide) with a single integration.

In addition to handling the `payment_intent.succeeded` event, we recommend handling these other events when collecting payments with the Payment Element:

| Event                                                                                                                           | Description                                                                                                                                                                                                                                                                         | Action                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.succeeded)           | Sent when a customer successfully completes a payment.                                                                                                                                                                                                                              | Send the customer an order confirmation and _fulfill_ (Fulfillment is the process of providing the goods or services purchased by a customer, typically after payment is collected) their order. |
| [payment_intent.processing](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.processing)         | Sent when a customer successfully initiates a payment, but the payment has yet to complete. This event is most commonly sent when the customer initiates a bank debit. It’s followed by either a `payment_intent.succeeded` or `payment_intent.payment_failed` event in the future. | Send the customer an order confirmation that indicates their payment is pending. For digital goods, you might want to fulfill the order before waiting for payment to complete.                  |
| [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.payment_failed) | Sent when a customer attempts a payment, but the payment fails.                                                                                                                                                                                                                     | If a payment transitions from `processing` to `payment_failed`, offer the customer another attempt to pay.                                                                                       |
