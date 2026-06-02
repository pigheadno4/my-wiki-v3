<!-- Source URL: https://docs.stripe.com/payments/payment-on-invoice -->
<!-- Fetched: 2026-05-06 -->

# Payment on invoice

Learn how to offer payment on invoice, a buy now, pay later payment option that allows you to get paid up front.

Payment on invoice is a common way for customers to buy now and pay later in Germany. When you accept payments on invoice with Stripe, as soon as a payment is approved we add the full payment amount, minus fees, to your Stripe balance. We then send an invoice to your customer that reflects your branding. They must pay the invoice within 14 days.

To pay using payment on invoice, a buyer enters their details (including name, email, address, and date of birth). Using this data, a risk assessment is carried out and, if approved by the assessment, the payment is authorized on Stripe. The payment is then approved or declined based on the risk assessment result and you receive an [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) of the payment’s success or failure.

#### Payment method properties

- **Customer locations**

  Austria, Germany

- **Presentment currency**

  EUR

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Buy Now, Pay Later

- **Payout timing**

  [Standard payout timing](https://docs.stripe.com/payouts.md#payout-speed) applies (minimum T+2)

- **Notification timing**

  [Immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification)

- **Connect support**

  Yes

- **Recurring payments**

  No

- **Disputes**

  Yes

- **Refunds / Partial refunds**

  Yes / Yes

- **Manual capture**

  Yes

#### Business locations

Stripe accounts in the following countries can accept payment on invoice payments:

- DE
