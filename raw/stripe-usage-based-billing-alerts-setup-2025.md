<!-- Source URL: https://docs.stripe.com/billing/subscriptions/usage-based/alerts -->
<!-- Fetched: 2026-05-05 -->

# Set up usage-based alerts

Set up an alert for when a customer exceeds a usage threshold.

The new Usage Analytics API lets you build analytics dashboards for your end users.

Set up alerts to get notified when customers exceed meter usage thresholds, or to trigger an invoice when customers reach a specific billing threshold. You can create alerts that apply to either specific customers or all customers.

## Before you begin

You must [create a meter](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide.md#create-meter) before you create an alert.

## Create usage alerts

You can configure [alerts](https://docs.stripe.com/api/billing/alert/create.md) using the Stripe Dashboard or API.

For example, you can create a one-time alert for customers that triggers when they reach 100 API calls. When a customer reaches 100 API calls, you receive a webhook notifying you that the customer has exceeded the threshold.

Stripe provides a usage alert type called `One-time per-customer usage alert`. This alert triggers when a customer exceeds the specified usage level for the first time, and only triggers one time per customer, regardless of future usage.

#### Dashboard

1. On the [Billing Alerts](https://dashboard.stripe.com/settings/billing/alerts) page, click **Create alert**.

1. On the **New alert** page, do the following:
   - For **Name**, enter the name for your alert. This isn’t visible to customers.
   - Under **Alert type**, select the meter that you want to set up alerts for.
   - For **Unit threshold**, set the usage amount to reach for an alert to trigger.
   - (Optional) Under **Application**, select **Specific customer** and the customer name, if you want the alert to apply only to that customer. Otherwise, leave the default of **Any customer** to configure the alert for all customers.
   - Click **Create alert**.

#### API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const alert = await stripe.billing.alerts.create({
  title: "Sample alert",
  alert_type: "usage_threshold",
  usage_threshold: {
    filters: [
      {
        type: "customer",
        customer: "{{CUSTOMER_ID}}",
      },
    ],
    meter: "{{METER_ID}}",
    gte: 100,
    recurrence: "one_time",
  },
});
```

## Listen for webhooks

After you configure an alert and start sending usage for that meter, you can listen for *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests). These events trigger when there’s a status change in Stripe, such as creating a new subscription or invoice.

In your application, set up an HTTP handler to accept a POST request containing the webhook event, and verify the signature of the event.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

app.post(
  "/webhook",
  bodyParser.raw({ type: "application/json" }),
  async (req, res) => {
    // Retrieve the event by verifying the signature using the raw body and secret.
    let event;

    try {
      event = stripe.webhooks.constructEvent(
        req.body,
        req.headers["stripe-signature"],
        process.env.STRIPE_WEBHOOK_SECRET,
      );
    } catch (err) {
      console.log(err);
      console.log(`⚠️  Webhook signature verification failed.`);
      console.log(
        `⚠️  Check the env file and enter the correct webhook secret.`,
      );
      return res.sendStatus(400);
    }
    // Extract the object from the event.
    const dataObject = event.data.object;

    // Handle the event
    // Review important events for Billing webhooks
    // https://stripe.com/docs/billing/webhooks
    // Remove the comment to see the various objects sent for this sample.
    switch (event.type) {
      case "billing.alert.triggered":
        // If the meter exceeds the defined threshold in the alert
        // Only triggers if it matches to at least one Stripe customer.
        break;
      default:
      // Unexpected event type
    }
    res.sendStatus(200);
  },
);
```

During development, use the Stripe CLI to [monitor webhooks and forward them to your application](https://docs.stripe.com/webhooks.md#test-webhook). Run the following in a new terminal while your development app is running:

#### curl

```bash
stripe listen --forward-to localhost:4242/webhook
```

For production, set up a webhook endpoint URL in the Dashboard, or use [Webhook Endpoints](https://docs.stripe.com/api/webhook_endpoints.md).

## Limitations

Consider the following limitations for usage alerts:

- We evaluate alerts when you report usage data after you create the alert. However, the evaluation includes usage data that you reported before you created the alert.
- You can create a maximum of 25 alerts for each combination of a specific meter and customer. However, you can create an alert for a specific meter for each of your customers.
- Alerts currently don’t work with test clocks.
