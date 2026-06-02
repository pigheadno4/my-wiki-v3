<!-- Source URL: https://docs.stripe.com/payments/bancontact -->
<!-- Fetched: 2026-05-03 -->

# Bancontact payments

Learn about Bancontact, a common payment method in Belgium.

Bancontact is a common online payment method in Belgium. Customers use a Bancontact card or mobile app linked to a Belgian bank account to make online payments.

For information on payment method transaction fees, refer to [pricing details](https://stripe.com/pricing/local-payment-methods#bancontact).

To pay with Bancontact, customers are redirected to the Bancontact website or mobile app to [authorize the payment](https://docs.stripe.com/payments/payment-methods.md#customer-actions) and then return to your website where there is [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) about the success or failure of the payment.

#### Payment method properties

- **Customer locations**

  Belgium

- **Presentment currency**

  EUR

- **Payment confirmation**

  Customer-authenticated

- **Payment method family**

  Authenticated bank-debit

- **Recurring payments**

  with [SEPA Direct Debit](https://docs.stripe.com/billing/subscriptions/bancontact.md)

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  Yes

- **Dispute support**

  [No](https://docs.stripe.com/payments/bancontact.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/bancontact.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept Bancontact payments:

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
- Checkout
- Payment Links
- Subscriptions
- Invoicing1

- Elements2

1Available by invite only.2Express Checkout Element doesn’t support SEPA Direct Debit.

## Payment flows

![](assets/stripe-acss-debit-checkout-flow.svg)

Customer selects Bancontact at checkout
![](assets/stripe-bancontact-redirect.svg)

Customer is redirected to Bancontact and enters credentials
![](assets/stripe-bancontact-redirect-success.svg)

Customer is notified that payment is complete
![](assets/stripe-acss-debit-success.svg)

(Optional) Customer returns back to business’s site for payment confirmation
![](assets/stripe-acss-debit-checkout-flow.svg)

Customer selects Bancontact at checkout
![](assets/stripe-bancontact-qr-redirect.svg)

Customer is redirected to Bancontact and scans QR code
![](assets/stripe-bancontact-mobile-pincode.svg)

Customer enters pincode
![](assets/stripe-bancontact-mobile-redirect.svg)

Customer is notified that payment is complete
![](assets/stripe-acss-debit-success.svg)

(Optional) Customer returns back to business’s site for payment confirmation

## Get started

You don’t have to integrate Bancontact and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Bancontact. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Bancontact from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)

If you prefer to manually list payment methods or want to save Bancontact details for future payments, see the following guides:

- [Manually configure Bancontact as a payment](https://docs.stripe.com/payments/bancontact/accept-a-payment.md)
- [Save Bancontact details for future payments](https://docs.stripe.com/payments/bancontact/set-up-payment.md)

## Disputes

The risk of fraud or unrecognized payments is low because the customer must authenticate the payment with their bank. As a result, you won’t have disputes that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

Bancontact payments can be refunded up to 180 days after the original payment date.
