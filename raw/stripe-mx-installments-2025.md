<!-- Source URL: https://docs.stripe.com/payments/mx-installments -->
<!-- Fetched: 2026-05-01 -->

# Mexico installments (meses sin intereses)

Learn about credit card payments using an installment plan.

Installments (meses sin intereses) are a type of credit card payment in Mexico that allows customers to split purchases over multiple billing statements. You receive the full amount (minus a fee) as if it were a normal charge, and the customer’s bank handles collecting the money over time.

Stripe supports installment payments for Stripe Mexico accounts using the Payment Intents and Payment Methods APIs, Checkout, Invoicing, Payment Element, and Payment Links.

#### Payment method properties

- **Customer locations**

  Mexico

- **Presentment currency**

  MXN

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Cards

- **Recurring payments**

  Yes

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  [Yes](https://docs.stripe.com/payments/mx-installments.md#connect-compatibility)

- **Dispute support**

  Yes

- **Manual capture support**

  Yes

- **Refunds / Partial refunds**

  Yes / yes

#### Business locations

Stripe accounts in Mexico can accept Mexico installment payments:

## Get started

Get started with accepting [installments](https://docs.stripe.com/payments/meses-sin-intereses/accept-a-payment.md).

## User experience

In a [Stripe-hosted payment UI](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md?platform=web&ui=stripe-hosted), the option to pay in installments only displays after a user enters a supported card number. Use a [test card number](https://docs.stripe.com/payments/meses-sin-intereses/accept-a-payment.md#testing) to test the functionality in the [Checkout Demo](https://checkout.stripe.dev/checkout). If you’ve built a custom payment UI using the [direct API](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md?platform=web&ui=direct-api), we recommend you similarly collect the card number first, then display any available installment plans.

## Connect

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with installments to process payments on behalf of connected accounts. As a platform, you can set the default installment configuration for your connected accounts in Mexico. Standard connected accounts can override these settings in the Dashboard.

## Connectors and plugins

A variety of connectors and plugins that integrate with Stripe also support installments. These connectors provide no-code and low-code solutions for accepting a wide range of local payment methods using Stripe, including installments.

For example, the [latest version of the Stripe app for Adobe Commerce](https://docs.stripe.com/use-stripe-apps/adobe-commerce/payments/install.md#upgrade) has built-in support for accepting payments with installments. For information regarding setup instructions and features for specific plugins, contact the plugin developers directly.

If you use a plugin that doesn’t yet support installments, you can [contact our support team](https://support.stripe.com/) to let us know, and we’ll do our best to see if we can enable installments for that plugin.

## Fees

When you accept a payment with installments, an additional fee is added to the standard credit card transaction fee. The fee varies according to the number of installments, or months, applied to the transaction.

| **Installment Plan Duration** | **Default Minimum Transaction Amount** | **Additional Fee %** |
| ----------------------------- | -------------------------------------- | -------------------- |
| 3 months                      | 300.00 MXN                             | 5%                   |
| 6 months                      | 600.00 MXN                             | 7.5%                 |
| 9 months                      | 900.00 MXN                             | 10%                  |
| 12 months                     | 1,200.00 MXN                           | 12.5%                |
| 18 months                     | 1,800.00 MXN                           | 17.5%                |
| 24 months                     | 2,400.00 MXN                           | 22.5%                |

## Requirements

There are restrictions on which transactions and cards can use meses sin intereses. You don’t need to implement these rules yourself. Stripe automatically determines meses sin intereses eligibility after you set up the payment method.

- Stripe only supports installments for Stripe Mexico accounts.
- The payment method must be a credit card issued in Mexico.
- The card must be a consumer card–installments don’t support corporate cards.
- The card must be issued by one of our [supported issuers](https://docs.stripe.com/payments/mx-installments.md#supported-cards).
- The currency value must be MXN (pesos).
- The total payment amount must be above a [minimum transaction amount](https://docs.stripe.com/payments/mx-installments.md#fees). Stripe provides a minimum transaction amount based on the number of months in the plan selected. You can specify which installment plans you want to enable and define your own custom minimum and maximum transaction amounts by [configuring custom installment settings](https://docs.stripe.com/payments/meses-sin-intereses/accept-a-payment.md#custom-settings) in the Dashboard.

## Supported cards

You can accept payments in Installments on cards from the following issuers:

- Afirme
- American Express
- Banamex (3-, 6-, 9-, and 12- plans only)
- BanBajío
- Banca Mifel
- Banco Azteca
- Banco Famsa
- Banco Invex
- Banco Multiva
- Bancoppel
- Banjercito
- Banorte
- Banregio
- BBVA
- Caja Morelia Valladolid
- CrediClub
- Didi
- Efevoo Pay
- Falabella
- Hey Banco
- Inbursa
- Klar
- Konfio
- Liverpool
- MercadoPago
- NanoPay
- Nubank
- RappiCard
- Santander
- Scotiabank
- Stori
- Suburbia
