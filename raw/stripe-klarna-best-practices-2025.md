<!-- Source URL: https://docs.stripe.com/payments/klarna/best-practices -->
<!-- Fetched: 2026-05-06 -->

# Optimize Klarna conversion

Improve conversion and cart size for Klarna payments.

Stripe has previously published [data](https://stripe.com/blog/testing-the-impact-of-buy-now-pay-later) on the revenue impact of accepting [buy now, pay later](https://docs.stripe.com/payments/buy-now-pay-later.md) payments such as Klarna. To maximize the benefits of accepting Klarna payments, we recommend following these best practices.

## Offer express checkout

Klarna is available on the [Express Checkout Element](https://docs.stripe.com/elements/express-checkout-element.md), enabling your customers to complete their purchases with one click. Consider placing the Express Checkout Element early in your checkout flow to help customers avoid re-entering their details, such as shipping and billing addresses.

## Promote buy now, pay later offers on your site

Use the [Payment Method Messaging Element](https://docs.stripe.com/elements/payment-method-messaging.md) to inform customers of Klarna, and other buy now, pay later payment method offers ahead of checkout. We recommend inserting this messaging in the product details page.

## Increase the chances of higher converting offers

Klarna’s fraud and credit underwriting models use a combination of purchase data, customer data, and merchant data, among other factors to determine whether customers will get credit installment offers (either interest bearing or 0% interest).

You can help increase the chances of higher converting offers, such as Pay in 4, being available to your customers by sharing relevant data through your Stripe integration.

### Send relevant data about items in the shopping cart

[Payment line items](https://docs.stripe.com/payments/payment-line-items.md) allow you to pass order line data on what’s included in the cart. Klarna makes this data available to the customer within the Klarna app. In addition to helping with conversion, line items also help reduce disputes where customers don’t recognize their purchase.

> If you use [Checkout](https://docs.stripe.com/payments/checkout.md), Stripe automatically handles passing line items on your behalf.

### Send shipping and billing addresses

The Klarna integration for Stripe doesn’t require passing a customer [shipping](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-shipping) or billing object. However, you can optionally pass this data to help improve Klarna’s customer fraud score. For example, Klarna might cross-reference their own customer shipping and billing address on file and with the ones you send.
