<!-- Source URL: https://docs.stripe.com/payments/off-session-payments/integrate-with-off-session-payments -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# How Off-Session Payments work

Learn how to build an integration with the Off-Session Payments API.

## Before you begin

- Your integration must use [Stripe API v2](https://docs.stripe.com/api-v2-overview.md), which uses JSON encoding (application/json) for requests and responses. Set the `Stripe-Version` request header to `2026-08-26.preview`.
- The Off-Session Payments API supports Card, Apple Pay, Google Pay, SEPA Direct Debit, and ACH Direct Debit payment methods.

## Register an event destination [Server-side]

Because authorizations run asynchronously, you need a v2 event destination to receive webhook notifications about payment state changes. Responses to create requests alone won’t carry final payment outcomes. This v2 API requires a separate setup from your existing v1 webhook integrations. Learn how to [set up event destinations](https://docs.stripe.com/events/set-up-events.md).

```curl
curl -X POST https://api.stripe.com/v2/core/event_destinations \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.preview" \
  --json '{
    "name": "Off-Session Payments Events",
    "enabled_events": [
        "v2.payments.off_session_payment.created",
        "v2.payments.off_session_payment.attempt_failed",
        "v2.payments.off_session_payment.attempt_started",
        "v2.payments.off_session_payment.succeeded",
        "v2.payments.off_session_payment.canceled",
        "v2.payments.off_session_payment.failed",
        "v2.payments.off_session_payment.paused",
        "v2.payments.off_session_payment.resumed"
    ],
    "type": "webhook_endpoint",
    "event_payload": "thin",
    "webhook_endpoint": {
        "url": "http://example.com/webhook"
    }
  }'
```

The following events are available for off-session payments:

| Event | Description |
| --- | --- |
| `v2.payments.off_session_payment.created` | Sent immediately following a successful request to the Off-Session Payments create endpoint. |
| `v2.payments.off_session_payment.attempt_started` | Sent whenever Stripe initiates an asynchronous attempt at authorization, whether it’s a retry or an initial authorization. |
| `v2.payments.off_session_payment.attempt_failed` | Sent after an authorization attempt fails, and there are still retries remaining on the retry schedule configured for smart retries. |
| `v2.payments.off_session_payment.succeeded` | Sent immediately after a successful authorization when using automatic capture, or immediately after calling the capture endpoint when using manual capture. |
| `v2.payments.off_session_payment.failed` | Sent after a failed authorization attempt when there are no retries remaining, or if the failure isn’t retryable based on the [decline code](https://docs.stripe.com/declines/codes.md). |
| `v2.payments.off_session_payment.canceled` | Sent after a request to cancel to terminate the Off-Session Payment or subsequent retries. |
| `v2.payments.off_session_payment.paused` | Sent immediately after a successful call to the pause endpoint. |
| `v2.payments.off_session_payment.resumed` | Sent immediately after a successful call to the resume endpoint. |

## Create an off-session payment [Server-side]

Pass the customer and payment method that you saved earlier, along with the desired amount and currency:

```curl
curl -X POST https://api.stripe.com/v2/payments/off_session_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-08-26.preview" \
  --json '{
    "amount": {
        "value": 1000,
        "currency": "usd"
    },
    "customer": "{{CUSTOMER_ID}}",
    "payment_method": "{{PAYMENTMETHOD_ID}}",
    "cadence": "recurring",
    "metadata": {},
    "retry_details": {
        "retry_strategy": "best_available"
    }
  }'
```

The following is an example of an Off-Session Payments API response:

```json
{
	"id": "osp_test_123456abcedf",
	"object": "v2.payments.off_session_payment",
	"amount_requested": {
	  "value": 1000,
	  "currency": "usd"
	},
	"cadence": "recurring",
	"created": "2025-05-15T16:09:26.693838357Z",
	"customer": "cus_abc123",
	"description": null,
	"failure_reason": null,
	"last_authorization_attempt_error": null,
	"latest_payment_attempt_record": null,
	"livemode": false,
	"metadata": {},
	"on_behalf_of": null,
	"payment_method": "pm_abc123",
	"payment_record": null,
	"retry_details": {
	  "attempts": 0,
	  "retry_strategy": "smart"
	},
	"statement_descriptor_suffix": null,
	"status": "pending",
	"test_clock": null
}
```

## Optional: Specify a retry policy

When creating the off-session payment, specify a retry policy:

```curl
curl -X POST https://api.stripe.com/v2/payments/off_session_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-08-26.preview" \
  --json '{
    "amount": {
        "value": 1000,
        "currency": "usd"
    },
    "customer": "{{CUSTOMER_ID}}",
    "payment_method": "{{PAYMENTMETHOD_ID}}",
    "cadence": "recurring",
    "metadata": {},
    "retry_details": {
        "retry_policy": "retry_policy_*"
    }
  }'
```

## Listen for events [Server-side]

Stripe attempts the first authorization shortly after returning the response to your request to `/v2/payments/off_session_payments`. After we receive the result from the authorization, we send an event to your event destination.

### On successful authorization

You receive an event `v2.payments.off_session_payments.succeeded`. The payload of the event contains the ID of the off-session payment object, which you can then retrieve with the API

Example `v2.payments.off_session_payment.succeeded` Event:

```json
{
  "id": "evt_test_12345abc",
  "object": "v2.core.event",
  "context": null,
  "created": "2025-05-15T16:09:36.153Z",
  "data": {},
  "reason": null,
  "related_object": {
    "id": "osp_test_123456abcedf",
    "type": "v2.payments.off_session_payment",
    "url": "/v2/payments/off_session_payments/osp_test_123456abcedf"
  },
  "type": "v2.payments.off_session_payment.succeeded",
  "livemode": false
}
```

```curl
curl https://api.stripe.com/v2/payments/off_session_payments/osp_test_12345abc \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-08-26.preview"
```

Example Off-Session Payments GET API Response:

```json
{
  "id": "osp_test_123456abcedf",
  "object": "v2.payments.off_session_payment",
  "amount_requested": {
    "value": 1000,
    "currency": "usd"
  },
  "cadence": "recurring",
  "created": "2025-05-15T16:09:26.693838357Z",
  "customer": "cus_abc123",
  "description": null,
  "failure_reason": null,
  "last_authorization_attempt_error": null,
  "latest_payment_attempt_record": "par_test_abc123",
  "livemode": false,
  "metadata": {},
  "on_behalf_of": null,
  "payment_method": "pm_abc123",
  "payment_record": "pr_test_abc123",
  "retry_details": {
    "attempts": 1,
    "retry_strategy": "smart"
  },
  "statement_descriptor": "Subscription PLUS",
  "statement_descriptor_suffix": null,
  "status": "succeeded",
  "transfer_data": null,
  "test_clock": "clock_12345abced"
}
```

To learn more about the authorization that was performed, you can retrieve the `Payment Record` object included in the `OffSessionPayment` object. It contains roughly the same information that’s on the `Charge` object when you’re using the Payment Intents API.

After you receive this event, you can move forward with fulfilling the customer’s order.

### On unsuccessful authorization

You receive an event `v2.payments.off_session_payment.attempt_failed`. The payload of the event contains the ID of the `OffSessionPayment` object, which you can then retrieve with the API:

```curl
curl https://api.stripe.com/v2/payments/off_session_payments/osp_xxxxx \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-08-26.preview"
```

Example Off-Session Payments API response:

```json
{
  "id": "osp_test_123456abcedf",
  "object": "v2.payments.off_session_payment",
  "amount_requested": {
    "value": 1000,
    "currency": "usd"
  },
  "cadence": "recurring",
  "created": "2025-05-15T16:09:26.693838357Z",
  "customer": "cus_abc123",
  "description": null,
  "failure_reason": null,
  "last_authorization_attempt_error": "generic_decline",
  "latest_payment_attempt_record": "par_test_abc123",
  "livemode": false,
  "metadata": {},
  "on_behalf_of": null,
  "payment_method": "pm_abc123",
  "payment_record": "pr_test_abc123",
  "retry_details": {
    "attempts": 1,
    "retry_strategy": "smart"
  },
  "statement_descriptor": "Subscription PLUS",
  "statement_descriptor_suffix": null,
  "status": "pending_retry",
  "transfer_data": null,
  "test_clock": "clock_12345abced"
}
```

Similarly, you can retrieve information about the failure using the `Payment Record` object, which contains information similar to what might be on a failed charge.

No action is necessary if you receive this event, because Stripe automatically retries the transaction using our Smart Retry logic. Continue to listen for events on this `OffSessionPayment` object.

## Handle terminal states [Server-side]

After Stripe exhausts the retries available on a payment, you receive the `v2.payments.off_session_payment.failed` event. The payload of the event contains the ID of the `Off-Session Payment` object, which you can then retrieve with the API.

```curl
curl https://api.stripe.com/v2/payments/off_session_payments/osp_xxxxx \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-08-26.preview"
```

Example off-session payments GET API response:

```json
{
  "id": "osp_test_123456abcedf",
  "object": "v2.payments.off_session_payment",
  "amount_requested": {
    "value": 1000,
    "currency": "usd"
  },
  "cadence": "recurring",
  "created": "2025-05-15T16:09:26.693838357Z",
  "customer": "cus_abc123",
  "description": null,
  "failure_reason": "retries_exhausted",
  "last_authorization_attempt_error": "generic_decline",
  "latest_payment_attempt_record": "par_test_abc123",
  "livemode": false,
  "metadata": {},
  "on_behalf_of": null,
  "payment_method": "pm_abc123",
  "payment_record": "pr_test_abc123",
  "retry_details": {
    "attempts": 5,
    "retry_strategy": "smart"
  },
  "statement_descriptor_suffix": null,
  "status": "failed",
  "transfer_data": null,
  "test_clock": "clock_12345abced"
}
```

The off-session payment is now in a terminal state, and you won’t be able to perform any more operations on it. The `failure_reason` field indicates why the payment failed:

- `retries_exhausted` — Stripe attempted all scheduled retries without success.
- `exceeded_retry_window` — The payment was paused and its retry window elapsed before it was resumed.
- `no_valid_payment_method` — The payment method was detached from the customer, the underlying card was deleted, or the attached mandate was deactivated.

If you need to bring the customer back on-session to collect payment, you need to do so using other on-session payments APIs, such as PaymentIntents or CheckoutSessions.

## Optional: Pause and resume a payment [Server-side]

If you want to temporarily stop retries for a payment in `pending_retry` status, you can pause it. Pausing halts all scheduled retries until you explicitly resume the payment.

```curl
curl -X POST https://api.stripe.com/v2/payments/off_session_payments/osp_test_123456abcedf/pause \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-08-26.preview"
```

To resume retries, call the resume endpoint:

```curl
curl -X POST https://api.stripe.com/v2/payments/off_session_payments/osp_test_123456abcedf/resume \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-08-26.preview"
```

A paused payment has `status: "paused"`. If the payment’s retry window elapses while it is paused, the payment transitions to `status: "failed"` with `failure_reason: "exceeded_retry_window"`.

## Optional: Cancel an off-session payment [Server-side]

```curl
curl -X POST https://api.stripe.com/v2/payments/off_session_payments/osp_test_123456abcedf/cancel \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-08-26.preview"
```

Example Off-Session Payments API response:

```json
{
  "id": "osp_test_123456abcedf",
  "object": "v2.payments.off_session_payment",
  "amount_requested": {
    "value": 1000,
    "currency": "usd"
  },
  "cadence": "recurring",
  "created": "2025-05-15T16:09:26.693838357Z",
  "customer": "cus_abc123",
  "description": null,
  "failure_reason": null,
  "last_authorization_attempt_error": "generic_decline",
  "latest_payment_attempt_record": "par_test_abc123",
  "livemode": false,
  "metadata": {},
  "on_behalf_of": null,
  "payment_method": "pm_abc123",
  "payment_record": "pr_test_abc123",
  "retry_details": {
    "attempts": 1,
    "retry_strategy": "smart"
  },
  "statement_descriptor": "Subscription PLUS",
  "statement_descriptor_suffix": null,
  "status": "canceled",
  "transfer_data": null,
  "test_clock": "clock_12345abced"
}
```

## Payment Records and Payment Attempt Records 

PaymentRecords represent a record of an individual payment and include all attempts and outcomes associated with it. It’s the primary reference point for understanding the lifecycle and status of a payment.

Learn more about the [Payment Records API](https://docs.stripe.com/payments/payment-records.md#understand-the-state-of-your-payments) in our integration guide.

## Configure Smart Retries 

Go to the [Revenue Recovery](https://dashboard.stripe.com/settings/payment-retries) section of the Dashboard if you want to customize your Smart Retries configuration.

Make sure the Smart Retry policy is selected, and set your desired retry frequency and duration. Our ML engine automatically determines the best times to retry within the parameters you specify. You can configure the Smart Retry policy to retry 4-8 times over intervals that you can configure from 1 week up to 2 months.

## Testing in a sandbox 

To test your integration with off-session payments without moving real money, you need to use a [Sandbox](https://docs.stripe.com/sandboxes.md). After you set up a sandbox, you can use the secret key associated with it to make POST requests to the Off-Session Payments API as in step 1.

To test Smart Retries, you can pass the `test_clock` parameter on the Off-Session Payments API. Advancing the [test clock](https://docs.stripe.com/billing/testing.md#test-clocks) simulates the passage of time and triggers a retry at the scheduled time.

```curl
curl -X POST https://api.stripe.com/v2/payments/off_session_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-08-26.preview" \
  --json '{
    "amount": {
        "value": 1000,
        "currency": "usd"
    },
    "customer": "{{CUSTOMER_ID}}",
    "payment_method": "{{PAYMENTMETHOD_ID}}",
    "cadence": "recurring",
    "metadata": {},
    "test_clock": "{{TESTHELPERSTESTCLOCK_ID}}",
    "retry_details": {
        "retry_strategy": "best_available"
    }
  }'
```

The following is an example of an Off-Session Payments API response in a sandbox using a test clock:

```json
{
	"id": "osp_test_123456abcedf",
	"object": "v2.payments.off_session_payment",
	"amount_requested": {
	  "value": 1000,
	  "currency": "usd"
	},
	"cadence": "recurring",
	"created": "2025-05-15T16:09:26.693838357Z",
	"customer": "cus_abc123",
	"description": null,
	"failure_reason": null,
	"last_authorization_attempt_error": null,
	"latest_payment_attempt_record": null,
	"livemode": false,
	"metadata": {},
	"on_behalf_of": null,
	"payment_method": "pm_abc123",
	"payment_record": null,
	"retry_details": {
	  "attempts": 0,
	  "retry_strategy": "smart"
	},
	"statement_descriptor_suffix": null,
	"status": "pending",
	"test_clock": "clock_12345abcefd"
}
```

## Test payment methods 

Go to [test cards](https://docs.stripe.com/testing.md) to see card numbers you can use for testing. Off-session payments also supports special test payment methods that simulate a failed authorization followed by a successful retry:

- Use `pm_osp_decline_then_succeed` as the `payment_method` parameter to simulate a card decline followed by a successful retry.
- Use `pm_osp_usBankAccount_decline_then_succeed` as the `payment_method` parameter to simulate a US bank account insufficient-funds failure followed by a successful retry. The debit payment remains pending until its network submission event and succeeds only after its guarantee event.
