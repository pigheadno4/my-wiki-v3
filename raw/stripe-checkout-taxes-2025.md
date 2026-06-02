<!-- Source: Stripe Checkout — Collect taxes -->
<!-- Fetched: 2026-04-20 -->

# Collect taxes

Learn how to collect taxes with Stripe Tax.

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/taxes?payment-ui=stripe-hosted.

Stripe Tax allows you to calculate the tax on your one-time and recurring payments when you use Checkout. You can enable Stripe Tax to automatically compute taxes on all of your Checkout purchases and subscriptions.

## Create a Checkout Session

You can create Checkout sessions for one-time and recurring purchases.

To calculate tax for new customers, Checkout validates and uses the provided shipping or billing address. For existing customers, Checkout calculates tax by validating and using the attached customer shipping or billing address. If you capture a new billing or shipping address for an existing customer, Checkout doesn’t automatically override the previous billing or shipping information. You must explicitly request customer address changes.

### Apple Pay and Google Pay

To ensure that Google Pay is offered as a payment method while using Stripe Tax in Checkout, you must either require collecting a shipping address, or provide an existing customer with a saved shipping address. Apple Pay with Stripe Tax displays only when the customer’s browser supports Apple Pay version 12 or greater.

## Calculate tax for new customers

If you don’t pass in an existing customer when creating a Checkout session, Checkout creates a new customer and automatically saves the billing address and shipping information. Checkout uses the shipping address entered during the session to determine the customer’s location for calculating tax. If you don’t collect shipping information, Checkout uses the billing address.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  mode: "payment",
  success_url: "https://example.com/success",
});
```

## Optional: Update your products and prices

Stripe Tax uses information stored on _products_ (Products represent what your business sells—whether that's a good or a service) and _prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) to calculate tax, such as _tax code_ (A tax code is the category of your product for tax purposes) and _tax behavior_ (Tax behavior determines whether you want to include taxes in the price ("inclusive") or add them on top ("exclusive")). If you don’t explicitly specify these configurations, Stripe Tax will use the default tax code selected in [Tax Settings](https://dashboard.stripe.com/settings/tax).

For more information, see [Specify product tax codes and tax behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md).

## Optional: Calculate tax for existing customers

To calculate tax on an existing customer’s Checkout session, set the `automatic_tax[enabled]` parameter to `true` when you create the session. You can base the tax calculations on the customer’s existing addresses or the new addresses that you collected during checkout:

### Use existing addresses on the customer for taxes

If you’ve already collected your existing customers’ addresses, you can base the tax calculations on those addresses rather than the addresses collected during checkout:

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

If available, Checkout uses the customer’s [configuration.customer.shipping.address](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer-shipping-address) to calculate taxes. Otherwise, it uses the customer’s billing address ([identity.individual.address](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-identity-individual-address) or [identity.business_details.address](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-identity-business_details-address)). You can verify that a customer’s saved addresses are valid by checking that their [configuration.customer.capabilities.automatic_indirect_tax.status](https://docs.stripe.com/api/v2/core/accounts/retrieve.md#v2_retrieve_accounts-response-configuration-customer-capabilities-automatic_indirect_tax-status) is `active`. This property is only available after you request the capability by setting [configuration.customer.capabilities.automatic_indirect_tax.requested](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer-capabilities-automatic_indirect_tax-requested) to true.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  mode: "payment",
  success_url: "https://example.com/success",
});
```

#### Customers v1

If available, Checkout uses the customer’s [shipping.address](https://docs.stripe.com/api/customers/object.md#customer_object-shipping-address) to calculate taxes. Otherwise, it uses the customer’s billing address ([address](https://docs.stripe.com/api/customers/object.md#customer_object-address)) to calculate taxes. You can verify that a customer’s saved addresses are valid by checking their [tax.automatic_tax](https://docs.stripe.com/api/customers/object.md#customer_object-tax-automatic_tax) property. If `tax.automatic_tax` is `supported` or `not_collecting`, the customer’s saved addresses are valid, and you can enable Stripe Tax on Checkout sessions for that customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  customer: "{{CUSTOMER_ID}}",
  mode: "payment",
  success_url: "https://example.com/success",
});
```

### Use addresses collected during Checkout for taxes

You can configure Checkout to save a customer’s new billing or shipping addresses. In this case, Checkout calculates the tax by using the address entered during checkout.

#### Accounts v2

If you [collect shipping addresses](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_address_collection), Checkout saves the shipping address entered during the session to the customer’s [configuration.customer.shipping](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer-shipping) property and uses it to calculate taxes. Otherwise, Checkout saves the billing address entered during the session to the customer’s [identity.individual.address](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-identity-individual-address) property and uses it to calculate taxes. In both cases, the address entered during checkout replaces any existing address.

If you collect shipping addresses with Checkout, set the `customer_update.shipping` property to `auto`. This automatically copies the shipping information from Checkout to the customer’s `Account`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  customer_update: {
    shipping: "auto",
  },
  shipping_address_collection: {
    allowed_countries: ["US"],
  },
  mode: "payment",
  success_url: "https://example.com/success",
});
```

If you don’t collect shipping addresses with Checkout, and you want Stripe Tax to use billing addresses entered during checkout, you must save the billing address to the customer. Set the `customer_update.address` property to `auto` to automatically copy the entered address to the customer’s `Account`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  customer_update: {
    address: "auto",
  },
  mode: "payment",
  success_url: "https://example.com/success",
});
```

#### Customers v1

If you [collect shipping addresses](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_address_collection), Checkout saves the shipping address entered during the session to the customer’s [shipping.address](https://docs.stripe.com/api/customers/object.md#customer_object-shipping-address) property and uses it to calculate taxes. Otherwise, Checkout saves the billing address entered during the session to the customer’s [address](https://docs.stripe.com/api/customers/object.md#customer_object-address) property and uses it to calculate taxes. In both cases, the address entered during checkout replaces any existing address.

If you collect shipping addresses with Checkout, set the `customer_update.shipping` property to `auto`. This automatically copies the shipping information from Checkout to the customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  customer: "{{CUSTOMER_ID}}",
  customer_update: {
    shipping: "auto",
  },
  shipping_address_collection: {
    allowed_countries: ["US"],
  },
  mode: "payment",
  success_url: "https://example.com/success",
});
```

If you don’t collect shipping addresses with Checkout, and you want to use billing addresses entered during checkout for taxes, you must save the billing address to the customer. Set the `customer_update.address` property to `auto` to automatically copy the entered address to the `Customer`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  customer: "{{CUSTOMER_ID}}",
  customer_update: {
    shipping: "auto",
  },
  mode: "payment",
  success_url: "https://example.com/success",
});
```

## Optional: Check the response

To see the results of the latest tax calculation, the [total_details.amount_tax](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-total_details) property in the Checkout Session resource shows the calculated tax amount. Additionally, you can use the [Dashboard](https://dashboard.stripe.com/) to view the tax outcome for each payment.

# Embedded page

> This is a Embedded page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/taxes?payment-ui=embedded-form.

Stripe Tax allows you to calculate the tax on your one-time and recurring payments when you use Checkout. You can enable Stripe Tax to automatically compute taxes on all of your Checkout purchases and subscriptions.

## Create a Checkout Session

After updating your products and prices, you’re ready to start calculating tax on your Checkout sessions. You can create sessions for one-time and recurring purchases.

To calculate tax for new customers, Checkout validates and uses the provided shipping or billing address. For existing customers, Checkout calculates tax by validating and using the attached customer shipping or billing address. If you capture a new billing or shipping address for an existing customer, Checkout won’t automatically override the previous billing or shipping information. You must explicitly request customer address changes.

### Apple Pay and Google Pay

To ensure that Google Pay is offered as a payment method while using Stripe Tax in Checkout, you must either require collecting a shipping address, or provide an existing customer with a saved shipping address. Apple Pay with Stripe Tax displays only when the customer’s browser supports Apple Pay version 12 or greater.

## Calculate tax for new customers

If you don’t pass in an existing customer when creating a Checkout session, Checkout creates a new customer and automatically saves the billing address and shipping information. Checkout uses the shipping address entered during the session to determine the customer’s location for calculating tax. If you don’t collect shipping information, Checkout uses the billing address.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  mode: "payment",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
});
```

## Optional: Update your products and prices

Stripe Tax uses information stored on _products_ (Products represent what your business sells—whether that's a good or a service) and _prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) to calculate tax, such as _tax code_ (A tax code is the category of your product for tax purposes) and _tax behavior_ (Tax behavior determines whether you want to include taxes in the price ("inclusive") or add them on top ("exclusive")). If you don’t explicitly specify these configurations, Stripe Tax will use the default tax code selected in [Tax Settings](https://dashboard.stripe.com/settings/tax).

For more information, see [Specify product tax codes and tax behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior.md).

## Optional: Calculate tax for existing customers

To calculate tax on an existing customer’s Checkout session, set the `automatic_tax.enabled` parameter to true when you create the session. You can base the tax calculations on the customer’s existing addresses or the new addresses that you collected during checkout:

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/connect/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

### Use existing addresses on the customer for taxes

If you already collected your existing customers’ addresses, you can base the tax calculations on those addresses rather than the addresses collected during checkout:

#### Accounts v2

If available, Checkout uses the customer’s [configuration.customer.shipping.address](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer-shipping-address) to calculate taxes. Otherwise, it uses the customer’s billing address ([identity.individual.address](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-identity-individual-address) or [identity.business_details.address](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-identity-business_details-address)). You can verify that a customer’s saved addresses are valid by checking that their [configuration.customer.capabilities.automatic_indirect_tax.status](https://docs.stripe.com/api/v2/core/accounts/retrieve.md#v2_retrieve_accounts-response-configuration-customer-capabilities-automatic_indirect_tax-status) is `active`. This property is only available after you request the capability by setting [configuration.customer.capabilities.automatic_indirect_tax.requested](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer-capabilities-automatic_indirect_tax-requested) to true.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  mode: "payment",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
});
```

#### Customers v1

If available, Checkout uses the customer’s [shipping.address](https://docs.stripe.com/api/customers/object.md#customer_object-shipping-address) to calculate taxes. Otherwise, it uses the customer’s billing address ([address](https://docs.stripe.com/api/customers/object.md#customer_object-address)) to calculate taxes. You can verify that a customer’s saved addresses are valid by checking their [tax.automatic_tax](https://docs.stripe.com/api/customers/object.md#customer_object-tax-automatic_tax) property. If `tax.automatic_tax` is `supported` or `not_collecting`, the customer’s saved addresses are valid, and you can enable Stripe Tax on Checkout sessions for that customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  customer: "{{CUSTOMER_ID}}",
  mode: "payment",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
});
```

### Use addresses collected during Checkout for taxes

You can configure Checkout to save a customer’s new billing or shipping addresses. In this case, Checkout calculates the tax by using the address entered during checkout.

#### Accounts v2

If you [collect shipping addresses](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_address_collection), Checkout saves the shipping address entered during the session to the customer’s [configuration.customer.shipping](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer-shipping) property and uses it to calculate taxes. Otherwise, Checkout saves the billing address entered during the session to the customer’s [identity.individual.address](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-identity-individual-address) property and uses it to calculate taxes. In both cases, the address entered during checkout replaces any existing address.

If you collect shipping addresses with Checkout, set the `customer_update.shipping` property to `auto`. This automatically copies the shipping information from Checkout to the customer’s `Account`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  customer_update: {
    shipping: "auto",
  },
  shipping_address_collection: {
    allowed_countries: ["US"],
  },
  mode: "payment",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
});
```

If you don’t collect shipping addresses with Checkout, and you want to use billing addresses entered during checkout for taxes, you must save the billing address to the customer. Set the `customer_update.address` property to `auto` to automatically copy the entered address to the customer’s `Account`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  customer_update: {
    address: "auto",
  },
  mode: "payment",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
});
```

#### Customers v1

If you [collect shipping addresses](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-shipping_address_collection), Checkout saves the shipping address entered during the session to the customer’s [shipping.address](https://docs.stripe.com/api/customers/object.md#customer_object-shipping-address) property and uses it to calculate taxes. Otherwise, Checkout saves the billing address entered during the session to the customer’s [address](https://docs.stripe.com/api/customers/object.md#customer_object-address) property and uses it to calculate taxes. In both cases, the address entered during checkout replaces any existing address.

If you collect shipping addresses with Checkout, set the `customer_update.shipping` property to `auto`. This automatically copies the entered shipping information from Checkout to the `Customer`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  customer: "{{CUSTOMER_ID}}",
  customer_update: {
    shipping: "auto",
  },
  shipping_address_collection: {
    allowed_countries: ["US"],
  },
  mode: "payment",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
});
```

If you don’t collect shipping addresses with Checkout, and you want to use billing addresses entered during checkout for taxes, you must save the billing address to the customer. Set the `customer_update.address` property to `auto` to automatically copy the entered address to the `Customer`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price: "{{PRICE_ID}}",
      quantity: 2,
    },
  ],
  automatic_tax: {
    enabled: true,
  },
  customer: "{{CUSTOMER_ID}}",
  customer_update: {
    address: "auto",
  },
  mode: "payment",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
});
```

## Optional: Check the response

To see the results of the latest tax calculation, the [total_details.amount_tax](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-total_details) property in the Checkout Session resource shows the calculated tax amount. Additionally, you can use the [Dashboard](https://dashboard.stripe.com/) to view the tax outcome for each payment.
