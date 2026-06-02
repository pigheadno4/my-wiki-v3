<!-- Source URL: https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api -->
<!-- Fetched: 2026-05-05 -->

# Record usage for billing with the API

Learn how to record usage using the Stripe API.

You must record usage in Stripe to make sure you bill your customers the correct amounts each billing period. To record usage, first [configure your meter](https://docs.stripe.com/billing/subscriptions/usage-based/meters/configure.md), and then send meter events that include the event name configured on the meter, customer ID, numerical value, and a timestamp (optional).

You can decide how often you record usage in Stripe, for example as it occurs or in batches. Stripe processes meter events asynchronously, so aggregated usage in meter event summaries and on upcoming invoices might not immediately reflect recently received meter events.

## Create meter events

Create a [Meter Event](https://docs.stripe.com/api/billing/meter-event/create.md) using the API.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const meterEvent = await stripe.billing.meterEvents.create({
  event_name: "hypernian_tokens",
  payload: {
    value: "25",
    stripe_customer_id: "{{CUSTOMER_ID}}",
  },
});
```

### Idempotency

Use [idempotency keys](https://docs.stripe.com/api/idempotent_requests.md) to prevent reporting usage for each event more than one time because of latency or other issues. Every meter event corresponds to an [identifier](https://docs.stripe.com/api/billing/meter-event/create.md#create_billing_meter_event-identifier) that you can specify in your request. If you don’t specify an identifier, we auto-generate one for you.

### Event timestamps

Make sure the timestamp is within the past 35 calendar days and isn’t more than 5 minutes in the future. The 5-minute window is for clock drift between your server and Stripe systems.

### Usage values

The numerical usage value in the payload accepts decimal values. Decimal values are also supported on invoices. If the overall cycle usage is negative, Stripe reports the invoice line item usage quantity as 0.

### Rate limits

The [Meter Event](https://docs.stripe.com/api/billing/meter-event/create.md) endpoint allows 1,000 calls per second in live mode. If you anticipate exceeding this limit, you have two options:

- Pre-aggregate your usage data before sending it to Stripe. For example, instead of sending a Event for each individual user action, you could accumulate usage across multiple actions and send a single aggregated event periodically. This reduces the number of API calls while still accurately reporting total usage.
- Use the high-throughput ingestion method with meter event streams for significantly higher volumes.

In sandbox mode, calls to the `meter event` and `meter event stream` endpoint count toward the [basic limit](https://docs.stripe.com/rate-limits.md#rate-limiter).

> If you’re a Connect platform making requests on behalf of a connected account using the `Stripe-Account` header, you’re subject to [regular Stripe rate limits](https://docs.stripe.com/rate-limits.md), which is 100 operations per second.

You can monitor for `429` status codes and implement a retry mechanism with an exponential back-off schedule to manage request volume.

### High-throughput ingestion with higher rate limits (API v2)

With the [API v2](https://docs.stripe.com/api-v2-overview.md), you can send up to 10,000 events per second to Stripe using meter event streams. This works in live mode only.

[Contact sales](https://stripe.com/contact/sales) if you need to send up to 200,000 events per second.

This endpoint uses stateless authentication sessions. First, create a [Meter Event Session](https://docs.stripe.com/api/v2/billing/meter-event-sessions/create.md) to receive an authentication token. Authentication tokens are only valid for 15 minutes, so you must create a new meter event session when your token expires.

Next, use the returned authentication token to create your high-throughput meter events with the [Meter Event Stream](https://docs.stripe.com/api/v2/billing/meter-event-stream/create.md).

> Because of the large volume of API requests, we don’t include meter event stream requests in the [Workbench Logs tab](https://docs.stripe.com/workbench/overview.md#request-logs).

You can monitor for `429` status codes and implement a retry mechanism with an exponential backoff schedule to manage request volume.

#### Node.js

```node
import { Stripe } from "stripe";

const apiKey = "{{API_KEY}}";
const customerId = "{{CUSTOMER_ID}}";

let meterEventSession = null;

async function refreshMeterEventSession() {
  if (
    meterEventSession === null ||
    new Date(meterEventSession.expires_at * 1000) <= new Date()
  ) {
    // Create a new meter event session in case the existing session expired
    const client = new Stripe(apiKey);
    meterEventSession = await client.v2.billing.meterEventSession.create();
  }
}

async function sendMeterEvent(meterEvent) {
  // Refresh the meter event session, if necessary
  await refreshMeterEventSession();

  // Create a meter event
  const client = new Stripe(meterEventSession.authentication_token);
  await client.v2.billing.meterEventStream.create({
    events: [meterEvent],
  });
}

// Send meter events
sendMeterEvent({
  event_name: "hypernian_tokens",
  payload: {
    stripe_customer_id: customerId, // Replace with actual customer ID
    value: "27",
  },
}).catch((error) => {
  console.error("Error sending meter event:", error);
});
```

## Handle meter event errors

Stripe asynchronously processes meter events. If we find an error, we create one of the following [Events](https://docs.stripe.com/api/events.md):

| Event                                     | Description                                                            | Payload type |
| ----------------------------------------- | ---------------------------------------------------------------------- | ------------ |
| `v1.billing.meter.error_report_triggered` | This event occurs when a meter has invalid usage events.               | `thin`       |
| `v1.billing.meter.no_meter_found`         | This event occurs when usage events have missing or invalid meter IDs. | `thin`       |

> To create an event destination that subscribes to thin events, enable Workbench in your [Developer settings](https://dashboard.stripe.com/settings/developers).

### Example payloads

#### Example error report event

The following is an example payload for a `v1.billing.meter.error_report_triggered` event.

```json
{
  "id": "evt_test_65R2GpwDsnmpzihMjdT16R2GDhI4SQdXJGRbvn7JA8mPEm",
  "object": "v2.core.event",
  "created": "2024-08-28T20:54:12.051Z",
  "data": {
    "developer_message_summary": "There is 1 invalid event",
    "reason": {
      "error_count": 1,
      "error_types": [
        {
          "code": "meter_event_no_customer_defined",
          "error_count": 1,
          "sample_errors": [
            {
              "error_message": "Customer mapping key stripe_customer_id not found in payload.",
              "request": {
                "id": "",
                "idempotency_key": "37c741d8-1f7e-4adc-af16-afdca1d73b37"
              }
            }
          ]
        }
      ]
    },
    "validation_end": "2024-08-28T20:54:10.000Z",
    "validation_start": "2024-08-28T20:54:00.000Z"
  },
  "reason": null,
  "related_object": {
    "id": "mtr_test_61R2GlpFXJ4R3L5DN41Fb82guyGVEUmO",
    "type": "billing.meter",
    "url": "/v1/billing/meters/mtr_test_61R2GlpFXJ4R3L5DN41Fb82guyGVEUmO"
  },
  "type": "v1.billing.meter.error_report_triggered"
}
```

#### Example error event for an incorrect meter

The following is an example payload for a `v1.billing.meter.no_meter_found` event.

```json
{
  "created": "2024-10-01T20:42:52.203Z",
  "id": "evt_test_61REarcdWIsXleUiz16REahOMTSQbAhSD0fdnF9JAUdk",
  "object": "v2.core.event",
  "context": null,
  "type": "v1.billing.meter.no_meter_found",
  "data": {
    "developer_message_summary": "There is 1 invalid event",
    "reason": {
      "error_count": 1,
      "error_types": [
        {
          "code": "no_meter",
          "error_count": 1,
          "sample_errors": [
            {
              "error_message": "No meter was found matching event_name d2aa8cb3-3f00-44a4-b98f-3fbd1d0e93b1.",
              "request": {
                "identifier": "df5d4002-515b-4090-8fe2-a1b1f6f5b945"
              }
            }
          ]
        }
      ]
    },
    "validation_end": "2024-10-01T20:42:50.000Z",
    "validation_start": "2024-10-01T20:42:40.000Z"
  },
  "livemode": false,
  "reason": null,
  "related_object": {}
}
```

### Error codes

The `reason.error_types.code` provides the error categorization that triggered the error. Possible error codes include:

- `meter_event_customer_not_found`
- `meter_event_no_customer_defined`
- `meter_event_dimension_count_too_high`
- `archived_meter`
- `timestamp_too_far_in_past`
- `timestamp_in_future`
- `meter_event_value_not_found`
- `meter_event_invalid_value`
- `no_meter` (supported only for the `v1.billing.meter.no_meter_found` event type)

### Listen to events

You can listen to events by setting up a [webhook endpoint or another type of event destination](https://docs.stripe.com/event-destinations.md).

1. On the [Webhooks](https://dashboard.stripe.com/webhooks) tab in Workbench, click **Create new destination**. Alternatively, use this [template](https://dashboard.stripe.com/webhooks/create?payload_style=thin&events=v1.billing.meter.error_report_triggered%2Cv1.billing.meter.no_meter_found) to configure a new destination in Workbench with the two event types pre-selected.

1. Click **Show advanced options**, then select the **Thin** payload style.

1. Select `v1.billing.meter.error_report_triggered` and `v1.billing.meter.no_meter_found` from the list of events.

1. Create a handler to process the event.

   #### Node.js

   ```javascript
   const express = require("express");
   const { Stripe } = require("stripe");

   const app = express();

   const apiKey = process.env.STRIPE_API_KEY;
   const webhookSecret = process.env.WEBHOOK_SECRET;

   const client = new Stripe(apiKey);

   app.post(
     "/webhook",
     express.raw({ type: "application/json" }),
     async (req, res) => {
       const sig = req.headers["stripe-signature"];

       try {
         const thinEvent = client.parseThinEvent(req.body, sig, webhookSecret);

         // Fetch the event data to understand the failure
         const event = await client.v2.core.events.retrieve(thinEvent.id);
         if (event.type == "v1.billing.meter.error_report_triggered") {
           const meter = await event.fetchRelatedObject();
           const meterId = meter.id;
           // Record the failures and alert your team
           // Add your logic here
         }
         res.sendStatus(200);
       } catch (err) {
         console.log(`Webhook Error: ${err.message}`);
         res.status(400).send(`Webhook Error: ${err.message}`);
       }
     },
   );

   app.listen(4242, () => console.log("Running on port 4242"));
   ```

1. Test your handler by configuring a [local listener](https://docs.stripe.com/cli/listen) with the [Stripe CLI](https://docs.stripe.com/stripe-cli.md) to send events to your local machine for testing before deploying the handler to production. Use the `--forward-thin-to` flag to specify which URL to forward the `thin` events to and the `--thin-events` flag to specify which thin events to forward. You can forward all thin events with an asterisk (`*`), or a subset of thin events to your application.

   ```sh
   $ stripe listen --forward-thin-to localhost:4242/webhooks --thin-events "*"
   ```

1. Trigger test events to your handler. Use the [trigger function](https://docs.stripe.com/cli/trigger) to run the following commands, which simulates the respective events in your account for testing.

   ```sh
   $ stripe trigger v1.billing.meter.error_report_triggered --api-key <your-secret-key>
   $ stripe trigger v1.billing.meter.no_meter_found --api-key <your-secret-key>
   ```

1. If you process events with a webhook endpoint, [verify the webhook signatures](https://docs.stripe.com/webhooks.md#verify-official-libraries) to secure your endpoint and validate all requests are from Stripe.

1. Correct and resend invalid events for re-processing.
