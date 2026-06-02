<!-- Source URL: https://docs.stripe.com/payments/upi -->
<!-- Fetched: 2026-05-06 -->

# UPI payments

Learn about UPI, a common payment method in India.

UPI is a real-time payment system developed by the National Payments Corporation of India. UPI works by instantly transferring funds between two bank accounts.

Customers use their preferred banking or wallet app to authenticate and approve payments. On desktop, customers scan a QR code using their UPI app. On mobile, customers are redirected to their UPI app to complete the payment.

UPI supports both one-time payments and recurring payments through e-mandates (also known as UPI AutoPay). For recurring payments, customers authorize a mandate in their UPI app, which allows you to charge them automatically for future payments within the mandate terms.

#### Payment method properties

- **Customer locations**

  India

- **Presentment currency**

  INR

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Real-time payments

- **Recurring payments**

  Yes

- **Payout timing**

  [Standard payout timing](https://docs.stripe.com/payouts.md#payout-speed) applies

- **Connect support**

  Yes

- **Refunds / Partial refunds**

  Yes / yes

- **Dispute support**

  Yes

- **Manual capture support**

  No

#### Business locations

Stripe accounts in the following countries can accept UPI payments:

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

## Get started

You don’t have to integrate UPI and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable UPI. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add UPI from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)

If you prefer to manually list payment methods, learn how to [manually configure UPI as a payment](https://docs.stripe.com/payments/upi/accept-a-payment.md).

## Refunds

You can refund UPI payments up to 60 days after the original payment. Refunds are asynchronous and can take up to 7 business days to complete. Stripe notifies you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. In the rare instance that a refund fails, the Refund object’s status transitions to `failed` and Stripe returns the amount to your Stripe balance. You’ll need to arrange an alternative way to refund your customer.

## Disputes

The risk of fraud or unrecognized payments is low because the customer must authenticate the payment with their bank. However, the customer might dispute a UPI transaction with their bank or PSP. For example, they might dispute the payment when their bank account is debited for a failed transaction, or after a failure to receive goods and services. If their bank or PSP accepts the request to return funds, you can’t contest the dispute and Stripe immediately removes funds from your Stripe account.

## Transaction limits

UPI payments must be between 1 INR and 100,000 INR. Recurring payments are limited to a maximum of 15,000 INR.
