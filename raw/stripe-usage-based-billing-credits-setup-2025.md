<!-- Source URL: https://docs.stripe.com/billing/subscriptions/usage-based/set-up-billing-credits -->
<!-- Fetched: 2026-05-05 -->

# Set up billing credits

Learn how to implement a prepaid billing solution with billing credits.

Use [Meters](https://docs.stripe.com/api/billing/meter.md) and [billing credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits.md) to offer credits to your customers when they prepay for usage-based products or services, or as a promotional offering.

## Before you begin

Before you can use billing credits, you must [set up usage-based billing](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide.md):

1. Create a [billing meter](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide.md#create-meter).
1. Create a [pricing model](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide.md#create-pricing-model) and add the meter to it.
1. Create a [subscription](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide.md#create-subscription) that includes your customer, product, and usage-based price.

## Grant billing credits to your customer

Use the Stripe Dashboard or API to create a credit grant for your customer.

Billing credits only apply to [subscription](https://docs.stripe.com/api/invoices/object.md#invoice_object-subscription) line items that link to a [meter price](https://docs.stripe.com/api/prices/object.md#price_object-recurring-meter). The ([Usage Records API](https://docs.stripe.com/api/usage_records.md)) isn’t supported.

#### Dashboard

1. On the [Customers](https://dashboard.stripe.com/test/customers) page, select the customer name.
1. On the customer page, under **Credit grants**, click the plus (**+**) symbol.
1. On the **New credit grant** page, do the following:

- For **Name**, enter a name for your credit grant.
- For **Amount**, specify the amount of the credit grant.
- (Optional) Under **Effective date**, specify a date for when to grant the credit.
- (Optional) Under **Expiry date**, specify the date, if any, when the credits expire.
- (Optional) Under **Priority**, specify the priority for this credit grant.
- (Optional) Under **Eligibility**, specify a list of usage-based prices that this credit grant applies to.
- Click **Create grant**.

#### API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const creditGrant = await stripe.billing.creditGrants.create({
  customer: "{{CUSTOMER_ID}}",
  name: "Credit grant",
  applicability_config: {
    scope: {
      price_type: "metered",
    },
  },
  category: "paid",
  amount: {
    type: "monetary",
    monetary: {
      value: 1000,
      currency: "usd",
    },
  },
});
```

To create a credit grant that only applies to a specific metered item, pass the ID in the [billable_items](https://docs.stripe.com/api/billing/credit-grant/create.md?api-version=preview#create_billing_credit_grant-applicability_config-scope-billable_items) array:

```curl
curl https://api.stripe.com/v1/billing/credit_grants \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d customer={{CUSTOMER_ID}} \
  -d "name=Credit grant" \
  -d "applicability_config[scope][billable_items][0][id]={{BILLABLE_ITEM_ID}}" \
  -d category=paid \
  -d "amount[type]=monetary" \
  -d "amount[monetary][value]=1000" \
  -d "amount[monetary][currency]=usd"
```

## Apply billing credits to invoices

After the invoice finalizes, Stripe automatically applies all applicable billing credits. The available balance on the credit grant updates based on the amount of billing credits applied to the invoice.

You can find the amount of billing credits applied to an invoice in the Stripe Dashboard.

1. On the [Customers](https://dashboard.stripe.com/test/customers) page, select the customer name.
1. On the customer page, under **Invoices**, select an invoice.
1. On the invoice page, under **Subtotal**, find the line for **Credit grant applied**.

## Retrieve the available billing credit balance

Use the Stripe Dashboard or API to see the available billing credit balance for a customer. When using the API, retrieve the [Credit Balance Summary](https://docs.stripe.com/api/billing/credit-balance-summary/retrieve.md) endpoint.

#### Dashboard

1. On the [Customers](https://dashboard.stripe.com/test/customers) page, select the customer name.
1. On the customer page, under **Credit grants**, find the list of credit grants that can apply to invoices. You can see the credit grant’s [available_balance](https://docs.stripe.com/api/billing/credit-balance-summary/object.md#billing_credit_balance_summary_object-balances-available_balance) in the **Available** column.

#### API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const creditBalanceSummary = await stripe.billing.creditBalanceSummary.retrieve(
  {
    customer: "{{CUSTOMER_ID}}",
    filter: {
      type: "applicability_scope",
      applicability_scope: {
        price_type: "metered",
      },
    },
  },
);
```

## List transactions for a credit grant

Use the Stripe Dashboard or API to see the transactions for a specific credit grant or customer. When using the API, call the [Credit Balance Transaction](https://docs.stripe.com/api/billing/credit-balance-transaction/list.md) endpoint.

#### Dashboard

1. On the [Customers](https://dashboard.stripe.com/test/customers) page, select the customer name.
1. On the customer page, under **Credit grants**, select a credit grant.
1. View details for the credit balance transactions.

#### API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const creditBalanceTransactions =
  await stripe.billing.creditBalanceTransactions.list({
    customer: "{{CUSTOMER_ID}}",
    credit_grant: "{{CREDIT_GRANT_ID}}",
  });
```

## Optional: Fund the credit grant

Use the Stripe Dashboard or API to create a one-off [invoice](https://docs.stripe.com/invoicing.md) to collect payment from a customer. When using the API, listen for the `invoice.paid` [webhook](https://docs.stripe.com/webhooks.md) and grant billing credits to your customer.

#### Dashboard

1. On the [Customers](https://dashboard.stripe.com/test/customers) page, select the customer name.
1. On the customer page, click **Create invoice**.
1. Follow the instructions to [create an invoice](https://docs.stripe.com/invoicing/dashboard.md).

#### API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoice = await stripe.invoices.create({
  customer: "{{CUSTOMER_ID}}",
  description: "credit purchase",
  collection_method: "charge_automatically",
});
```

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoiceItem = await stripe.invoiceItems.create({
  customer: "{{CUSTOMER_ID}}",
  description: "billing credits purchase",
  unit_amount_decimal: Decimal.from("1000"),
  currency: "usd",
  invoice: "{{INVOICE_ID}}",
});
```

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoice = await stripe.invoices.finalizeInvoice("{{INVOICE_ID}}", {
  auto_advance: true,
});
```

## See also

- [Credit application eligibility](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits.md#credit-grant-eligibility)
- [Usage-based billing](https://docs.stripe.com/billing/subscriptions/usage-based.md)
