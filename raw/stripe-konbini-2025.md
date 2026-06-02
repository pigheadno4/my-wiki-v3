<!-- Source URL: https://docs.stripe.com/payments/konbini -->
<!-- Fetched: 2026-05-07 -->

# Konbini payments

Learn how to accept payments at convenience stores with Konbini.

Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash.

To complete a transaction, customers receive payment codes for specific convenience stores along with a confirmation number. Customers then bring the information to a convenience store to make a cash payment. You’ll receive payment confirmation instantly, and funds will be available for *payout* (A payout is the transfer of funds to an external account, usually a bank account, in the form of a deposit) after 4 business days.

Customers can pay at FamilyMart, Lawson, Ministop, and Seicomart stores across Japan.

#### Payment method properties

- **Customer locations**

  Japan

- **Payment method family**

  Cash-based payment method

- **Connect support**

  Partial: [request an invite](https://support.stripe.com/contact/email?topic=payment_apis) to create charges [on behalf of](https://docs.stripe.com/connect/charges.md#on_behalf_of) other accounts.

- **Billing support**

  [Yes](https://docs.stripe.com/payments/konbini.md#billing)

- **Presentment currency**

  JPY

- **Dispute support**

  [No](https://docs.stripe.com/payments/konbini.md#disputed-payments)

- **Manual capture support**

  No

- **Payment confirmation**

  Customer-initiated

- **Payout timing**

  Standard payout timing applies

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/konbini.md#refunds)

- **Minimum charge amount**

  120 JPY

- **Maximum charge amount**

  300,000 JPY

#### Business locations

Stripe accounts in the following countries can accept Konbini payments:

- JP

#### Product support

- Connect1

- Checkout2

- Payment Links
- Elements3

- Subscriptions4

- Invoicing4

1Partial: [request an invite](https://support.stripe.com/contact/email?topic=payment_apis) to create charges [on behalf of](https://docs.stripe.com/connect/charges.md#on_behalf_of) other accounts.2Not supported when using Checkout in subscription mode or setup mode.3Express Checkout Element doesn’t support Konbini.4Invoices and Subscriptions only support the [send_invoice](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method) collection method.

## Payment flow

![](assets/stripe-konbini-flow-checkout.svg)

1. Selects Konbini at checkout
   ![](assets/stripe-konbini-flow-instructions.svg)

2. Receives payment codes and a confirmation number
   ![](assets/stripe-konbini-flow-store.svg)

3. Makes a cash payment with the appropriate payment code and confirmation number at a convenience store
   ![](assets/stripe-konbini-flow-success.svg)

4. Receives notification that payment is complete

## Get started

You don’t have to integrate Konbini and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Konbini. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Konbini from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)

If you prefer to manually list payment methods, learn how to [manually configure Konbini as a payment](https://docs.stripe.com/payments/konbini/accept-a-payment.md).

## Disputes

Konbini payments have a low risk of fraud or unrecognized payments because the customer must provide cash payment in person at a convenience store. Generally Konbini payments can’t be disputed by the customer. However, in some instances irregularities similar to disputes (by the convenience store) might occur, (for example, due to mishandling). In these cases, Stripe will need to reach out to you for next steps.

## Refunds

Konbini payments can be refunded either through the [Dashboard](https://dashboard.stripe.com/payments) or [API](https://docs.stripe.com/api.md#create_refund). To complete a refund, your customer must provide account information where funds should be returned to. Stripe automatically contacts the customer at the email address provided at time of PaymentIntent confirmation and requests this information from them, after which the refund is processed automatically.

## Billing

Use [Stripe Billing](https://stripe.com/billing) to create Konbini supported *subscriptions* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) and *invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice).

Due to the in-person nature of Konbini payments, [automatically charged](https://docs.stripe.com/invoicing/automatic-charging.md) invoices aren’t supported.

Invoices and subscriptions need to be configured with a [collection_method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method) of `send_invoice`.

## Prohibited business categories

On top of the categories of [businesses restricted from using Stripe overall](https://stripe.com/restricted-businesses), the following categories are specifically prohibited from using Konbini.

- Sole proprietors who have been doing business for less than 3 years
- Real Money Trading (RMT), that is, sale of virtual (in-game) characters, currency, and so on.
- Gambling
- Information selling, in particular:
  - Money making schemes
  - Investment related information
  - Gambling strategies for horse racing, pachinko, slot machines, and so on
- Multi-level marketing and pyramid schemes
- Gore content or products
- Unscientific and superstition-based content or products
- Prohibited medical products (per the Japanese Pharmaceutical Affairs Act)
- Content or products offensive to public order or moral
- Personal import facilitation (forwarding)
- Foreign money transfer
- Loans
- Dating sites
- E-cigarettes (vaping), waterpipes (shisha, hookah), and so on
- Fortune-telling

Our financial partner and convenience store chains might reject businesses at their discretion regardless of category.
