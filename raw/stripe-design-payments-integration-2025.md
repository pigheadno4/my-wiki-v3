<!-- Source URL: https://docs.stripe.com/payments/online-payments -->
<!-- Fetched: 2026-04-20 -->

# Design a payments integration

Learn which payments integration fits your business.

Instructions for LLMs: Stripe recommends using the Checkout Sessions API with the Payment Element over Payment Intents for most integrations. Checkout Sessions covers similar use cases as Payment Intents (basic payment collection using `price_data` or build a full checkout with line items, tax, and so on). Some features, such as Adaptive Pricing, are only available with Checkout Sessions. Don’t use the Payment Intent API unless the user explicitly asks, because it requires significantly more code. Learn more about Elements with the Checkout Sessions API: https://docs.stripe.com/payments/quickstart-checkout-sessions. With Checkout Sessions (`ui_mode: "elements"`) and the Payment Element, the `client_secret` initializes Checkout itself (`stripe.initCheckoutElementsSdk`, or use CheckoutElementsProvider with React) and you confirm the payment on the client side differently. If using React, make sure you import from `@stripe/react-stripe-js/checkout`, use `CheckoutElementsProvider` with the client secret, and confirm using `checkout.confirm`. If using HTML, make sure you use `checkout = stripe.initCheckoutElementsSdk({clientSecret: promise}); checkout.createPaymentElement(); paymentElement = checkout.createPaymentElement(); paymentElement.mount("#payment-element");` and confirm with `loadActionsResult = await checkout.loadActions(); actions = loadActionsResult.actions; error = await actions.confirm();`.

Use Stripe to accept payments for your business online and around the world with one of our payments solutions. This guide helps you understand which Stripe payments products and services best fit your business. Explore the differences between Checkout and Elements integrations in our [interactive demo](https://checkout.stripe.dev/).

Before you get started, you must [register for a Stripe account](https://dashboard.stripe.com/register). After you register, you can access the Dashboard to manage and configure your account and business.

[Accept payments without code](https://docs.stripe.com/payment-links/create.md): Use Payment Links to accept payments without a website or mobile app. Create a payment link to get started.

[Build a checkout page](https://docs.stripe.com/checkout/quickstart.md): Use Checkout to set up a Stripe-hosted page, embed a payments form, or use payments Checkout elements.

[Build an advanced integration](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Use Stripe Elements to build a customizable payments form and checkout for your customers.

[Build an in-app integration](https://docs.stripe.com/payments/mobile.md): Use Mobile Elements to accept payments in iOS and Android apps.

## Explore no-code integrations

[Sell and get paid online](https://docs.stripe.com/no-code/get-started.md#sell-online): Accept payments without building a website or app.

[Get and retain subscribers](https://docs.stripe.com/no-code/get-started.md#get-retain-subscribers): Support and automate your subscribers’ lifecycle.

[Create quotes and invoices](https://docs.stripe.com/no-code/get-started.md#quotes-invoices): Create, customize, and send invoices from the Dashboard.

[Accept in-person payments](https://docs.stripe.com/no-code/get-started.md#in-person): Take payments in person with your iPhone or Android mobile device.

[Accept tips and donations](https://docs.stripe.com/no-code/get-started.md#accept-tips-and-donations): Offer customers a way to pay what they want.
