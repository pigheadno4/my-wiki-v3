<!-- Source URL: https://docs.stripe.com/billing/subscriptions/mixed-interval -->
<!-- Fetched: 2026-05-13 -->

# Mixed interval subscriptions

Manage subscriptions for items with different intervals.

You can include multiple [subscription](https://docs.stripe.com/billing/subscriptions/overview.md) items with different prices and billing periods on a single subscription and Stripe automatically handles invoice generation.

For example, if you offer a service with an annual [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate), plus a monthly [usage-based fee](https://docs.stripe.com/billing/subscriptions/usage-based.md), you can include both prices as items on the same subscription. Stripe generates a single, combined invoice when item-level billing periods align and separate invoices when billing periods diverge.

> Mixed interval subscriptions must use [flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md). You must upgrade your API version to `2025-06-30.basil` or later to use flexible billing mode in the Dashboard and API.

# Dashboard

> This is a Dashboard for when dashboard-or-api is dashboard. View the full page at https://docs.stripe.com/billing/subscriptions/mixed-interval?dashboard-or-api=dashboard.

## Create a mixed interval subscription

1. Go to the [Subscriptions](https://dashboard.stripe.com/subscriptions) page in the Dashboard.
1. Select **+Create Subscription**.
1. Under **Billing and payment collection**, set **Billing mode** to **Flexible**.
1. Add products that bill on different intervals, such as monthy and yearly billing periods. Learn how to manage [products and prices](https://docs.stripe.com/products-prices/manage-prices.md).
1. Configure your **Subscription options**.
1. Click **Create the subscription**.

## Add mixed interval items to an existing subscription

1. Go to the [Subscriptions](https://dashboard.stripe.com/subscriptions) page in the Dashboard.
1. Find the subscripton, click its overflow menu (⋯), and click **Update Subscription**.
1. Add products that bill on different intervals, such as monthy and yearly billing periods. Learn how to manage [products and prices](https://docs.stripe.com/products-prices/manage-prices.md).
1. Click **Update Subscription**.

# API

> This is a API for when dashboard-or-api is api. View the full page at https://docs.stripe.com/billing/subscriptions/mixed-interval?dashboard-or-api=api.

## Create a mixed interval subscription

Call the [Create subscription](https://docs.stripe.com/api/subscriptions/create.md) endpoint. The following code sample creates a new subscription that charges 100 USD each quarter and 15 USD each month starting on January 1, 2024:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price_data: {
        currency: "usd",
        product: "{{PRODUCT_ID}}",
        recurring: {
          interval: "month",
          interval_count: 1,
        },
        unit_amount: 1500,
      },
      quantity: 1,
    },
    {
      price_data: {
        currency: "usd",
        product: "{{PRODUCT_ID}}",
        recurring: {
          interval: "month",
          interval_count: 3,
        },
        unit_amount: 10000,
      },
      quantity: 1,
    },
  ],
  collection_method: "send_invoice",
  days_until_due: 5,
  proration_behavior: "none",
  billing_mode: {
    type: "flexible",
  },
  expand: ["latest_invoice"],
});
```

The response returns the subscription with both items and bills for them on the first invoice (`latest_invoice`):

```json
{
  "object": "subscription",
  "id": "{{SUBSCRIPTION_ID}}",
  "current_period_start": 1704067200, // Jan 1 2024
  "current_period_end": 1706745600, // Feb 1 2024
  "items": {
    "data": [
      {
        "id": "si_A",
        "price": "price_id_monthly",
        "current_period_start": 1704067200, // Jan 1 2024
        "current_period_end": 1706745600 // Feb 1 2024
      },
      {
        "id": "si_B",
        "price": "price_id_quarterly",
        "current_period_start": 1704067200, // Jan 1 2024
        "current_period_end": 1711929600 // Apr 1 2024
      }
    ]
    // ...
  },
  "latest_invoice": {
    "object": "invoice",
    "id": "in_A",
    "created": 1704067200, // Jan 1 2024
    "period_start": 1704067200, // Jan 1 2024
    "period_end": 1704067200, // Jan 1 2024
    "lines": {
      "data": [
        {
          "description": "1 × Monthly Price (at $15.00 / month)",
          "period": {
            "start": 1704067200, // Jan 1 2024
            "end": 1706745600 // Feb 1 2024
          }
          // ...
        },
        {
          "description": "1 × Quarterly Price (at $100.00 every 3 months)",
          "period": {
            "start": 1704067200, // Jan 1 2024
            "end": 1711929600 // Apr 1 2024
          }
          // ...
        }
      ]
    }
    // ...
  }
  // ...
}
```

On February 1 and March 1, the subscription renews and generates a new invoice for the monthly item only. On April 1, the subscription renewal creates an invoice for both the monthly and quarterly item.

## Create a subscription schedule with mixed intervals

You can also use subscription schedules to create subscriptions using items with different prices and billing periods.

> We recommend you use `duration` in [Subscription Schedule](https://docs.stripe.com/api/subscription_schedules/create.md) endpoints. You can define time-based durations for subscription schedule phases (for example, “3 months”) rather than using phase iteration counts, enabling clearer modeling for subscriptions with mixed billing periods. Phase [iterations](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-phases-iterations) is deprecated.

The following code sample creates a subscription schedule with the same parameters as the subscription example:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer: "{{CUSTOMER_ID}}",
  start_date: "now",
  phases: [
    {
      items: [
        {
          price_data: {
            currency: "usd",
            product: "{{PRODUCT_ID}}",
            recurring: {
              interval: "month",
              interval_count: 1,
            },
            unit_amount: 1500,
          },
          quantity: 1,
        },
        {
          price_data: {
            currency: "usd",
            product: "{{PRODUCT_ID}}",
            recurring: {
              interval: "month",
              interval_count: 3,
            },
            unit_amount: 10000,
          },
          quantity: 1,
        },
      ],
      end_date: 1735718400,
    },
  ],
  billing_mode: {
    type: "flexible",
  },
  expand: ["subscription.latest_invoice"],
});
```

The response returns a subscription with both items and bills for them on the first invoice (`latest_invoice`):

```json
{
  "object": "subscription_schedule",
  "id": "{{SUBSCRIPTION_SCHEDULE_ID}}",
  "billing_mode": "flexible",
  "phases": {
    "data": [
      {
        "start_date": 1704096000, // Jan 1 2024
        "end_date": 1735718400, // Jan 1 2025
        "items": [
          {
            "price": "price_id_monthly"
            // ...
          },
          {
            "price": "price_id_quarterly"
            // ...
          }
        ]
      }
    ]
  },
  "subscription": {
    "items": {
      "data": [
        {
          "id": "si_A",
          "price": "price_id_monthly",
          "current_period_start": 1704067200, // Jan 1 2024
          "current_period_end": 1706745600 // Feb 1 2024
          // ...
        },
        {
          "id": "si_B",
          "price": "price_id_quarterly",
          "current_period_start": 1704067200, // Jan 1 2024
          "current_period_end": 1711929600 // Apr 1 2024
          // ...
        }
      ]
      // ...
    },
    "latest_invoice": {
      "object": "invoice",
      "id": "in_A",
      "created": 1704067200, // Jan 1 2024
      "period_start": 1704067200, // Jan 1 2024
      "period_end": 1704067200, // Jan 1 2024
      "lines": {
        "data": [
          {
            "description": "1 × Monthly Price (at $15.00 / month)",
            "period": {
              "start": 1704067200, // Jan 1 2024
              "end": 1706745600 // Feb 1 2024
            }
            // ...
          },
          {
            "description": "1 × Quarterly Price (at $100.00 every 3 months)",
            "period": {
              "start": 1704067200, // Jan 1 2024
              "end": 1711929600 // Apr 1 2024
            }
            // ...
          }
        ]
      }
      // ...
    }
    // ...
  }
}
```

## Update a subscription to mixed interval subscription

1. Update your subscription to flexible billing mode.
1. Call [migrate endpoint](https://docs.stripe.com/api/subscriptions/migrate.md) and set `billing_mode` to `flexible` for the existing subscription.
1. Call [update subscription](https://docs.stripe.com/api/subscriptions/update.md) to adding items with different prices and intervals.

## Cancel a subscription

Canceling a mixed interval subscription or schedule cancels all the subscription items, regardless of their interval.

Subscriptions have a single behavior for [dunning](https://docs.stripe.com/billing/revenue-recovery/smart-retries.md). If all retries for a payment fail, even if the failing payment is for an invoice related to only one of the items on the subscription, Stripe cancels the entire subscription and marks it as unpaid or past due, depending on your configured dunning settings.

Learn more about [canceling or deleting subscriptions](https://docs.stripe.com/no-code/subscriptions.md#create-subscriptions).

## Billing periods for mixed interval subscriptions

Each subscription item has its own [current_period_start](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-items-data-current_period_start) and [current_period_end](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-items-data-current_period_end). [Subscription items](https://docs.stripe.com/api/subscription_items/object.md) track their respective billing periods directly instead of as a top-level shared billing period on the [subscription](https://docs.stripe.com/api/subscriptions/object.md) resource.

For example, a subscription created on January 1 with a monthly, bimonthly, and quarterly item has the following periods:

|                 | current_period_start | current_period_end |
| --------------- | -------------------- | ------------------ |
| Monthly item    | January 1            | February 1         |
| Bi-monthly item | January 1            | March 1            |
| Quarterly item  | January 1            | April 1            |
| Subscription    | January 1            | February 1         |

After renewal on February 1 (`subscription.current_period_end`), the subscription’s current period adjusts to match the latest `current_period_start` and earliest `current_period_end` of all the items:

|                 | current_period_start | current_period_end |
| --------------- | -------------------- | ------------------ |
| Monthly item    | February 1           | March 1            |
| Bi-monthly item | January 1            | March 1            |
| Quarterly item  | January 1            | April 1            |
| Subscription    | February 1           | March 1            |

After cycling a third time:

|                 | current_period_start | current_period_end |
| --------------- | -------------------- | ------------------ |
| Monthly item    | March 1              | April 1            |
| Bi-monthly item | March 1              | May 1              |
| Quarterly item  | January 1            | April 1            |
| Subscription    | March 1              | April 1            |

### Free trial

The item-level billing period dates are affected by free trial end dates, similar to regular subscriptions. When the subscription has a future-dated [trial_end](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-trial_end), all the `current_period_end` dates (subscription and items) are set to the `trial_end` date.

### Pause at trial end and resume

You can configure a mixed interval subscription to pause at trial end when the payment method is missing through the [trial_settings.end_behavior.missing_payment_method](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-trial_settings-end_behavior-missing_payment_method) parameter as with regular subscriptions. You can [resume](https://docs.stripe.com/billing/subscriptions/trials/free-trials.md?how=api#resume-a-paused-subscription) paused subscriptions using [stripe.subscription.resume](https://docs.stripe.com/api/subscriptions/resume.md), as with regular subscriptions.

> When resuming a mixed interval subscription with `billing_cycle_anchor: 'unchanged'` and `proration_behavior: 'none'`, the debit proration for the partial period between the date of resumption and the end of the current billing period for each of the items aren’t generated or billed. See an example below:

For a mixed interval subscription with a monthly and a bimonthly item with

- `billing_cycle_anchor` = January 1
- `trial_end` = February 1
- `trial_settings.end_behavior.missing_payment_method` = “pause”

This example assumes this subscription is paused on February 1 because of a missing payment method, and the subscription resumes on February 15 with `proration_behavior: 'none'`:

|              | billing_cycle_anchor: ‘unchanged’       | billing_cycle_anchor: ‘now’ |
| ------------ | --------------------------------------- | --------------------------- |
| Monthly item | Item current period: February 1–March 1 |

- Not billing for this period, so no new invoice is created
- Monthly item is next billed on March 1 for the period March 1–April 1 | Item current period: February 15–March 15
- Generates a new invoice, and bills for a monthly item from February 15–March 15 |
  | Bimonthly item | Item current period: February 1–April 1
- Not billing for this period, so no new invoice is created
- Bimonthly item is next billed on April 1 for the period April 1–June 1 | Item current period: February 15–April 15
- Generates a new invoice and bills for a monthly item from February 15–April 15 |
  | Subscription | - billing_cycle_anchor: February 1
- Subscription transitions to active immediately | - Generate a subscription pending update for billing_cycle_anchor: February 15 (applied when resumed invoice is paid)
- Subscription remains paused until resumption invoice is paid |

### Interval alignment

In mixed interval subscriptions, every item’s price interval (the combination of `price.recurring.interval` and `price.recurring.interval_count`) must be a multiple of the shortest price interval in the subscription. Some price interval combinations aren’t supported for mixed interval subscriptions.

- **Examples of supported interval combinations**:

  When validating that the intervals on your subscription align, Stripe considers the following intervals as equivalent:
  - 1 week and 7 days
  - 12 months and 1 year

  - 1 month, 3 months
  - 1 month, 1 year
  - 1 day, 1 week
  - 1 day, 3 months
  - 1 day, 2 years
  - 2 weeks, 4 weeks
  - 2 months, 4 months, 6 months

- **Examples of unsupported interval combinations**:

  There are no equivalences between the following price [interval](https://docs.stripe.com/api/prices/object.md#price_object-recurring-interval) types:
  - Week and month
  - Week and year
  - Day and month
  - Day and year

  - 2 months, 3 months
  - 4 months, 6 months
  - 1 week, 1 month
  - 2 days, 1 week
  - 5 months, 1 year

## Limitations

Mixed interval subscriptions are subject to the following limitations:

- The deprecated [cancel_at_period_end](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-cancel_at_period_end) can’t detect which subscription item’s `current_period_end` to use as the cancellation date, so defaults to `min_period_end`. Alternatively:
  - Use the `cancel_at` parameter to cancel a subscription on a future date.
  - Use the `min_period_end` or `max_period_end` helpers to determine which item’s end period triggers the subscription cancelation.
- Mixed interval subscriptions can’t calculate total [iterations](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-phases-iterations) accurately. Use `duration` to specify the subscription schedule instead.
- You can’t apply a retention coupon on mixed interval subscriptions through the customer portal.
- You currently can’t create mixed interval subscriptions on [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions/create.md).
