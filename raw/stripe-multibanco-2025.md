<!-- Source URL: https://docs.stripe.com/payments/multibanco -->
<!-- Fetched: 2026-05-07 -->

# Multibanco payments

Learn how to accept payments with Multibanco.

Multibanco is a voucher-based payment method in Portugal. If your business is based in Europe or the United States, you can accept Multibanco payments from customers in Portugal using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md).

To complete a transaction, customers receive a voucher that includes Multibanco entity and reference numbers. Customers use these voucher details to make a payment outside your checkout flow through online banking or from an ATM.

For information on payment method transaction fees, refer to [pricing details](https://stripe.com/pricing/local-payment-methods#multibanco).

Payment confirmation might be delayed by several days due to the initiation of a bank transfer when a customer pays for a Multibanco voucher. Bank transfers can encounter delays, particularly over weekends, contributing to the delay in payment confirmation.

#### Payment method properties

- **Customer locations**

  Portugal

- **Presentment currency**

  EUR

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Voucher

- **Recurring payments**

  No

- **Payout timing**

  [Standard payout timing](https://docs.stripe.com/payouts.md#payout-speed) applies

- **Refunds / partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/multibanco.md#refunds)

- **Connect support**

  [Yes](https://docs.stripe.com/payments/multibanco.md#connect)

- **Dispute support**

  [No](https://docs.stripe.com/payments/multibanco.md#disputes)

- **Manual capture support**

  No

- **Minimum charge amount**

  0.50 EUR

- **Maximum charge amount**

  99,999 EUR

#### Business locations

Stripe accounts in the following countries can accept Multibanco payments:

- AT
- BE
- BG
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
- GI
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
- SI
- SK
- US

#### Product support

- Connect
- Checkout
- Payment Links
- Elements1

- Subscriptions2

- Invoicing2

1Express Checkout Element doesn’t support Multibanco.2Invoices and Subscriptions only support the [send_invoice](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method) collection method.

## Payment flows

### Online banking flow

![](assets/stripe-multibanco-flow-checkout.svg)

Selects Multibanco at checkout
![](assets/stripe-multibanco-flow-show-details.svg)

Receives voucher details (incl. entity, reference, and amount)
![](assets/stripe-multibanco-flow-redirect.svg)

Logs into online banking
![](assets/stripe-multibanco-flow-bank-pincode.svg)

Uses voucher details to complete the payment with online banking
![](assets/stripe-multibanco-flow-redirect-success.svg)

Receives confirmation of funds sent

### ATM flow

![](assets/stripe-multibanco-flow-checkout.svg)

Selects Multibanco at checkout
![](assets/stripe-multibanco-flow-show-details.svg)

Receives voucher details (incl. entity, reference, and amount)
![](assets/stripe-multibanco-flow-atm.svg)

Uses voucher details to complete the payment at an ATM
![](assets/stripe-multibanco-flow-atm-success.svg)

Receives confirmation of funds sent

## Get started

You don’t have to integrate Multibanco and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Multibanco. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Multibanco from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)

If you prefer to manually list payment methods, learn how to [manually configure Multibanco as a payment method](https://docs.stripe.com/payments/multibanco/accept-a-payment.md).

## Disputes

The risk of fraud or unrecognized payments is low with Multibanco because the customer must push funds from their bank account. As a result, there’s no dispute process that can result in a chargeback and funds withdrawn from your Stripe account.

## Refunds

You can refund Multibanco payments in the [Dashboard](https://dashboard.stripe.com/payments) or using the [Refunds API](https://docs.stripe.com/api/refunds.md).

The refund period for Multibanco is up to 365 days after the original payment. Full and partial refunds are supported. Customers typically receive refunds in their bank accounts within 1 day. However, this time frame varies by bank.

If a Multibanco [Refund](https://docs.stripe.com/api/refunds/object.md) object’s `status` transitions to `succeeded`, the [destination_details.multibanco.reference](https://docs.stripe.com/api/refunds/object.md#refund_object-destination_details-multibanco-reference) property contains a refund identifier that you can provide the customer.

## Billing

Use [Stripe Billing](https://stripe.com/billing) to create Multibanco supported *invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) and *subscriptions* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis). Multibanco invoices and subscriptions only support the `send_invoice` [collection method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method).

## Connect

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with Multibanco to process payments on behalf of a connected account. Connect users can use Multibanco with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

### Enable Multibanco for connected accounts that use the Stripe Dashboard

Connected accounts that use the Stripe Dashboard can enable Multibanco in their [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard.

### Enable Multibanco for connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe

Request the `multibanco_payments` capability on any connected account you want to enable Multibanco for. Follow the instructions to [enable payment methods for your connected accounts](https://docs.stripe.com/connect/account-capabilities.md).
