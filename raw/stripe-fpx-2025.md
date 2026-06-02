<!-- Source URL: https://docs.stripe.com/payments/fpx -->
<!-- Fetched: 2026-05-03 -->

# FPX payments

Learn about FPX, a common payment method in Malaysia.

Financial Process Exchange (FPX) is a Malaysia-based payment method that allows customers to complete transactions online using their bank credentials. Bank Negara Malaysia (BNM), the Central Bank of Malaysia, and 11 other major Malaysian financial institutions are members of the PayNet Group, which owns and operates FPX. It’s one of the most popular online payment methods in Malaysia, with nearly 90 million transactions in 2018 according to BNM.

To pay with FPX, customers are redirected to their online banking environment where they have to perform two-step authorization. The exact payment flow varies depending on the customer’s bank. The FPX payment flow is well understood and intuitive to Malaysian customers.

As part of being regulatory compliant, Stripe requires businesses to provide their Business Registration Number (BRN) to process FPX charges and receive payouts.

#### Payment method properties

- **Customer locations**

  Malaysia

- **Presentment currency**

  MYR

- **Payment confirmation**

  Customer-authenticated

- **Payment method family**

  Authenticated bank debit

- **Recurring payments**

  No

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/fpx.md#refunds)

- **Dispute support**

  [No](https://docs.stripe.com/payments/fpx.md#disputed-payments)

- **Manual capture support**

  No

- **Connect support**

  Yes

- **Payout timing**

  5 business days

#### Business locations

Stripe accounts in the following countries can accept FPX payments:

- MY

#### Product support

- Connect
- Checkout1

- Payment Links
- Invoicing
- Elements2

1Not supported when using Checkout in subscription mode or setup mode.2Express Checkout Element doesn’t support FPX.

## Payment flow

[Watch a video](#payment-flow-video)
![](https://d37ugbyn3rpeym.cloudfront.net/videos/apms/fpx.mp4)![](assets/stripe-acss-debit-checkout-flow.svg)

Customer selects FPX at checkout
![](assets/stripe-eps-select-bank.svg)

Chooses bank and gets redirected
![](assets/stripe-bancontact-redirect.svg)

Customer enters account credentials
![](assets/stripe-eps-pincode-sms.svg)

Customer completes authorization process
![](assets/stripe-bancontact-redirect-success.svg)

Customer gets notification that payment is complete
![](assets/stripe-acss-debit-success.svg)

(Optional) Customer returns back to business’s site for payment confirmation

## Get started

You don’t have to integrate FPX and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable FPX. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add FPX from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)

If your integration requires manually listing payment methods, learn how to [manually configure FPX as a payment](https://docs.stripe.com/payments/fpx/accept-a-payment.md).

Check out the FPX [sample on GitHub](https://github.com/stripe-samples/accept-a-payment).

## Disputes

The risk of fraud or unrecognized payments is low because the customer must authenticate the payment with their bank. As a result, you won’t have disputes that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

FPX payments can be refunded up to 60 days after the original payment. Refunds for FPX payments are asynchronous and take approximately 1 week to complete. We’ll notify you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. A refund can fail if the customer’s bank is unable to process it correctly (for example, the bank account is closed). In the rare instance that a refund fails, the Refund object’s status transitions to `failed` and we return the amount to your Stripe balance. You then need to arrange an alternative way of providing your customer with a refund.
