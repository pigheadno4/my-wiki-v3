<!-- Source URL: https://docs.stripe.com/payments/oxxo -->
<!-- Fetched: 2026-05-07 -->

# OXXO payments

Learn how to accept payments with OXXO.

OXXO is a Mexican chain of convenience stores in Latin America. OXXO allows customers to pay bills and pay for online purchases in-store with cash.

To complete a transaction, customers receive a voucher that includes a reference number for the transaction. Customers then bring their voucher to an OXXO store to make a cash payment. You’ll receive payment confirmation by the next business day along with the settled funds.

#### Payment method properties

- **Customer locations**

  Mexico

- **Presentment currency**

  MXN

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Cash-based payment method

- **Recurring payments**

  No

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  Yes

- **Dispute support**

  [No](https://docs.stripe.com/payments/oxxo.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [No / No](https://docs.stripe.com/payments/oxxo.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept OXXO payments:

- MX

#### Product support

- Connect
- Checkout1

- Payment Links
- Elements2

1Not supported when using Checkout in subscription mode or setup mode.2Express Checkout Element doesn’t support OXXO.

## Payment flow

![](assets/stripe-oxxo-flow-checkout.svg)

Step 1. Selects OXXO at checkout
![](assets/stripe-oxxo-flow-voucher.svg)

Step 2. Receives voucher with transaction reference
![](assets/stripe-oxxo-flow-store.svg)

Step 3. Provides voucher and cash payment at OXXO store
![](assets/stripe-oxxo-flow-success.svg)

Step 4. Receives notification that payment is complete

## Get started

You don’t have to integrate OXXO and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable OXXO. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

[Payment Links](https://docs.stripe.com/payment-links.md) also supports adding OXXO from the Dashboard.

If your integration requires manually listing payment methods, learn how to [manually configure OXXO as a payment](https://docs.stripe.com/payments/oxxo/accept-a-payment.md).

Check out the OXXO [sample on GitHub](https://github.com/stripe-samples/accept-a-payment).

## Disputes

OXXO payments have a low risk of fraud or unrecognized payments because the customer must provide cash payment in person at an OXXO convenience store. Customers can’t dispute OXXO payments.

## Refunds

OXXO payments can’t be refunded. Some businesses have created a separate process to credit their customers who reach out directly.

## Amount limits

The amount for a single OXXO must be at least 10.00 MXN and no more than 10,000.00 MXN.

## Unsupported businesses

Stripe can’t accept payments for certain types of businesses. In addition to the [Prohibited and Restricted Business list](https://stripe.com/restricted-businesses), Stripe doesn’t support Oxxo if your business falls into any of the following categories:

- Direct Marketing - Other
- Direct Marketing - Subscription
- Gift, Card, Novelty, and Souvenir Shops
- Service Stations
