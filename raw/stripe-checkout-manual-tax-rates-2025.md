<!-- Source: Stripe Checkout — Use manual Tax Rates -->
<!-- Fetched: 2026-04-20 -->

# Use manual Tax Rates

Learn how to collect taxes using manual Tax Rates.

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/use-manual-tax-rates?payment-ui=stripe-hosted.

Stripe supports manually defining [Tax Rates](https://docs.stripe.com/api/tax_rates.md) to collect taxes (sales, VAT, GST, and others) for different locations. However, [Stripe Tax](https://docs.stripe.com/payments/checkout/taxes.md) is recommended instead of manual tax rates to automatically enable support for 60+ countries.

There are two ways to collect taxes in Checkout:

- Use _fixed tax rates_ when you know the exact tax rate to charge your customer before they start the checkout process (for example, you only sell to customers in the UK and always charge 20% VAT).
- Use _dynamic tax rates_ with the Prices API when you need more information from your customer (for example, their billing or shipping address) to determine the tax rate to charge. With dynamic tax rates, you create tax rates for different regions (for example, a 20% VAT tax rate for customers in the UK and a 7.25% sales tax rate for customers in California, US) and Stripe attempts to match your customer’s location to one of those tax rates.

## Create tax rates

First, create tax rates for regions you need to collect taxes for. If you’re working with a small number of tax rates, it’s often simpler to use the [Dashboard](https://dashboard.stripe.com/test/tax-rates) to create and manage them. After creating tax rates, you can pass them as either [fixed](https://docs.stripe.com/payments/checkout/use-manual-tax-rates.md#fixed-tax-rates) or [dynamic tax rates](https://docs.stripe.com/payments/checkout/use-manual-tax-rates.md#dynamic-tax-rates) to the Checkout Session.

#### Create tax rates with the API

The following example demonstrates how you can create a tax rate with the API.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const taxRate = await stripe.taxRates.create({
  display_name: "Sales Tax",
  inclusive: false,
  percentage: 7.25,
  country: "US",
  state: "CA",
  jurisdiction: "US - CA",
  description: "CA Sales Tax",
});
```

Required properties:

- The `display_name` is a short-name that describes the specific type of tax, such as `Sales`, `VAT`, or `GST`.
- The `inclusive` property determines whether the tax `percentage` is either added to, or included in, the overall amount.
- The `percentage` is a number (up to 4 decimal places) that represents the tax percentage to be collected.

Optional properties:

- The optional `country` property is a valid [two-letter ISO country code](https://www.nationsonline.org/oneworld/country_code_list.htm). Some countries (for example, United States) require an additional two-letter `state` property. Use these properties to apply dynamic tax rates based on your customer’s billing or shipping address in Checkout Sessions.

- The optional `jurisdiction` property represents the tax rate’s tax jurisdiction and you can use it to differentiate between tax rates of the same percentage. In the Dashboard, jurisdiction appears as the tax rate’s _Region_ label.

- You can also store additional details in the `description`. This property isn’t exposed to your customers.

> The `percentage`, `country`, and `state` properties are immutable and can only be set when you create the tax rate. This is to ensure existing subscriptions and invoices using tax rates aren’t affected. If you need to update these properties, create a new tax rate and archive the old object.

## Fixed tax rates

- For one-time payments, pass the Tax Rate ID to [line_item.tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-tax_rates).
- For recurring payments, pass the Tax Rate ID to [subscription_data.default_tax-rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-default_tax_rates).

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
      tax_rates: ["{{TAXRATE_ID}}"],
    },
  ],
  mode: "payment",
  success_url: "https://example.com/success",
});
```

#### Recurring payments

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
  subscription_data: {
    default_tax_rates: ["{{TAXRATE_ID}}"],
  },
  mode: "subscription",
  success_url: "https://example.com/success",
});
```

## Dynamic tax rates

Pass the array of tax rates to [line_items.dynamic_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates). Each tax rate must have a [supported country](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates), and for the US, a `state`. The current list of supported countries are:

- AT
- AU
- BE
- BG
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
- LT
- LU
- LV
- MT
- NL
- PL
- PT
- RO
- SE
- SI
- SK
- US

This list matches tax rates to your customer’s [shipping address](https://docs.stripe.com/payments/collect-addresses.md?payment-ui=checkout) or billing address. The shipping address takes precedence over the billing address for determining the tax rate to charge.

Billing address collection is automatically enabled when using dynamic tax rates. If you’re not collecting a shipping address, your customer’s billing address is used to determine the tax rate. If you haven’t passed a tax rate that matches your customer’s shipping or billing address, no tax rate is applied.

> [line_items.tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-tax_rates) can’t be used in combination with [line_items.dynamic_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
      dynamic_tax_rates: ["{{FIRST_TAX_RATE_ID}}", "{{SECOND_TAX_RATE_ID}}"],
    },
  ],
  mode: "payment",
  success_url: "https://example.com/success",
});
```

### Apple Pay and Google Pay

When using dynamic tax rates without [shipping_address_collection](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_address_collection), Apple Pay and Google Pay aren’t available to customers.

## Tax reporting and remittance

Any business collecting taxes ultimately needs to remit tax to the appropriate government. You can use Stripe’s data exports to populate the periodic reports that you’re required to make to taxation authorities.

### Data exports

From the Dashboard’s [Tax Rates list](https://dashboard.stripe.com/test/tax-rates/), you can export data files required for tax reporting calculations. Different Checkout modes require different processes.

#### Payment mode

When using Checkout in payment mode, use the following two tax reporting exports:

- **Checkout payment mode line item tax export**—Includes details down to the line-item level, including per-line-item tax rates, inclusive and exclusive, amounts, and so on. This is a lower-level export.
- **Checkout payment mode totals export**—Shows the aggregate tax collected on the Checkout Session as a whole, including adjustments for any refunds.

For remittance reporting, use the Checkout payment mode line item tax export to sum all of the amounts paid for all of the tax rates used. To factor in any refunds, you also need to pivot against the Checkout payment mode totals export.

#### Subscription mode

When using Checkout in subscription mode, use the [Stripe Billing tax exports](https://docs.stripe.com/billing/taxes/tax-rates.md#remittance) instead.

# Embedded page

> This is a Embedded page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/use-manual-tax-rates?payment-ui=embedded-form.

Stripe supports manually defining [Tax Rates](https://docs.stripe.com/api/tax_rates.md) to collect taxes (sales, VAT, GST, and others) for different locations. However, [Stripe Tax](https://docs.stripe.com/payments/checkout/taxes.md) is recommended instead of manual tax rates to automatically enable support for 60+ countries.

There are two ways to collect taxes in Checkout:

- Use _fixed tax rates_ when you know the exact tax rate to charge your customer before they start the checkout process (for example, you only sell to customers in the UK and always charge 20% VAT).
- Use _dynamic tax rates_ with the Prices API when you need more information from your customer (for example, their billing or shipping address) to determine the tax rate to charge. With dynamic tax rates, you create tax rates for different regions (for example, a 20% VAT tax rate for customers in the UK and a 7.25% sales tax rate for customers in California, US) and Stripe attempts to match your customer’s location to one of those tax rates.

## Create tax rates

First, create tax rates for regions you need to collect taxes for. If you’re working with a small number of tax rates, it’s often simpler to use the [Dashboard](https://dashboard.stripe.com/test/tax-rates) to create and manage them. After creating tax rates, you can pass them as either [fixed](https://docs.stripe.com/payments/checkout/use-manual-tax-rates.md#fixed-tax-rates) or [dynamic tax rates](https://docs.stripe.com/payments/checkout/use-manual-tax-rates.md#dynamic-tax-rates) to the Checkout Session.

#### Create tax rates with the API

The following example demonstrates how you can create a tax rate with the API.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const taxRate = await stripe.taxRates.create({
  display_name: "Sales Tax",
  inclusive: false,
  percentage: 7.25,
  country: "US",
  state: "CA",
  jurisdiction: "US - CA",
  description: "CA Sales Tax",
});
```

Required properties:

- The `display_name` is a short-name that describes the specific type of tax, such as `Sales`, `VAT`, or `GST`.
- The `inclusive` property determines whether the tax `percentage` is either added to, or included in, the overall amount.
- The `percentage` is a number (up to 4 decimal places) that represents the tax percentage to be collected.

Optional properties:

- The optional `country` property is a valid [two-letter ISO country code](https://www.nationsonline.org/oneworld/country_code_list.htm). Some countries (for example, United States) require an additional two-letter `state` property. Use these properties to apply dynamic tax rates based on your customer’s billing or shipping address in Checkout Sessions.

- The optional `jurisdiction` property represents the tax rate’s tax jurisdiction and you can use it to differentiate between tax rates of the same percentage. In the Dashboard, jurisdiction appears as the tax rate’s _Region_ label.

- You can also store additional details in the `description`. This property isn’t exposed to your customers.

> The `percentage`, `country`, and `state` properties are immutable and can only be set when you create the tax rate. This is to ensure existing subscriptions and invoices using tax rates aren’t affected. If you need to update these properties, create a new tax rate and archive the old object.

## Fixed tax rates

- For one-time payments, pass the Tax Rate ID to [line_item.tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-tax_rates).
- For recurring payments, pass the Tax Rate ID to [subscription_data.default_tax-rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-default_tax_rates).

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
      tax_rates: ["{{TAXRATE_ID}}"],
    },
  ],
  mode: "payment",
  ui_mode: "embedded_page",
  return_url:
    "https://example.com/return.html?session_id={CHECKOUT_SESSION_ID}",
});
```

#### Recurring payments

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
  subscription_data: {
    default_tax_rates: ["{{TAXRATE_ID}}"],
  },
  mode: "subscription",
  ui_mode: "embedded_page",
  return_url:
    "https://example.com/return.html?session_id={CHECKOUT_SESSION_ID}",
});
```

## Dynamic tax rates

Pass the array of tax rates to [line_items.dynamic_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates). Each tax rate must have a [supported country](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates), and for the US, a `state`. The current list of supported countries are:

- AT
- AU
- BE
- BG
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
- LT
- LU
- LV
- MT
- NL
- PL
- PT
- RO
- SE
- SI
- SK
- US

This list matches tax rates to your customer’s [shipping address](https://docs.stripe.com/payments/collect-addresses.md?payment-ui=checkout) or billing address. The shipping address takes precedence over the billing address for determining the tax rate to charge.

Billing address collection is automatically enabled when using dynamic tax rates. If you’re not collecting a shipping address, your customer’s billing address is used to determine the tax rate. If you haven’t passed a tax rate that matches your customer’s shipping or billing address, no tax rate is applied.

> [line_items.tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-tax_rates) can’t be used in combination with [line_items.dynamic_tax_rates](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items-dynamic_tax_rates).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
      dynamic_tax_rates: ["{{FIRST_TAX_RATE_ID}}", "{{SECOND_TAX_RATE_ID}}"],
    },
  ],
  mode: "payment",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
});
```

### Apple Pay and Google Pay

When using dynamic tax rates without [shipping_address_collection](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_address_collection), Apple Pay and Google Pay aren’t available to customers.

## Tax reporting and remittance

Any business collecting taxes ultimately needs to remit tax to the appropriate government. You can use Stripe’s data exports to populate the periodic reports that you’re required to make to taxation authorities.

### Data exports

From the Dashboard’s [Tax Rates list](https://dashboard.stripe.com/test/tax-rates/), you can export data files required for tax reporting calculations. Different Checkout modes require different processes.

#### Payment mode

When using Checkout in payment mode, use the following two tax reporting exports:

- **Checkout payment mode line item tax export**—Includes details down to the line-item level, including per-line-item tax rates, inclusive and exclusive, amounts, and so on. This is a lower-level export.
- **Checkout payment mode totals export**—Shows the aggregate tax collected on the Checkout Session as a whole, including adjustments for any refunds.

For remittance reporting, use the Checkout payment mode line item tax export to sum all of the amounts paid for all of the tax rates used. To factor in any refunds, you also need to pivot against the Checkout payment mode totals export.

#### Subscription mode

When using Checkout in subscription mode, use the [Stripe Billing tax exports](https://docs.stripe.com/billing/taxes/tax-rates.md#remittance) instead.
