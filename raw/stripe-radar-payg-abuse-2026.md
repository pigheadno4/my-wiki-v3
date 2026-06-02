<!-- Source URL: https://docs.stripe.com/radar/pay-as-you-go-abuse -->
<!-- Fetched: 2026-05-10 -->

# Pay-as-you-go abuse evaluation

Learn how to identify subscription customers at risk of service abuse by not paying their next invoice.

The Radar API provides a pay-as-you-go abuse signal that can help you identify subscription customers who are likely to abuse the platform by intentionally not paying their next invoice. Use this signal for post-paid billing models where customers accumulate usage before being charged. For example, use it for usage-based services that bill at the end of the month.

Use this signal to manually review high-risk accounts, issue an early invoice, or limit product access before a billing cycle ends.

## How it works

Instead of evaluating a payment at checkout, you simulate a future invoice payment to receive a non-payment abuse risk signal. The risk signal indicates whether the customer’s upcoming invoice is at risk of abuse.
A diagram showing the non-payment abuse evaluation flow for a subscription. (See full diagram at https://docs.stripe.com/radar/pay-as-you-go-abuse)
Use the [Payment Evaluation](https://docs.stripe.com/api/radar/payment-evaluation.md) endpoint for evaluation outside of a checkout flow, such as a background worker that evaluates subscriptions mid-billing cycle. A Radar Session isn’t required, so the `client_device_metadata_details` field is optional for this use case.

## Create a payment evaluation

To request a non-payment abuse risk level, you need a payment method, customer, and the expected invoice amount. Call `POST /v1/radar/payment_evaluations` with the `money_movement_details` set to indicate a recurring off-session charge:

```curl
curl https://api.stripe.com/v1/radar/payment_evaluations \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-03-25.dahlia" \
  -d "payment_details[amount]=2500" \
  -d "payment_details[currency]=usd" \
  --data-urlencode "payment_details[payment_method_details][payment_method]=pm_****" \
  -d "payment_details[money_movement_details][money_movement_type]=card" \
  -d "payment_details[money_movement_details][card][customer_presence]=off_session" \
  -d "payment_details[money_movement_details][card][payment_type]=recurring" \
  --data-urlencode "customer_details[customer]=cus_****"
```

Stripe returns a `signals.non_payment_abuse` object in the response:

```json
{
  "id": "peval_***",
  "object": "radar.payment_evaluation",
  "created_at": 1773177872,
  "livemode": false,
  "metadata": {},
  "recommended_action": "continue",
  "signals": {
    "fraudulent_payment": {
      "evaluated_at": 1773177872,
      "risk_level": "not_assessed",
      "score": -1.0
    },
    "non_payment_abuse": {
      "evaluated_at": 1773177872,
      "risk_level": "highest"
    }
  }
}
```

The `signals.fraudulent_payment` fields return default values (`-1.0` for scores) because they don’t apply to the subscription invoice use case. The `recommended_action` field is at the evaluation level, not the signal level, so its value reflects the overall evaluation outcome and won’t always be `continue`. Use `signals.non_payment_abuse.risk_level` for your evaluation logic.

### Retrieve payment details from a subscription

If you’re evaluating a Stripe Billing subscription, you can retrieve the necessary inputs by fetching the subscription and upcoming invoice.

Retrieve the payment method and customer from the subscription:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.retrieve(
  "{{SUBSCRIPTION_ID}}",
  {
    expand: ["customer"],
  },
);
```

Get the invoice amount:

```bash
curl -G https://api.stripe.com/v1/invoices/upcoming \
  -u "{{SECRET_KEY}}:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "subscription={{SUBSCRIPTION_ID}}"
```

Use `default_payment_method` from the subscription (or alternatively `customer.invoice_settings.default_payment_method`) and `amount_due` from the upcoming invoice.

## Risk levels

| Value          | Description                                                              |
| -------------- | ------------------------------------------------------------------------ |
| `normal`       | This level is low risk. No action is required.                           |
| `elevated`     | This level is moderate risk. Consider manual review or usage limits.     |
| `highest`      | This level is high risk. Consider pausing usage or requiring prepayment. |
| `low`          | This level is low risk. No action is required.                           |
| `not_assessed` | This signal wasn’t assessed.                                             |
| `unknown`      | The risk level is unknown.                                               |

## Outcome labeling

No outcome or event reporting is required for this use case.

## Sandbox behavior

In a sandbox, `signals.non_payment_abuse.risk_level` returns a simulated `risk_level` that can vary based on the input data. To test a specific risk level, use the following test payment method:

| Payment method             | Card number      | Risk level |
| -------------------------- | ---------------- | ---------- |
| `pm_card_riskLevelHighest` | 4000000000004954 | `highest`  |

For more test payment methods, see [fraud prevention testing](https://docs.stripe.com/testing.md?testing-method=payment-methods#fraud-prevention).

## API behavior

This endpoint is fail-open. A `4xx` or `5xx` response from Stripe won’t affect your subscription or billing flow. You can retry the call or proceed without the signal.
