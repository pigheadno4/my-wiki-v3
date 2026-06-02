<!-- Source URL: https://docs.stripe.com/payments/eps -->
<!-- Fetched: 2026-05-03 -->

# EPS payments

Learn about EPS, a common payment method in Austria.

EPS is an Austria-based payment method that lets customers complete transactions online using their bank credentials. All Austrian banks support EPS, and most Austrian online retailers accept it.

For information on payment method transaction fees, refer to [pricing details](https://stripe.com/pricing/local-payment-methods#eps).

EPS redirects customers to their bank’s website to [authenticate a payment](https://docs.stripe.com/payments/payment-methods.md#customer-actions). You receive [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) about the success or failure of a payment.

#### Payment method properties

- **Customer locations**

  Austria

- **Presentment currency**

  EUR

- **Payment confirmation**

  Customer-authenticated

- **Payment method family**

  Authenticated bank debit

- **Recurring payments**

  No

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  Yes

- **Dispute support**

  [No](https://docs.stripe.com/payments/eps.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/eps.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept EPS payments:

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
- GI
- GR
- HK
- HR
- HU
- IE
- IT
- JP
- LI
- LT
- LU
- LV
- MT
- MX
- NL
- NO
- NZ
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
- Checkout1

- Payment Links
- Invoicing2

- Elements3

1Not supported when using Checkout in subscription mode or setup mode.2Available by invite only.3Express Checkout Element doesn’t support EPS.

## Payment flow

![](assets/stripe-acss-debit-checkout-flow.svg)

Customer selects EPS at checkout
![](assets/stripe-eps-select-bank.svg)

Customer chooses their bank and is redirected to that bank’s login page
![](assets/stripe-bancontact-redirect.svg)

Customer enters account credentials
![](assets/stripe-eps-pincode-sms.svg)

Customer completes authorization process (with scanner or SMS)
![](assets/stripe-bancontact-redirect-success.svg)

Customer is notified that payment is complete
![](assets/stripe-acss-debit-success.svg)

(Optional) Customer returns back to the business’s site for payment confirmation

## Get started

You don’t have to integrate EPS and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable EPS. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add EPS from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)

If your integration requires manually listing payment methods, learn how to [manually configure EPS as a payment](https://docs.stripe.com/payments/eps/accept-a-payment.md).

## Disputes

The risk of fraud or unrecognized payments is low because the customer must authenticate the payment with their bank. As a result, you won’t have disputes that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

EPS payments can be refunded up to 180 days after the original payment date.
