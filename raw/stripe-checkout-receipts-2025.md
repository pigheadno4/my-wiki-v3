<!-- Source: Stripe Checkout — Email receipts and paid invoices -->
<!-- Fetched: 2026-04-20 -->

# Email receipts and paid invoices

Send receipts for payments and refunds automatically.

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/receipts?payment-ui=stripe-hosted.

You can manually or automatically send customized email receipts or [paid invoices](https://docs.stripe.com/payments/checkout/receipts.md#paid-invoices). Learn more about [receipts for payments](https://docs.stripe.com/receipts.md).

## Automatically send receipts

To enable automated receipts, toggle **Successful payments** on in your [Customer emails settings](https://dashboard.stripe.com/settings/emails). Receipts are only sent when a successful payment has been made—no receipt is sent if the payment fails or is declined.

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

In addition to ordinary receipts, Checkout can generate paid invoices as proof of payment. Invoices have more information than receipts. For subscriptions, Stripe generates invoices automatically, but for one-time payments, you need to enable them.

> Invoice creation for one-time payments through the [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions.md) is not an [Invoicing](https://stripe.com/invoicing) feature, and is priced separately. Review [this support article](https://support.stripe.com/questions/pricing-for-post-payment-invoices-for-one-time-purchases-via-checkout-and-payment-links) to learn more.

To generate invoices, first, in your [Customer emails settings](https://dashboard.stripe.com/settings/emails), under **Email customers about**, select **Successful payments**. Then, when creating a Checkout session, set [invoice_creation[enabled]](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-invoice_creation-enabled) to `true`.

> Enabling `invoice_creation` isn’t supported if you set `payment_intent_data[capture_method]` to `manual`.

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
  success_url: "https://example.com",
});
```

After the payment completes, Stripe sends an invoice summary with links to download the invoice PDF and invoice receipt to the email address your customer provides during checkout.

> Invoices for delayed notification payment methods might take longer to send because we send the invoice after successful payment, not upon checkout session completion. These methods include: [Bacs Direct Debit](https://docs.stripe.com/payments/bacs-debit/accept-a-payment.md), [Bank transfers](https://docs.stripe.com/payments/bank-transfers/accept-a-payment.md), [Boleto](https://docs.stripe.com/payments/boleto/accept-a-payment.md), [Canadian pre-authorized debits](https://docs.stripe.com/payments/acss-debit/accept-a-payment.md), [Konbini](https://docs.stripe.com/payments/konbini/accept-a-payment.md), [OXXO](https://docs.stripe.com/payments/oxxo/accept-a-payment.md), [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank/accept-a-payment.md), [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit/accept-a-payment.md), and [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md).
> ![Screenshot of the invoice PDF that customers can download from the invoice summary email](assets/stripe-checkout-invoice-pdf.png)

The downloadable invoice PDF
![Screenshot of the invoice receipt that customers can download from the invoice summary email](assets/stripe-checkout-invoice-receipt.png)

The downloadable invoice receipt
![Screenshot of the invoice summary email Stripe sends](assets/stripe-checkout-invoice-email.png)

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
  success_url: "https://example.com",
});
```

Review [invoice best practices](https://docs.stripe.com/invoicing/customize.md) for your region to make sure you’re collecting the right information from your customers. Information like the customer’s billing and shipping addresses, phone number and tax ID appear on the resulting invoice.

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

# Embedded page

> This is a Embedded page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/receipts?payment-ui=embedded-form.

You can manually or automatically send customized email receipts or [paid invoices](https://docs.stripe.com/payments/checkout/receipts.md#paid-invoices-embedded-form). Learn more about [receipts for payments](https://docs.stripe.com/receipts.md).

## Automatically send receipts

To enable automated receipts, toggle **Successful payments** on in your [Customer emails settings](https://dashboard.stripe.com/settings/emails). Receipts are only sent when a successful payment has been made—no receipt is sent if the payment fails or is declined.

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

In addition to ordinary receipts, Checkout can generate paid invoices as proof of payment. Invoices have more information than receipts. For subscriptions, Stripe generates invoices automatically, but for one-time payments, you need to enable them.

> Invoice creation for one-time payments through the [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions.md) is not an [Invoicing](https://stripe.com/invoicing) feature, and is priced separately. Review [this support article](https://support.stripe.com/questions/pricing-for-post-payment-invoices-for-one-time-purchases-via-checkout-and-payment-links) to learn more.

To generate invoices, first, in your [Customer emails settings](https://dashboard.stripe.com/settings/emails), under **Email customers about**, select **Successful payments**. Then, when creating a Checkout session, set [invoice_creation[enabled]](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-invoice_creation-enabled) to `true`.

> Enabling `invoice_creation` isn’t supported if you set `payment_intent_data[capture_method]` to `manual`.

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
  ui_mode: "embedded_page",
  return_url: "https://example.com",
});
```

After the payment completes, Stripe sends an invoice summary with links to download the invoice PDF and invoice receipt to the email address your customer provides during checkout.

> Invoices for delayed notification payment methods might take longer to send because we send the invoice after successful payment, not upon checkout session completion. These methods include: [Bacs Direct Debit](https://docs.stripe.com/payments/bacs-debit/accept-a-payment.md), [Bank transfers](https://docs.stripe.com/payments/bank-transfers/accept-a-payment.md), [Boleto](https://docs.stripe.com/payments/boleto/accept-a-payment.md), [Canadian pre-authorized debits](https://docs.stripe.com/payments/acss-debit/accept-a-payment.md), [Konbini](https://docs.stripe.com/payments/konbini/accept-a-payment.md), [OXXO](https://docs.stripe.com/payments/oxxo/accept-a-payment.md), [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank/accept-a-payment.md), [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit/accept-a-payment.md), and [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md).
> ![Screenshot of the invoice PDF that customers can download from the invoice summary email](assets/stripe-checkout-invoice-pdf.png)

The downloadable invoice PDF
![Screenshot of the invoice receipt that customers can download from the invoice summary email](assets/stripe-checkout-invoice-receipt.png)

The downloadable invoice receipt
![Screenshot of the invoice summary email Stripe sends](assets/stripe-checkout-invoice-email.png)

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
  ui_mode: "embedded_page",
  return_url: "https://example.com",
});
```

Review [invoice best practices](https://docs.stripe.com/invoicing/customize.md) for your region to make sure you’re collecting the right information from your customers. Information like the customer’s billing and shipping addresses, phone number and tax ID appear on the resulting invoice.

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

## See also

- [Send customer emails](https://docs.stripe.com/invoicing/send-email.md)
- [Automate customer emails](https://docs.stripe.com/billing/revenue-recovery/customer-emails.md)
