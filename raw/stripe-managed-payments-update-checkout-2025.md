<!-- Source URL: https://docs.stripe.com/payments/managed-payments/update-checkout -->
<!-- Fetched: 2026-04-23 -->

# Update a Stripe Checkout integration to use Managed Payments

Learn how to update your existing Stripe integration to use Managed Payments.

> #### Terms of service required
>
> You must accept the [Managed Payments terms of service](https://stripe.com/legal/managed-payments) in the [Dashboard](https://dashboard.stripe.com/settings/managed-payments) before you can use Managed Payments.

Update your existing [Stripe Checkout](https://docs.stripe.com/payments/checkout.md) integration to use Managed Payments. Your integration must already accept payments by creating _Checkout Sessions_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription) in `payment` or `subscription` mode.

If you don’t have an existing Checkout integration, see [Set up Managed Payments](https://docs.stripe.com/payments/managed-payments/set-up.md) instead.

### Reasons to update

A Managed Payments integration enables Stripe to take on the responsibility for indirect taxes compliance, fraud prevention, customer transaction support, and order management for you. To learn more, see [How Managed Payments works](https://docs.stripe.com/payments/managed-payments/how-it-works.md).

### Existing subscriptions

During this preview, you can only enable Managed Payments for new subscriptions purchased through a Managed Payments Checkout Session. Existing subscriptions aren’t eligible.

## Before you begin

- You have an existing Stripe Checkout integration (either [hosted](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) or [embedded form](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=embedded-form)) that creates Checkout Sessions in `payment` or `subscription` mode.
- Activate Managed Payments in your [Dashboard](https://dashboard.stripe.com/settings/managed-payments).
- Make sure your products meet the [eligibility requirements](https://docs.stripe.com/payments/managed-payments/eligibility.md) for Managed Payments. To process a payment through Managed Payments, all the products the customer purchases must meet eligibility.
- Use an API version of `2025-03-31.basil` or [later](https://docs.stripe.com/changelog.md).

## Configure your products for Managed Payments

To calculate taxes, Managed Payments requires your _products_ (Products represent what your business sells—whether that's a good or a service) have a set _tax code_ (A tax code is the category of your product for tax purposes). See the [eligible tax codes](https://docs.stripe.com/payments/managed-payments/eligibility.md#eligible-tax-codes).

Use the Dashboard or the API to set a tax code for each of your products.

#### Dashboard

To update a product’s tax code:

1. Navigate to the **Dashboard** > [Product catalog](https://dashboard.stripe.com/products).
1. Click the overflow menu (⋯) next to the product you want to update.
1. Click **Edit product**.
1. Select a **Product tax code**. Eligible tax codes will be labelled “**Eligible** for Managed Payments”.
1. Click **Update product**.

#### API

To update a product’s tax code:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.update("{{PRODUCT_ID}}", {
  tax_code: "{{TAX_CODE}}",
});
```

Repeat this for each product you want to use with Managed Payments.

If you create your products inline when creating your [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md), include `tax_code` in the `product_data` object. For example, depending on whether you accept subscriptions or one-time payments:

#### Subscriptions

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        product_data: {
          name: "Basic subscription",
          tax_code: "{{TAX_CODE}}",
        },
        recurring: {
          interval: "month",
        },
      },
      quantity: 1,
    },
  ],
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

#### One-time payments

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        product_data: {
          name: "1000 tokens",
          tax_code: "{{TAX_CODE}}",
        },
      },
      quantity: 1,
    },
  ],
  mode: "payment",
  success_url: "https://example.com/success",
});
```

## Enable Managed Payments when creating your Checkout Session

Update your server’s call to the [Checkout Session API](https://docs.stripe.com/api/checkout/sessions/create.md) to set the `managed_payments[enabled]` parameter.

For example:

#### Subscriptions

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  managed_payments: {
    enabled: true,
  },
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

#### One-time payments

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 1,
    },
  ],
  managed_payments: {
    enabled: true,
  },
  mode: "payment",
  success_url: "https://example.com/success",
});
```

## Remove unsupported parameters [Server-side]

#### Subscriptions

To act as the merchant of record, Stripe controls some parts of the Checkout Session. As a result, some parameters aren’t available when using Managed Payments, and you must remove them when creating Managed Payments Checkout Sessions.

| Category                              | Parameter                                   | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Adaptive Pricing                      | `adaptive_pricing`                          | Adaptive Pricing is always enabled on Managed Payments.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Tax                                   | `automatic_tax`                             | Managed Payments handles tax calculation and withholding for you.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `tax_id_collection`                   |
| `subscription_data.default_tax_rates` |
| Payment methods                       | `payment_method_configuration`              | Managed Payments controls the payment methods available in the Checkout Session using [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) to display the most relevant payment methods to your customer. Refer to [Payment method configurations](https://support.stripe.com/questions/payment-method-configurations-for-managed-payments) for information about how to configure payment method settings for Managed Payments.                     |
| `payment_method_options`              |
| `payment_method_types`                |
| Customer update                       | `customer_update[name]`                     | Managed Payments requires that your customer has a name and a valid billing address to calculate sales tax. If you provide the ID of an existing [customer_account](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_account) or [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) when you create the Checkout Session, that object is updated with any changes to the customer’s name or billing address. |
| `customer_update[address]`            |
| Shipping                              | `shipping_address_collection`               | Managed Payments only supports digital products, so shipping information is never collected.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `shipping_options`                    |
| Connect                               | `subscription_data.application_fee_percent` | Managed Payments doesn’t support Connect integrations.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `subscription_data.on_behalf_of`      |
| `subscription_data.transfer_data`     |
| Post-sale                             | `subscription_data.invoice_settings`        | Managed Payments handles post-sale actions, such as invoicing and confirmation emails for you.                                                                                                                                                                                                                                                                                                                                                                                                         |
| `invoice_creation`                    |

#### One-time payments

To act as the _merchant of record_ (The legal entity responsible for facilitating the sale of products to a customer that handles any applicable regulations and liabilities, including sales taxes. In a Connect integration, it can be the platform or a connected account), Stripe controls some parts of the Checkout Session. As a result, some parameters aren’t available when using Managed Payments, and you must remove them when creating Managed Payments Checkout Sessions.

| Category                                                     | Parameter                                    | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------ | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Tax                                                          | `automatic_tax`                              | Managed Payments handles tax calculation and withholding for you.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `tax_id_collection`                                          |
| Payment methods                                              | `excluded_payment_method_types`              | Managed Payments controls the payment methods available in the Checkout Session using [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) to display the most relevant payment methods to your customer. Refer to [Payment method configurations](https://support.stripe.com/questions/payment-method-configurations-for-managed-payments) for information about how to configure payment method settings for Managed Payments.                     |
| `adaptive_pricing`                                           |
| `payment_intent_data.setup_future_usage`                     |
| `payment_method_configuration`                               |
| `payment_method_options.{payment_method}.setup_future_usage` |
| `payment_method_types`                                       |
| Customer update                                              | `customer_update[name]`                      | Managed Payments requires that your customer has a name and a valid billing address to calculate sales tax. If you provide the ID of an existing [customer_account](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_account) or [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) when you create the Checkout Session, that object is updated with any changes to the customer’s name or billing address. |
| `customer_update[address]`                                   |
| Shipping                                                     | `shipping_address_collection`                | Managed Payments only supports digital products, so shipping information is never collected.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `shipping_options`                                           |
| `payment_intent_data.shipping`                               |
| Connect                                                      | `payment_intent_data.application_fee_amount` | Managed Payments doesn’t support Connect integrations.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `payment_intent_data.on_behalf_of`                           |
| `payment_intent_data.transfer_data`                          |
| `payment_intent_data.transfer_group`                         |
| Post-sale                                                    | `invoice_creation`                           | Managed Payments handles post-sale actions such as invoicing and confirmation emails for you.                                                                                                                                                                                                                                                                                                                                                                                                          |
| `payment_intent_data.statement_descriptor`                   |
| `payment_intent_data.statement_descriptor_suffix`            |
| `payment_intent_data.receipt_email`                          |

## Testing

Test that your integration works correctly for your customers.

### Checkout

1. Start your server and go to your checkout page (for example, <http://localhost:4242/checkout.html> from [Build your checkout](https://docs.stripe.com/payments/managed-payments/set-up.md#build-your-checkout)).
1. Click the checkout button to be redirected to the Managed Payments checkout page.
1. On the checkout page, enter different billing addresses to see how Managed Payments calculates tax for customers in different locations.
1. To process the payment, enter your email, phone number, and the test card number `4242 4242 4242 4242` with any CVC and an expiration date in the future.

For additional information, see [Testing](https://docs.stripe.com/testing.md).

### Payment details

#### Item 1

1. After you confirm the test payment, go to the **Dashboard** > [Transactions](https://dashboard.stripe.com/test/payments)
1. Click your test payment to view the payment details. This page shows the:
   - Product that was purchased
   - [Subscription](https://docs.stripe.com/api/subscriptions.md) that was created
   - [Invoice](https://docs.stripe.com/api/invoices.md) that was created
   - Amount of tax calculated and withheld through Managed Payments
   - Statement descriptor that displays on your customer’s statements

> #### Customer authorization
>
> When a customer purchases a subscription through Managed Payments, it only authorizes their payment method to be charged by Managed Payments. Make sure you obtain the appropriate consent from your customer to charge this payment method for any transactions outside of Managed Payments.

#### Item 2

1. After you confirm the test payment, go to the **Dashboard** > [Transactions](https://dashboard.stripe.com/test/payments)
1. Click your test payment to view the payment details. This page shows the:
   - Product that was purchased
   - [Subscription](https://docs.stripe.com/api/subscriptions.md) that was created (if purchased)
   - [Invoice](https://docs.stripe.com/api/invoices.md) that was created
   - Amount of tax calculated and withheld through Managed Payments
   - Statement descriptor that displays on your customer’s statements

#### Preview the receipt

1. Under **Receipt history**, click **View receipt**.
1. Click **Send receipt** to preview the receipt email sent to your customer.

> In sandbox mode, you won’t receive receipt emails automatically after purchase but can manually send them using the instructions above.

### Link

[Link](https://docs.stripe.com/payments/link.md) acts as the merchant of record at checkout and provides subscription management and transaction support on the [Link website](https://link.com).

You can test how Link works during checkout by creating a Link account during an initial Checkout Session. After you create the Link account, attempt another session using the same email address. To authenticate, use the test passcode `000000`.

Test purchases won’t appear in the Link app. You can test the order management tools in the Link app by creating a Link account during a live mode Checkout Session.

## Optional: Configure the tax behavior of your prices

The [tax_behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#tax-behavior) of a price specifies whether tax is added on top of the price you set (`tax_behavior: exclusive`) or included already in the price (`tax_behavior: inclusive`).

Managed Payments uses the [tax behavior specified on your price](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md#set-tax-behavior-on-price). If you don’t specify the price’s tax behavior, by default, Managed Payments adds tax on top of the price you set.

To change the default, go to the **Dashboard** > [Tax settings](https://dashboard.stripe.com/settings/tax) and update the **Include tax in prices** setting.
