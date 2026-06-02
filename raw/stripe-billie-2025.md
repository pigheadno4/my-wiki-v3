<!-- Source URL: https://docs.stripe.com/payments/billie -->
<!-- Fetched: 2026-05-06 -->

# Billie payments

Offer businesses "Pay in 30" payment terms while getting paid instantly.

[Billie](https://billie.io/) is a Buy Now, Pay Later payment method available to businesses in Germany, France, Netherlands, Sweden, Norway, Finland, Austria, Spain, Denmark, Switzerland, and the UK that gives your customers payment flexibility.

If customers select Billie as their payment method, Stripe redirects them to Billie’s website, where they’re granted the ability to pay in 30 days. You receive total payment immediately.

#### Payment method properties

- **Customer locations**

  EU, UK

- **Presentment currencies**

  EUR, SEK, NOK, DKK, GBP, CHF

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Buy Now, Pay Later

- **Recurring payments**

  No

- **Payout timing**

  Standard

- **Connect support**

  Yes

- **Dispute support**

  [ Yes ](https://docs.stripe.com/payments/billie.md#disputed-payments)

- **Manual capture support**

  [ Yes ](https://docs.stripe.com/payments/billie/accept-a-payment.md)

- **Refunds / Partial refunds**

  [ Yes ](https://docs.stripe.com/payments/billie.md#refunds) / [ Yes ](https://docs.stripe.com/payments/billie.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept Billie payments that settle in a [supported currency](https://docs.stripe.com/payments/billie.md#supported-currencies).

- AT
- CH
- DE
- DK
- ES
- FI
- FR
- GB
- NL
- NO
- SE

#### Product support

- Connect
- Payment Links
- Checkout1
- Elements2

1Not supported when using Checkout in subscription mode or setup mode.

2Express Checkout Element doesn’t support Billie.

## Payment flow

Below is a demonstration of the Billie payment flow from your checkout page:
![](https://docs.stripecdn.com/913aa3a2b56d1491d16350f9040b157c3ce5175a1e14850c0f348bc644a51bdf.mp4)

## Get started

You don’t have to integrate Billie and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Billie. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

> #### Unified line items
>
> To maximize approval rates when you integrate with Billie, include `line_items` data to represent what’s in a shopper’s cart. For early access, see [Payments line items](https://docs.stripe.com/payments/payment-line-items.md).

### Other payment products

The following Stripe products also let you add Billie from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)

If your integration requires manually listing payment methods, learn how to [ configure Billie](https://docs.stripe.com/payments/billie/accept-a-payment.md).

## Payment options

The minimum charge limit is 0,01 EUR or the equivalent for other supported currencies.

## Prohibited and restricted business categories

In addition to the categories of goods or services sold and businesses [restricted from using Stripe overall](https://stripe.com/restricted-businesses), the following categories are prohibited from using Billie:

- Betting/Casino Gambling
- Country Clubs
- Adult Content and Services
- Financial Institutions
- General Services
- Cryptocurrency exchanges and wallets
- Postal Services - Government Only
- Precious Stones and Metals, Watches and Jewelry
- Other categories at the discretion of Billie

## Disputes

Billie has a claims process that allows transaction disputes. Customers can open disputes for cases of suspected fraud, double payments, or a difference between an order and a transaction amount.

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to receive [webhooks](https://docs.stripe.com/webhooks.md))

Stripe holds back the disputed amount from your balance until Billie resolves the dispute.

We request that you upload compelling evidence proving that you fulfilled the purchase order [using the Stripe Dashboard](https://docs.stripe.com/disputes/responding.md#respond). This evidence can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or proof of receipt
- Record of refund (for purchase you’ve already refunded)

To handle disputes programmatically, [respond to disputes using the API](https://docs.stripe.com/disputes/api.md).

This information helps Billie determine if a dispute is valid. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 12 calendar days. If Billie resolves the dispute with you winning, we return the disputed amount to your Stripe balance. If Billie rules in favor of the customer, the disputed amount stays with the customer.

## Refunds

Billie supports full and partial refunds.

- The refund period is up to 180 days after the purchase.
- Refunds for Billie payments are asynchronous and take up to 5 minutes to complete.

Stripe notifies you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. If a refund fails (the `Refund` object’s status transitions to `failed`), then we return the amount to your Stripe balance, and you must arrange an alternative way of providing your customer with a refund.

## Connect

If you use *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), you must consider the following before you enable and use Billie.

### Request Billie capabilities for your connected accounts

Set the `billie_payments` capability to `active` on your platform account, and on any connected accounts you want to enable Billie for. You can also [request more account capabilities](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting).

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

You can create Billie payments in the currencies that map to your country. The default local currency for Billie is `eur`.

- eur: DE, FR, NL, SE, NO, FI, AT, ES, DK
- sek: DE, FR, NL, SE, NO, FI, AT, ES, DK
- nok: DE, FR, NL, SE, NO, FI, AT, ES, DK
- dkk: DE, FR, NL, SE, NO, FI, AT, ES, DK
- gbp: GB
- chf: CH
