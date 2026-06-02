<!-- Source URL: https://docs.stripe.com/billing/subscriptions/usage-based/manage-billing -->
<!-- Fetched: 2026-05-05 -->

# Manage your usage-based billing setup

Learn how to handle billing-related tasks for your usage-based billing model.

After you create your usage-based billing model, you can modify different parts of your billing setup. For example, you can update a subscription item’s price during a billing period, backdate a subscription to include usage in the next invoice, or cancel usage-based subscriptions.

## Transform quantities

You can use the [transform_quantity](https://docs.stripe.com/api/prices/create.md#create_price-transform_quantity) option to transform usage before applying the price, which you can use when you want pricing on packages of a product instead of individual units. This allows you to divide the reported usage by a specific number and round the result up or down.

> Quantity transformation isn’t compatible with [tiered pricing](https://docs.stripe.com/billing/subscriptions/usage-based/thresholds.md#tiered-pricing-threshold).

For example, say you have a car rental service and you want to charge customers for each hour they rent a car. In this case, you report usage as a number of minutes.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const product = await stripe.products.create({
  name: "Car Rental Service",
});
```

Create a price for the car rental service product. Charge 10 USD per hour, and round up to charge for a full hour, even if the customer uses only part of the hour.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  nickname: "Car Rental Per Hour Rate",
  unit_amount: 1000,
  currency: "usd",
  recurring: {
    interval: "month",
    usage_type: "metered",
  },
  product: "{{CAR_RENTAL_SERVICE_PRODUCT_ID}}",
  transform_quantity: {
    divide_by: 60,
    round: "up",
  },
});
```

If a customer rents the car for 150 minutes, that customer is charged 30 USD for 3 hours of rental (2 hours and 30 minutes, rounded up).

## Update prices mid-cycle

You can update a subscription item’s price during a billing period.

With `billing_mode=flexible` subscriptions, we create an invoice item that bills for previously reported metered usage when you remove a metered price from a subscription.

For example, say you have a monthly subscription that you switch from price A to price B on January 16. On January 16, we create an invoice item billing for usage from January 1 to January 16. When the subscription renews on February 1, we bill for price B from January 16 to February 1.

The [proration_behavior](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-proration_behavior) you specify when removing a metered price affects these metered invoice items. If you want to remove a metered price without billing for it, set `proration_behavior` to `none`.

With `billing_mode=classic` subscriptions, limitations apply when switching from one [meter price](https://docs.stripe.com/api/prices/object.md#price_object-recurring-meter) to another.

On future invoices, we reflect only usage that occurs after the update. For example, say you have a monthly subscription that you switch from price A to price B on January 16. At the end of the month, the invoice includes usage from January 16 to January 31 at price B. Usage from January 1 to January 16 isn’t billed.

An exception exists if you use [billing thresholds](https://docs.stripe.com/billing/subscriptions/usage-based/thresholds.md) and have a threshold invoice already generated at the old price. For example, say you generate a threshold invoice on January 10 using price A. You still charge that threshold invoice to the customer. At the end of the month, the invoice includes usage from January 16 to January 31 at price B. The earlier threshold invoice doesn’t offset any usage for this end-of-month invoice.

Similar restrictions apply if you add a new subscription item with a billing meter price in the middle of the service period. For example, say you add a new subscription item with price C on January 16. At the end of the month, the invoice includes usage from January 16 to January 31 at price C for that subscription item.

To capture previously reported usage when changing prices, choose one of these options:

- Report the aggregated usage again to capture it in the cycle on the new price.
- Reset the [billing_cycle_anchor](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-billing_cycle_anchor) parameter to `now`, applying the old price to previously reported usage.

To update the price for a subscription item:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionItem = await stripe.subscriptionItems.update(
  "{{SUBSCRIPTION_ITEM_ID}}",
  {
    price: "{{NEW_PRICE_ID}}",
  },
);
```

To delete a subscription item:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const deleted = await stripe.subscriptionItems.del("{{SUBSCRIPTION_ITEM_ID}}");
```

After deletion, the invoice doesn’t reflect any usage from that item.

## Create a backdated subscription

You can record usage for a customer even before creating a subscription for them. After recording usage for a customer, use the [backdate_start_date](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-backdate_start_date) to create a subscription before the first report.

With `billing_mode=flexible` subscriptions, the subscription’s first invoice includes this backdated usage.

With `billing_mode=classic` subscriptions, the subscription’s next invoice, generated when it cycles, includes this backdated usage.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  backdate_start_date: 1710000000,
});
```

## Cancel usage-based subscriptions

With usage-based billing, the bill the customer pays varies based on consumption during the billing period. When changing the billing period results in a service period ending early, you charge the customer for the usage accrued during the shortened billing period.

> We don’t support [proration](https://docs.stripe.com/billing/subscriptions/prorations.md) with usage-based billing.

You can’t reactivate canceled subscriptions. Instead, you can collect updated billing information from your customer, update their default payment method, and create a new subscription with their existing customer record.

If you use [cancel_at_period_end](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-cancel_at_period_end) to schedule the cancellation of a subscription, you can reactivate the subscription at any time up to the end of the period. To do so, update `cancel_at_period_end` to `false`.

For subscriptions that cancel at the end of the period, the final invoice at the end of the period includes metered usage from the last billing period.
