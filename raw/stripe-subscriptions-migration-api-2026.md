<!-- Source URL: https://docs.stripe.com/billing/subscriptions/import-subscriptions -->
<!-- Fetched: 2026-05-12 -->

# Migrate subscriptions to Stripe Billing using Stripe APIs

Learn how to migrate your existing subscriptions to Stripe using Stripe APIs.

Learn how to migrate your existing _subscriptions_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) from a third-party, an in-house system, or an existing Stripe account to Stripe Billing using Stripe APIs.

## Before you begin

1. If you haven’t already, review the [migration stages](https://docs.stripe.com/billing/subscriptions/migrate-subscriptions.md).
1. [Set up a Stripe Billing integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md). This prerequisite is only required once before importing subscriptions to Stripe, and you don’t need to repeat it for future migrations.
1. [Request a PAN data import](https://docs.stripe.com/get-started/data-migrations/pan-import.md) from your current processor. If you’re attempting a Stripe-to-Stripe migration, this prerequisite isn’t necessary because you’re already using Stripe for payment processing.

## Manage legacy products and prices

If you have _legacy_ (Technology that's no longer recommended) _pricing model_ (The pricing model consists of the products or services you sell, how much they cost, what currency you accept for payments, and the service period to charge (for subscriptions). To build the pricing model, you use Products—what you sell—and Prices—how much and how often to charge for your products)s that you need to continue supporting in Stripe, create a placeholder product, such as `Legacy plan`. Here’s an example:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  id: "{{NEW_PRODUCT_ID}}",
  name: "Legacy plan",
  description: "Imported legacy plan from source system",
  metadata: {
    OLD_PRODUCT_ID: "{{OLD_PRODUCT_ID}}",
  },
});
```

When you need to update subscriptions with legacy plans, pass in the prices as needed using `items.price_data`. This overrides any existing legacy price. To learn more, see [variable pricing](https://docs.stripe.com/products-prices/how-products-and-prices-work.md#variable-pricing).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price_data: {
        currency: "USD",
        product: "{{PRODUCT_ID}}",
        recurring: {
          interval: "month",
          interval_count: 3,
        },
        unit_amount: 1000,
      },
      quantity: 1,
    },
  ],
});
```

## Import your subscriptions

After you import your customers and create a pricing model, you can start importing your subscriptions. You should be able to export subscription data from third-party systems through their UI or API. Contact your subscriptions processor if they don’t provide this option through either interface.

To import subscriptions, use your list of customers to create the appropriate subscription for each one. For example, if a subscriber has a monthly `Basic` pricing plan in your old model, use the monthly recurring price associated with that level when you create their subscription in Stripe.

### Make source data Stripe-compatible

Before you start importing subscriptions into Stripe, make sure that all of your source data is compatible with our expected format.

#### Important fields for migrating subscriptions

If you use relevant subscription data in your custom integration that Stripe doesn’t also use, you can apply your data to the `metadata` field of the subscriptions you create in Stripe. The following table describes other important fields to consider when importing subscriptions.

| Field                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [customer](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-customer)                                 | Make sure that you’ve properly mapped the customer ID from your source data to the new customer ID in Stripe.                                                                                                                                                                                                                |
| [phases.items.price](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-phases-items-price)             | Make sure that you’ve mapped the price ID from your source data to the new price ID in Stripe.                                                                                                                                                                                                                               |
| [current_phase.start_date](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-current_phase-start_date) | Make sure that the subscription schedule you define in Stripe lines up with and maintains continuity from your original source data. For example, if a customer has 6 months left on a yearly subscription in your source system, make sure that `billing_cycle_anchor` and `start_date` reflect the correct mid-cycle term. |
| Third-party metadata                                                                                                                           | Import any additional data fields from your source data, which might include product names, plan names, and third-party application IDs.                                                                                                                                                                                     |
| Tax settings                                                                                                                                   | Include any tax IDs, VAT IDs, or other tax information.                                                                                                                                                                                                                                                                      |

#### Prepare legacy prices

If you created placeholders for [legacy prices](https://docs.stripe.com/billing/subscriptions/import-subscriptions.md#legacy-prices), you need to map those prices to the subscriptions and customers you’re importing. For each subscription with a legacy price, use the [price_data](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data) parameter of the [Subscriptions](https://docs.stripe.com/api/subscriptions.md#subscriptions) API to pass in information about the price and subscription. The required fields are:

| Parameter                                                                                                                                     | Description                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [currency](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data-currency)                                 | Currency of the price, in three-letter ISO format.                                                                                                                                                                                                                                 |
| [product](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data-product)                                   | ID of the placeholder product. You can use this for all of the legacy prices.                                                                                                                                                                                                      |
| [recurring](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data-recurring)                               | Information about the amount and frequency of the recurring price.                                                                                                                                                                                                                 |
| [recurring.interval](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data-recurring)                      | Frequency of the interval-`day`, `week`, `month`, or `year`.                                                                                                                                                                                                                       |
| [recurring.interval_count](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data-recurring-interval_count) | Number of intervals between billings. For example, setting `interval=day` and `interval_count=30` means that you bill the customer every 30 days. The maximum interval is 1 year (1 year, 12 months, or 52 weeks).                                                                 |
| [recurring.unit_amount_decimal](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data-unit_amount_decimal) | Same as [unit_amount](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data-unit_amount), but allows you to specify more granular decimal amounts in cents, up to 12 decimals. You can only set one of `unit_amount` and `unit_amount_decimal`. |

### Import subscription data into Stripe

After you’ve prepared your source data, you can start importing subscriptions into Stripe.

#### Testing

Use a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) to run through the pricing model import process at least once before running the import in live mode. You need to remap your script:

- If you wipe the data in a sandbox and rerun the import.
- When you move to live mode, because the price IDs are different in a sandbox and live mode.

In a sandbox, you can use [test clocks](https://docs.stripe.com/billing/testing/test-clocks.md) to simulate subscriptions advancing through time. This allows you to see how the migrated subscriptions work in production.

#### Create subscriptions

While you can use the [Subscription](https://docs.stripe.com/api/subscriptions.md) API to create subscriptions, we recommend using the [Subscription Schedules](https://docs.stripe.com/api/subscription_schedules.md) API. With this API, you can schedule subscriptions to start in the future. For example, it’s the only way to start monthly subscriptions more than 30 days in advance. The ability to start subscriptions in the future also allows you to review the import before you start to bill your customers in production.

Additionally, the Subscription Schedules API provides `phases`, which provide much more flexibility in defining settings such as tax behavior, collection method, and coupon usage within more granular intervals. You can also define different behavior for different intervals. For example, you could apply a coupon only for the first 3 months of a yearly subscription.

Here’s how to create subscriptions that start on June 1, 2022 at 12:00 AM UTC.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer: "{{CUSTOMER_ID}}",
  default_settings: {
    billing_cycle_anchor: "phase_start",
  },
  phases: [
    {
      items: [
        {
          price: "{{PRICE_ID}}",
        },
      ],
    },
  ],
  start_date: 1654066801,
});
```

## Confirm your migration

After you’ve imported your subscriptions, use the API to confirm that the subscriptions exist in Stripe.

Use the [list Subscriptions](https://docs.stripe.com/api/subscriptions/list.md) API to view all of the Subscriptions in Stripe. You can pass the [created](https://docs.stripe.com/api/subscriptions/list.md#list_subscriptions-created) parameter to filter for recently created Subscriptions.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptions = await stripe.subscriptions.list({
  created: {
    gt: 1647294709,
  },
});
```

## See also

- [Subscriptions schedules](https://docs.stripe.com/api/subscription_schedules.md)
