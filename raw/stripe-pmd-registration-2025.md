<!-- Source URL: https://docs.stripe.com/payments/payment-methods/pmd-registration -->
<!-- Fetched: 2026-05-08 -->

# Register domains for payment methods

Register domains to use payment methods (including Link, Apple Pay, and Google Pay) in Elements or Checkout's embeddable payment form.

For certain payment methods, you must register every web domain that shows the payment method if your integration uses _Elements_ (A set of UI components for building a web checkout flow. They adapt to your customer's locale, validate input, and use tokenization, keeping sensitive customer data from touching your server) or [Checkout’s embeddable payment page](https://docs.stripe.com/payments/checkout/how-checkout-works.md?payment-ui=embedded-page). This includes registering top-level domains and subdomains. For example, if you have the domain **example.com** and subdomains like **shop.example.com** and **www.example.com**, this guide explains how to register them.

After you register a domain, that domain is ready for use with other payment methods that you might enable in the future.

Register your domains for the following payment methods:

- [Apple Pay](https://docs.stripe.com/apple-pay.md) (Required)
- [Amazon Pay](https://docs.stripe.com/payments/amazon-pay.md)
- [Google Pay](https://docs.stripe.com/google-pay.md)
- [Klarna](https://docs.stripe.com/payments/klarna.md)
- [Link](https://docs.stripe.com/payments/wallets/link.md)
- [PayPal](https://docs.stripe.com/payments/paypal.md)

> #### Apple Pay and merchant validation
>
> The Apple Pay documentation describes their process of “merchant validation," which Stripe handles for you behind the scenes. You don’t need to create an Apple Merchant ID or CSR. Instead, follow the steps in this guide.

## Testing

You also need to register domains for testing. When testing locally, you can use a tool such as [ngrok](https://ngrok.com/) to get an HTTPS domain. You can either register in a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), or register in live mode and the domain will also be registered in sandboxes automatically. Remember to register your domains in live mode before going live.

# Dashboard

> This is a Dashboard for when dashboard-or-api is dashboard. View the full page at https://docs.stripe.com/payments/payment-methods/pmd-registration?dashboard-or-api=dashboard.

You can create and manage domains in the Dashboard on the [Payment method domains page](https://dashboard.stripe.com/settings/payment_method_domains) for use in production and testing.

> #### Using Connect
>
> Connect platforms that create direct charges must use the API to manage domains for their [connected accounts](https://docs.stripe.com/payments/payment-methods/pmd-registration.md#register-your-domain-while-using-connect), not the Stripe Dashboard.

## Register your domain

To register a domain:

1. On the [Payment method domains page](https://dashboard.stripe.com/settings/payment_method_domains), click **Add a new domain**.
1. Enter your domain name.
1. Click **Save and continue**.
1. (Optional) Repeat steps 1-3 for additional domains that you need to register.

After completing these steps, your domain shows up on the Payment method domains page.

### Using an iframe

- **Using an iframe with [Elements](https://docs.stripe.com/payments/elements.md)**: When using an iframe, its origin must match the top-level origin (except for Safari 17+ when specifying `allow="payment"` attribute). Two pages have the same origin if the protocol, host (full domain name), and port (if specified) are the same for both pages.
- **Top-level domain and iframe domain**: If the top-level domain differs from the iframe domain, the top-level domain and the iframe’s source domain must both be registered payment method domains on the associated account.

## Manage your domain

You can see a list of all of your domains in the Dashboard.

To disable a domain, click the row action and then click **Disable**. If a domain is disabled, the payment methods no longer appear in Elements or Checkout’s embeddable payment form on that domain.

To enable a disabled domain, click the row action and then click **Enable**.

# API

> This is a API for when dashboard-or-api is api. View the full page at https://docs.stripe.com/payments/payment-methods/pmd-registration?dashboard-or-api=api.

## Register your domain

To register a domain, do the following:

```node
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethodDomain = await stripe.paymentMethodDomains.create({
  domain_name: "example.com",
});
```

Repeat for all domains that you need to register.

### Using an iframe

- When using an iframe, its origin must match the top-level origin, except in Safari 17+. Two pages have the same origin if the protocol, host (full domain name), and port (if specified) are the same for both pages.
- When using a cross-origin iframe in Safari 17+ you must specify the `allow=“payment”` attribute. To enable Apple Pay, you must also register the source domain that the iframe loads.

## Manage your domain

Using the [PaymentMethodDomain API](https://docs.stripe.com/api/payment_method_domains/object.md) you can do the following:

- Retrieve a domain.
- See a list of all of your domains.
- Enable or disable a domain. If a domain is disabled, the payment methods no longer appear in Elements or Checkout’s embeddable payment form on that domain.

This sample shows how to disable a domain:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethodDomain = await stripe.paymentMethodDomains.update(
  "{{PAYMENT_METHOD_DOMAIN_ID}}",
  {
    enabled: false,
  },
);
```

## Register your domain while using Connect

Connect platforms must register all domains where Elements or Checkout’s embeddable payment form displays the payment methods listed above. The domain where the charge is being run needs to be registered for the user running the charge.

If the platform creates [direct charges](https://docs.stripe.com/connect/direct-charges.md), use your platform’s secret key to authenticate the request and set the Stripe-Account header to your connected account’s Stripe ID.

If the platform creates [destination charges](https://docs.stripe.com/connect/destination-charges.md) or [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md), use your platform’s secret key to authenticate the request and omit the Stripe-Account header.

Learn more about [Making API calls for connected accounts](https://docs.stripe.com/connect/authentication.md).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentMethodDomain = await stripe.paymentMethodDomains.create(
  {
    domain_name: "example.com",
  },
  {
    stripeAccount: "{{CONNECTEDACCOUNT_ID}}",
  },
);
```
