<!-- Source URL: https://docs.stripe.com/billing/subscriptions/import-subscriptions -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Migrate subscriptions to Stripe Billing using Stripe APIs

Learn how to migrate your existing subscriptions to Stripe using Stripe APIs.

Learn how to migrate your existing *subscriptions* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) from a third-party, an in-house system, or an existing Stripe account to Stripe Billing using Stripe APIs.

## Before you begin

1. If you haven’t already, review the [migration stages](https://docs.stripe.com/billing/subscriptions/migrate-subscriptions.md).
2. [Set up a Stripe Billing integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md). This prerequisite is only required once before importing subscriptions to Stripe, and you don’t need to repeat it for future migrations.
3. [Request a payments data import](https://docs.stripe.com/get-started/data-migrations/pan-import.md) from your current processor. If you’re attempting a Stripe-to-Stripe migration, this prerequisite isn’t necessary because you’re already using Stripe for payment processing.
4. Make sure the customers you want to charge automatically have a default payment source (a [payment method](https://docs.stripe.com/api/payment_methods.md)), or [add a default](https://docs.stripe.com/billing/subscriptions/import-subscriptions.md#add-missing-payment-source). Without a default payment source, subscription invoices can’t collect payment.

## Manage legacy products and prices

If you have *legacy* (Technology that's no longer recommended) *pricing model* (The pricing model consists of the products or services you sell, how much they cost, what currency you accept for payments, and the service period to charge (for subscriptions). To build the pricing model, you use Products—what you sell—and Prices—how much and how often to charge for your products)s that you need to continue supporting in Stripe, create a placeholder product, such as `Legacy plan`. Here’s an example:

```curl
curl https://api.stripe.com/v1/products \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d id={{NEW_PRODUCT_ID}} \
  -d "name=Legacy plan" \
  -d "description=Imported legacy plan from source system" \
  -d "metadata[OLD_PRODUCT_ID]={{OLD_PRODUCT_ID}}"
```

When you need to update subscriptions with legacy plans, pass in the prices as needed using `items.price_data`. This overrides any existing legacy price. To learn more, see [variable pricing](https://docs.stripe.com/products-prices/how-products-and-prices-work.md#variable-pricing).

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d customer={{CUSTOMER_ID}} \
  -d "items[0][price_data][currency]=USD" \
  -d "items[0][price_data][product]={{PRODUCT_ID}}" \
  -d "items[0][price_data][recurring][interval]=month" \
  -d "items[0][price_data][recurring][interval_count]=3" \
  -d "items[0][price_data][unit_amount]=1000" \
  -d "items[0][quantity]=1"
```

## Optional: Add a missing default payment source

If a customer is missing a default payment source, you need to set one before creating subscriptions. If the customer already has a payment method attached but it isn’t set as the default, you can set it directly without creating a new one.

1. [Create](https://docs.stripe.com/api/payment_methods/create.md) or [retrieve](https://docs.stripe.com/api/payment_methods/retrieve.md) an existing `PaymentMethod`.
2. [Attach](https://docs.stripe.com/api/payment_methods/attach.md) it to the customer if it isn’t already attached.
3. Set the payment method as the default for the applicable customer:

```curl
curl https://api.stripe.com/v1/customers/CUSTOMER_ID \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "invoice_settings[default_payment_method]=PAYMENT_METHOD_ID"
```

> #### Migrating from another processor
> 
> If you’re migrating payment data from a third-party processor, your customers’ card data might not have been imported to Stripe yet. You need to first complete the [PAN import](https://docs.stripe.com/get-started/data-migrations/pan-import.md), then set default payment methods as needed.

## Import your subscriptions

After you import your customers and create a pricing model, you can start importing your subscriptions. You should be able to export subscription data from third-party systems through their UI or API. Contact your subscriptions processor if they don’t provide this option through either interface.

To import subscriptions, use your list of customers to create the appropriate subscription for each one. For example, if a subscriber has a monthly `Basic` pricing plan in your old model, use the monthly recurring price associated with that level when you create their subscription in Stripe.

### Make source data Stripe-compatible

Before you start importing subscriptions into Stripe, make sure that all of your source data is compatible with our expected format.

#### Important fields for migrating subscriptions

If you use relevant subscription data in your custom integration that Stripe doesn’t also use, you can apply your data to the `metadata` field of the subscriptions you create in Stripe. The following table describes other important fields to consider when importing subscriptions.

| Field | Description |
| --- | --- |
| [customer](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-customer) | Make sure that you’ve properly mapped the customer ID from your source data to the new customer ID in Stripe. |
| [phases.items.price](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-phases-items-price) | Make sure that you’ve mapped the price ID from your source data to the new price ID in Stripe. |
| [current_phase.start_date](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-current_phase-start_date) | Make sure that the subscription schedule you define in Stripe lines up with and maintains continuity from your original source data. For example, if a customer has 6 months left on a yearly subscription in your source system, make sure that `billing_cycle_anchor` and `start_date` reflect the correct mid-cycle term. |
| Third-party metadata | Import any additional data fields from your source data, which might include product names, plan names, and third-party application IDs. |
| Tax settings | Include any tax IDs, VAT IDs, or other tax information. |

#### Prepare legacy prices

If you created placeholders for [legacy prices](https://docs.stripe.com/billing/subscriptions/import-subscriptions.md#legacy-prices), you need to map those prices to the subscriptions and customers you’re importing. For each subscription with a legacy price, use the [price_data](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data) parameter of the [Subscriptions](https://docs.stripe.com/api/subscriptions.md#subscriptions) API to pass in information about the price and subscription. The required fields are:

| Parameter | Description |
| --- | --- |
| [currency](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data-currency) | Currency of the price, in three-letter ISO format. |
| [product](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data-product) | ID of the placeholder product. You can use this for all of the legacy prices. |
| [recurring](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data-recurring) | Information about the amount and frequency of the recurring price. |
| [recurring.interval](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data-recurring) | Frequency of the interval-`day`, `week`, `month`, or `year`. |
| [recurring.interval_count](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data-recurring-interval_count) | Number of intervals between billings. For example, setting `interval=day` and `interval_count=30` means that you bill the customer every 30 days. The maximum interval is 3 years (3 years, 36 months, or 156 weeks). |
| [recurring.unit_amount_decimal](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data-unit_amount_decimal) | Same as [unit_amount](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-items-price_data-unit_amount), but allows you to specify more granular decimal amounts in cents, up to 12 decimals. You can only set one of `unit_amount` and `unit_amount_decimal`. |

### Import subscription data into Stripe

After you’ve prepared your source data, you can start importing subscriptions into Stripe.

#### Testing 

Use a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) to run through the pricing model import process at least once before running the import in live mode. You need to remap your script:

- If you wipe the data in a sandbox and rerun the import.
- When you move to live mode, because the price IDs are different in a sandbox and live mode.

In a sandbox, you can use [test clocks](https://docs.stripe.com/billing/testing.md#test-clocks) to simulate subscriptions advancing through time. This allows you to see how the migrated subscriptions work in production.

#### Create subscriptions

While you can use the [Subscription](https://docs.stripe.com/api/subscriptions.md) API to create subscriptions, we recommend using the [Subscription Schedules](https://docs.stripe.com/api/subscription_schedules.md) API. With this API, you can schedule subscriptions to start in the future. For example, it’s the only way to start monthly subscriptions more than 30 days in advance. The ability to start subscriptions in the future also allows you to review the import before you start to bill your customers in production.

Additionally, the Subscription Schedules API provides `phases`, which provide much more flexibility in defining settings such as tax behavior, collection method, and coupon usage within more granular intervals. You can also define different behavior for different intervals. For example, you could apply a coupon only for the first 3 months of a yearly subscription.

Here’s how to create subscriptions that start on May 31, 2022 at 5:00 PM GMT-7.

```curl
curl https://api.stripe.com/v1/subscription_schedules \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "default_settings[billing_cycle_anchor]=phase_start" \
  -d "phases[0][items][0][price]={{PRICE_ID}}" \
  -d start_date=1654066801
```

## Confirm your migration

After you’ve imported your subscriptions, use the API to confirm that the subscriptions exist in Stripe.

Use the [list Subscriptions](https://docs.stripe.com/api/subscriptions/list.md) API to view all of the Subscriptions in Stripe. You can pass the [created](https://docs.stripe.com/api/subscriptions/list.md#list_subscriptions-created) parameter to filter for recently created Subscriptions.

```curl
curl -G https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "created[gt]=1647294709"
```

## See also

- [Subscriptions schedules](https://docs.stripe.com/api/subscription_schedules.md)
