<!-- Source URL: https://docs.stripe.com/invoicing/payment-methods -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Payment methods

Learn about the supported payment methods for Invoicing.

By default, customers can pay *invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) with any of the payment methods that you’ve enabled in your [Invoice template](https://dashboard.stripe.com/settings/billing/invoice). In some situations, there might be restrictions that prevent payment methods from being used for an invoice. For instance, a payment method might only operate in one currency or have limitations on the amount that can be paid. If there’s a limitation on a payment method, Stripe won’t automatically select it for you.

## Supported payment methods 

Stripe Invoicing supports the following payment methods:

| Payment method | Description | Currencies | Business location | Limitations |
| --- | --- | --- | --- | --- |
| [ACH Direct Debit](https://docs.stripe.com/invoicing/ach-direct-debit.md) | Accept debit payments from customers with a US bank account using the Automated Clearing House (ACH) payments system operated by *Nacha* (Nacha is the governing body that oversees the ACH network). | USD | United States | None |
| [Affirm](https://docs.stripe.com/payments/affirm.md) | Enable customers to split their payments over time while your business gets paid up front. | CAD, USD | Canada, United States | You can only add this payment method to individual invoices. Invoices that use this payment method only support the `send_invoice` [collection method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method). |
| [Afterpay/Clearpay](https://docs.stripe.com/payments/afterpay-clearpay.md) | Enable customers to split their payments over time while your business gets paid up front. | AUD, CAD, GBP, NZD, USD | Australia, Canada, New Zealand, United Kingdom, United States | You can only add this payment method to individual invoices. Invoices that use this payment method only support the `send_invoice` [collection method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method). |
| [Alipay](https://docs.stripe.com/payments/alipay.md) | Allow customers to pay on the web or a mobile device using login credentials or the Alipay app. | AUD, CAD, CNY, EUR, GBP, HKD, JPY, MYR, NZD, SGD, USD | Australia, Canada, Europe, Hong Kong, Japan, New Zealand, Singapore, United States | None |
| [Apple Pay](https://docs.stripe.com/apple-pay.md) | Allow customers to securely make payments using Apple Pay on their iPhone, iPad, or Apple Watch. | [Supported presentment currencies](https://docs.stripe.com/currencies.md#presentment-currencies) | Worldwide | None |
| [Bancontact](https://docs.stripe.com/payments/bancontact.md) | Allow customers to authorize payments on the Bancontact website or mobile app and then return to your website for immediate notification about the success or failure of the payment. | EUR | Australia, Canada, Europe, Hong Kong, Japan, Mexico, New Zealand, Singapore, United States | None |
| [Bank transfer](https://docs.stripe.com/payments/bank-transfers.md) | Receive bank transfers directly from customers using [Payment Intents](https://docs.stripe.com/payments/payment-intents.md). | EUR, GBP, IDR, JPY, MXN, USD | Europe (SEPA), Indonesia, Japan, Mexico, United Kingdom, United States | You can only add this payment method to individual invoices. Invoices that use this payment method only support the `send_invoice` [collection method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method). |
| [Bacs Direct Debit](https://docs.stripe.com/payments/bacs-debit.md) | Accept debit payments from customers with a UK bank account. | GBP | United Kingdom | None |
| [BECS Direct Debit](https://docs.stripe.com/payments/au-becs-debit.md) | Accept debit payments from customers with an Australian bank account. | AUD | Australia | None |
| [BLIK](https://docs.stripe.com/payments/blik.md) | Allow customers in Poland to pay using a six-digit code from their banking app. | PLN | Australia, Canada, Europe, Singapore, United States | Invoices that use this payment method only support the `send_invoice` [collection method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method). |
| [Boleto](https://docs.stripe.com/payments/boleto.md) | Allow customers to pay for services or goods at authorized agencies or banks, ATMs, or online bank portals. | BRL | Brazil | None |
| [Cash App Pay](https://docs.stripe.com/payments/cash-app-pay.md) | Allow customers to make single or recurring payments to businesses using their digital wallet. Customers must authenticate their payment. | USD | United States | None |
| [Cards](https://docs.stripe.com/payments/cards/overview.md) | Allow customers to pay online using cards, which are linked to a debit or credit account at a bank. | Most currencies | Most locations | None |
| [Crypto](https://docs.stripe.com/payments/stablecoin-payments.md) | Accept stablecoin payments that settle as fiat in your Stripe balance. | USD | United States | Invoices that use this payment method only support the `send_invoice` [collection method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method). |
| [EPS](https://docs.stripe.com/payments/eps.md) | Allow customers to pay online using their Austrian bank credentials. | EUR | Australia, Canada, Europe, Hong Kong, Japan, Mexico, New Zealand, Singapore, United States | None |
| [Financial Process Exchange (FPX)](https://docs.stripe.com/payments/fpx.md) | Allow customers to pay online using their Malaysian bank credentials. | MYR | Malaysia | None |
| [Google Pay](https://docs.stripe.com/google-pay.md) | Allow customers to make payments in your app or website using any card saved to their Google Account, including from Google Play, YouTube, Chrome, or an Android device. | [Supported presentment currencies](https://docs.stripe.com/currencies.md#presentment-currencies) | Worldwide except India | None |
| [iDEAL](https://docs.stripe.com/payments/ideal.md) | Allow customers to pay online using their Netherlands bank credentials. | EUR | Australia, Canada, Europe, Hong Kong, Japan, Mexico, New Zealand, Singapore, United States | None |
| [Klarna](https://docs.stripe.com/payments/klarna.md) | Enable customers to pay with flexible payment options, such as pay over time or pay now, while your business gets paid up front. | AUD, CAD, CHF, CZK, DKK, EUR, GBP, NOK, NZD, PLN, RON, SEK, USD | Australia, Canada, most of Europe, New Zealand, United Kingdom, United States | You can only add this payment method to individual invoices. Invoices that use this payment method only support the `send_invoice` [collection method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method). |
| [Konbini](https://docs.stripe.com/payments/konbini.md) | Allow customers in Japan to pay for bills and online purchases at convenience stores with cash. | JPY | Japan | Invoices that use this payment method only support the `send_invoice` [collection method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method). |
| [Link](https://docs.stripe.com/payments/link.md) | Save and autofill payment and shipping information for your customers so they don’t need to enter payment details manually. | Most currencies | Most locations | None |
| [MB WAY](https://docs.stripe.com/payments/mb-way.md) | Allow customers to pay using a phone number linked to their MB WAY app. | EUR | Most locations | Invoices that use this payment method only support the `send_invoice` [collection method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method). |
| [Multibanco](https://docs.stripe.com/payments/multibanco.md) | Allow customers to pay using a voucher through their online banking platform or at an ATM. | EUR | Europe, United Kingdom, United States | Invoices that use this payment method only support the `send_invoice` [collection method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method). |
| [PayNow](https://docs.stripe.com/payments/paynow.md) | Allow customers to pay using their preferred app from participating banks or non-bank financial institutions. | SGD | Singapore | Invoices that use this payment method only support the `send_invoice` [collection method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method). |
| [PayPal](https://docs.stripe.com/payments/paypal.md) | Allow customers to pay using their PayPal account. Customers are redirected to the PayPal website to choose a funding source, such as their PayPal wallet, a linked card or bank account, or buy-now-pay-later. | AUD, CAD, CHF, CZK, DKK, EUR, GBP, HKD, NOK, NZD, PLN, SEK, SGD, USD | Europe, Switzerland, United Kingdom | None |
| [Pix](https://docs.stripe.com/payments/pix.md) | Allow customers to pay by scanning a QR code or copying a Pix string in their preferred banking app. | BRL | Australia, Canada, Europe, Singapore, Switzerland, United Kingdom, United States | None |
| [Pre-authorized debit payments (PADs)](https://docs.stripe.com/payments/acss-debit.md) | Accept debit payments from customers with a Canadian bank account using the Automated Clearing Settlement System (ACSS). | CAD, USD | Canada, United States | None |
| [PromptPay](https://docs.stripe.com/payments/promptpay.md) | Allow customers to pay using their preferred app from participating banks. | THB | Thailand | Invoices that use this payment method only support the `send_invoice` [collection method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method). |
| [Przelewy24](https://docs.stripe.com/payments/p24.md) | Allow customers to pay online using bank transfers and other methods. | EUR, PLN | Australia, Canada, Europe, Hong Kong, Japan, Mexico, New Zealand, Singapore, United States | None |
| [SEPA direct debit](https://docs.stripe.com/payments/sepa-debit.md) | Accept debit payments from customers with an EUR-denominated bank account within the SEPA region. | EUR | Most locations | None |
| [UPI](https://docs.stripe.com/payments/upi.md) | Allow customers in India to pay using UPI, a real-time payment system that instantly transfers funds between bank accounts using their preferred banking or wallet app. | INR | Australia, Canada, Europe, Singapore, United States | None |
| [WeChat Pay](https://docs.stripe.com/payments/wechat-pay.md) | Allow customers to use WeChat Pay to pay for goods and services inside of business apps and websites. | AUD, CAD, CHF (depending on business location), CNY, DKK, EUR, GBP, HKD, JPY, NOK, SEK, SGD, USD | Australia, Canada, Europe, Hong Kong, Japan, Singapore, United Kingdom, United States | None |

\* P.O. boxes don’t accept deliveries from other couriers, such as FedEx or UPS.

## Configure payment methods

You can use the Dashboard or API to add and configure payment methods.

#### Dashboard

To enable payment methods, you need to activate them in the [Invoice default payment methods configuration](https://dashboard.stripe.com/settings/billing/invoice).

### Connect

If you’re a platform using *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), you can manage the invoice [payment methods](https://docs.stripe.com/connect/manage-payment-methods.md) of your connected accounts in the Stripe Dashboard:

1. Go to **Settings** > **Billing** > [Invoice](https://dashboard.stripe.com/settings/billing/invoice).
2. In the **Default payment methods** section, click the **Connected accounts payment method configuration** drop-down.
3. Select **Default** to enable Stripe to provide the default configuration of payment methods.

Your connected accounts still have the ability to enable and disable individual payment methods after you enable the default configuration. You can also manage the payment methods of individual connected accounts using the [payment method configuration](https://docs.stripe.com/api/payment_method_configurations/create.md) API. If your integration uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md), you can create your own payment method configuration. To learn more, see [Multiple configurations for your Connect accounts](https://docs.stripe.com/connect/multiple-payment-method-configurations.md). If you create a custom payment method configuration, it displays as an option in the **Connected accounts payment method configuration** drop-down.

### Overdue payments 

An invoice is considered overdue when its due date has passed and the invoice hasn’t been paid. By default, Stripe reminds your customer to pay the invoice even after the due date. However, by modifying your [Automatic collection settings](https://dashboard.stripe.com/settings/billing/automatic), you can disable [automatic collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection.md) on the invoice when it becomes past due.

#### API

You can use the Invoicing API to select payment methods, decipher errors, and customize the payment experience.

### Select payment methods 

You can override the payment methods that can be used to pay an invoice by changing its [payment settings](https://docs.stripe.com/api/invoices/object.md#invoice_object-payment_settings). If you configured a default payment method on either the customer (as a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer-billing-default_payment_method) object or a [Customer](https://docs.stripe.com/api/customers/object.md#customer_object-invoice_settings-default_payment_method) object) or the [Subscription](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-default_payment_method) object associated with the invoice, be sure to include it in the list of `payment_method_types`. Otherwise, the payment will fail.

#### curl

```bash
curl https://api.stripe.com/v1/invoices/:id \
  -u <<YOUR_SECRET_KEY>>: \
  -d "payment_settings[payment_method_types][]"="card" \
  -d "payment_settings[payment_method_types][]"="customer_balance"
```

### Payment method errors 

Payment method errors can prevent an invoice from being finalized. This can happen when:

- Stripe attempts to automatically select payment methods, but all of the payment methods have restrictions that prevent them from being used (this often happens when only one or two payment methods are enabled).
- You manually select a payment method but a restriction prevents it from being used.

In these cases, Stripe can’t finalize the invoice and sends an `invoice.finalization_failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to notify you of the problem. Look at the [last finalization error](https://docs.stripe.com/api/invoices/object.md#invoice_object-last_finalization_error) for the invoice to view the error. To finalize the invoice and complete the payment, change the [payment_settings](https://docs.stripe.com/api/invoices/object.md#invoice_object-payment_settings) for the invoice so that it has at least one valid payment method.

### Payment method options 

Some payment methods have additional options that you can set to customize the payment experience. See [payment_method_options](https://docs.stripe.com/api/invoices/object.md#invoice_object-payment_settings-payment_method_options) for details.
