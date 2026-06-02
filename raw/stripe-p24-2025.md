<!-- Source URL: https://docs.stripe.com/payments/p24 -->
<!-- Fetched: 2026-05-03 -->

# Przelewy24 payments

Learn about Przelewy24, a common payment method in Poland.

Przelewy24 is a Poland-based payment method aggregator that allows customers to complete transactions online using bank transfers and other methods.

For information on payment method transaction fees, refer to [pricing details](https://stripe.com/pricing/local-payment-methods#przelewy24).

Przelewy24 redirects customers to their website to [authenticate a payment](https://docs.stripe.com/payments/payment-methods.md#customer-actions) and there is [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) about the success or failure of a payment.

#### Payment method properties

- **Customer locations**

  Poland

- **Presentment currency**

  EUR or PLN

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

  [No](https://docs.stripe.com/payments/p24.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/p24.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept Przelewy24 payments:

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

- Elements

1Not supported when using Checkout in subscription mode or setup mode.2Available by invite only.

## Payment flow

![](assets/stripe-acss-debit-checkout-flow.svg)

Customer selects Przelewy24 at checkout
![](assets/stripe-eps-select-bank.svg)

Customer is redirected to Przelewy24 and chooses bank
![](assets/stripe-bancontact-redirect.svg)

Customer enters account credentials
![](assets/stripe-eps-pincode-sms.svg)

Customer completes authorization process
![](assets/stripe-bancontact-redirect-success.svg)

Customer is notified that payment is complete
![](assets/stripe-acss-debit-success.svg)

(Optional) Customer returns back to business’s site for payment confirmation

## Get started

You don’t have to integrate Przelewy24 and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Przelewy24. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Przelewy24 from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)

If your integration requires manually listing payment methods, learn how to [manually configure Przelewy24 as a payment](https://docs.stripe.com/payments/p24/accept-a-payment.md).

## Prohibited business categories

In addition to the industry and business categories listed in Stripe’s [Prohibited and restricted businesses](https://stripe.com/restricted-businesses) list, the following categories are prohibited from using Przelewy24:

- Dropshipping businesses
- Automotive sales, services, and rentals
- Specialty food retail
- Pawn shops
- Higher education and vocational training services
- Healthcare providers and medical services
- Entertainment and event promotion services
- Information technology and telecommunications services
- Advertising agencies and marketing services
- Real estate management and brokerage services

To learn more about P24 eligibility for your account, see your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard.

## Additional requirements

Przelewy24 requires that your website or app be publicly available and contain the following information:

- A list of the products and services you sell and their prices
- Your company’s legal details, including: address, tax number, and registration number
- Links to your refund policy and privacy policies

Przelewy24 has the right to suspend or terminate your use of Przelewy24 for breaching the prohibited business categories or failing to meet the additional requirements listed above.

## Disputes

The risk of fraud or unrecognized payments is low because the customer must authenticate the payment with their bank. As a result, you won’t have disputes that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

Payments made with Przelewy24 can only be submitted for refund within 180 days from the date of the original charge. After 180 days, it’s no longer possible to refund the charge.
