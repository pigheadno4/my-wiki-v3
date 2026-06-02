<!-- Source URL: https://docs.stripe.com/payments/wallets/link -->
<!-- Fetched: 2026-05-07 -->

# Link

Learn about Link's core features.

*Link* (Stripe’s digital wallet. It securely saves and autofills customer address and payment details, with support for cards, US bank accounts, BNPLs, and more) is Stripe’s digital wallet. It lets your customers securely save and reuse payment methods for fast checkout. Where available, your customers can pay with cards, bank accounts, [buy‑now‑pay‑later](https://docs.stripe.com/payments/link/klarna.md) options, and other methods. By offering more ways to pay and a streamlined checkout, you can increase conversion—and when customers pay with lower‑cost alternatives to cards, like [Instant Bank Payments](https://docs.stripe.com/payments/link/instant-bank-payments.md) (available exclusively through Link), you can reduce processing costs.

Link confirms all transactions immediately, and successful payments settle to your Stripe balance on the same timeline as card payments, regardless of the funding method.

Customers can make changes to their account, view their purchase history, or reach out to the Link customer support team by visiting [link.com](https://www.link.com). For information about how your payment integration affects Link, see [Link in different payment integrations](https://docs.stripe.com/payments/link/link-payment-integrations.md).

#### Payment method properties

- **Customer locations**

  Worldwide except India

- **Presentment currency**

  See [supported presentment currencies](https://docs.stripe.com/currencies.md#presentment-currencies)

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Wallet

- **Recurring payments**

  Yes

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  Yes

- **Dispute support**

  [Yes](https://docs.stripe.com/payments/wallets/link.md#disputes)

- **Manual capture support**

  Yes

- **Refunds or partial refunds**

  [Yes and Yes](https://docs.stripe.com/payments/wallets/link.md#refunds)

#### Business locations

With the exception of India, Stripe accounts worldwide can accept Link payments with local currency settlement. In Thailand or Brazil, Link isn’t supported in the Payment Element.

#### Product support

- Connect
- Checkout
- Payment Links
- Elements1

- Invoicing
- Billing

1 The Payment Element doesn’t support Link in Thailand or Brazil.

## Payment flow

The Link payment flow varies depending on the Stripe product that you’re using. To learn more, see [Faster checkout with link](https://docs.stripe.com/payments/link.md).

## Get started

To use Link, you must enable it under **Wallets** in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods) and integrate it appropriately for your use case. After you’ve enabled and integrated it, Stripe automatically displays Link to your customers for eligible transactions. All Link transactions confirm immediately, and successful payments settle to your Stripe balance on the same timeline as card payments, regardless of the payment method that funds the payment.

You can integrate Link in two ways:

- [As a payment method](https://docs.stripe.com/payments/link/link-payment-integrations.md?link-integrations=link-payment-method): Recommended. This integration works with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) and in most cases requires no additional configuration.
- [Within a card-specific integration](https://docs.stripe.com/payments/link/link-payment-integrations.md?link-integrations=link-card-integrations): Use this integration type instead if you only accept card payments, or if you require access to card details such as the brand or last 4 digits.

Both Link integrations accept all types of payment methods supported by Link, including credit cards, debit cards, [Instant Bank Payments](https://docs.stripe.com/payments/link/instant-bank-payments.md), and [Klarna](https://docs.stripe.com/payments/link/klarna.md).

If you integrate [Link as a payment method](https://docs.stripe.com/payments/link/link-payment-integrations.md?link-integrations=link-payment-method), then each Link transaction has a [PaymentMethod object](https://docs.stripe.com/api/payment_methods/object.md) with a [type](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-type) of `link` and no `wallet` hash.

If you incorporate [Link into a card-specific integration](https://docs.stripe.com/payments/link/link-payment-integrations.md?link-integrations=link-card-integrations), then each Link transaction has a [PaymentMethod object](https://docs.stripe.com/api/payment_methods/object.md) with a [type](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-type) of `card` and a `card.wallet` hash with a [type](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-card-wallet-type) of `link`.

## Refunds

Link supports full and partial refunds. You can initiate refunds through the Stripe Dashboard or API, similar to other payment methods. The refund process is typically completed within 5-10 business days, depending on your bank.

## Disputes

[Disputes](https://docs.stripe.com/disputes.md) for Link payments follow a similar process to card disputes. You can respond to disputes through the Stripe Dashboard or API. The dispute process and timelines might vary, depending on whether the saved payment method used for the transaction was a card or bank account.

> If you prefer to handle disputes programmatically, you can [respond to disputes](https://docs.stripe.com/disputes/api.md) using the API.

## Supported currencies

Link supports all [currencies](https://docs.stripe.com/currencies.md) that Stripe supports for card payments.

## See also

- [Link with Checkout](https://docs.stripe.com/payments/link/checkout-link.md)
- [Link with Elements](https://docs.stripe.com/payments/link/elements-link.md)
- [Link with Invoicing](https://docs.stripe.com/payments/link/invoicing.md)
