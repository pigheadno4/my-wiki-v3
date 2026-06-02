<!-- Source URL: https://docs.stripe.com/payments/countries/nigeria -->
<!-- Fetched: 2026-05-08 -->

# Nigerian payment methods

Accept Nigerian local payment methods without a local entity.

You can accept payments from most payment methods available in Nigeria by using our merchant of record solution through our Nigerian partner. You don’t need a local Nigerian entity, and the partner provides a localized checkout flow.

Nigerian customers typically pay using local cards, bank transfers, wallets, and USSD. You can accept a selection of local wallets and cards by offering your services through our Nigerian merchant of record.

## Payment flow

After the customer enters their information in Stripe’s checkout page, clicking **Pay** redirects them to the checkout page of the merchant of record service provider and their local processor. They complete the payment there.

## Available payment methods

You can accept the following local payment methods:

- [Naira card](https://docs.stripe.com/payments/ng-card/accept-a-payment.md)
- [Naira bank transfer](https://docs.stripe.com/payments/ng-bank-transfer/accept-a-payment.md)

> #### Nigerian VAT
>
> When the merchant of record services provider processes local transactions in Nigeria, it remits buyer VAT. Accordingly, for Nigerian buyers, include VAT in your presentment pricing. For more information, see the [full merchant of record services terms](<https://d37ugbyn3rpeym.cloudfront.net/docs/GSSL%20-%20Buyer%20T&Cs%20(Final).pdf>).

#### Payment method properties

- **Customer locations**

  Nigeria

- **Presentment currency**

  NGN

- **Payment confirmation**

  Customer-authenticated

- **Payment method family**

  Countries

- **Recurring payments**

  Yes

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  Yes

- **Dispute support**

  No

- **Manual capture support**

  Yes

- **Refunds / Partial refunds**

  Yes / Yes

#### Business locations

Stripe accounts in the following countries can accept Naira payments with USD settlement.

- US

## Get started

You don’t have to integrate Naira payment methods and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Naira payment methods. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Naira payment methods from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)

### Integrate through the API

You can also use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) to enable Naira payment methods, as detailed in the table below. To test your integration’s redirect-handling logic, follow our guide to [simulate a payment that uses a redirect flow](https://docs.stripe.com/testing.md#redirects).

## Payment process

Customers who elect to pay with Naira payment methods are redirected to a localized checkout experience provided by the local merchant of record service provider and their processor partner. After they [authorize the transaction](https://docs.stripe.com/payments/payment-methods.md#customer-actions) and the payment is approved, funds are available in your Stripe account after 3 days.

## Payment methods

We support the following local Naira payment methods:

|                                                                                              | One-time    | Recurring   |
| -------------------------------------------------------------------------------------------- | ----------- | ----------- |
| [Naira cards](https://docs.stripe.com/payments/ng-card/accept-a-payment.md)                  | Yes         | Yes         |
| [Naira bank transfer](https://docs.stripe.com/payments/ng-bank-transfer/accept-a-payment.md) | Yes         | Coming soon |
| Naira wallet                                                                                 | Coming soon | No          |

## Refunds

Payments made with Nigerian payment methods can only be submitted for refund within 365 calendar days from the date of the original charge. After 365 days, it’s no longer possible to refund the charge.

For some Nigerian payment method transactions, refunds can take up to 7 calendar days from the purchase date to return a status.

## Disputes

With Nigerian payment methods, you can’t challenge buyer-initiated disputes. If Stripe is notified that the relevant payment service providers have accepted a request to return customer funds, Stripe immediately removes the funds from your Stripe account. To resolve the situation, you must contact your customer directly.
