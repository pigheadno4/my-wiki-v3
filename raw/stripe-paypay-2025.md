<!-- Source URL: https://docs.stripe.com/payments/paypay -->
<!-- Fetched: 2026-05-07 -->

# PayPay payments

Learn about PayPay, a digital wallet payment method in Japan.

PayPay is a popular digital payment platform and mobile wallet service in Japan.

#### Payment method properties

- **Customer locations**

  Japan

- **Presentment currencies**

  JPY

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Wallets

- **Recurring payments**

  No

- **Payout timing**

  Standard

- **Connect support**

  No

- **Dispute support**

  No

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [ Yes ](https://docs.stripe.com/payments/paypay.md#refunds) / [ Yes ](https://docs.stripe.com/payments/paypay.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept PayPay payments that settle in a [supported currency](https://docs.stripe.com/payments/paypay.md#supported-currencies).

- JP

#### Product support

- Payment Links
- Checkout1
- Elements2

1Not supported when using Checkout in subscription mode or setup mode.

2Express Checkout Element doesn’t support PayPay.

## Get started

You don’t have to integrate PayPay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable PayPay. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add PayPay from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)

If your integration requires manually listing payment methods, learn how to [ configure PayPay](https://docs.stripe.com/payments/paypay/accept-a-payment.md).

## Payment options

The minimum charge limit is 50 JPY or the equivalent for other supported currencies.

The maximum charge limit is 1,000,000 JPY or the equivalent for other supported currencies.

## Prohibited and restricted business categories

In addition to the categories of goods or services sold and businesses [restricted from using Stripe overall](https://stripe.com/restricted-businesses), the following categories are prohibited from using PayPay:

- Cryptocurrency exchanges and wallets
- Other categories at the discretion of PayPay

## Refunds

PayPay supports full and partial refunds.

- The refund period is up to 365 days after the purchase.
- Refunds for PayPay payments complete instantly.

Stripe notifies you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. If a refund fails (the `Refund` object’s status transitions to `failed`), then we return the amount to your Stripe balance, and you must arrange an alternative way of providing your customer with a refund.

## Supported currencies

You can create PayPay payments in the currencies that map to your country. The default local currency for PayPay is `jpy`.

- jpy: JP
