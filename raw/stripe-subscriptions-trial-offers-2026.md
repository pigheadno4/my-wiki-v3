<!-- Source URL: https://docs.stripe.com/billing/subscriptions/trial-offers -->
<!-- Fetched: 2026-05-12 -->

# Configure trial offers on subscriptions

Offer free or paid trials for items in a subscription.
![](assets/stripe-subs-trial-offer.png)

Use the [Trial Offer](https://docs.stripe.com/api/product-catalog/trial-offer.md?api-version=2026-03-25.preview) API to manage both free and paid introductory periods for your [subscriptions](https://docs.stripe.com/subscriptions.md) with a single API integration. Trial offers enable you to qualify high-intent leads, reduce trial abuse, and provide discounted rates to your customers for a limited duration (for example, 1 USD for the first week of an offer).

## Use cases

With trial offers, you can run promotional pricing and product offering experiments directly in Stripe. Common use cases for trial offers include:

| Use case              | Description                                                                                                                                                                                                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Discounted trials** | To improve trial-to-paid conversion and generate revenue, you can set up discounted trials. For example, you offer a reduced introductory price of 4 USD for 4 weeks or a free 7-day trial.                                                                |
| **Free trials**       | To offer a free trial subscription, include a 0 USD item in the subscription.                                                                                                                                                                              |
| **Upgrade trials**    | To upsell premium features, you can configure upgrade trials. For example, you offer a customer on a basic plan a 7-day trial to access premium features at the basic rate. Then, when the trial ends, you automatically convert them to the premium rate. |
| **Item-level trials** | To sell add-ons, AI packs, and other feature bundles, you can set up item-level trials. You can offer customers a trial for a single line item in a subscription while billing other items at their regular price.                                         |

## Before you begin

- Your integration must be on [2026-03-25.preview](https://docs.stripe.com/changelog.md?channel=preview#2026-03-25.preview). You must specify that [Stripe version](https://docs.stripe.com/api/versioning.md) in your request header to access preview features.
- You must upgrade your subscription from `classic` [billing mode](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-billing_mode) to `flexible` [billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md) to use trial offers.

### Limitations

- Trial offers apply to recurring subscription items only. Non-recurring items aren’t eligible for paid trials or discounted trial pricing.
- Dashboard and customer portal support is limited during public preview. You can use both the dashboard and customer portal to view trial offers created using the API, but you can’t use them to create, manage, or modify trial offer items.
- You can’t modify the trial length after you create the subscription or schedule trial extensions and reductions.
- Trial offers revenue isn’t available in [Billing Analytics](https://docs.stripe.com/billing/subscriptions/analytics.md). Stripe tracks trial revenue using the `trialing` status, but paid trials use `active`, meaning Stripe considers trial revenue as regular subscription revenue.
- [Trial Offer API](https://docs.stripe.com/api/product-catalog/trial-offer.md?api-version=2026-03-25.preview) and [trial_end](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-trial_end) limitations:
  - You can’t use trial offers and the legacy `trial_end` parameter together. We recommend using the Trial Offer API to configure discounted trials and free trials.
  - If you use [Checkout](https://docs.stripe.com/payments/checkout.md), you can’t use trial offers. To create trialing subscriptions through Checkout, you must use legacy free trials with `trial_end`. See [Configure free trials](https://docs.stripe.com/payments/checkout/free-trials.md).

## How trial offers work

_Products_ (Products represent what your business sells—whether that's a good or a service) describe the specific goods or services you offer to your customers and _Prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) define the unit cost. A subscription charges a customer for those products, at the specified price, on a recurring basis. When you create a trial offer, you specify a trial price and a duration of the trial for a product. When the trial ends, the subscription automatically transitions to the regular price or another price you configure.

Trial offers don’t replace [products or prices](https://docs.stripe.com/products-prices/how-products-and-prices-work.md). `Trial Offer` is a separate object that attaches a discounted or free price to a [Subscription item](https://docs.stripe.com/api/subscription_items.md) for a limited time, without modifying the item’s underlying [price](https://docs.stripe.com/api/subscription_items/object.md?#subscription_item_object-price).

## Create a trial offer

To [create a trial offer](https://docs.stripe.com/api/product-catalog/trial-offer/create.md?api-version=2026-03-25.preview), pass a [price](https://docs.stripe.com/api/product-catalog/trial-offer/create.md?api-version=2026-03-25.preview#create_product_catalog_trial_offer-price) using the [price.id](https://docs.stripe.com/api/prices/object.md#price_object-id) to define the cost during the trial period. You can set this to 0 USD for free trials or any positive amount for paid trials. Next, set the trial [duration.type](https://docs.stripe.com/api/product-catalog/trial-offer/create.md?api-version=2026-03-25.preview#create_product_catalog_trial_offer-duration-type) to `relative` (based on billing intervals) or `timestamp` (based on an absolute date). For relative duration, use [iterations](https://docs.stripe.com/api/product-catalog/trial-offer/object.md?api-version=2026-03-25.preview#product_catalog_trial_offer_object-duration-relative-iterations) to define the number of billing intervals. Then, define what happens when the trial ends using the [end_behavior](https://docs.stripe.com/api/product-catalog/trial-offer/create.md?api-version=2026-03-25.preview#create_product_catalog_trial_offer-end_behavior). Use `transition` to specify the [price.id](https://docs.stripe.com/api/prices/object.md#price_object-id) that the subscription transitions to when the trial ends.

### Create a trial offer with a relative duration

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const trialOffer = await stripe.productCatalog.trialOffers.create({
  price: "{{PRICE_ID}}",
  duration: {
    relative: {
      iterations: 1,
    },
    type: "relative",
  },
  end_behavior: {
    transition: {
      price: "{{PRICE_ID}}",
    },
  },
});
```

### Create a trial offer with a timestamp duration

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const trialOffer = await stripe.productCatalog.trialOffers.create({
  price: "{{PRICE_ID}}",
  duration: {
    type: "timestamp",
  },
  end_behavior: {
    transition: {
      price: "{{PRICE_ID}}",
    },
  },
});
```

## Attach a trial offer to a new subscription

To attach a trial offer to a [subscription](https://docs.stripe.com/api/subscriptions/object.md), specify the [trial_offer.id](https://docs.stripe.com/api/product-catalog/trial-offer/object.md?api-version=2026-03-25.preview#product_catalog_trial_offer_object-id) in the [items.current_trial.trial_offer](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-items-current_trial) parameter:

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  billing_mode: {
    type: "flexible",
  },
  items: [
    {
      current_trial: {
        trial_offer: "to_123",
      },
      quantity: 1,
    },
  ],
});
```

#### Customer v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  billing_mode: {
    type: "flexible",
  },
  items: [
    {
      current_trial: {
        trial_offer: "to_123",
      },
      quantity: 1,
    },
  ],
});
```

## Update subscriptions with a trial offer

### Add a trial offer to an existing subscription

To add a trial offer to an existing subscription, specify the [trial_offer.id](https://docs.stripe.com/api/product-catalog/trial-offer/object.md?api-version=2026-03-25.preview#product_catalog_trial_offer_object-id) in the [items.current_trial.trial_offer](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-items-current_trial) parameter:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.update("{{SUBSCRIPTION_ID}}", {
  items: [
    {
      current_trial: {
        trial_offer: "to_123",
      },
    },
  ],
});
```

### Add a trial offer to a subscription with existing items

To add a trial offer as another item to a subscription that has existing items, add an item to the [items](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-items) array and specify the [trial_offer.id](https://docs.stripe.com/api/product-catalog/trial-offer/object.md?api-version=2026-03-25.preview#product_catalog_trial_offer_object-id) in the [items.current_trial.trial_offer](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-items-current_trial) parameter:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.update("{{SUBSCRIPTION_ID}}", {
  items: [
    {
      id: "{{SUBSCRIPTIONITEM_ID}}",
    },
    {
      current_trial: {
        trial_offer: "to_123",
      },
      quantity: 1,
    },
  ],
});
```

### Convert a subscription item to a trial offer

To convert an existing subscription item to a trial offer, include the [items.id](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-items-id) and specify the [trial_offer.id](https://docs.stripe.com/api/product-catalog/trial-offer/object.md?api-version=2026-03-25.preview#product_catalog_trial_offer_object-id) in the [items.current_trial.trial_offer](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-items-current_trial) parameter:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.update("{{SUBSCRIPTION_ID}}", {
  items: [
    {
      id: "{{SUBSCRIPTIONITEM_ID}}",
      current_trial: {
        trial_offer: "to_123",
      },
    },
  ],
});
```

### Change the item quantity for a trial offer

To modify the item [quantity](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-items-quantity) for a trial offer, update the subscription:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.update("{{SUBSCRIPTION_ID}}", {
  items: [
    {
      id: "{{SUBSCRIPTIONITEM_ID}}",
      quantity: 2,
    },
  ],
});
```

## Add a trial offer to a subscription schedule

You can only use timestamp trial offers with [subscription schedules](https://docs.stripe.com/api/subscription_schedules.md). Unlike relative duration trials, which end after a set number of billing intervals, timestamp trials end on an absolute date. To create one, set the trial offer’s [duration.type](https://docs.stripe.com/api/product-catalog/trial-offer/object.md?api-version=2026-03-25.preview#product_catalog_trial_offer_object-duration-type) to `timestamp`:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const trialOffer = await stripe.productCatalog.trialOffers.create({
  price: "{{PRICE_ID}}",
  duration: {
    type: "timestamp",
  },
  end_behavior: {
    transition: {
      price: "{{PRICE_ID}}",
    },
  },
});
```

Next, use [phases.items.trial_offer](https://docs.stripe.com/api/subscription_schedules/create.md?api-version=2026-03-25.preview#create_subscription_schedule-phases-items-trial_offer) to attach the trial offer to the schedule [phase](https://docs.stripe.com/api/subscription_schedules/create.md?#create_subscription_schedule-phases) of the subscription schedule:

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  start_date: 1610403705,
  phases: [
    {
      items: [
        {
          trial_offer: "to_123",
        },
      ],
      end_date: 1610403706,
    },
  ],
});
```

#### Customer v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer: "{{CUSTOMER_ID}}",
  start_date: 1610403705,
  phases: [
    {
      items: [
        {
          trial_offer: "to_123",
        },
      ],
      end_date: 1610403706,
    },
  ],
});
```

## View subscriptions with trial offers

When you [retrieve a subscription](https://docs.stripe.com/api/subscriptions/retrieve.md), the response includes the configuration for each item, including trial offers:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.retrieve("{{SUBSCRIPTION_ID}}");
```

## Cancel a subscription at the end of a paid trial

To cancel the subscription when the paid trial ends, create a subscription with a trial offer and set the [cancel_at](https://docs.stripe.com/api/subscriptions/update.md?#update_subscription-cancel_at) parameter to the end of the trial period.

This pattern supports opt-in renewals by ensuring customers aren’t converted to a recurring subscription by default.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  items: [
    {
      current_trial: {
        trial_offer: "to_123",
      },
      quantity: 1,
    },
  ],
  cancel_at: 1610403706,
});
```

#### Customer v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      current_trial: {
        trial_offer: "to_123",
      },
      quantity: 1,
    },
  ],
  cancel_at: 1610403706,
});
```

## Use trial offers with other features

### Trial offers with usage-based billing

When creating a [Price](https://docs.stripe.com/api/prices/object.md) object, you can specify a metered price instead of a recurring price and attach it to a trial offer. This lets you offer the same [usage-based billing](https://docs.stripe.com/billing/subscriptions/usage-based.md) functionality at a discounted price.

To use a metered price, set the [usage_type](https://docs.stripe.com/api/prices/object.md?#price_object-recurring-usage_type) to `metered` and add an existing [meter](https://docs.stripe.com/api/prices/object.md?#price_object-recurring-meter) to track usage.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  currency: "usd",
  billing_scheme: "per_unit",
  unit_amount: 1,
  recurring: {
    interval: "week",
    usage_type: "metered",
    meter: "mtr_123",
  },
  product_data: {
    name: "Trial Period Price",
  },
});
```

Next, attach the price to a trial offer as you would with any other recurring price:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const trialOffer = await stripe.productCatalog.trialOffers.create({
  price: "{{PRICE_ID}}",
  duration: {
    relative: {
      iterations: 1,
    },
    type: "timestamp",
  },
  end_behavior: {
    transition: {
      price: "{{PRICE_ID}}",
    },
  },
});
```

## Additional considerations

### Subscription trialing status and trial offer

When using trial offers, a subscription’s `status` is determined by the price of the trial:

- **Free Trials (0 USD)**: If a subscription only contains trial offers, and all trial offer prices are set to 0 USD, the subscription status is `trialing`. This matches the legacy `trial_end` behavior and is ideal for “no-card-required” or standard free trial flows.
- **Paid Trials (>0 USD)**: If the subscription has a regular price item, or the trial offers have a non-zero price, the subscription status will be `active`, `incomplete`, or `past_due`. This behavior mimics other subscriptions without trial offers. Because a paid trial requires an immediate successful payment to begin, the subscription follows the standard `PaymentIntent` lifecycle. This ensures that your existing billing logic—such as webhooks for successful payments—remains consistent, whether the customer is paying a promotional price or the full recurring amount.

### Events

Every time a trial changes, it triggers [Events](https://docs.stripe.com/api.md#event_types). Make sure that your integration handles them. For example, you might want to email a customer before a trial ends. Learn more about [handling subscription events](https://docs.stripe.com/billing/subscriptions/webhooks.md#events).

The following table describes the events that trigger before a free trial ends, when a trial subscription pauses or cancels, and when a subscription resumes and becomes active.

| Event                                  | Description                                                                                                                                                                                                                                    | Use case                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `customer.subscription.deleted`        | Sent when a subscription ends.                                                                                                                                                                                                                 | Stop providing access to your product in response to this event. The subscription moves to the `canceled` status and sends this event after a free trial ends without a payment method, and if the subscription’s `missing_payment_method` end behavior is set to `cancel`.                                                         |
| `customer.subscription.resumed`        | Sent when a subscription is no longer paused. When you receive this event, grant the customer access to the product if they lost access while the subscription was paused.                                                                     | Paused subscriptions are converted into active subscriptions they resume. Resuming a subscription might generate an invoice and corresponding Payment Intent that must be paid before the subscription moves out of the `paused` status.                                                                                            |
| `customer.subscription.paused`         | Sent when a subscription is fully paused. Invoicing won’t occur until the subscription resumes. When you receive this event, you can revoke the customer’s access to the product until they add a payment method and the subscription resumes. | Stop providing access to your product in response to this event. The subscription moves to the `paused` status and sends this event after a free trial ends without a payment method and if the subscription’s `missing_payment_method` end behavior is set to `pause`. The subscription remains `paused` until explicitly resumed. |
| `customer.subscription.trial_will_end` | Sent 3 days before the trial period ends. If the trial is less than 3 days, it triggers this event immediately.                                                                                                                                | Configure the subscription to automatically send an email to your customer 3 days before the trial period ends.                                                                                                                                                                                                                     |

### Setting a billing anchor when a trial offer ends

When a trial offer ends and transitions to the regular recurring price, customers need to begin a fresh billing cycle immediately. By default, the subscription’s [billing_cycle_anchor](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-trial_settings-end_behavior-billing_cycle_anchor) automatically resets to the time the trial ends (now). This ensures that your customers are charged the full amount for their first regular interval immediately, without generating prorations.

If you don’t want your `billing_cycle_anchor` to change, you can set it to `unchanged`.

Configuration options for `billing_cycle_anchor` include:

- `now` (default): Resets the subscription’s `billing_cycle_anchor` to the exact time the trial offer completes. This creates a new billing cycle for the regular price and generates a full-amount invoice with no proration.
- `unchanged`: Maintains the original anchor from when the subscription was first created. The period between the trial end and the next natural anchor date are billed as a prorated amount.

For example, if you offer a 7-day trial for 1 USD and want the first 20 USD monthly charge to cover a full month starting on day 8:

1. Jan 1: Subscription created with a 7-day trial offer.
1. Jan 8: Trial ends. The `billing_cycle_anchor` automatically resets to Jan 8.
1. Invoice: Stripe generates an invoice for the full 20 USD recurring price for the period of Jan 8–Feb 8. No proration is applied.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
      current_trial: {
        trial_offer: "{{TRIAL_OFFER_ID}}",
      },
    },
  ],
  trial_settings: {
    end_behavior: {
      billing_cycle_anchor: "unchanged",
    },
  },
});
```

#### Customer v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
      current_trial: {
        trial_offer: "{{TRIAL_OFFER_ID}}",
      },
    },
  ],
  trial_settings: {
    end_behavior: {
      billing_cycle_anchor: "unchanged",
    },
  },
});
```

## See also

- [Products and prices](https://docs.stripe.com/products-prices/overview.md)
- [Prices](https://docs.stripe.com/api.md#prices)
- [Subscriptions](https://docs.stripe.com/api.md#subscriptions)
- [Managing subscription billing periods](https://docs.stripe.com/billing/subscriptions/billing-cycle.md)
