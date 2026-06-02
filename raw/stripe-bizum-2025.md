<!-- Source URL: https://docs.stripe.com/payments/bizum -->
<!-- Fetched: 2026-05-06 -->

# Bizum payments

Learn about Bizum, a real-time payment method in Spain.

Bizum is a real-time payment system in Spain. When making a payment with Bizum, the buyer enters the phone number they’ve registered with Bizum and authenticates and approves the payment in their bank’s app directly.

#### Payment method properties

- **Customer locations**

  Spain

- **Presentment currencies**

  EUR

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Real-Time Payment

- **Recurring payments**

  No

- **Payout timing**

  Standard

- **Connect support**

  No

- **Dispute support**

  [ Yes ](https://docs.stripe.com/payments/bizum.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [ Yes ](https://docs.stripe.com/payments/bizum.md#refunds) / [ Yes ](https://docs.stripe.com/payments/bizum.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept Bizum payments that settle in a [supported currency](https://docs.stripe.com/payments/bizum.md#supported-currencies).

- AT
- AU
- BE
- CA
- CH
- CZ
- DE
- DK
- ES
- FI
- FR
- GB
- GR
- HU
- IE
- IT
- LT
- LU
- NL
- NO
- PL
- PT
- RO
- SE
- SG
- SI
- SK
- US

#### Product support

- Payment Links
- Checkout1
- [Elements](https://docs.stripe.com/payments/bizum/accept-a-payment.md?payment-ui=elements&api-integration=checkout)2

1Not supported when using Checkout in subscription mode or setup mode.

2Express Checkout Element doesn’t support Bizum.

## Get started

You don’t have to integrate Bizum and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Bizum. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Bizum from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)

If your integration requires manually listing payment methods, learn how to [ configure Bizum](https://docs.stripe.com/payments/bizum/accept-a-payment.md).

## Payment options

The minimum charge limit is 0.50 EUR or the equivalent for other supported currencies.

The maximum charge limit is 5,000.00 EUR or the equivalent for other supported currencies.

## Prohibited and restricted business categories

In addition to the categories of goods or services sold and businesses [restricted from using Stripe overall](https://stripe.com/restricted-businesses), the following categories are prohibited from using Bizum:

- Art Dealers and Galleries
- Bail and Bond Payments
- Betting/Casino Gambling
- Charitable and Social Service Organizations - Fundraising
- Financial Institutions
- Government Licensed On-line Casinos (On-Line Gambling)
- Government-Licensed Horse/Dog Racing
- Government-Owned Lotteries (US Region only)
- Jewelry Stores, Watches, Clocks, and Silverware Stores
- Cryptocurrency exchanges and wallets
- Non-FI, Stored Value Card Purchase/Load
- Political Organizations
- Precious Stones and Metals, Watches and Jewelry
- Religious Organizations
- Security Brokers/Dealers
- Timeshares
- Watch/Jewelry Repair
- Other categories at the discretion of Bizum

## Additional requirements

Make sure you comply with the following Bizum requirements *before* requesting access to Bizum as a payment method in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) or through the [capabilities API](https://docs.stripe.com/api/capabilities.md).

- **Companies**: Provide a valid tax identification number for your country using the [`company.tax_id`](https://docs.stripe.com/api/accounts/object.md#account_object-company-tax_id) field. Alternatively, you can provide a VAT ID using the [`company.vat_id`](https://docs.stripe.com/api/accounts/object.md#account_object-company-vat_id) field.
- **Individuals and sole proprietors**: Provide a valid personal identification number using the [`individual.id_number`](https://docs.stripe.com/api/persons/object.md#person_object-id_number) field.
  - **Spain**: Provide your [DNI](https://sede.policia.gob.es/dni-y-pasaporte/) (Documento Nacional de Identidad) or [NIE](https://sede.policia.gob.es/dni-y-pasaporte/) (Número de Identificación de Extranjero) if you are a foreign resident.
  - **Other supported countries**: Provide the standard personal identification number for your country.

You must also set the [`business_type`](https://docs.stripe.com/api/accounts/object.md#account_object-business_type) on your account.

If you use the Dashboard, you can provide these details in your [tax settings](https://dashboard.stripe.com/settings/taxation). After you request the Bizum capability, any outstanding requirements appear in your account status with a link to the relevant settings page.

> The Bizum payments capability stays in a `pending` state until compliance with Bizum onboarding requirements is verified. Contact [Stripe support](https://support.stripe.com/contact) if you’re unsure about your Bizum payments capability status.

## Disputes

Bizum has a claims process that allows transaction disputes. Customers can open disputes for cases of suspected fraud, double payments, or a difference between an order and a transaction amount. Customers can initiate a dispute within 120 calendar days of the transaction.

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to receive [webhooks](https://docs.stripe.com/webhooks.md))

Stripe holds back the disputed amount from your balance until Bizum resolves the dispute.

We request that you upload compelling evidence proving that you fulfilled the purchase order [using the Stripe Dashboard](https://docs.stripe.com/disputes/responding.md#respond). This evidence can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or proof of receipt
- Record of refund (for purchase you’ve already refunded)

To handle disputes programmatically, [respond to disputes using the API](https://docs.stripe.com/disputes/api.md).

This information helps Bizum determine if a dispute is valid. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 40 calendar days. Bizum provides a decision within 90 calendar days. If Bizum resolves the dispute with you winning, we return the disputed amount to your Stripe balance. If Bizum rules in favor of the customer, the disputed amount stays with the customer.

## Refunds

Bizum supports full and partial refunds.

- The refund period is up to 395 days after the purchase.
- Refunds for Bizum payments are asynchronous and take up to 5 minutes to complete.

Stripe notifies you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. If a refund fails (the `Refund` object’s status transitions to `failed`), then we return the amount to your Stripe balance, and you must arrange an alternative way of providing your customer with a refund.

## Supported currencies

Bizum only supports payments in `eur`.

- eur: AT, BE, CZ, DE, DK, ES, FI, FR, GR, HU, IE, IT, LT, LU, NL, NO, PL, PT, RO, SE, SI, SK
- eur: CH
- eur: GB
- eur: US
- eur: SG
- eur: AU
- eur: CA
