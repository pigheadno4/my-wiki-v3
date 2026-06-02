<!-- Source URL: https://docs.stripe.com/billing/subscriptions/prebilling -->
<!-- Fetched: 2026-05-13 -->

# Bill customers in advance

Use prebilling to bill your customers now for future cycles or upcoming renewals.

With prebilling, you can bill customers in advance for multiple service periods, as opposed to the typical billing cycle for licensed prices, where you bill a customer for one service period. You can enable prebilling when you start a subscription or for upcoming renewals.

Here are some example use cases for prebilling:

- Create a monthly subscription and prebill for the first 45 days.
- When a monthly subscription has an upcoming renewal in 7 days, prebill and send the customer the renewal invoice now.
- Prebill now for the next 2 months from the time of renewal.

You can use prebilling when you create or update a subscription. Prebilling applies at the item-level: you can prebill for a specific item, set of items, or all items on a subscription. You can adjust the time range for prebilling at the item level, but it must cover at least one service period. For example, if you prebill an item with a monthly price, you must prebill for at least one month.

## Limitations

During public preview, prebilling has the following limitations:

- Prebilling isn’t available for [subscription schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules.md), or subscriptions backed by a subscription schedule.
- You can only use coupons with [percent_off](https://docs.stripe.com/api/coupons/object.md#coupon_object-percent_off) and a [duration](https://docs.stripe.com/api/coupons/object.md#coupon_object-duration) of `once` or `forever` with prebilling.
- Prebilling is applied immediately when you create or update a subscription and configure [billing_schedules](https://docs.stripe.com/api/subscriptions/create.md?api-version=preview#create_subscription-billing_schedules).
- You can’t use prebilling on subscriptions that have been [migrated from classic to flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md#migrate-existing-subscriptions-to-flexible-billing-mode).
- You can’t enable prebilling if all the subscription items have usage-based prices. Prebilling doesn’t apply to any usage-based prices in a subscription. You can’t set [applies_to[price]](https://docs.stripe.com/api/subscriptions/create.md?api-version=preview#create_subscription-billing_schedules-applies_to) if the price has [usage_type=metered](https://docs.stripe.com/api/prices/object.md?api-version=preview#price_object-recurring-usage_type).
- You must enable proration for subscriptions to use prebilling. You can’t set [proration_behavior](https://docs.stripe.com/api/subscriptions/create.md?api-version=preview#create_subscription-proration_behavior) to `none`.
- You can only enable prebilling up to the scheduled cancellation time if you update a subscription that’s been scheduled for cancellation.
- You can’t use prebilling if [payment_behavior](https://docs.stripe.com/api/subscriptions/create.md?api-version=preview#create_subscription-payment_behavior) is set to `pending_if_incomplete`.

## Before you begin

To use prebilling, you must:

- Create subscriptions with flexible billing mode enabled. [Learn more about flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md).
- Have an integration on Stripe API version [2025-09-30.preview](https://docs.stripe.com/changelog.md#2025-09-30.preview) or later. Learn how to [upgrade your API version](https://docs.stripe.com/upgrades.md#how-can-i-upgrade-my-api).

## Set up prebilling

You can enable prebilling when you create or update a subscription in the Dashboard or through the API.

When you set the end date for prebilling:

- The end date can’t be sooner than the start of the shortest billing period on the subscription. For example, if the shortest billing period on the subscription is monthly, the end date for prebilling must be at least a month from the start of the billing period.
- The end date can’t be later than the end of 12 cycles of the shortest billing period on the subscription. For example, if the shortest billing period on the subscription is monthly, the end date for prebilling can’t be more than 12 months from the start of the billing period.

#### Dashboard

To create a subscription with prebilling in the Dashboard:

1. Go to the [Subscriptions page](https://dashboard.stripe.com/subscriptions?status=active).
1. Click **+ Create subscription**.
1. In the **Subscription settings** section, enable **Bill upfront**.
1. Select the end date for prebilling. All items in the subscription are prebilled until the date you select.
1. In the **Advanced settings** section, set **Billing mode** to **Flexible**.
1. Click **Create subscription**.

To update an existing subscription:

> The subscription must already be in `billing_mode=flexible` to enable prebilling. See the [Limitations](https://docs.stripe.com/billing/subscriptions/prebilling.md#limitations) for more details.

1. Go to the [Subscriptions page](https://dashboard.stripe.com/subscriptions?status=active).
1. Click the subscription to update, then select **Actions** > **Update subscription**.
1. In the **Subscription settings** section, enable **Bill upfront**.
1. Select the end date for prebilling. All items in the subscription are prebilled until the date you select.
1. Click **Update subscription**.

#### API

To configure prebilling for a subscription through the API, use [billing_schedules](https://docs.stripe.com/api/subscriptions/object.md?api-version=preview#subscription_object-billing_schedules) to specify which items to prebill and how long to prebill.

- Use the `applies_to` array to specify which items to prebill. You can prebill specific items or omit this parameter to prebill all applicable items.
- Use the `bill_until` parameter to specify the end date for prebilling. You can set a duration from the start of the billing cycle or specify an exact timestamp.
- Use the [proration_behavior](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-proration_behavior) parameter to control when the prebilling invoice is generated.

For example, to prebill for 2 months for a specific price on a subscription with multiple items, use the following request:

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2025-09-30.preview" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][applies_to][0][type]=price" \
  -d "billing_schedules[0][applies_to][0][price]={{PRICE_ID}}" \
  -d "billing_schedules[0][bill_until][type]=duration" \
  -d "billing_schedules[0][bill_until][duration][interval]=month" \
  -d "billing_schedules[0][bill_until][duration][interval_count]=2"
```

To prebill for multiple items, add multiple objects to the `applies_to` array:

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2025-09-30.preview" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][applies_to][0][type]=price" \
  -d "billing_schedules[0][applies_to][0][price]={{PRICE_ID}}" \
  -d "billing_schedules[0][applies_to][1][type]=price" \
  -d "billing_schedules[0][applies_to][1][price]={{PRICE_ID}}" \
  -d "billing_schedules[0][bill_until][type]=duration" \
  -d "billing_schedules[0][bill_until][duration][interval]=month" \
  -d "billing_schedules[0][bill_until][duration][interval_count]=2"
```

To prebill for all applicable items, omit the `applies_to` array. In this case, prebilling applies to all items on the subscription with a licensed price and the item cycling at least once until the prebilling end date.

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2025-09-30.preview" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][bill_until][type]=duration" \
  -d "billing_schedules[0][bill_until][duration][interval]=month" \
  -d "billing_schedules[0][bill_until][duration][interval_count]=2"
```

To prebill for a specified duration, set `type` to `duration` to prebill for a specific duration of time from the current time and set the appropriate `interval` and `interval_count`. For example, to prebill for 2 months from the start of the billing cycle, set `interval` to `month` and `interval_count` to 2.

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2025-09-30.preview" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][bill_until][type]=duration" \
  -d "billing_schedules[0][bill_until][duration][interval]=month" \
  -d "billing_schedules[0][bill_until][duration][interval_count]=2"
```

To prebill up to a specific date, set `type` to `timestamp` and set `timestamp` to the Unix date time when prebilling should end.

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2025-09-30.preview" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][bill_until][type]=timestamp" \
  -d "billing_schedules[0][bill_until][timestamp]=1679609767"
```

To generate the invoice immediately, set `proration_behavior` to `always_invoice`:

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2025-09-30.preview" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d proration_behavior=always_invoice \
  -d "billing_schedules[0][bill_until][type]=timestamp" \
  -d "billing_schedules[0][bill_until][timestamp]=1679609767"
```

To generate the invoice at the next billing cycle date, set `proration_behavior` to `create_prorations`:

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2025-09-30.preview" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d proration_behavior=create_prorations \
  -d "billing_schedules[0][bill_until][type]=timestamp" \
  -d "billing_schedules[0][bill_until][timestamp]=1679609767"
```

### Preview invoices with prebilling

You can preview a customer’s invoice before you create or update a subscription to use prebilling. Use the API to [create a preview invoice](https://docs.stripe.com/api/invoices/create_preview.md) and include [billing_schedules](https://docs.stripe.com/api/invoices/create_preview.md?api-version=preview#create_create_preview-subscription_details-billing_schedules) in the `subscription_details` parameter. This allows you to see the invoice that’s generated for prebilling.
