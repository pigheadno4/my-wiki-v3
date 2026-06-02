<!-- Source URL: https://docs.stripe.com/payments/pix -->
<!-- Fetched: 2026-05-06 -->

# Pix payments

Learn about Pix, a common payment method in Brazil.

Pix is a real-time payment system developed by the Central Bank of Brazil. The service works by transferring funds between two bank accounts. To pay with Pix, customers authenticate and approve by scanning a QR code or copying a Pix string in their preferred banking apps.

Pix supports both one-time payments and recurring payments through Pix Automático. For recurring payments, customers authorize a mandate in their bank app, which allows you to charge them automatically for future payments within the mandate terms.

#### Payment method properties

- **Customer locations**

  Brazil

- **Presentment currency**

  BRL

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Real-time payment

- **Payout timing**

  Standard payout timing applies

- **Recurring Payments**

  Yes

- **Connect support**

  [Yes](https://docs.stripe.com/payments/pix.md#connect)

- **Dispute support**

  [Yes](https://docs.stripe.com/payments/pix.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [Yes / yes](https://docs.stripe.com/payments/pix.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept Pix payments. [Settlement currency](https://docs.stripe.com/payments/pix.md#supported-currencies) depends on your account country.

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
- GR
- HR
- HU
- IE
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
- SG
- SI
- SK
- US

Stripe accounts in Brazil can accept Pix one-time payments with BRL settlement. Pix Automático isn’t available in Brazil. (Invite only)

- BR

#### Product support

- Connect
- Payment Links
- Checkout1
- Elements

1 For Checkout in subscription mode, use Pix Automático.

## Payment flow

![](assets/stripe-pix-flow-checkout.svg)

Selects Pix at checkout
![](assets/stripe-pix-flow-qr-code.svg)

Receives Pix string or QR code (or both)
![](assets/stripe-pix-flow-bank-portal.svg)

Makes a payment through bank apps or internet banking
![](assets/stripe-pix-flow-success.svg)

Receives notification that payment is complete

## Getting started

You don’t have to integrate Pix and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Pix. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Pix from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)

To list payment methods manually, learn how to [accept a Pix payment with a direct integration](https://docs.stripe.com/payments/pix/accept-a-payment.md).

To accept recurring payments with Pix, learn how to [set up Pix Automático](https://docs.stripe.com/payments/pix/pix-automatico.md).

## Disputes

Pix permits disputes in a limited set of circumstances. Buyers can raise disputes with their banks and must provide evidence of their issue, for example, fraud or account takeover. You can’t challenge such disputes. If Stripe receives notification that our partner has accepted a request to return customer funds, Stripe removes the funds from your account.

## Refunds

You can refund Pix payments up to 90 days after the original payment date and view the refund reflected in your account within a few minutes.

## Connect

Use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with Pix to process payments on behalf of connected accounts. *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) users use Pix with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

Pix availability on Connect depends on the [merchant of record](https://docs.stripe.com/connect/merchant-of-record.md) (MoR) for the payment. The MoR is determined by the [charge type](https://docs.stripe.com/connect/charges.md) you use:

- **Connected account is the MoR** (for example, [direct charges](https://docs.stripe.com/connect/direct-charges.md), or charges using the [`on_behalf_of`](https://docs.stripe.com/connect/separate-charges-and-transfers.md#settlement-merchant) parameter): Pix is supported if the connected account is in a supported country for Pix.
- **Platform is the MoR** (for example, [destination charges](https://docs.stripe.com/connect/destination-charges.md) or [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md) without `on_behalf_of`): Pix is supported if the platform account is in a supported country for Pix.

### Accept Pix payments as the connected account

[Direct charges](https://docs.stripe.com/connect/direct-charges.md) and charge types using the [on_behalf_of](https://docs.stripe.com/connect/separate-charges-and-transfers.md#settlement-merchant) parameter require the connected account itself (not the platform) to have activated the Pix payment method. Connect platforms can use the [`pix_payments` capability](https://docs.stripe.com/connect/account-capabilities.md#payment-methods) to determine whether that’s the case for a connected account:

- In the case of connected accounts that use the Stripe Dashboard, the owner of the account needs to activate the payment method in their [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard.
- In the case of connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe, the platform needs to request the `pix_payments` capability.

## Settlement currencies

Accepted Pix payments settle in a currency based on your Stripe account country.

| Account country                                                                                                    | Settlement currency |
| ------------------------------------------------------------------------------------------------------------------ | ------------------- |
| BR                                                                                                                 | BRL                 |
| US                                                                                                                 | USD                 |
| AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK | EUR                 |
| CH, GB                                                                                                             | GBP                 |
| CA                                                                                                                 | CAD                 |
| AU                                                                                                                 | AUD                 |
| SG                                                                                                                 | SGD                 |

## Transaction limits

The amount for a single Pix must be at least 0.50 BRL and no more than 3,000 USD.

For recurring transactions, the amount that can be charged is limited by the amount that the buyer authorizes during the mandate creation. If you charge above the amount that was authorized, the payment fails. Additionally, a single buyer can’t transact more than 10,000 USD per month with any single business.

## Handle Brazilian consumer tax (IOF)

IOF is a Brazilian tax on all transactions that involve foreign exchange (for example, from BRL to USD). The IOF is collected from Brazilian buyers paying international businesses (that is, those domiciled outside of Brazil). The current rate is 3.5% of the transaction value.

> The IOF rate can be subject to change by the Brazilian authorities. Check the Stripe documentation periodically to see if the rate changes.

Stripe and our partner handle the collection and remittance of this IOF fee for you. However, you must decide how you want to present this tax to your customer. By default, your customer pays the IOF. To change this behavior, you can use the `amount_includes_iof` parameter in the field `payment_method_options` for Pix.

| amount_includes_iof | Description                                                                                                                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `never`             | This is the default behavior where your customer pays the IOF. The amount that you collect on a payment intent is marked up by 3.5% in your customer’s banking app.                                                 |
| `always`            | You absorb the IOF on behalf of your customer. If you think an extra 3.5% could hurt conversion, you can elect to pay the IOF on behalf of your customer. In this scenario, we deduct the IOF from your settlement. |

If you’re integrating Pix through Checkout or Elements, Stripe handles customer disclosures on your behalf.

If you’re an API user, you must show the appropriate disclosures based on which IOF handling option you choose. See the following section for suggested language.

### IOF suggested language for API users

If you’re integrating as a Direct API user, you must show the appropriate customer disclosures for processing Pix transactions at checkout, depending on which IOF handling option you choose:

| amount_includes_iof | Suggested Language (English)                                                                                                                                                                                                      | Suggested Language (Brazilian Portuguese)                                                                                                                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `never`             | This is an international purchase and excludes a 3.5% IOF fee. By proceeding, you acknowledge and accept [Ebanx’s terms and conditions](https://www.ebanx.com/pt-br/legal/consumidores/brasil/termos-para-processar-pagamentos/). | Esta é uma compra internacional e não inclui a tarifa de 3.5% de IOF. Ao prosseguir, você reconhece e aceita os [termos e condições do Ebanx](https://www.ebanx.com/pt-br/legal/consumidores/brasil/termos-para-processar-pagamentos/). |
| `always`            | This is an international purchase and includes a 3.5% IOF fee. By proceeding, you acknowledge and accept [Ebanx’s terms and conditions](https://www.ebanx.com/pt-br/legal/consumidores/brasil/termos-para-processar-pagamentos/). | Esta é uma compra internacional e inclui a tarifa de 3.5% de IOF. Ao prosseguir, você reconhece e aceita os [termos e condições do Ebanx](https://www.ebanx.com/pt-br/legal/consumidores/brasil/termos-para-processar-pagamentos/).     |

## Customer communications

### Receipts

In Brazil, businesses commonly send a receipt for each transaction and itemize the IOF amount.

By default, our Pix partner, Ebanx, sends customer receipts. If you want to disable those emails and send your own receipts, include a line item for the IOF amount. If you absorb the IOF fee, we recommend itemizing the IOF amount in your customer receipts.

To disable these emails, go to your [Customer emails settings](https://dashboard.stripe.com/settings/emails) and use the **Pix payments** section to disable Pix receipts.

### Complete transaction reminder emails

Enable customer emails to help them complete the transaction. The email includes a Pix QR code and Pix key that they can scan outside the checkout flow.

These emails are disabled by default. Enable them in the Stripe Dashboard at [Customer emails settings](https://dashboard.stripe.com/settings/emails) in the **Pix payments** section.

## Statement descriptors

Customized statement descriptors aren’t supported by Pix—the value specified in the [statement_descriptor](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-statement_descriptor) is ignored. The Stripe service provider (`Ebanx`) is shown as the recipient of payments and in the statement descriptor on the customer’s bank statements. Your business name appears in the `identifier` field when making a payment.

## Prohibited business categories

In addition to the industry and business categories listed in [Prohibited and Restricted Businesses](https://stripe.com/legal/restricted-businesses), the following categories aren’t allowed to use Pix:

- Crypto businesses
- Insurance companies
- Telehealth or medicine vendors
- Non-profits and charities

For more information about Pix eligibility for your account, go to your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods).
