<!-- Source URL: https://docs.stripe.com/payments/wero -->
<!-- Fetched: 2026-05-05 -->

# Wero payments

Learn about Wero, a pan-European payment method.

[Wero](https://wero-wallet.eu/) is a pan-European payment method that allows customers to make secure transactions on desktop and mobile devices. To perform a Wero payment, customers connect their bank accounts to their Wero wallet.

#### Payment method properties

- **Customer locations**

  Germany

- **Presentment currency**

  EUR

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Authenticated bank transfer

- **Recurring payments**

  No

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  Yes

- **Dispute support**

  No

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  Yes / Yes

#### Business locations

Stripe accounts in the following countries can accept Wero payments:

- AT
- BE
- BG
- CY
- CZ
- DE
- DK
- EE
- ES
- FI
- FR
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
- SI
- SK

#### Product support

- Connect
- Checkout1
- Payment Links
- Elements2

1Not supported when using Checkout in subscription mode or setup mode.2Express Checkout Element doesn’t support Wero.

To get in touch regarding a Wero integration, fill out the interest form below.

## Get started

You don’t have to integrate Wero and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Wero. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Wero from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)

If you prefer to manually list payment methods, learn how to [manually configure Wero as a payment](https://docs.stripe.com/payments/wero/accept-a-payment.md).

When you’re ready to go live, enable Wero on the [Payment Methods settings page](https://dashboard.stripe.com/settings/payment_methods).

## Payment flow

When customers choose Wero as their payment method, Stripe redirects them to Wero’s authentication page. On this page, customers scan a QR code to launch the Wero App on their phone, where they can approve the payment. The payment is processed instantly, typically completing in under 10 seconds, and the customer is redirected back to your site.

## Refunds

Wero supports full and partial refunds. You can refund Wero charges up to 2 years after the original payment. You can also issue multiple partial refunds up to the amount of the original charge.

## Transaction amount limits

The minimum payment amount for Wero is 0.50 EUR. The maximum payment amount varies by bank, but is usually determined by the customer’s bank limits.
