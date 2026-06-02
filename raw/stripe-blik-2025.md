<!-- Source URL: https://docs.stripe.com/payments/blik -->
<!-- Fetched: 2026-05-03 -->

# BLIK payments

Learn about BLIK, a common payment method in Poland.

BLIK is a [single use](https://docs.stripe.com/payments/payment-methods.md#usage) payment method that requires customers to [authenticate](https://docs.stripe.com/payments/payment-methods.md#customer-actions) their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form.

The bank sends a push notification to your customer’s mobile phone asking to authorize the payment inside their banking application. The BLIK code is valid for 2 minutes; customers have 60 seconds to authorize the payment after starting a payment. After 60 seconds, it times out and they must request a new BLIK code. Customers typically approve BLIK payments in less than 10 seconds.

#### Payment method properties

- **Customer locations**

  Poland

- **Presentment currency**

  PLN

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Authenticated bank debit

- **Recurring payments**

  Yes (Private preview)

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  [Yes](https://docs.stripe.com/payments/blik.md#connect)

- **Dispute support**

  [Yes](https://docs.stripe.com/payments/blik.md#disputed-payments)

- **Manual capture support**

  No

- **Deferred intent support**

  Client-side confirmation only (Private preview)

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/blik.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept BLIK payments:

- AT
- AU
- BE
- BG
- CA
- CH
- CY
- CZ
- DE
- DK
- EE
- ES
- FI
- FR
- GB
- GR
- HR
- HU
- IE
- IS
- IT
- LI
- LT
- LU
- LV
- MT
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

- Connect
- Checkout
- Payment Links
- Elements1, 2

1 Express Checkout Element and Mobile Payment Element don’t support BLIK.2 Not supported when [collecting payment details before creating a PaymentIntent](https://docs.stripe.com/payments/accept-a-payment-deferred.md).

## Payment flow

![](assets/stripe-blik-flow-1-checkout.svg)

Customer selects BLIK at checkout.
![](assets/stripe-blik-flow-2-generate-code.svg)

Customer is directed to their mobile banking app to generate a 6-digit code.
![](assets/stripe-blik-flow-3-enter-code.svg)

Customer puts the code into the checkout.
![](assets/stripe-blik-flow-4-complete.svg)

Customer is notified that payment is complete.

## Get started

You don’t have to integrate BLIK and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable BLIK. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

If you prefer to manually list payment methods, learn how to [manually configure BLIK as a payment](https://docs.stripe.com/payments/blik/accept-a-payment.md).

To save BLIK for future recurring payments, see [Save BLIK details during a payment](https://docs.stripe.com/payments/blik/save-during-payment.md) or [Set up future BLIK recurring payments](https://docs.stripe.com/payments/blik/set-up-payment.md).

## Disputes

BLIK has a claims process that allows transaction disputes. Customers can open disputes for cases of suspected fraud, double payments, or a difference between an order and a transaction amount.

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to receive [webhooks](https://docs.stripe.com/webhooks.md))

Stripe holds back the disputed amount from your balance until BLIK resolves the dispute.

We request that you upload compelling evidence proving that you fulfilled the purchase order [using the Stripe Dashboard](https://docs.stripe.com/disputes/responding.md#respond). This evidence can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or proof of receipt
- Record of refund (for purchase you’ve already refunded)

To handle disputes programmatically, [respond to disputes using the API](https://docs.stripe.com/disputes/api.md).

This information helps BLIK determine if a dispute is valid. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 12 calendar days. If BLIK resolves the dispute with you winning, we return the disputed amount to your Stripe balance. If BLIK rules in favor of the customer, the balance charge becomes permanent.

## Refunds

BLIK supports full and partial refunds. Depending on the bank, refunds are processed immediately or within a couple of hours.

## Connect

If you use *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), you must consider the following before you enable and use BLIK.

### Request BLIK capabilities for your connected accounts

Set the `blik_payments` capability to `active` on your platform account, and on any connected accounts you want to enable BLIK for. You can also [request more account capabilities](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the default statement descriptor and the merchant name that appears on the customer’s banking application and confirmation emails.

| Charge type                                        | Descriptor taken from |
| -------------------------------------------------- | --------------------- |
| Direct                                             | Connected Account     |
| Destination                                        | Platform              |
| Separate charge and transfer                       | Platform              |
| Destination (with `on_behalf_of`)                  | Connected Account     |
| Separate charge and transfer (with `on_behalf_of`) | Connected Account     |
