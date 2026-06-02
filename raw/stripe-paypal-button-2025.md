<!-- Source URL: https://docs.stripe.com/payments/paypal/paypal-button -->
<!-- Fetched: 2026-05-07 -->

# PayPal Button

Learn how the PayPal button simplifies payments for your customers.

Your customers can make PayPal payments through a redirect or by using the PayPal button. Stripe determines whether to present the redirect or the button, but you can configure your pages to increase availability of the button. The PayPal button is available in the [Express Checkout Element](https://docs.stripe.com/elements/express-checkout-element.md) and [Stripe Checkout](https://docs.stripe.com/payments/checkout.md).

This demo shows the PayPal button in the Express Checkout Element:

Before you start, we recommend you create a [PayPal Sandbox account](https://developer.paypal.com/tools/sandbox/accounts/) to test your integration.

#### Express Checkout Element

The PayPal button works in Stripe’s Express Checkout Element. To learn how to integrate PayPal with the Express Checkout Element, see [the Express Checkout Element guide](https://docs.stripe.com/elements/express-checkout-element.md).

**Recommended options**

In certain scenarios, the Express Checkout Element doesn’t support the PayPal button. These scenarios include:

- Billing address collection is enabled
- Shipping address collection is enabled (for recurring payments)
- Phone number collection is enabled

To maximize the chance of presenting the PayPal button, we recommend using the following options when [creating](https://docs.stripe.com/js/elements_object/create_express_checkout_element) the Express Checkout Element. For recurring payments with the PayPal button, you must explicitly define `billingAddressRequired` as `false`.

#### HTML + JS

```javascript
elements.create("expressCheckout", {
  phoneNumberRequired: false,
  billingAddressRequired: false,
  shippingAddressRequired: false, // Only supported for one-off payments
});
```

#### React

```jsx
const options = {
  phoneNumberRequired: false,
  billingAddressRequired: false,
  shippingAddressRequired: false, // Only supported for one-off payments
};
```

#### Stripe Checkout

Stripe Checkout supports the PayPal button out of the box. To learn how to use Stripe Checkout, see [the Stripe Checkout guide](https://docs.stripe.com/payments/checkout.md).

In certain scenarios, Stripe Checkout doesn’t support the PayPal button, and presents PayPal only as a redirect. These scenarios include:

- Billing address collection is enabled
- Consent collection is enabled
- Custom fields are used
- PayPal is the only payment method type
- Phone number collection is enabled
- Shipping address collection is enabled for recurring payments
- Tax ID collection is enabled

The following example generates a Checkout session using options that maximize availability of the PayPal button:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  automatic_tax: {
    enabled: false,
  },
  line_items: [
    {
      price_data: {
        unit_amount: 1000,
        currency: "eur",
        product_data: {
          name: "Coconut",
        },
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  billing_address_collection: "auto",
  payment_method_types: ["card", "paypal"],
  success_url: "https://example.com/success",
});
```
