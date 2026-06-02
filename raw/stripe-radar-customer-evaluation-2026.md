<!-- Source URL: https://docs.stripe.com/radar/multi-account-and-account-sharing-abuse -->
<!-- Fetched: 2026-05-10 -->

# Multi-account and account sharing abuse evaluation

Get risk evaluations for customer account registration and login events.

The [Customer Evaluation API](https://docs.stripe.com/api/radar/customer-evaluation.md) provides risk intelligence for your registration and login flows to detect multi-accounting patterns and suspicious account sharing:

- **No payment collection required**: Evaluate risk during registration and at login, before collecting any payment information.
- **Get risk scores upfunnel**: Apply decision signals earlier in your workflow to get risk scores sooner (login or registration) than traditional Stripe PaymentIntents. This can help you make informed decisions about allowing or blocking account access where service abuse is suspected.

### Multi-account abuse

The `multi_accounting` signal identifies whether a single fraudulent actor is registering multiple accounts to abuse your service.

### Account sharing abuse

The `account_sharing` signal identifies whether a single user account is being used simultaneously in multiple locations.

## Customer evaluation lifecycle

To request a customer evaluation to detect abuse:

1. On the client side, use [Stripe.js](https://docs.stripe.com/sdks/stripejs-react.md) to create a [Radar Session](https://docs.stripe.com/radar/radar-session.md) that captures device metadata, then send the session token to your server.
1. [Create a customer](https://docs.stripe.com/api/customers/create.md) (or use an existing `Customer` object).
1. Request a `CustomerEvaluation` when customers register or log in.
1. After the customer registers or logs in, report the outcome to Stripe to improve future evaluations.

The following diagram shows the high-level interactions between you (the business), Stripe, and your end customer at registration time.
A diagram showing the Customer Evaluation API sequence of interactions for a registration flow. (See full diagram at https://docs.stripe.com/radar/multi-account-and-account-sharing-abuse)

## Create a Radar Session

Before requesting a customer evaluation, you must capture device metadata from the client using Stripe.js. Pass the [Radar Sessions](https://docs.stripe.com/radar/radar-session.md) token from the response to your server to use it in the Customer Evaluation request.

## Create a CustomerEvaluation

After you create a [Radar Session](https://docs.stripe.com/radar/radar-session.md) to capture device metadata, request a [CustomerEvaluation](https://docs.stripe.com/api/radar/customer-evaluation/create.md) to get risk signals from Stripe.

### Registration flow

Use the `registration` event type to evaluate new user registrations. You can reference an existing `Customer`. To ensure accurate fraud detection, preserve the customer ID to use in future payment requests.

```curl
curl https://api.stripe.com/v1/radar/customer_evaluations \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-03-04.preview" \
  -d event_type=registration \
  -d "evaluation_context[0][type]=customer_details" \
  --data-urlencode "evaluation_context[0][customer_details][customer]=cus_****" \
  -d "evaluation_context[1][type]=client_details" \
  --data-urlencode "evaluation_context[1][client_details][radar_session]=rse_****"
```

### Login flow

Use the `login` event type to evaluate user login attempts and detect account sharing patterns. Use the same customer ID that you created during registration.

```curl
curl https://api.stripe.com/v1/radar/customer_evaluations \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-03-04.preview" \
  -d event_type=login \
  -d "evaluation_context[0][type]=customer_details" \
  --data-urlencode "evaluation_context[0][customer_details][customer]=cus_****" \
  -d "evaluation_context[1][type]=client_details" \
  --data-urlencode "evaluation_context[1][client_details][radar_session]=rse_****"
```

### Risk signals

Stripe returns risk signals in the response based on the evaluation type. Use these signals to make informed decisions about allowing or blocking the action.

| Evaluation type | Signal returned    | Description                                                                     |
| --------------- | ------------------ | ------------------------------------------------------------------------------- |
| `registration`  | `multi_accounting` | Risk that the same end customer is registering multiple times                   |
| `login`         | `account_sharing`  | Risk that the same account is being used from multiple locations simultaneously |

### Score interpretation

Each signal returns a `score` from 0 to 100 and a corresponding `risk_level` that categorizes the score into a qualitative band. Use the `risk_level` to make quick decisions, or use the raw `score` for fine-grained control.

| Risk level | Score range | Description                                                                             |
| ---------- | ----------- | --------------------------------------------------------------------------------------- |
| `highest`  | 75-100      | Indicates a high risk of abuse. Consider blocking or requiring additional verification. |
| `elevated` | 65–74       | Indicates an elevated risk of abuse. Consider applying additional friction or review.   |
| `normal`   | 0–64        | Indicates typical risk. No additional action recommended.                               |

## Report outcome

After you evaluate a customer, report the final outcome to Stripe. This feedback improves our accuracy in abuse detection over time.

Call [report](https://docs.stripe.com/api/radar/customer-evaluation/report.md) and pass the `type` of event you’re reporting. Supported event types include:

- `registration_success`: Report when a registration completes successfully
- `registration_failed`: Report when a registration attempt fails
- `login_success`: Report when a login completes successfully
- `login_failed`: Report when a login attempt fails

The following example shows a successful registration:

```curl
curl https://api.stripe.com/v1/radar/customer_evaluations/caeval_******/report \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-03-04.preview" \
  -d type=registration_success
```

## Reuse customer at time of payment

When creating payments, you must use the same customer ID that you used for the customer evaluation. This helps with providing accurate risk assessments by connecting registration, login, and payment activity for the same customer.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  customer: "cus_****",
  payment_method: "pm_****",
  confirm: true,
});
```

> The `customer` parameter at the time of payment must match the customer ID used when creating the `CustomerEvaluation`.
