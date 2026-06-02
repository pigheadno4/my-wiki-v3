<!-- Source URL: https://docs.stripe.com/receipts -->
<!-- Fetched: 2026-05-11 -->

# Receipts and paid invoices

Send payment or refund receipts automatically.

Each receipt contains a link to view it in a browser and a unique [receipt number](https://docs.stripe.com/api.md#charge_object-receipt_number) that’s useful when looking up payment information.

You can also access the link to view the receipt in a browser through the API in the _PaymentIntent’s_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) related [Charge](https://docs.stripe.com/api/charges/object.md#charge_object-receipt_url) object. When you visit the link, the receipt always shows the latest status of that charge. If it’s been refunded, the receipt accurately reflects the refund. Stripe-hosted receipts are designed to be viewed in a web browser. You can’t directly download them.

As a security measure, receipt links expire within 30 days. Expired receipt links require the customer to provide the original email address to resend the receipt to that address.

## Automatically send receipts

You can enable automated receipts with:

- [Payment Links](https://docs.stripe.com/payment-links/post-payment.md#send-email-receipts)
- [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions.md)
  - [Full hosted page](https://docs.stripe.com/payments/checkout/receipts.md?payment-ui=stripe-hosted#automatically-send-receipts)
  - [Full embedded page](https://docs.stripe.com/payments/checkout/receipts.md?payment-ui=embedded-page#automatically-send-receipts-embedded-page)
  - [Elements](https://docs.stripe.com/payments/advanced/receipts.md?payment-ui=embedded-components)
- [Advanced integrations](https://docs.stripe.com/payments/advanced/receipts.md#automatically-send-receipts)

## Manually send receipts

To send receipts in the [Dashboard](https://dashboard.stripe.com/payments), click **Send receipt** within the **Receipt history** section of a Payment details page. You can also hover over a payment within the **Payments** section of a customer’s page and click the **Send receipt** icon. To resend an email receipt, input a different email address, or specify a comma-separated list of addresses to send it to several recipients. A record of the last 10 receipts is visible on the payment’s page.

To give your customer direct access to a receipt through your application, use the [`receipt_url`](https://docs.stripe.com/api/charges/object.md#charge_object-receipt_url).

## Customize receipts

Learn how to customize receipts with:

- [Payment Links](https://docs.stripe.com/payment-links/post-payment.md#send-email-receipts)
- [Checkout Sessions API](https://docs.stripe.com/payments/checkout/receipts.md#customizing-receipts)
  - [Full hosted page](https://docs.stripe.com/payments/checkout/receipts.md?payment-ui=stripe-hosted#customizing-receipts)
  - [Full embedded page](https://docs.stripe.com/payments/checkout/receipts.md?payment-ui=embedded-page#customizing-receipts-embedded-page)
  - [Elements](https://docs.stripe.com/payments/advanced/receipts.md?payment-ui=embedded-components)
- [Advanced integrations](https://docs.stripe.com/payments/advanced/receipts.md#automatically-send-receipts)

## Refund receipts

When a payment is refunded, Stripe can automatically send a receipt to the same email address provided in the original charge. You can also use the Dashboard to manually send a copy of the refund receipt. To enable automated refund receipts, toggle **Refunds** on in your [Customer emails settings](https://dashboard.stripe.com/settings/emails).

Businesses in Mexico can also download refund receipts from the Dashboard. These receipts contain additional information about the refund, such as refund status and refund type.

## Invoice and subscription payment receipts

Stripe creates a receipt when a customer pays an _invoice_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) or makes any _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) payment. Receipts for subscription and invoice payments are itemized to include line items, discounts, and taxes. After payment, the [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page.md) includes a link to a receipt that the customer can download for their own records.

## Test receipts

Test payments created using your [test API keys](https://docs.stripe.com/keys.md#test-live-modes) don’t automatically send receipts unless the associated email belongs to you or to another user with a verified email and access to the testing environment. For test payments associated with other email addresses, view or manually send a receipt using the [Dashboard](https://dashboard.stripe.com/test/payments).

## Stripe Connect receipts

Receipt settings depend on the charge and account type:

- [Destination charges](https://docs.stripe.com/connect/destination-charges.md) and [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md): Receipts use the platform account’s **Customer emails**, **Branding**, and **Public details** settings.

- [Direct charges](https://docs.stripe.com/connect/direct-charges.md): Receipts use the connected account’s **Customer emails**, **Branding**, and **Public details** settings.

Platform accounts can send a receipt for a connected account by passing `receipt_email` when making a charge request.

For connected accounts that use the Stripe Dashboard (which includes Standard connected accounts), you can configure receipt settings under [Branding](https://dashboard.stripe.com/settings/branding). For connected accounts that don’t use the Dashboard (which includes Express and Custom connected accounts), the platform configures receipt settings through [settings.branding](https://docs.stripe.com/api/accounts/update.md#update_account-settings-branding).

## See also

- [Send customer emails](https://docs.stripe.com/invoicing/send-email.md)
- [Automate customer emails](https://docs.stripe.com/billing/revenue-recovery/customer-emails.md)
