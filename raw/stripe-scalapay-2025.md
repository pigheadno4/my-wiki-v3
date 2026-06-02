<!-- Source URL: https://docs.stripe.com/payments/scalapay -->
<!-- Fetched: 2026-05-06 -->

# Scalapay payments

Use Scalapay to pay in 3 or 4 installments.

Offer [Scalapay](https://scalapay.com/) Pay in 3 or 4 installments to your customers.

#### Payment method properties

- **Customer locations**

  EU

- **Presentment currencies**

  EUR

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Buy Now, Pay Later

- **Recurring payments**

  No

- **Payout timing**

  Standard

- **Connect support**

  No

- **Dispute support**

  [ Yes ](https://docs.stripe.com/payments/scalapay.md#disputed-payments)

- **Manual capture support**

  [ Yes ](https://docs.stripe.com/payments/scalapay/accept-a-payment.md)

- **Refunds / Partial refunds**

  [ Yes ](https://docs.stripe.com/payments/scalapay.md#refunds) / [ Yes ](https://docs.stripe.com/payments/scalapay.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept Scalapay payments that settle in a [supported currency](https://docs.stripe.com/payments/scalapay.md#supported-currencies).

- AT
- AU
- BE
- CA
- CH
- CZ
- DE
- DK
- ES
- FI
- FR
- GB
- GR
- HU
- IE
- IT
- LT
- LU
- NL
- NO
- PL
- PT
- RO
- SE
- SG
- SI
- SK
- US

#### Product support

- Payment Links
- Checkout1
- Elements2

1Not supported when using Checkout in subscription mode or setup mode.

2Express Checkout Element doesn’t support Scalapay.

## Payment flow

Below is a demonstration of the Scalapay payment flow from your checkout page:
![](https://d37ugbyn3rpeym.cloudfront.net/videos/scalapay_demo_video.mp4)

## Get started

You don’t have to integrate Scalapay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Scalapay. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Scalapay from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)

If your integration requires manually listing payment methods, learn how to [ configure Scalapay](https://docs.stripe.com/payments/scalapay/accept-a-payment.md).

## Payment options

The minimum charge limit is 5,00 EUR or the equivalent for other supported currencies.

The maximum charge limit is 4,999,99 EUR or the equivalent for other supported currencies.

## Allowed business categories

The following business categories are the only ones allowed to use Scalapay:

- Other categories at the discretion of Scalapay

## Disputes

Scalapay has a claims process that allows transaction disputes. Customers can open disputes for cases of suspected fraud, double payments, or a difference between an order and a transaction amount.

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to receive [webhooks](https://docs.stripe.com/webhooks.md))

Stripe holds back the disputed amount from your balance until Scalapay resolves the dispute.

We request that you upload compelling evidence proving that you fulfilled the purchase order [using the Stripe Dashboard](https://docs.stripe.com/disputes/responding.md#respond). This evidence can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or proof of receipt
- Record of refund (for purchase you’ve already refunded)

To handle disputes programmatically, [respond to disputes using the API](https://docs.stripe.com/disputes/api.md).

This information helps Scalapay determine if a dispute is valid. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 12 calendar days. If Scalapay resolves the dispute with you winning, we return the disputed amount to your Stripe balance. If Scalapay rules in favor of the customer, the disputed amount stays with the customer.

## Refunds

Scalapay supports full and partial refunds.

- The refund period is up to 90 days after the purchase.
- Refunds for Scalapay payments are asynchronous and take up to 5 minutes to complete.

Stripe notifies you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. If a refund fails (the `Refund` object’s status transitions to `failed`), then we return the amount to your Stripe balance, and you must arrange an alternative way of providing your customer with a refund.

## Supported currencies

You can create Scalapay payments in the currencies that map to your country. The default local currency for Scalapay is `eur`.

- eur: AT, BE, CZ, DE, DK, ES, FI, FR, GR, HU, IE, IT, LT, LU, NL, NO, PL, PT, RO, SE, SI, SK
- eur: US
- eur: CH
- eur: GB
- eur: SG
- eur: AU
- eur: CA
