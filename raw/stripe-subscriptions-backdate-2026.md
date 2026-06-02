<!-- Source URL: https://docs.stripe.com/billing/subscriptions/backdate -->
<!-- Fetched: 2026-05-13 -->

# Backdate subscriptions

Learn how to backdate subscriptions.

You can backdate a subscription to bill customers for time that has already elapsed. This is often used when migrating to Stripe or for record keeping purposes. The `backdate_start_date` field specifies the subscription’s backdated start date. You also have the option to bill customers for this elapsed time and set the next billing date.

## Billing mode considerations

As of [API version 2025-04-30](https://docs.stripe.com/changelog/basil.md#2025-04-30.preview), the behavior of backdating depends on your subscription’s [billing_mode](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-billing_mode):

### Before

Use `billing_mode=classic` to create a single prorated line item for the backdated period.

### After

Use `billing_mode=flexible` to generate one line item for each natural billing period that occurs during the backdated period, which behaves similarly to regular billing.

> Backdating isn’t supported when an invoice has more than 250 line items, which is the default limit.

## Backdating and charging users

Sometimes users can have access to your service before you create a subscription for them, and you want to charge them for that access.

#### Dashboard

To charge users for this time through the Dashboard:

1. Go to the **Payments** > **Subscriptions** page.

1. Click **+Create subscription**.

1. Find or add a customer.

1. Enter the pricing and product information.

1. In the **Subscription details** section, select the start and end dates of the subscription. To backdate it, select a start date in the past.

1. Select the date that you want to start the billing period on.

1. (Optional) Set the **Payment** or **Advanced** options.

1. Click **Create subscription**. The subscription starts on the date you selected.

#### API

To charge for backdated time using the API, create a backdated subscription by passing the `customer`, `price`, and `backdate_start_date`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  backdate_start_date: 1575176400,
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
});
```

This creates an _invoice_ (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) with charges for the time between the backdated start date and the current time.

If a subscription has `billing_mode=classic`, Stripe creates a single prorated amount for the backdated period based on an imagined interval starting from the backdated start date. For example, if you have a monthly billing period beginning on the first of the month and set `backdate_start_date` to February 15 (in a non-leap year), Stripe calculates the proration based on an imagined month running from February 15 to March 15. Because February has 28 days, the prorated amount for the 14 days from February 15 to March 1 is exactly half the amount of a normal monthly charge.

Similarly, if you set the `backdate_start_date` to January 15, Stripe bases the proration calculation on an imagined month running from January 15 to February 15. That imagined month has 31 days, so the prorated amount for the 17 days from January 15 to February 1 is 17 divided by 31 (approximately 0.548) of a normal monthly charge.

You can also view the calculation by considering the backdated start date as the original start date. The beginning of the first full billing period then becomes the updated start date.

If a subscription has `billing_mode=flexible`, Stripe generates separate line items for each natural billing period that occurred during the backdated period. This means that each cycle is treated as if Stripe billed it normally during that time.

## Backdating without charging users

You can also backdate a subscription without charging the customer for the backdated period, which you can use if you’re migrating to Stripe. To do so, pass `proration_behavior: 'none'` when you create the subscription. That sets the `start_date` to the same value as `backdate_start_date`, but it doesn’t charge the customer for backdated time.

## Backdating and setting the billing cycle anchor

You can combine `backdate_start_date` with `billing_cycle_anchor` to backdate a subscription and set the billing cycle anchor to a date in the future. This creates a prorated item on the next invoice for the time between the backdated start date and the billing cycle anchor. You can use this if you’re migrating to Stripe and need to carry over the next billing date for your subscriptions while billing customers for elapsed time.

For example, say it’s October 15 and you’re migrating to Stripe. You have a subscription that started on September 1, and the next billing date is November 1. To migrate that subscription, create a new subscription and set `backdate_start_date` to September 1 and `billing_cycle_anchor` to November 1.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  backdate_start_date: 1575176400,
  billing_cycle_anchor: 1572580800,
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
});
```

This immediately issues an invoice for the prorated amount covering the time between September 1 and November 1. It also sets the `start_date` of the subscription to September 1. Stripe issues the next invoice on November 1.

## Backdating and discounts

When you apply a [coupon](https://docs.stripe.com/billing/subscriptions/coupons.md) to a backdated subscription, the coupon’s duration starts counting from the backdated start date, not from the date you make the API call. This means the coupon’s duration is consumed by the backdated period.

For example, if you create a subscription on March 1 with `backdate_start_date` set to January 1 and apply a coupon with `duration=repeating` and `duration_in_months=2`, the coupon applies to the January and February billing periods (the 2 months starting from January 1). Since the coupon’s 2-month duration has been fully consumed by the backdated period, it doesn’t apply to the March invoice or any future invoices, and the discount is removed from the subscription item.

If you want the coupon to apply to current and future invoices after the backdated period, the coupon’s duration must be longer than the backdated period. Using the same example, a coupon with `duration_in_months=3` would cover January, February, and March, applying the discount to the first invoice after the backdated period.

> If a coupon’s duration is shorter than or equal to the length of the backdated period, the discount only applies to invoices within the backdated period. It won’t carry forward to any new invoices after the backdate.

The following table summarizes how coupon duration interacts with backdating:

| |
| |
| Coupon duration | Behavior with backdating |
| `once` | Applies only to the first invoice, which covers the backdated period. |
| `repeating` (N months) | Duration starts from the backdated start date. If N is less than or equal to the backdated period, the discount expires before any future invoices are created. |
| `forever` | Applies to all invoices, including those in the backdated period and all future invoices. No special considerations. |

## Backdating an update

To set the effective date of [prorations](https://docs.stripe.com/billing/subscriptions/prorations.md) when updating a subscription, use the [proration_date](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-proration_date) parameter. Pass an integer Unix timestamp that occurs within the current period of the subscription’s items. If the subscription uses a subscription schedule, make sure that the timestamp is before the start date of the next phase of the schedule.

You can set the `proration_date` earlier than the current period only during the first period of a backdated subscription. In this situation, the `proration_date` must be on or after the `subscription[start_date]` (the backdated start date). In all other cases, the `proration_date` can’t be earlier than the `current_period_start`.
