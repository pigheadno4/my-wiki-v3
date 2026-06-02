<!-- Source URL: https://docs.stripe.com/payments/satispay -->
<!-- Fetched: 2026-05-08 -->

# Satispay payments

Learn how to accept payments with Satispay, a digital wallet popular with Italian customers.

[Satispay](https://satispay.com/) is a stored value wallet payment method available to merchants on Stripe. When customers select Satispay as their payment method, Stripe redirects them to Satispay’s website to finish the transaction. You’re paid immediately.

#### Payment method properties

- **Customer locations**

  Italy

- **Presentment currencies**

  EUR

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Wallets

- **Recurring payments**

  No

- **Payout timing**

  Standard

- **Connect support**

  Yes

- **Dispute support**

  [ Yes ](https://docs.stripe.com/payments/satispay.md#disputed-payments)

- **Manual capture support**

  [ Yes ](https://docs.stripe.com/payments/satispay/accept-a-payment.md)

- **Refunds / Partial refunds**

  [ Yes ](https://docs.stripe.com/payments/satispay.md#refunds) / [ Yes ](https://docs.stripe.com/payments/satispay.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept Satispay payments that settle in a [supported currency](https://docs.stripe.com/payments/satispay.md#supported-currencies).

- AT
- BE
- CY
- DE
- EE
- ES
- FI
- FR
- GR
- HR
- IE
- IT
- LT
- LU
- LV
- MT
- NL
- PT
- SI
- SK

#### Product support

- Connect
- Payment Links
- Checkout
- Elements2

2Express Checkout Element doesn’t support Satispay.

## Payment flow

Below is a demonstration of the Satispay payment flow from your checkout page:
![](assets/stripe-satispay-flow.mp4)

## Get started

You don’t have to integrate Satispay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Satispay. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Satispay from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)

If your integration requires manually listing payment methods, learn how to [ configure Satispay](https://docs.stripe.com/payments/satispay/accept-a-payment.md).

## Prohibited and restricted business categories

In addition to the categories of goods or services sold and businesses [restricted from using Stripe overall](https://stripe.com/restricted-businesses), the following categories are prohibited from using Satispay:

- Automobile Associations
- Betting/Casino Gambling
- Counseling Services
- Credit Reporting Agencies
- Detective Agencies
- Direct Marketing - Catalog Merchant
- Direct Marketing - Outbound Telemarketing
- Door-To-Door Sales
- Employment/Temp Agencies
- Financial Institutions
- Cryptocurrency exchanges and wallets
- Pawn Shops
- Security Brokers/Dealers
- Other categories at the discretion of Satispay

## Disputes

Satispay has a claims process that allows transaction disputes. Customers can open disputes for cases of suspected fraud, double payments, or a difference between an order and a transaction amount.

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to receive [webhooks](https://docs.stripe.com/webhooks.md))

Stripe holds back the disputed amount from your balance until Satispay resolves the dispute.

We request that you upload compelling evidence proving that you fulfilled the purchase order [using the Stripe Dashboard](https://docs.stripe.com/disputes/responding.md#respond). This evidence can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or proof of receipt
- Record of refund (for purchase you’ve already refunded)

To handle disputes programmatically, [respond to disputes using the API](https://docs.stripe.com/disputes/api.md).

This information helps Satispay determine if a dispute is valid. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 12 calendar days. If Satispay resolves the dispute with you winning, we return the disputed amount to your Stripe balance. If Satispay rules in favor of the customer, the disputed amount stays with the customer.

## Refunds

Satispay supports full and partial refunds.

- The refund period is up to 180 days after the purchase.
- Refunds for Satispay payments are asynchronous and take up to 5 minutes to complete.

Stripe notifies you of the final refund status using the `refund.updated` or `refund.failed` _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. If a refund fails (the `Refund` object’s status transitions to `failed`), then we return the amount to your Stripe balance, and you must arrange an alternative way of providing your customer with a refund.

## Connect

If you use _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), you must consider the following before you enable and use Satispay.

### Request Satispay capabilities for your connected accounts

Set the `satispay_payments` capability to `active` on your platform account, and on any connected accounts you want to enable Satispay for. You can also [request more account capabilities](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the default statement descriptor and the merchant name that appears on the customer’s banking application and confirmation emails.

| Charge type                                        | Descriptor taken from |
| -------------------------------------------------- | --------------------- |
| Direct                                             | Connected account     |
| Destination                                        | Platform              |
| Separate charge and transfer                       | Platform              |
| Destination (with `on_behalf_of`)                  | Connected account     |
| Separate charge and transfer (with `on_behalf_of`) | Connected account     |

To check or update your statement descriptor, go to your [account settings](https://docs.stripe.com/get-started/account/statement-descriptors.md). For Connect integrations, see [setting statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

## Supported currencies

You can create Satispay payments in the currencies that map to your country. The default local currency for Satispay is `eur`.

- eur: AT, BE, CY, DE, EE, ES, FI, FR, GR, HR, IE, IT, LT, LU, LV, MT, NL, PT, SI, SK
