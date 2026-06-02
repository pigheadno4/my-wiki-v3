<!-- Source URL: https://docs.stripe.com/billing/subscriptions/subscription-schedules -->
<!-- Fetched: 2026-05-13 -->

# Subscription schedules

Learn about subscription schedules and how to use them.

> This feature is only available in the classic version of the [Subscription editor](https://dashboard.stripe.com/subscriptions) in the Dashboard. You can switch between the classic and the new version anytime, and your choice persists for 30 days. This means when you reopen the editor, it defaults to whichever version you last selected.

Use [subscription schedules](https://docs.stripe.com/api/subscription_schedules.md) to automate changes to subscriptions over time. You can [create](https://docs.stripe.com/api/subscription_schedules/create.md) subscriptions directly through a schedule or you can add a schedule to an existing subscription. Use the [phases](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-phases) attribute to define the changes you want to make to the subscription. After a schedule completes all of its phases, it completes based on its [end_behavior](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-end_behavior).

Some changes you might want to schedule include:

- Starting a subscription on a future date
- Backdating a subscription to a past date
- Upgrading or downgrading a subscription

Subscription schedules are available in both the Stripe Billing Dashboard and the API.

For examples of how you can use subscription schedules, see [Use cases](https://docs.stripe.com/billing/subscriptions/subscription-schedules.md#use-cases).

## Phases

When creating a subscription schedule, use the [phases](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-phases) attribute to define when changes occur and what properties of the subscription to change. For example, you might offer a coupon for 50% off for the first three months of a subscription. In this scenario, you’d create a subscription schedule where the first phase is three months long and contains the 50% off coupon. In the second phase, the subscription reverts to the normal cost and the coupon is removed. Phases must be sequential, meaning only one phase can be active at a given time. You can have up to 10 phases.

### Set the length of a phase

You can set the length of a phase using the API or the Dashboard.

#### API

Phases have a [duration](https://docs.stripe.com/api/subscription_schedules/update.md#update_subscription_schedule-phases-duration) attribute that you use to specify how long a phase should last. The `duration` parameter accepts the following values: `week`, `month` or `year`.

The `end_date` of one phase has to be the `start_date` for the next phase. Using `duration` automatically sets the `start_date` and `end_date` properly. You can set these values manually, but Stripe recommends using `duration` instead. Because manually setting the start and end dates is prone to errors, only use it for advanced use cases.

#### Dashboard

To set the length of a phase:

1. In the Dashboard, open the [subscription editor](https://dashboard.stripe.com/subscriptions?create=subscription).
1. Add a new customer, or find an existing one.
1. Add a new product, or find an existing one.
1. Click **+ Add phase**.
1. Select the phase duration. You can also select **Forever** to keep the subscription active indefinitely.

### Transition to the next phase

Phase transitions happen automatically after the `end_date` on a phase is reached. When a phase starts, Stripe updates the subscription based on the attributes of the next phase. You can optionally enable [prorations](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-phases-proration_behavior) to credit the user for unused items or time on the plan.

#### Proration behavior

There are two different proration behavior settings that control how Stripe handles billing adjustments during subscription schedule changes:

1. **Schedule update proration behavior**: The top-level [proration_behavior](https://docs.stripe.com/api/subscription_schedules/update.md#update_subscription_schedule-proration_behavior) parameter controls how to handle prorations when updating a subscription schedule in a way that affects the current phase’s billing configuration (such as changing prices or quantities).

1. **Phase transition proration behavior**: Each phase has its own [proration_behavior](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-phases-proration_behavior) attribute that controls how Stripe handles prorations when transitioning to that phase.

##### Schedule update proration behavior

When you update a subscription schedule and change the billing configuration of the `current_phase`, you can control how prorations are handled using the top-level `proration_behavior` parameter.

This parameter works similarly to the one in the [Update a subscription API](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-proration_behavior), and accepts the following values:

- (default) `create_prorations`: Generate proration adjustments for billing changes.
- `none`: No prorations are created for the update.
- `always_invoice`: Generate prorations and immediately finalize an invoice.

Changes to non-billing fields (like metadata) won’t generate prorations regardless of this setting.

##### Phase transition proration behavior

Each phase can define its own `proration_behavior` to control what happens when the subscription enters that phase. This setting applies specifically to prorations generated during phase transitions and is saved as a field on the phase.

For example, if `phases[1]` increases the quantity from 1 to 3 when it starts, the `proration_behavior` on `phases[1]` determines how those prorations are handled when transitioning from `phases[0]` to `phases[1]`:

- (default) `create_prorations`: Generate pending invoice items for billing changes.
- `none`: No prorations are created when entering this phase.
- `always_invoice`: Generate prorations and immediately create an invoice when entering this phase.

If you need to change how a future phase transition handles prorations, update the `proration_behavior` setting on the future phase before it becomes active.

### Use trials

You can add a trial period to the first phase of a subscription using the API or the Dashboard.

#### API

You can add trial periods by setting [trial end](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-phases-trial_end) on a phase. If you want the entire phase to be a trial, set the value of `trial_end` to the same time as the `end_date` of the phase. You can also set `trial_end` to a time before the `end_date` if you want to make only part of the phase a trial. When scheduling updates, you must specify the new `trial_end` on each phase.

#### Dashboard

To add a trial period to the first phase of a new subscription:

1. In the Dashboard, open the [Subscription editor](https://dashboard.stripe.com/subscriptions?create=subscription).
1. Add a new customer, or find an existing one.
1. Add a new product, or find an existing one.
1. Under **Free trial days**, set the length of the free trial period.
   - If you want the entire phase to be a trial, set the length of the trial to be the same as the length of the phase.
   - If you want only part of the phase to be a trial, set the length of the trial to be shorter than the length of the phase.
1. Click **Create subscription**.

To add a trial period to the first phase of an existing subscription:

1. In the Dashboard, go to the [Subscriptions](https://dashboard.stripe.com/subscriptions) page, select an existing subscription, and click **Actions** > **Update subscription**.
1. In the subscription, click **Edit** for the first phase.
1. Under **Free trial days**, set the length of the free trial period.
   - If you want the entire phase to be a trial, set the length of the trial to be the same as the length of the phase.
   - If you want only part of the phase to be a trial, set the length of the trial to be shorter than the length of the phase.
1. Click **Update subscription**.

### Complete a schedule

Subscription schedules end after the last phase is complete. At this point, the subscription is left in place and is no longer associated with the schedule. If you want to cancel a subscription after the last phase of a schedule completes, you can set [end_behavior](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-end_behavior) to `cancel`. The subscription’s [cancel_on_date](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-cancel_at) isn’t set until the subscription transitions into the final phase.

### Phase attribute inheritance

When a phase becomes active, all attributes set on the phase are also set on the subscription. After the phase ends, attributes remain the same unless the next phase modifies them, or if the schedule has no default setting. You can set some attributes on both schedules and phases. This includes:

| Schedule attribute                                                                                                                                                           | Phase attribute                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [default_settings.billing_thresholds](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-default_settings-billing_thresholds)         | [phases.billing_thresholds](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-phases-billing_thresholds)         |
| [default_settings.collection_method](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-default_settings-collection_method)           | [phases.collection_method](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-phases-collection_method)           |
| [default_settings.default_payment_method](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-default_settings-default_payment_method) | [phases.default_payment_method](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-phases-default_payment_method) |
| [default_settings.invoice_settings](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-default_settings-invoice_settings)             | [phases.invoice_settings](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-phases-invoice_settings)             |

If one of these attributes is defined on the schedule, it becomes the default for all phases. When the same property is defined on both the schedule and the phase, the phase attribute overrides the schedule attribute. This behavior is explained more below:

| Schedule attribute present | Phase attribute present | Outcome                                      |
| -------------------------- | ----------------------- | -------------------------------------------- |
| No                         | No                      | Defaults to the customer or account settings |
| Yes                        | No                      | Schedule attribute set                       |
| Yes                        | Yes                     | Phase attribute set                          |
| No                         | Yes                     | Phase attribute set                          |

### Use phase metadata

You can use subscription schedule phases to set metadata on the underlying subscription. This allows you to control the metadata on a subscription with scheduled updates.

#### API

To use phase metadata with the API, set [metadata](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-phases-metadata) on the phases of a subscription schedule. When the underlying subscription enters a phase:

- Metadata from the phase with non-empty values are _added_ to the metadata on the subscription if the keys _aren’t_ already present in the latter.
- Metadata from the phase with non-empty values are used to _update_ the metadata on the subscription if the keys _are_ already present in the latter.
- Metadata from the phase with _empty values_ are used to _unset_ the corresponding keys in the metadata on the subscription.

To unset all keys in the subscription’s metadata, update the subscription directly or unset every key individually from the phase’s metadata. Updating the underlying subscription’s metadata directly doesn’t affect the current phase’s metadata.

The following example illustrates a subscription schedule with two phases, where each phase has its own metadata:

```json
{
  ...
  "object": "subscription_schedule",
  "phases": [
    { // Phase 1
      ...
      "metadata": {
        "channel": "self-serve",
        "region": "apac",
        "upsell-products": "alpha"
      }
    },
    { // Phase 2
      ...
      "metadata": {
        "channel": "sales",
        "churn-risk": "high",
        "upsell-products": ""
      }
    }
  ]
}
```

When this schedule creates a new subscription and the subscription enters `Phase 1`, the three keys in `Phase 1` metadata are added to the subscription’s metadata. Hence, the subscription in `Phase 1` has the following metadata:

```json
{
  ...
  "object": "subscription",
  "metadata": {
    "channel": "self-serve",
    "region": "apac",
    "upsell-products": "alpha"
  }
}
```

When the subscription enters `Phase 2`, the subscription’s metadata is updated:

- The value of `channel` is updated because a value is specified on the phase’s metadata and the subscription already has metadata with that key.
- The value of `region` is unchanged because it’s not specified on the phase.
- `churn-risk` is added because this is a new key.
- `upsell-products` is unset because an empty value is specified on the phase.

Hence, the subscription in `Phase 2` has the following metadata:

```json
{
  ...
  "object": "subscription",
  "metadata": {
    "channel": "sales",
    "region": "apac",
    "churn-risk": "high"
  }
}
```

#### Dashboard

You can add, edit, and remove metadata entries in each phase of a subscription schedule using the [Billing Dashboard subscription editor](https://dashboard.stripe.com/subscriptions?create=subscription). When a new phase activates, the metadata of the subscription object updates to match that phase’s metadata.

1. In the Dashboard, open the [subscription editor](https://dashboard.stripe.com/subscriptions?create=subscription).
1. Add a new customer, or find an existing one.
1. Add a new product, or find an existing one.
1. In a new or existing phase, click **+ Add metadata**.
1. Enter a **Key** and a **Value**, then click **Save**.

Learn how to [copy subscription metadata onto subscription invoices](https://docs.stripe.com/billing/invoices/subscription.md#subscription-metadata).

## Create subscription schedules

This example demonstrates how to create a subscription schedule using a customer. Creating a schedule this way automatically creates the subscription as well.

> Unlike when you create a subscription directly, the first invoice of a subscription schedule with `collection_method` set to `charge_automatically` behaves like a recurring invoice and _isn’t_ immediately finalized at the time the schedule’s subscription is created. The invoice begins in a `draft` status and is finalized by Stripe [approximately 1 hour after creation](https://docs.stripe.com/billing/subscriptions/webhooks.md#understand).
>
> For example, when you create a subscription schedule with the collection method set to charge automatically and with `start_date=now`, this also creates a subscription and an invoice in the `draft` status. You have 1 hour to [edit the invoice](https://docs.stripe.com/api/invoices/update.md). Later, the invoice auto-advances to `open` or `paid` status, depending on the outcome of the asynchronous payment attempt at finalization time.

#### API

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  start_date: "now",
  end_behavior: "release",
  phases: [
    {
      items: [
        {
          price: "price_1GqNdGAJVYItwOKqEHb",
          quantity: 1,
        },
      ],
      duration: {
        interval: "month",
        interval_count: 12,
      },
    },
  ],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer: "{{CUSTOMER_ID}}",
  start_date: "now",
  end_behavior: "release",
  phases: [
    {
      items: [
        {
          price: "price_1GqNdGAJVYItwOKqEHb",
          quantity: 1,
        },
      ],
      duration: {
        interval: "month",
        interval_count: 12,
      },
    },
  ],
});
```

This schedule:

- Starts as soon as it’s created.
- Sets the subscription to one instance of the product at `price_1GqNdGAJVYItwOKqEHb`.
- Lasts for 12 months and then releases the subscription from the schedule.

You can also create subscription schedules by passing a subscription ID:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  from_subscription: "sub_GB98WOvaRAWPl6",
});
```

Creating a schedule this way uses attributes on the subscription to set attributes on the schedule.

Similar to other Stripe APIs, you can retrieve and update [subscription schedules](https://docs.stripe.com/api/subscription_schedules.md). You can also cancel and release them. Canceling a subscription schedule cancels the subscription as well. If you only want to remove a schedule from a subscription, use the [release](https://docs.stripe.com/api/subscription_schedules/release.md) call.

#### Dashboard

To create multi-phase subscription schedules:

1. In the Dashboard, open the [subscription editor](https://dashboard.stripe.com/subscriptions?create=subscription).
1. Add a new customer, or find an existing one.
1. Add a new product, or find an existing one.
1. Set a duration for the first phase of the subscription schedule.
1. Click **+ Add phase**.
1. Select the phase duration. You can also select **Forever** to keep the subscription active indefinitely.
1. Make the required changes to your new phase. You can change the quantity, change the price, add or remove coupons, reset the billing period date, change proration behavior, or update metadata. If you change the metadata in a phase, it updates the subscription’s metadata when that phase activates.
1. Save the new phase.
1. Add any additional phases as needed.
1. Click **Schedule subscription**.

## Update subscription schedules

You can only update the current and future phases on subscription schedules.

#### API

You need to pass in all current and future phases when you update a subscription schedule. You also need to pass in any previously set parameters that you want to keep. Any parameters that were previously set are unset for the existing phase unless you pass those in the update request. You still receive information in the response about past phases.

You can include up to 10 current or future phases. Updating the active phase updates the underlying subscription as well. For example, this call updates the `quantity` to two:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.update(
  "{{SUBSCRIPTIONSCHEDULE_ID}}",
  {
    phases: [
      {
        items: [
          {
            price: "{{PRICE_ID}}",
            quantity: 2,
          },
        ],
        start_date: 1577865600,
        end_date: 1580544000,
      },
    ],
  },
);
```

You can also end the current phase immediately and start a new phase. This moves the active phase to the past and immediately applies the new phase to the subscription. The example below ends the current phase and starts a new phase:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.update(
  "{{SUBSCRIPTIONSCHEDULE_ID}}",
  {
    phases: [
      {
        items: [
          {
            price: "{{PRICE_ID}}",
            quantity: 1,
          },
        ],
        start_date: 1577865600,
        end_date: "now",
      },
      {
        items: [
          {
            price: "{{PRICE_ID}}",
            quantity: 2,
          },
        ],
        start_date: "now",
        end_date: 1580544000,
      },
    ],
  },
);
```

To add additional phases to a subscription schedule, pass in the current phase, and then define your new phases:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.update(
  "{{SUBSCRIPTIONSCHEDULE_ID}}",
  {
    phases: [
      {
        items: [
          {
            price: "{{PRICE_ID}}",
            quantity: 1,
          },
        ],
        start_date: 1577865600,
        end_date: 1580544000,
      },
      {
        items: [
          {
            price: "{{PRICE_ID}}",
            quantity: 2,
          },
        ],
        duration: {
          interval: "month",
          interval_count: 1,
        },
      },
    ],
  },
);
```

#### Dashboard

To update existing subscriptions to have future subscription schedule phases:

1. In the Dashboard, go to the [Subscriptions](https://dashboard.stripe.com/subscriptions) page, select an existing subscription, and click **Actions** > **Update subscription**.
1. Set a duration for the current phase of the subscription schedule by selecting an end date.
1. Click **+Add phase**.
1. Select your next phase duration. You can also select **Forever** to keep the subscription active indefinitely.
1. Make the required changes to your new phase. You can change the quantity, change the price, add or remove coupons, reset the billing period date, change proration behavior, or update metadata. If you change the metadata in a phase, it updates the subscription’s metadata when that phase activates.
1. Save the new phase.
1. Add any additional phases as needed.
1. Click **Schedule subscription**.

## Preview an invoice

Use the [schedule](https://docs.stripe.com/api/invoices/create_preview.md#create_create_preview-schedule) parameter in the [create preview](https://docs.stripe.com/api/invoices/create_preview.md) to preview the next invoice for a subscription schedule.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoice = await stripe.invoices.createPreview({
  schedule: "{{SUBSCRIPTIONSCHEDULE_ID}}",
});
```

### Previewing schedule creation and updates

Use the parameters in [schedule_details](https://docs.stripe.com/api/invoices/create_preview.md#create_create_preview-schedule_details) to preview creating or updating a subscription schedule. Pass an existing [schedule](https://docs.stripe.com/api/invoices/create_preview.md#create_create_preview-schedule) to tell Stripe whether it’s a creation or an update.

Pass all of the current and future [phases](https://docs.stripe.com/api/invoices/create_preview.md#create_create_preview-schedule_details-phases) you’re previewing.

For example, the following code previews the first invoice for a subscription schedule with `1` phase that lasts for `12` months.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const invoice = await stripe.invoices.createPreview({
  customer_details: {
    address: {
      line1: "920 5th Ave",
      city: "Seattle",
      state: "WA",
      postal_code: "98104",
      country: "US",
    },
  },
  schedule_details: {
    phases: [
      {
        start_date: "now",
        items: [
          {
            price: "{{PRICE_ID}}",
            quantity: 1,
          },
        ],
        duration: {
          interval: "month",
          interval_count: 12,
        },
      },
    ],
  },
});
```

## Additional considerations

Subscription schedules generally follow the same restrictions as subscriptions, but also introduce some of their own restrictions. Additionally, the interaction between subscription schedules and subscriptions can produce unexpected behavior. Review the following sections to understand limitations, product behavior, and general best practices when using subscription schedules.

### Restrictions

- You can only define up to 10 current or future phases at a time on a subscription schedule. Past phases don’t count against this limit.
- Subscription schedule phases also follow [the same restrictions as subscriptions](https://docs.stripe.com/billing/subscriptions/quantities.md#billing-periods-with-multiple-prices) when creating subscription schedule phases with multiple items.

### Dashboard limitations

You can create and update subscription schedules without code in the [Dashboard](https://dashboard.stripe.com/test/subscriptions).

In the Dashboard, you can set the following settings globally across all phases, but not on a per phase basis:

- Billing thresholds
- Payment methods
- Invoice settings
- Subscription description
- Trial days (only works with the first phase)

The following parameters aren’t supported in the Dashboard:

- Subscription schedule metadata
- Phase item metadata
- Currency
- All Connect parameters

### Subscription updates when a schedule is attached

Use [subscription schedules](https://docs.stripe.com/api/subscription_schedules.md) to modify subscriptions automatically when time passes and the schedule’s next phase is entered. Some changes that you make directly to the subscription propagate to the subscription schedule’s phases, but some don’t. This means that any modifications you make directly to the subscription might be overwritten by the subscription schedule when the next phase is entered.

When scheduling changes to a subscription, follow these best practices:

- If a subscription has a subscription schedule attached, use the [Subscription Schedule](https://docs.stripe.com/api/subscription_schedules.md) API to modify the subscription, instead of the [Subscriptions](https://docs.stripe.com/api/subscriptions.md#subscriptions) API.
- Store the subscription schedule IDs alongside the subscription ID for future API updates. The subscription schedule ID returns when you [use the API to create it](https://docs.stripe.com/api/subscription_schedules/create.md) or through the [subscription_schedule.created](https://docs.stripe.com/api/events/types.md#event_types-subscription_schedule.created) webhook when Stripe creates it automatically, such as when a customer scheduled a downgrade in the [Customer Portal](https://docs.stripe.com/customer-management/configure-portal.md#configure-subscription-management).
- Discard the subscription schedule IDs when a subscription schedule is released. You can make changes to the subscriptions directly or create a new subscription schedule. The subscription schedule ID is returned when [released with the API](https://docs.stripe.com/api/subscription_schedules/release.md) or through the [subscription_schedule.released](https://docs.stripe.com/api/events/types.md#event_types-subscription_schedule.released) webhook event when the subscription schedule releases.
- Use the Dashboard to modify subscriptions, if possible, which automatically updates any attached subscription schedule.

Specifically, when you change any of the following subscription attributes directly on a subscription, this action might automatically create a new subscription schedule phase:

- `discounts`
- `tax_rates`
- `items`
- `trial_end`, `trial_settings`, `trial_start`
- `application_fee_percent`
- `add_invoice_items`
- `automatic_tax`

For example, consider a subscription with two items. The subscription has a subscription schedule attached with a single phase, mirroring the current status of the subscription. If you [use the API to delete](https://docs.stripe.com/api/subscription_items/delete.md) one of the items, this automatically splits the attached subscription schedule’s phase into two phases:

1. The phase that just ended and had two subscription items
1. The new phase that has just one item on the subscription

When subscription schedule phases automatically split, the following properties are copied from the current phase to the new phase:

- `proration_behavior`
- `billing_cycle_anchor`
- `cancel_at_period_end`
- `description`
- `metadata`
- `pause_collection`

Additionally, Stripe might copy the following top-level subscription attributes to the subscription schedule or its [`default_settings`](https://docs.stripe.com/api/subscription_schedules/object.md#subscription_schedule_object-default_settings):

| Subscription attribute    | Copied to new subscription schedule phase | Copied to subscription schedule `default_settings` |
| ------------------------- | ----------------------------------------- | -------------------------------------------------- |
| `coupon`                  | ✓ Supported                               | - Unsupported                                      |
| `trial_end`               | ✓ Supported                               | - Unsupported                                      |
| `tax_rates`               | ✓ Supported                               | - Unsupported                                      |
| `application_fee_percent` | ✓ Supported                               | ✓ Supported                                        |
| `discounts`               | ✓ Supported                               | - Unsupported                                      |
| `collection_method`       | ✓ Supported                               | ✓ Supported                                        |
| `invoice_settings`        | ✓ Supported                               | ✓ Supported                                        |
| `default_payment_method`  | ✓ Supported                               | ✓ Supported                                        |
| `default_source`          | ✓ Supported                               | ✓ Supported                                        |
| `transfer_data`           | ✓ Supported                               | ✓ Supported                                        |
| `on_behalf_of`            | ✓ Supported                               | ✓ Supported                                        |
| `currency`                | ✓ Supported                               | - Unsupported                                      |
| `add_invoice_items`       | ✓ Supported                               | - Unsupported                                      |
| `automatic_tax`           | ✓ Supported                               | ✓ Supported                                        |
| `items.prices`            | ✓ Supported                               | - Unsupported                                      |
| `billing_thresholds`      | ✓ Supported                               | ✓ Supported                                        |

Updates to subscription `metadata` aren’t propagated to an attached subscription schedule.

## Use cases

To understand subscription schedules, imagine a fictional newspaper company called The Pacific that offers two subscription options:

- _Print_, where customers receive the physical paper
- _Digital_, where customers get access to exclusive content on The Pacific’s website

Both subscriptions bill monthly. Browse possible options for subscription schedules below.

If you represent your customers as customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md) objects instead of [Customer](https://docs.stripe.com/api/customers/object.md) objects, replace the `customer` parameter in these code examples with the `customer_account` parameter. For more details, see [Represent customers using Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md).

### Start a subscription in the future

By default, new print subscriptions start on the first day of the next month. To accomplish this, set the `start_date` to a point in the future. The code below creates a subscription that starts in the future:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer: "{{CUSTOMER_ID}}",
  start_date: 1690873200,
  end_behavior: "release",
  phases: [
    {
      items: [
        {
          price: "{{PRICE_PRINT}}",
          quantity: 1,
        },
      ],
      duration: {
        interval: "month",
        interval_count: 12,
      },
    },
  ],
});
```

### Backdate a subscription

When customers subscribe to the digital plan, The Pacific backdates their subscriptions to the first day of the current month. Backdating allows you to charge for time in the past and allows digital subscribers to access the website immediately.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer: "{{CUSTOMER_ID}}",
  start_date: 1688194800,
  end_behavior: "release",
  phases: [
    {
      items: [
        {
          price: "{{PRICE_DIGITAL}}",
          quantity: 1,
        },
      ],
      duration: {
        interval: "month",
        interval_count: 12,
      },
    },
  ],
});
```

### Add a schedule to an existing subscription

The Pacific might discover that some of their original customers are on subscriptions without schedules. Because these subscriptions exist already, you can pass the subscription IDs in the `from_subscription` attribute to add a schedule. Passing the subscription IDs in this way creates a schedule with one phase that’s based on the current billing period of the subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  from_subscription: "{{SUBSCRIPTION_ID}}",
});
```

While adding these schedules, some customers decide to get a print subscription, so The Pacific adds a second phase to the schedule to start the print plan one month from now. The [Upgrade subscriptions](https://docs.stripe.com/billing/subscriptions/subscription-schedules.md#upgrading-subscriptions) use case shows an example of this process.

### Upgrade subscriptions

The Pacific offers an option to start with a print subscription for one month, then automatically add the digital option. Some customers prefer this because they can try the print publication first and then decide if they want to continue or cancel their subscription.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer: "{{CUSTOMER_ID}}",
  start_date: "now",
  end_behavior: "release",
  phases: [
    {
      items: [
        {
          price: "{{PRICE_PRINT}}",
          quantity: 1,
        },
      ],
      duration: {
        interval: "month",
        interval_count: 1,
      },
    },
    {
      items: [
        {
          price: "{{PRICE_PRINT}}",
          quantity: 1,
        },
        {
          price: "{{PRICE_DIGITAL}}",
          quantity: 1,
        },
      ],
      duration: {
        interval: "month",
        interval_count: 11,
      },
    },
  ],
});
```

### Downgrade subscriptions

The Pacific also offers an option to start a subscription with both the print and digital publications, and then downgrade to only the print publication for the rest of the subscription. _Customers_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) use this option to try both publications and see how they like them.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer: "{{CUSTOMER_ID}}",
  start_date: "now",
  end_behavior: "release",
  phases: [
    {
      items: [
        {
          price: "{{PRICE_DIGITAL}}",
          quantity: 1,
        },
        {
          price: "{{PRICE_PRINT}}",
          quantity: 1,
        },
      ],
      duration: {
        interval: "month",
        interval_count: 1,
      },
    },
    {
      items: [
        {
          price: "{{PRICE_PRINT}}",
          quantity: 1,
        },
      ],
      duration: {
        interval: "month",
        interval_count: 11,
      },
    },
  ],
});
```

### Change subscriptions

The Pacific offers two print subscription options: a basic option with advertisements or a premium option without advertisements. Some customers on the premium option want to change to the basic option at the next billing period. You can create a schedule using the existing subscription, and then update the schedule with the basic option with advertisements as a new phase.

#### Node.js

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// Create a subscription schedule with the existing subscription
const schedule = await stripe.subscriptionSchedules.create({
  from_subscription: "sub_ERf72J8Sc7qx7D",
});

// Update the schedule with the new phase
const subscriptionSchedule = await stripe.subscriptionSchedules.update(
  schedule.id,
  {
    phases: [
      {
        items: [
          {
            price: schedule.phases[0].items[0].price,
            quantity: schedule.phases[0].items[0].quantity,
          },
        ],
        start_date: schedule.phases[0].start_date,
        end_date: schedule.phases[0].end_date,
      },
      {
        items: [
          {
            price: "{{PRICE_PRINT_BASIC}}",
            quantity: 1,
          },
        ],
        duration: {
          interval: "month",
          interval_count: 1,
        },
      },
    ],
  },
);
```

### Increase the quantity

You can also schedule increases to the quantities on a subscription. The schedule below starts with one instance of the digital publication for one month. In the second phase, the quantity is increased to 2 for 11 more months.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer: "{{CUSTOMER_ID}}",
  start_date: "now",
  end_behavior: "release",
  phases: [
    {
      items: [
        {
          price: "{{PRICE_ID}}",
          quantity: 1,
        },
      ],
      duration: {
        interval: "month",
        interval_count: 1,
      },
    },
    {
      items: [
        {
          price: "{{PRICE_ID}}",
          quantity: 2,
        },
      ],
      duration: {
        interval: "month",
        interval_count: 11,
      },
    },
  ],
});
```

### Use coupons

The Pacific occasionally runs subscription specials. The schedule below starts the customer on the print publication at 50% off for six months. The schedule removes the coupon from the subscription in the second phase for the remaining six months.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer: "{{CUSTOMER_ID}}",
  start_date: "now",
  end_behavior: "release",
  phases: [
    {
      items: [
        {
          price: "{{PRICE_ID}}",
          quantity: 1,
        },
      ],
      duration: {
        interval: "month",
        interval_count: 6,
      },
      discounts: [
        {
          coupon: "{{COUPON_ID}}",
        },
      ],
    },
    {
      items: [
        {
          price: "{{PRICE_ID}}",
          quantity: 1,
        },
      ],
      duration: {
        interval: "month",
        interval_count: 6,
      },
    },
  ],
});
```

### Change tax rates

The Pacific operates in several jurisdictions, and some have unique tax rates for subscription-based businesses. One of these jurisdictions requires two tax rates: one for the first month when a customer initially subscribes, and one for recurring billings.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer: "{{CUSTOMER_ID}}",
  start_date: "now",
  end_behavior: "release",
  phases: [
    {
      items: [
        {
          price: "{{PRICE_ID}}",
          quantity: 1,
          tax_rates: ["txr_2J8lmBBGHJYyuUJqF6QJtaAA"],
        },
      ],
      duration: {
        interval: "month",
        interval_count: 1,
      },
    },
    {
      items: [
        {
          price: "{{PRICE_ID}}",
          quantity: 1,
          tax_rates: ["txr_2J8lmBBGHJYyuUJqF6QJtbBB"],
        },
      ],
      duration: {
        interval: "month",
        interval_count: 11,
      },
    },
  ],
});
```

### Release a subscription from a schedule

You can [release](https://docs.stripe.com/api/subscription_schedules/release.md) a subscription from a schedule if the status is `not_started` or `active`. Releasing a subscription leaves it in place but removes the schedule and any remaining phases.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.release(
  "{{SUBSCRIPTIONSCHEDULE_ID}}",
);
```

### Cancel a schedule and subscription

If a subscription schedule has an active subscription, you can cancel it and its associated subscription immediately. You can only cancel a subscription schedule if its status is `not_started` or `active`.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.cancel(
  "{{SUBSCRIPTIONSCHEDULE_ID}}",
);
```

### Reset the billing cycle anchor

The Pacific bills their long-time print customers on whichever day of the month they originally subscribed. This day is their billing cycle anchor.

If these customers transition to the digital edition, The Pacific schedules their transition date for the 1st day of the following month. They also reset the billing cycle anchor to that same date.

You can verify that the billing cycle anchor gets reset by creating a subscription using the sample code below. Look at the subscription in the Dashboard, and notice that the Upcoming Invoice is scheduled to bill the customer as soon as the digital subscription starts on the 1st.

To see what happens if you don’t reset the anchor, run the sample code again, but remove the line that sets the billing cycle anchor to `phase_start`. Without that line, the Upcoming Invoice in the Dashboard waits to bill the customer until a full month from today, despite the transition that occurs on the 1st.

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
          price: "{{PRICE_PRINT}}",
          quantity: 1,
        },
      ],
      end_date: 1690873200,
    },
    {
      items: [
        {
          price: "{{PRICE_DIGITAL}}",
          quantity: 1,
        },
      ],
      duration: {
        interval: "month",
        interval_count: 11,
      },
      billing_cycle_anchor: "phase_start",
    },
  ],
});
```

### Installment plans

Installment plans allow customers to make partial payments for a set amount of time until the total amount is paid. For example, when The Pacific buys new printing presses, they sell the used ones to other publications. Smaller publications rarely have enough funds to pay for a printing press upfront, so they pay using an installment plan instead.

For most presses, The Pacific charges 1,000 USD per month so a reusable price is created:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const price = await stripe.prices.create({
  unit_amount: 100000,
  currency: "usd",
  product: "prod_Hh99apo1OViyGW",
  recurring: {
    interval: "month",
  },
});
```

Depending on the make, model, and age of the printing press, The Pacific charges different amounts. This example charges 1,000 USD each month for 6 months, for a total of 6,000 USD.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  start_date: "now",
  end_behavior: "cancel",
  phases: [
    {
      items: [
        {
          price: "{{PRICE_ID}}",
          quantity: 1,
        },
      ],
      iterations: 6,
    },
  ],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer: "{{CUSTOMER_ID}}",
  start_date: "now",
  end_behavior: "cancel",
  phases: [
    {
      items: [
        {
          price: "{{PRICE_ID}}",
          quantity: 1,
        },
      ],
      iterations: 6,
    },
  ],
});
```

The number of `iterations` is multiplied by the price’s interval—6 monthly payments in this example—to determine the number of times the customer is charged. `end_behavior` determines what happens to the subscription after the last iteration is complete. In an installment plan, the subscription isn’t needed anymore so `end_behavior` is set to `cancel`.

In rare cases, The Pacific charges less than the usual 1,000 USD per month. In these scenarios, they use `price_data` to create a single-use price. This example creates a 500 USD price, and charges monthly for 6 months:

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  start_date: "now",
  end_behavior: "cancel",
  phases: [
    {
      items: [
        {
          price_data: {
            currency: "usd",
            product: "prod_Hh99apo1OViyGW",
            recurring: {
              interval: "month",
            },
            unit_amount: 50000,
          },
          quantity: 1,
        },
      ],
      iterations: 6,
    },
  ],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscriptionSchedule = await stripe.subscriptionSchedules.create({
  customer: "{{CUSTOMER_ID}}",
  start_date: "now",
  end_behavior: "cancel",
  phases: [
    {
      items: [
        {
          price_data: {
            currency: "usd",
            product: "prod_Hh99apo1OViyGW",
            recurring: {
              interval: "month",
            },
            unit_amount: 50000,
          },
          quantity: 1,
        },
      ],
      iterations: 6,
    },
  ],
});
```
