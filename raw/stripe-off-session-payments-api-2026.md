<!-- Source URL: https://docs.stripe.com/payments/off-session-payments -->
<!-- Fetched: 2026-05-11 -->

# The Off-Session Payments API

Create your own payment flow for recurring and unscheduled payments.

The Off-Session Payments API has the following features:

- **Retry a payment using smart retries**: Configure a retry strategy using AI inference to choose the best times to retry failed payments that increase the chance of a successful payment.

- **Process payments on multiple processors**: Route payments to any of the Stripe-supported processors, or automatically route payments created through the Off-Session Payments API and other supported payments APIs.

## How it works

With a single API request, you can initiate a payment and let Stripe handle retries for you.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const offSessionPayment = await stripe.v2.payments.offSessionPayments.create({
  amount: {
    value: 1000,
    currency: "usd",
  },
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENTMETHOD_ID}}",
  cadence: "recurring",
  metadata: {},
  retry_details: {
    retry_strategy: "best_available",
  },
});
```

See the full [Off-Session Payments API](https://docs.stripe.com/api/v2/payments/off-session-payments/object.md?api-version=preview) reference for more details.

## Compatible APIs

Stripe offers three core payments APIs compatible with Off-Session Payments that allow you to accept various types of payments from your customers. You can integrate these APIs into the Stripe prebuilt payment interfaces. The APIs serve different use cases, depending on how you structure your checkout flow and how much control you require.

- Use the [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions.md) to handle collection and setup of payment information with a prebuilt payment form that presents the customer’s complete checkout flow. With the Checkout Sessions API, you can save a payment for future use [with a payment](https://docs.stripe.com/payments/checkout/save-during-payment.md?payment-ui=stripe-hosted#save-payment-method) or [without an initial payment](https://docs.stripe.com/payments/checkout/save-and-reuse.md), depending on your payment flow. Build a [checkout page with the Checkout Sessions API](https://docs.stripe.com/payments/quickstart-checkout-sessions.md).

- Use the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) to implement the payment step only, but with more control. Unlike the Checkout Sessions API, which requires line item details, you only pass in the final amount you want to charge. Use this for advanced payment flows where you want to manually compute the final amount. Build an [advanced integration with the Payment Intents API](https://docs.stripe.com/payments/advanced.md).

- Use the [Setup Intents API](https://docs.stripe.com/api/setup_intents.md) to save a customer’s payment details without an initial payment. Use this when you want to onboard customers now, set them up for payments, and charge them in the future. Use this integration to set up recurring payments, or to create one-time payments with a final amount determined later, often after the customer receives your service. Build an [advanced integration with the Setup Intents API](https://docs.stripe.com/payments/save-and-reuse.md).

## Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. These requirements generally apply if you want to save your customer’s payment method for future use, such as displaying a customer’s payment method to them in the checkout flow for a future purchase or charging them when they’re not actively using your website or app. Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in.

When you save a payment method, you can only use it for the specific usage you’ve included in your terms. To charge a payment method when a customer is offline and save it as an option for future purchases, make sure that you explicitly collect consent from the customer for this specific use. For example, include a “Save my payment method for future use” checkbox to collect consent.

To charge a customer when they’re offline, make sure your terms include the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for example, if the charges are for scheduled installments, subscription payments, or unscheduled top-ups).
- How you determine the payment amount.
- Your cancellation policy, if the payment method is for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.
