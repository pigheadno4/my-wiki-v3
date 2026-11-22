<!-- Source URL: https://docs.stripe.com/payments/off-session-payments/smart-retries -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Smart Retries on Off-Session Payments

Learn how to use smart retries to automatically recover failed payments.

Payments can fail for several reasons, and many failures are recoverable. Stripe can automatically retry eligible failed payments for you to reduce involuntary churn. To configure retries, go to the [Revenue Recovery](https://dashboard.stripe.com/settings/payment-retries) page in your Dashboard.

## Smart Retries

Smart Retries uses AI to schedule retry attempts, maximizing the likelihood of successful invoice payment recovery. Instead of following a rigid schedule, it analyzes signals such as:

- Payment method usage patterns across different devices
- Time-of-day payment success rates (for example, debit card transactions in some regions might have higher success rates at specific times).
- Card network processing patterns

Stripe Smart Retries model continuously learns from transactions across the Stripe network and adapts to evolving payment behaviors. Smart retries typically improves recovery rates compared to traditional rule-based retry logic.

## Enable Smart Retries in the Dashboard

Go to the [Revenue Recovery](https://dashboard.stripe.com/settings/payment-retries) page in your Dashboard. Click the option to use a Smart Retry policy for subscriptions.

You can set the Smart Retry policy to retry the payment a specific number of times within a time period: 1 week, 2 weeks, 3 weeks, 1 month, or 2 months. The recommended default is 8 tries within 2 weeks.

## Change your API integration to use retries

In your API call to `/v2/payments/off_session_payments`, pass the `retry_details[retry_strategy]` parameter to make the payment eligible to be retried.

```bash
curl -X POST https://api.stripe.com/v2/payments/off_session_payments \
  -H "Content-Type: application/json" \
  -H "Stripe-Version: 2026-04-22.preview" \
  -H "Authorization: Bearer {{YOUR_API_KEY}}" \
  -d '{
    ...
    "retry_details": {
      "retry_strategy": "best_available"
    }
    ...
  }'
```

The API response includes the same `retry_details` hash, but `retry_strategy` might differ depending on the best available strategy for the payment. If you see `retry_strategy: "smart"`, Smart Retries will retry the payment.

## Custom retry schedules

To opt out of AI-based retries, configure a custom retry schedule. You can configure up to three retry attempts per payment, with up to 9 days between attempts.

To use custom retry schedules, visit the [Revenue Recovery](https://dashboard.stripe.com/settings/payment-retries) page and select **Custom retry schedule**.

When creating the off-session payment, set `retry_details.retry_strategy` to `best_available`. The API response shows `retry_strategy: "scheduled"` when the payment uses a custom retry schedule.

## Direct Debit payments

AI-based retries aren’t available for Direct Debit payments. Stripe offers [heuristic retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries.md#direct-debit-retries), which are based on rules derived from Stripe historical observations about bank account payments.

To enable retries for Direct Debit payments, go to the [Revenue Recovery](https://dashboard.stripe.com/settings/payment-retries) page in your Dashboard. Toggle the option to use retries for ACH Direct Debit payments.

When creating the off-session payment, pass a Direct Debit `PaymentMethod` object and set `retry_details.retry_strategy` to `best_available`. The API response shows `retry_strategy: "heuristic"` when the payment is using heuristic retries.

## Webhook events

For both smart retries and custom retry schedules, Stripe reattempts the payment according to your specified retry strategy. Subscribe to the `v2.payments.off_session_payment.attempt_started` event to learn when Stripe makes these attempts.

The `retry_details.attempts` attribute on the `OffSessionPayment` object indicates how many authorization attempts have been made so far. If a failure returns a hard-decline code, Stripe won’t be able to retry the payment. The `last_authorization_attempt_error` field provides the specific decline reason.

When retries are still pending, the `OffSessionPayment` has a status of `pending_retry`. After Stripe exhausts all retries, you receive a `v2.payments.off_session_payment.failed` event. The `OffSessionPayment` has `status: "failed"` and a `failure_reason` indicating why it failed. The possible failure reasons are:

- `retries_exhausted` — Stripe attempted all scheduled retries without success.
- `exceeded_retry_window` — The payment was paused and its retry window elapsed before it was resumed.
- `no_valid_payment_method` — The payment method was detached from the customer, the underlying card was deleted, or the attached mandate was deactivated.

You can also manually pause a payment that is in `pending_retry` status to halt retries temporarily. See [Pause and resume a payment](https://docs.stripe.com/payments/off-session-payments/integrate-with-off-session-payments.md#pause-resume) for details.

To implement this integration, set up event destinations for the required events, including:

- `v2.payments.off_session_payment.created`
- `v2.payments.off_session_payment.attempt_failed`
- `v2.payments.off_session_payment.succeeded`
- `v2.payments.off_session_payment.failed`
- `v2.payments.off_session_payment.paused`
- `v2.payments.off_session_payment.resumed`

## Hard decline codes

Stripe can’t automatically retry a payment if the card issuer returns any of these hard-decline codes:

- `incorrect_number`
- `lost_card`
- `pickup_card`
- `stolen_card`
- `revocation_of_authorization`
- `revocation_of_all_authorizations`
- `authentication_required`
- `highest_risk_level`
- `transaction_not_allowed`
