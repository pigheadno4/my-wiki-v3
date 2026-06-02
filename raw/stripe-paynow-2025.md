<!-- Source URL: https://docs.stripe.com/payments/paynow -->
<!-- Fetched: 2026-05-06 -->

# PayNow payments

Learn about PayNow, a popular payment method in Singapore.

PayNow is a Singapore based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions.

Customers see a QR code when checking out with PayNow. They complete the payment by scanning it using [a participating app](https://www.abs.org.sg/consumer-banking/pay-now). You receive confirmation from Stripe instantly when they complete the payment.

#### Payment method properties

- **Customer locations**

  Singapore

- **Presentment currency**

  SGD

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Real-time payments

- **Billing support**

  [Yes](https://docs.stripe.com/payments/paynow.md#billing)

- **Payout timing**

  T+1 availability

- **Connect support**

  Yes

- **Dispute support**

  [Not applicable](https://docs.stripe.com/payments/paynow.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/paynow.md#refunds)

- **Pricing**

  1.3%

#### Business locations

Stripe accounts in the following countries can accept PayNow payments:

- SG

#### Product support

- Connect
- Checkout1

- Payment Links
- Elements2

- Subscriptions3

- Invoicing3

- Terminal

1Not supported when using Checkout in subscription mode or setup mode.2Express Checkout Element doesn’t support PayNow.3Invoices and Subscriptions only support the [send_invoice](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method) collection method.

## Get started

You don’t have to integrate PayNow and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable PayNow. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add PayNow from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)

If your integration requires manually listing payment methods, learn how to [manually configure PayNow as a payment](https://docs.stripe.com/payments/paynow/accept-a-payment.md). To [accept in-person PayNow payments](https://docs.stripe.com/terminal/payments/additional-payment-methods.md), you need to manually list PayNow.

## Refunds

You can refund PayNow payments up to 90 days after the original payment. Refunds for PayNow payments are asynchronous and Stripe notifies you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the status of the [Refund](https://docs.stripe.com/api/refunds/object.md) object transitions to `succeeded`.

If a refund fails, the status of the Refund object transitions to `failed` and Stripe returns the amount to your Stripe balance. At this point, you need to arrange an alternative way of providing your customer with a refund.

## QR code expiration

PayNow QR codes are valid for 1 hour after they’re generated. If a customer doesn’t authenticate the payment within 1 hour, the QR code expires and any payment attempts using that QR code fail with the error code `payment_intent_payment_attempt_expired`.

Set up a webhook to bring the customer back to the payment page again after the QR code expires. The customer must initiate a new payment session, which creates a new PaymentIntent and generates a new QR code.

## Statement descriptors

Customized statement descriptors aren’t supported by PayNow, the value specified in the [statement_descriptor](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-statement_descriptor) is ignored. Stripe’s company name (`STRIPE PAYMENTS SINGAPORE PTE. LTD.`) is shown when your customers complete payments on their mobile app. It’s also shown on bank statements along with the amount and a Stripe-generated reference code.

## Repeated payments

To prevent your customers from being charged multiple times, after your customer successfully completes a transaction, any subsequent attempts to pay using the same QR code are rejected. The rejection behavior depends on the bank and payment app used by the customer to attempt the transaction. If your customers contact you about repeated payments, you can advise them to check for text messages or notifications from their bank or payment app, which will show that the payment attempt was rejected.

## Billing

Use [Stripe Billing](https://stripe.com/billing) to create PayNow supported *subscriptions* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) and *invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice).

PayNow payments don’t support [automatically charging](https://docs.stripe.com/invoicing/automatic-charging.md) invoices. You need to configure invoices and subscriptions with `send_invoice` [collection_method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method).

## Payout timing

By default, it takes 1 day from the time of the transaction for the funds to be available in your Stripe balance. Stripe pays out available funds to your bank account according to the payout schedule set on your Stripe account.

For example, if the payment was made on Wednesday, the funds are available in your Stripe balance on Thursday. If you’re on an automatic daily payout schedule, the funds are paid out on Thursday. If you’re on a weekly (Monday) payout schedule, the funds are paid out on the coming Monday.

## Disputes

PayNow payments have a low risk of fraud or unrecognized payments because the customer must authenticate the payment through participating apps. As a result, there’s no dispute process that can result in a chargeback and funds being withdrawn from your Stripe account.

## Prohibited business categories

In addition to the categories of [businesses restricted from using Stripe overall](https://stripe.com/restricted-businesses), the following categories are specifically prohibited from using PayNow:

- Petroleum and Petroleum Products
- Fuel Dealers
- Service Stations
- Automated Fuel Dispensers

## Connect

You can use [Stripe Connect](https://docs.stripe.com/connect.md) with PayNow to process payments on behalf of a connected account. *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) users can use PayNow with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate Charges and Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

### Request PayNow capability

You must turn on the PayNow payment method in [your platform settings](https://dashboard.stripe.com/settings/payment_methods) and [request](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting) the `paynow_payments` capability for your connected accounts that will accept PayNow payments.

### Set correct MCC

Stripe and PayNow rely on merchant category codes (MCC) to determine eligibility of the connected accounts against the PayNow [prohibited business categories](https://docs.stripe.com/payments/paynow.md#prohibited-business-categories). Make sure that you set [correct MCCs](https://docs.stripe.com/connect/setting-mcc.md) for your connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe.

### Merchant of record

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the merchant name that appears on PayNow’s website or app during the redirect. The merchant of record determines the Stripe account authorized to create payments with a particular [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md).
