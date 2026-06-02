<!-- Source URL: https://docs.stripe.com/payments/managed-payments/changelog -->
<!-- Fetched: 2026-04-23 -->

# Managed Payments changelog

Keep track of changes to Managed Payments.

## April 22, 2026

### General availability

Managed Payments is now generally available to businesses in 39 countries, including new support for Australia.

### Payment links support

You can enable Managed Payments on [payment links](https://docs.stripe.com/payments/managed-payments/use-payment-links.md) created in the Dashboard or using the API.

### Improved flexibility of subscriptions

You can now do the following:

- Add [Invoice Items](https://docs.stripe.com/api/invoiceitems.md) and [Invoice Line Items](https://docs.stripe.com/api/invoice-line-item.md) with eligible product categories to invoices for Managed Payments subscriptions.
- Add [Subscription Items](https://docs.stripe.com/api/subscription_items.md) with eligible product categories to Managed Payments subscriptions.

### Invoice PDF enhancements

Your business name now shows on Managed Payments invoices along with the details of the products sold. Invoices are now issued by _Sold through Link_, aligning with customer branding at checkout.

### Subscription confirmation email

Customers who purchase a Managed Payments subscription that starts with a trial period now receive a confirmation email after checkout, with details on the subscription and trial period.

### Increased product tax code eligibility

Several new product tax codes for digital products are now eligible for Managed Payments. See the full list of [supported tax codes](https://docs.stripe.com/payments/managed-payments/eligibility.md#product-tax-code-requirements).

## February 9, 2026

### Additional payment methods available

Managed Payments supports 15 [payment methods](https://docs.stripe.com/payments/managed-payments/how-it-works.md#payment-method-availability).

### Subscription schedules support

You can use [subscription schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules.md) with Managed Payments subscriptions.

### Free trials without collecting a payment method

Managed Payments on Checkout supports [free trials without collecting a payment method](https://docs.stripe.com/payments/checkout/free-trials.md?payment-ui=stripe-hosted#free-trials-without-payment-method). Ahead of the trial end, customers receive an email with a link to a hosted form where they can provide payment details.

### Adaptive Pricing support for one-time and subscription payments

[Adaptive Pricing](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md) is automatically enabled at checkout to localize pricing into the customer’s local currency.

### API changes

- You can set the [payment_method_collection](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-payment_method_collection) parameter to `if_required` to allow customers to sign up for a free trial without a payment method.
- You can use the [payment_behavior](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-payment_behavior) parameter when updating Managed Payments subscriptions.
- Managed Payments invoices return the [hosted_invoice_url](https://docs.stripe.com/api/invoices/object.md#invoice_object-hosted_invoice_url) in `Invoice` objects.
- You can’t generate one-off invoices on Managed Payments subscriptions that are outside of the billing period.

## November 11, 2025

### New Dashboard page

- You can use the Managed Payments [Settings](https://dashboard.stripe.com/settings/managed-payments) page in the Dashboard to see the current status of your integration, review basic usage metrics, and edit Tax settings.

## October 7, 2025

### API changes

- You can use the [saved_payment_method_options](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-saved_payment_method_options) parameter when Managed Payments is enabled.

## September 22, 2025

### One-time payments support

You can accept one-time payments for digital products using Managed Payments. For one-time payment instructions, see the [Set up Managed Payments](https://docs.stripe.com/payments/managed-payments/set-up.md) and [Update a Checkout integration](https://docs.stripe.com/payments/managed-payments/update-checkout.md) pages.

### In-app payments support

Managed Payments has a Checkout UI for mobile that you can use for in-app payment flows. To accept payments without sending your customer to a browser outside of your mobile app, see [Mobile app payments](https://docs.stripe.com/payments/managed-payments/set-up-mobile.md).

### Link account requirement removed

Customers don’t need to sign in or register for a [Link](https://docs.stripe.com/payments/link.md) account to check out with Managed Payments. Receipt emails contain a URL that allows customers to associate a specific transaction with their Link account, where they can manage their subscription. Customers also don’t need to provide a phone number during checkout.

### API changes

- You can set the [mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode) parameter to `payment` when creating a Managed Payments Checkout Session.
- You can set the [origin_context](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-origin_context) parameter to `mobile_app` to show a Managed Payments Checkout page for mobile.
- To help support one-time payments and in-app payments, you can use Managed Payments for products with the following [product tax codes](https://docs.stripe.com/api/products/object.md#product_object-tax_code):
  - `txcd_10201000`: Video Games - downloaded - non subscription - with permanent rights
  - `txcd_10201001`: Video Games - downloaded - non subscription - with limited rights
  - `txcd_10201003`: Video Games - streamed - non subscription - with limited rights
  - `txcd_10401000`: Digital Audio Works - streamed - non subscription - with limited rights
  - `txcd_10401001`: Digital Audio Works - downloaded - non subscription - with limited rights
  - `txcd_10401100`: Digital Audio Works - downloaded - non subscription - with permanent rights
  - `txcd_10401200`: Digital Audio Works - streamed - subscription - with conditional rights
  - `txcd_10402000`: Digital Audio Visual Works - streamed - non subscription - with limited rights
  - `txcd_10402100`: Digital Audio Visual Works - downloaded - non subscription - with permanent rights
  - `txcd_10402110`: Digital Audio Visual Works - downloaded - non subscription - with limited rights
  - `txcd_10402200`: Digital Audio Visual Works - streamed - subscription - with conditional rights
  - `txcd_10505000`: Digital Finished Artwork - downloaded - non subscription - with limited rights
  - `txcd_10505001`: Digital Finished Artwork - downloaded - non subscription - with permanent rights
  - `txcd_10505002`: Digital Finished Artwork - downloaded - subscription - with conditional rights
  - `txcd_10701410`: Electronically Delivered Information Services - Business Use
  - `txcd_10701411`: Electronically Delivered Information Services - Personal Use
  - `txcd_10701000`: Website Advertising
  - `txcd_10804001`: Digital Audio Visual Works - bundle - downloaded with permanent rights and streamed - subscription - with conditional rights
  - `txcd_10804002`: Digital Audio Visual Works - bundle - downloaded with limited rights and streamed - non subscription
  - `txcd_10804003`: Digital Audio Visual Works - bundle - downloaded with permanent rights and streamed - non subscription
  - `txcd_10804010`: Digital Audio Works - bundle - downloaded with permanent rights and streamed - subscription - with conditional rights

## August 22, 2025

### API changes

- The [customer_update[address]](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_update-address) and [customer_update[name]](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_update-name) parameters are no longer available when [creating a Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) with Managed Payments enabled.

  Managed Payments requires that your customer has a name and a valid billing address in order to calculate sales tax, and always updates the [Customer](https://docs.stripe.com/api/customers/object.md) with the name and billing address collected during the Checkout Session.

- Products with the following [product tax codes](https://docs.stripe.com/api/products/object.md#product_object-tax_code) are now eligible to use with Managed Payments:
  - `txcd_10701400`: Website Information Services - Business Use
  - `txcd_10701401`: Website Information Services - Personal Use

## August 15, 2025

### Support for Radar for Fraud Teams

Managed Payments supports [Radar for Fraud Teams](https://docs.stripe.com/radar.md), which you can use to define [fraud prevention rules](https://docs.stripe.com/radar/rules.md), such as blocking card payments from certain countries, or [always requesting 3D Secure authentication](https://docs.stripe.com/radar/rules.md#request-3d-secure). These rules apply in addition to the fraud prevention already provided by Managed Payments.

## August 13, 2025

### Refunding withheld sales tax

Stripe only keeps the original sales tax amount on refunded transactions where required. The **Payment breakdown** section of the transaction shows the refunded sales tax amount. Your customers aren’t affected by this behavior.
![The Payment breakdown of a transaction using Managed Payments, showing the sales tax withheld originally, and the amount of sales tax refunded, with currency conversion included as well.](assets/stripe-managed-payments-sales-tax-refund.png)
