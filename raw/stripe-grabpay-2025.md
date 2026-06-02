<!-- Source URL: https://docs.stripe.com/payments/grabpay -->
<!-- Fetched: 2026-05-07 -->

# GrabPay payments

Learn about GrabPay, a common payment method in Southeast Asia.

GrabPay is a payment method developed by [Grab](https://www.grab.com/sg/pay/). GrabPay is a digital wallet. Customers maintain a balance in their wallets that they pay out with.

To pay with GrabPay, customers are redirected to GrabPay’s website, where they have to authenticate the transaction using a one-time password. After authenticating, customers are redirected back to your website.

#### Payment method properties

- **Customer locations**

  Singapore, Malaysia

- **Presentment currency**

  SGD, MYR

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Wallet

- **Recurring payments**

  No

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  Yes

- **Dispute support**

  [No](https://docs.stripe.com/payments/grabpay.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/grabpay.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept GrabPay payments:

- MY
- SG

#### Product support

- Connect
- Checkout1

- Payment Links
- Elements2

- Invoicing

1Not supported when using Checkout in subscription mode or setup mode.2Express Checkout Element doesn’t support GrabPay.

## Payment flow

Below is a demonstration of the GrabPay payment flow from your checkout page:
![](https://d37ugbyn3rpeym.cloudfront.net/videos/grabpay_payment_demo.mp4)

## Get started

You don’t have to integrate GrabPay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable GrabPay. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add GrabPay from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)

If your integration requires manually listing payment methods, learn how to [manually configure GrabPay as a payment](https://docs.stripe.com/payments/grabpay/accept-a-payment.md).

Check out the GrabPay [sample on GitHub](https://github.com/stripe-samples/accept-a-payment).

## Refunds

GrabPay payments can be refunded up to 90 days after the original payment. Refunds for GrabPay payments are asynchronous and take up to 5 minutes to complete. We’ll notify you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. If a refund fails, the Refund object’s status transitions to `failed` and we return the amount to your Stripe balance. You then need to arrange an alternative way of providing your customer with a refund.

## Disputes

GrabPay payments have a low risk of fraud or unrecognized payments because the customer must authenticate the payment with Grab. Therefore, there is no dispute process that can result in a chargeback and funds being withdrawn from your Stripe account.

## Branding guidelines

Use the [branding guidelines](https://d37ugbyn3rpeym.cloudfront.net/docs/files/GrabPay_Online_Partners_Brand_Guidelines.pdf) provided by GrabPay when building your checkout page. Assets such as logos and buttons are available for download [as a zip file](https://d37ugbyn3rpeym.cloudfront.net/docs/files/GrabPay-Branding-Guidelines-with-Logos-and-Artworks.zip).
