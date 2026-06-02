<!-- Source URL: https://docs.stripe.com/billing/subscriptions/usage-based/meters/configure -->
<!-- Fetched: 2026-05-05 -->

# Create and configure a meter

Create and configure a meter for usage-based billing.

Before you can [record customer usage](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage.md), you must create a meter, then configure it. After you configure the meter, you can’t make any changes aside from the display name.

## Create a meter

Meters specify how to aggregate meter events over a billing period. Meter events represent all actions that customers take in your system (for example, API requests). Meters attach to prices and form the basis of what’s billed.

For the Hypernian example, meter events are the number of tokens a customer uses in a query. The meter is the sum of tokens over a month.

You can use the Stripe Dashboard or API to configure a meter. To use the API with the Stripe CLI to create a meter, [get started with the Stripe CLI](https://docs.stripe.com/stripe-cli.md).

#### Dashboard

1. On the [Meters](https://dashboard.stripe.com/test/meters) page, click **Create meter**.
1. In the meter editor:
   - For **Meter name**, enter the name of the meter to display and for organization purposes. For the Hypernian example, enter “Hypernian tokens.”
   - For **Event name**, enter the name to display in meter events when reporting usage to Stripe. For the Hypernian example, enter “hypernian_tokens.”
   - Set the **Aggregation method** in the dropdown:
     - For the Hypernian example, select **Sum**. This will *sum the values* reported (in this example, number of tokens a customer uses) to determine the usage to bill for.
     - Choose **Count** to bill based on the *number* of events reported.
     - Choose **Last** to bill based on the *last value* reported.
     - Use the preview pane to set example usage events and verify the aggregation method.
   - Click **Create meter**.

#### API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const meter = await stripe.billing.meters.create({
  display_name: "Hypernian tokens",
  event_name: "hypernian_tokens",
  default_aggregation: {
    formula: "sum",
  },
  customer_mapping: {
    event_payload_key: "stripe_customer_id",
    type: "by_id",
  },
  value_settings: {
    event_payload_key: "value",
  },
});
```

## Meter configuration attributes

| Meter attribute | Description                                                                                                                                                                                                                                                                                                                                                           |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Event name      | The name of the meter event that you want to record usage for with the meter. When you send usage to Stripe, specify this event name in the `event_name` field for the [Meter Event](https://docs.stripe.com/api/billing/meter-event/object.md). This allows the correct meter to record and aggregate the usage. You can only use an event name with a single meter. |
| Event ingestion | Specify how to send events to Stripe:                                                                                                                                                                                                                                                                                                                                 |

- **Raw**: Handle all meter events as standalone events. Multiple events sent for the same timestamp don’t overwrite each other. The aggregation includes the multiple events. This is the default option if you don’t specify anything.
- **Pre-aggregated**: If you send events for a specific time interval (hourly or daily), Stripe only uses the most recently received meter event in that time interval. A newer event sent within the same hourly or daily window overwrites the previous one. The meter event timestamp in UTC dictates the hour and day boundaries. |
  | Aggregation formula | Specify how to aggregate usage over the billing period:

- **Sum**: Bill customers based on the sum of all usage values for the billing period.
- **Count**: Bill customers based on the count of all usage for the billing period.
- **Last**: Bill customers based on the most recent usage event’s value for the billing period. |
  | Payload key overrides | Specify which keys in the event payload refer to the customer and numerical usage values:

- **value_settings**: Use this parameter to define the key in the event payload that refers to the numerical usage value. The default key is `value`, but you can specify a different key, such as tokens.
- **customer_mapping**: Use this parameter to define the key in the event payload that refers to the [Customer ID](https://docs.stripe.com/api/customers/object.md#customer_object-id). The default key is `stripe_customer_id`, but you can specify a different key, such as `customer_id`. |

## Fix incorrect usage data

If you identify incorrectly recorded events in the current billing period, you can create a [Meter Event Adjustment](https://docs.stripe.com/api/billing/meter-event-adjustment/create.md) to cancel those events. You must specify the [identifier](https://docs.stripe.com/api/billing/meter-event/object.md#billing_meter_event_object-identifier) for the meter event.

You can only cancel events sent to Stripe within the last 24 hours. If you cancel usage that’s included on a finalized invoice, we won’t update the invoice or issue a corrected invoice for the canceled usage. We don’t support billing adjustments for canceled usage on a finalized invoice sent to a customer.

You can also fix incorrectly recorded usage data by recording negative quantities. If the overall cycle usage is negative, Stripe reports the invoice line item usage quantity as 0.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const meterEventAdjustment = await stripe.billing.meterEventAdjustments.create({
  type: "cancel",
  event_name: "hypernian_tokens",
  cancel: {
    identifier: "{{METER_EVENT_IDENTIFIER}}",
  },
});
```
