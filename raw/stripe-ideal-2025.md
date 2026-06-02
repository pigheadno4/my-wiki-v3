<!-- Source URL: https://docs.stripe.com/payments/ideal -->
<!-- Fetched: 2026-05-03 -->

# iDEAL | Wero payments

Learn about iDEAL | Wero, a common payment method in the Netherlands.

> #### iDEAL to Wero migration
>
> Wero [acquired iDEAL](https://ideal.nl/en/epi-successfully-completes-acquisition-of-ideal-and-payconiq-international). If you use iDEAL, you must:
>
> - Rebrand your integration in the first quarter of 2026 to iDEAL | Wero.

- Switch to [Wero](https://docs.stripe.com/payments/wero.md) in the course of 2026 and 2027 to continue accepting [bank redirects](https://docs.stripe.com/payments/bank-redirects.md) payments from customers in the Netherlands.
  > Read how to [migrate from iDEAL to Wero](https://support.stripe.com/questions/ideal-to-wero-migration).

iDEAL | Wero (formerly iDEAL) is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the organization that operates iDEAL | Wero.

For information on payment method transaction fees, refer to [pricing details](https://stripe.com/pricing/local-payment-methods#ideal).

iDEAL | Wero redirects customers to their online banking environment to authenticate a payment using a [second factor of authentication](https://docs.stripe.com/payments/payment-methods.md#customer-actions) and there is [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) about the success or failure of a payment. The exact customer experience depends on their bank.

#### Payment method properties

- **Customer locations**

  Netherlands

- **Presentment currency**

  EUR

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Authenticated bank transfer

- **Recurring payments**

  with [SEPA Direct Debit](https://docs.stripe.com/billing/subscriptions/ideal.md)

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  Yes

- **Dispute support**

  [No](https://docs.stripe.com/payments/ideal.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/ideal.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept iDEAL | Wero payments:

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
- Invoicing
- Elements

## Payment flow

Below is a demonstration of the iDEAL | Wero payment flow from your checkout page:
![](https://docs.stripecdn.com/ideal_payment_demo.2c691dc0c587eb5eb6bdecff31aa5d34ebbe8bb2f9b6b108c99e98fbee8e246d.mp4)

## Get started

You don’t have to integrate iDEAL and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable iDEAL. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add iDEAL from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)

If you prefer to manually list payment methods or want to save iDEAL | Wero details for future payments, see the following guides:

- [Manually configure iDEAL | Wero as a payment method](https://docs.stripe.com/payments/ideal/accept-a-payment.md)
- [Save iDEAL | Wero details for future payments](https://docs.stripe.com/payments/ideal/set-up-payment.md)

Check out the iDEAL | Wero [sample on GitHub](https://github.com/stripe-samples/accept-a-payment).

## Disputes

Customers can’t dispute iDEAL | Wero payments with their bank. Encourage your customers to reach out to you directly with any concerns.

## Refunds

iDEAL | Wero payments can be refunded up to 180 days after the original payment. Refunds can remain in a pending state for up to 7 days. After 7 days, if no failure signal is received, the refund is considered successful.

## Website requirements

If you’re based in the Netherlands, your website must comply with iDEAL | Wero scheme rules by clearly displaying your KVK (company registration) number with the Chamber of Commerce. If you aren’t based in the Netherlands, your website must display your registration number with the equivalent local official body.

## Connect

When using iDEAL | Wero with *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), the connected account’s name must map to its actual business, not to the platform. This is important for regulatory compliance and customer trust, because customers will see this business name during the iDEAL | Wero payment flow.
