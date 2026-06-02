<!-- Source URL: https://docs.stripe.com/payments/advanced/receipts -->
<!-- Fetched: 2026-04-22 -->

# Email receipts

Automatically send receipts and paid invoices.

# Checkout Sessions API

> This is a Checkout Sessions API for when payment-ui is embedded-components. View the full page at https://docs.stripe.com/payments/advanced/receipts?payment-ui=embedded-components.

You can manually or automatically send customized email receipts or [paid invoices](https://docs.stripe.com/payments/advanced/receipts.md#customizing-receipts-embedded-components). Learn more about [receipts for payments](https://docs.stripe.com/receipts.md).

## Automatically send receipts

To enable automated receipts, toggle **Successful payments** on in your [customer emails settings](https://dashboard.stripe.com/settings/emails). Receipts are only sent for a successful payment. Receipts aren’t sent for failed or declined payments.

## Customize receipts

Alter the appearance and functionality of your receipts with the following customization options:

- **Branding**: Modify the logo and colors in your [Branding settings](https://dashboard.stripe.com/settings/branding). The upper limit for a custom logo image file size is 512KB. Ideally, the logo should be a square image exceeding 128 x 128 pixels. JPG, PNG, and GIF file types are supported.
- **Public information**: Specify the public information you want to include, such as your contact number or website address, in your [Public details settings](https://dashboard.stripe.com/settings/public).

To display custom text, use the [payment_intent_data.description](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_intent_data-description) attribute on the [Checkout Session](https://docs.stripe.com/api/checkout/sessions/object.md). Some examples include:

- Description of goods or services provided
- Authorization code
- Subscription information
- Cancellation policies

You can see a real-time preview of your email receipt on your Dashboard Branding settings page. To send a test receipt, hover over the preview image and click **Send test receipt**, then enter your email address.

> Receipts pull data from the `Charge` object generated when the PaymentIntent is confirmed. To update receipt data such as the `description` after the charge is generated, you must [update the Charge](https://docs.stripe.com/api/charges/update.md). Changes to a confirmed PaymentIntent don’t appear on receipts.

## Automatically send paid invoices

In addition to ordinary receipts, you can configure the Checkout Session to generate paid invoices as proof of payment. Invoices have more information than receipts. For subscriptions, Stripe generates invoices automatically, but for one-time payments, you need to enable them.

> Invoice creation for one-time payments through the [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions.md) is not an [Invoicing](https://stripe.com/invoicing) feature, and is priced separately. Review [this support article](https://support.stripe.com/questions/pricing-for-post-payment-invoices-for-one-time-purchases-via-checkout-and-payment-links) to learn more.

To generate invoices, select **Successful payments** under **Email customers about** in your [customer emails settings](https://dashboard.stripe.com/settings/emails). Then, set [invoice_creation[enabled]](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-invoice_creation-enabled) to `true` when creating a Checkout Session.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  invoice_creation: {
    enabled: true,
  },
  line_items: [
    {
      price: "{{ONE_TIME_PRICE_ID}}",
      quantity: 1,
    },
  ],
  ui_mode: "elements",
  return_url: "https://example.com",
});
```

After the payment completes, Stripe sends an invoice summary with links to download the invoice PDF and invoice receipt to the email address your customer provides during checkout.

> Invoices for delayed notification payment methods might take longer to send because we send the invoice after successful payment, not when the checkout session completes. These payment methods include [Bacs Direct Debit](https://docs.stripe.com/payments/bacs-debit/accept-a-payment.md), [Bank transfers](https://docs.stripe.com/payments/bank-transfers/accept-a-payment.md), [Boleto](https://docs.stripe.com/payments/boleto/accept-a-payment.md), [Canadian pre-authorized debits](https://docs.stripe.com/payments/acss-debit/accept-a-payment.md), [Konbini](https://docs.stripe.com/payments/konbini/accept-a-payment.md), [OXXO](https://docs.stripe.com/payments/oxxo/accept-a-payment.md), [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank/accept-a-payment.md), [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit/accept-a-payment.md), and [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md).
> ![Screenshot of the invoice PDF that customers can download from the invoice summary email](assets/stripe-invoice-pdf-example.png)

The downloadable invoice PDF
![Screenshot of the invoice receipt that customers can download from the invoice summary email](assets/stripe-invoice-receipt-example.png)

The downloadable invoice receipt
![Screenshot of the invoice summary email Stripe sends](assets/stripe-invoice-summary-email.png)

The customer email with links to the invoice PDF and receipt

You can also view the invoice in the [Dashboard](https://dashboard.stripe.com/invoices) or access it programmatically by listening to the [invoice.paid](https://docs.stripe.com/api/events/types.md#event_types-invoice.paid) event through an [event destination](https://docs.stripe.com/event-destinations.md).

You can use the `invoice_data` hash inside `invoice_creation` to further customize the invoice generated by the Checkout Session.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  mode: "payment",
  invoice_creation: {
    enabled: true,
    invoice_data: {
      description: "Invoice for Product X",
      metadata: {
        order: "order-xyz",
      },
      account_tax_ids: ["DE123456789"],
      custom_fields: [
        {
          name: "Purchase Order",
          value: "PO-XYZ",
        },
      ],
      rendering_options: {
        amount_tax_display: "include_inclusive_tax",
      },
      footer: "B2B Inc.",
    },
  },
  line_items: [
    {
      price: "{{ONE_TIME_PRICE_ID}}",
      quantity: 1,
    },
  ],
  ui_mode: "elements",
  return_url: "https://example.com",
});
```

Review [invoice best practices](https://docs.stripe.com/invoicing/customize.md) for your region to make sure you’re collecting the right information from your customers. Information like the customer’s billing and shipping addresses, phone number, and tax ID appear on the resulting invoice.

## Localization

When using Checkout Sessions, the language of the receipt and invoice is determined by several factors:

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

- If you set a customer, we use the language specified in the [defaults.locales](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-defaults-locales) attribute of a customer-configured `Account` or the [preferred_locales](https://docs.stripe.com/api/customers/object.md#customer_object-preferred_locales) attribute of a `Customer`, if available.
- If you set a customer without any preferred locales, we apply the [language setting](https://dashboard.stripe.com/settings/emails) from the Dashboard.
- If you don’t set a customer at all, the language defaults to the browser locale of the user opening the Checkout Session URL.

# Payment Intents API

> This is a Payment Intents API for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/advanced/receipts?payment-ui=elements.

With payments using _Elements_ (A set of UI components for building a web checkout flow. They adapt to your customer's locale, validate input, and use tokenization, keeping sensitive customer data from touching your server) and the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md), you can manually or automatically send customized email receipts. Learn more about [receipts for payments](https://docs.stripe.com/receipts.md).

## Automatically send receipts

To enable automated receipts, toggle **Successful payments** on in your [customer emails settings](https://dashboard.stripe.com/settings/emails). Only a successful payment triggers a receipt. Failed or declined payments don’t send a receipt.

You can optionally specify a [receipt_email](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-receipt_email) when you create a _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods). If you do, Stripe sends a receipt to that address in addition to the customer’s email address and any [additional email recipients](https://docs.stripe.com/invoicing/send-email.md#additional-email-recipients) configured for the customer. We don’t send a receipt to an email address included in a payment’s [PaymentMethod billing_details](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-billing_details-email).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: "usd",
  payment_method_types: ["card"],
  description: "Thanks for your purchase!",
  receipt_email: "Sent.in.addition.to.customer.email.addresses@example.com",
});
```

The receipt displays the amount, your [public business information](https://dashboard.stripe.com/settings/public), and any value in the `description` parameter of the request. Receipts for one-time payments include only this information. You can’t add additional line items.

To trigger an automatic receipt after the payment is complete, update the PaymentIntent’s [receipt_email](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-receipt_email).

## Customize receipts

Alter the appearance and functionality of your receipts with the following customization options:

- **Branding**: Modify the logo and colors in your [Branding settings](https://dashboard.stripe.com/settings/branding). The upper limit for a custom logo image file size is 512KB. Ideally, the logo should be a square image exceeding 128 x 128 pixels. JPG, PNG, and GIF file types are supported.
- **Public information**: Specify the public information you want to include, such as your contact number or website address, in your [Public details settings](https://dashboard.stripe.com/settings/public).

To display custom text, use the [description](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-description) attribute on the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md). Some examples include:

- Description of goods or services provided
- Authorization code
- Subscription information
- Cancellation policies

You can see a real-time preview of your email receipt on your Dashboard Branding settings page. To send a test receipt, hover over the preview image and click **Send test receipt**, then enter your email address.

> Receipts pull data from the `Charge` object generated when the PaymentIntent is confirmed. To update receipt data such as the `description` after the charge is generated, you must [update the Charge](https://docs.stripe.com/api/charges/update.md). Changes to a confirmed PaymentIntent don’t appear on receipts.

## Automatically send paid invoices

The [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) can’t generate invoices. Use Stripe Billing to directly [create the invoice](https://docs.stripe.com/invoicing/integration/quickstart.md).

## Localization

When using the Payment Intents API, the language of the receipt is determined by several factors:

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

- If you set a customer, we use the language specified in the [defaults.locales](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-defaults-locales) attribute of a customer-configured `Account` or the [preferred_locales](https://docs.stripe.com/api/customers/object.md#customer_object-preferred_locales) attribute of a `Customer`, if available.
- If you set a customer without any preferred locales, or if you don’t set a customer at all, we apply the [language setting](https://dashboard.stripe.com/settings/emails) from the Dashboard.
