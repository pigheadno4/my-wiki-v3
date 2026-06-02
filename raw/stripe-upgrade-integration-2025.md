<!-- Source URL: https://docs.stripe.com/payments/upgrades -->
<!-- Fetched: 2026-04-20 -->

# Upgrade your integration

Increase conversion and get access to new features by upgrading your integration.

Discover the recommended options for upgrading both your entire payments integration, and individual features. For a comprehensive list of changes to the API, see [API upgrades](https://docs.stripe.com/upgrades.md).

## Payment integration upgrades

Take advantage of new features by upgrading your existing integration.

| Legacy integration                                                                  | Recommended integration                                                | Why you should upgrade                                                                             | Upgrade path |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------ |
| [Card Element](https://docs.stripe.com/payments/payment-card-element-comparison.md) | [Payment Element](https://docs.stripe.com/payments/payment-element.md) | - Use a single UI component to present over 100 payment methods and build a customizable checkout. |

- Access the latest compatible features.
- Have Stripe handle the presentment logic using various factors, such as location, currency, and success metrics.
- Customize payment method preferences in the Dashboard. | [Migrate to the Payment Element](https://docs.stripe.com/payments/payment-element/migration-ewcs.md) |
  | _Legacy Checkout_ (A modal dialog to collect card details) | - [Checkout](https://docs.stripe.com/payments/checkout/how-checkout-works.md)
- [Payment Links](https://docs.stripe.com/payment-links.md) | - Checkout:
  - Checkout offers a prebuilt payment form to securely accept online payments.
  - Embed Checkout on your site or redirect to a Stripe-hosted Checkout page.
  - Checkout gives you access to additional features, such as [Dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) and [Adaptive Pricing](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md).

- Payment Links:

      - Accept a payment or sell subscriptions without building additional standalone websites or applications.
      - Share a link as many times as you want on social media, in emails, or on your website.
      - Access [Dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) from the Dashboard. | [Migrate to Checkout](https://docs.stripe.com/payments/checkout/migration.md)                                     |

  | [Payment request button](https://docs.stripe.com/stripe-js/elements/payment-request-button.md) | [Express checkout element](https://docs.stripe.com/elements/express-checkout-element.md) | - Accept additional payment method options, such as [Apple pay](https://docs.stripe.com/apple-pay.md), [Amazon Pay](https://docs.stripe.com/payments/amazon-pay.md), [Google Pay](https://docs.stripe.com/google-pay.md), [Link](https://docs.stripe.com/payments/link.md), and [PayPal](https://docs.stripe.com/payments/paypal.md).

- Display multiple payment method buttons at the same time. | [Migrate to the Express Checkout Element](https://docs.stripe.com/elements/express-checkout-element/migration.md) |

## Feature upgrades

We recommend upgrading these features to enhance your checkout process.

| Integration feature                                                                                                                                                                                      | Feature upgrade                                                                                                            | Why you should upgrade                       | Upgrade path |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ------------ |
| [Manual payment methods](https://docs.stripe.com/payments/payment-methods/integration-options.md#listing-payment-methods-manually)                                                                       | [Dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md)                     | - Manage payment methods from the Dashboard. |
| - Rely on Stripe to present eligible payment methods for each transaction using factors such as transaction amount, currency, payment flow, and the payment method preferences you set in the Dashboard. | [Payment Links, Checkout, or Payment Element](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) |
| [Manual payment methods](https://docs.stripe.com/payments/payment-methods/integration-options.md#listing-payment-methods-manually) in a [Connect integration](https://docs.stripe.com/connect.md)        | [Dynamic payment methods](https://docs.stripe.com/connect/dynamic-payment-methods.md)                                      | - Manage payment methods from the Dashboard. |
| - Rely on Stripe to present eligible payment methods for each transaction using factors such as transaction amount, currency, payment flow, and the payment method preferences you set in the Dashboard. | [Connect dynamic payment methods](https://docs.stripe.com/connect/dynamic-payment-methods.md)                              |
