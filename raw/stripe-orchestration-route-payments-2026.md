<!-- Source URL: https://docs.stripe.com/payments/orchestration/route-payments -->
<!-- Fetched: 2026-05-11 -->

# Route payments to multiple processors

Use Orchestration to route payments across your payment processors.

> #### Want access to Orchestration?
>
> Orchestration is in private preview.

Orchestration lets you configure payment processor selection using rules you create in the Dashboard. You can route payments based on conditions such as card country, currency, amount, and more. Within your rules, you can set up retry actions to attempt a payment that failed on your main processor one more time on another chosen processor. You can also view analytics for payment success rates and accepted payment volume across processors.

## Before you begin

To access Orchestration, contact your Stripe representative who can guide you through the following steps:

- Confirm that Stripe supports the destination processor.
- Onboard your Stripe account with Orchestration. You need to provide API keys for your destination processor in the Stripe Dashboard.
- Confirm your Stripe integration supports Orchestration. Your Stripe representative can assist as you go live.

## Add test rules in a sandbox [Dashboard]

Rules contain the [conditions and actions](https://docs.stripe.com/payments/orchestration/rules.md) for routing payments to a specific processor.

1. Create a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) if you don’t have an existing one. You use the sandbox to add and test rules before going live.
1. On the [Orchestration](https://dashboard.stripe.com/test/orchestration/rules) page in the Dashboard, click **Add rules**.
1. Add rules with a condition that routes the payment to one of the available processors if the `Card country` is equal to `United Kingdom`. Add an action to route the payment to Stripe if the condition isn’t met.
1. [Optional] Add a processor to retry the payment one more time if the payment fails on the main processor.
1. Click **Activate test rules**.

## Create a PaymentIntent [Server-side]

> You can also configure payments created by Billing, Checkout Sessions, Payment Links, or in the Dashboard to follow your rules. These payments automatically create a PaymentIntent. Contact your Stripe representative to configure these automatically-created PaymentIntents to use Orchestration.

When you create a [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md), include the `payments_orchestration` parameter to enable Orchestration.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 500,
  currency: "usd",
  payment_method_types: ["card"],
  payment_method: "pm_card_visa",
  payments_orchestration: {
    enabled: true,
  },
  confirm: true,
});
```

Orchestration doesn’t support the Setup Intents API and [flexible acquiring](https://docs.stripe.com/payments/flexible-payments.md) features on other processors. For transactions that involve a 3D Secure request, you’re responsible for providing Stripe with the Acquirer BIN that corresponds to the processor you route those transactions to. Check with your Stripe representative if you’re unsure whether Orchestration supports the features you use.

## Verify your test rules [Server-side] [Dashboard]

Use [test cards](https://docs.stripe.com/testing.md) to make sure Stripe routes payments to the processors specified by your rules. For example, to test if payments route to the processor you selected when the card country equals the United Kingdom, you can use the test payment method `pm_card_gb`:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 12345,
  currency: "gbp",
  payment_method_types: ["card"],
  payment_method: "pm_card_gb",
  payments_orchestration: {
    enabled: true,
  },
  confirm: true,
});
```

After creating a test payment, view the details page for your [payment](https://dashboard.stripe.com/test/payments) to see which processor the payment routed to. On the payment details page, you can see the processor under **Processor**. **Recent activity** also shows the processor and the rules that routed the payment. Click the link to view the rules that routed this payment.

The [Payment Record](https://docs.stripe.com/api/payment-record.md) contains the execution history for payments where Orchestration is enabled. Retrieve the Payment Record using its ID from the PaymentIntent.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentRecord = await stripe.paymentRecords.retrieve(
  "{{PAYMENT_RECORD_ID}}",
);
```

Alternatively, enter the Payment Record ID in the Inspector in [Workbench](https://dashboard.stripe.com/test/workbench).

Verify which processor the payment routed to by viewing the `processor_details` hash:

```json
{
  "id": "pr_123456",
  "object": "payment_record",
  "amount_authorized": {
    "currency": "gbp",
    "value": 12345
  },
  ..."processor_details": {
    "type": "processor_a",
    ...
  },
  ...
}
```

## Optional: Update your reporting back end [Server-side]

Using Orchestration might require the following two changes:

- Stripe creates [Payment Records](https://docs.stripe.com/api/payment-record.md) and [Payment Attempt Records](https://docs.stripe.com/api/payment-attempt-record.md) instead of [Charges](https://docs.stripe.com/api/charges.md) for payments routed to other processors. If you rely on Charges for any of your internal reporting or reconciliation, you must use Payment Attempt Records instead across all of your Stripe volume.
- Stripe only creates Balance Transactions for payment volume processed on Stripe. Payment volume from other processors won’t have Balance Transactions because funds don’t move through your Stripe account. If your back-end systems assume there’s always a Balance Transaction after a successful payment, that’s no longer true.
  A diagram displaying a sample PaymentIntent object with an accompanying PaymentRecord object (See full diagram at https://docs.stripe.com/payments/orchestration/route-payments)

## Optional: Update your webhook handler [Server-side]

For card payments handled by another processor, the underlying PaymentIntent for those transactions have an additional `processing` [status](https://docs.stripe.com/payments/paymentintents/lifecycle.md), and Stripe sends the [payment_intent.processing](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.processing) event. For example, if you sell physical items, you can use this status to place a temporary hold on your inventory to prevent overselling.

After the processor informs Stripe the payment is captured, the PaymentIntent status transitions from `processing` to `succeeded`, and we send the [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) event.
Orchestration API flows and webhooks events (See full diagram at https://docs.stripe.com/payments/orchestration/route-payments)
If you already handle post-payment events, such as order fulfillment or entitlement based on the `payment_intent.succeeded` event, no changes are required.

```json
{
  "id": "evt_123456",
  "object": "event",
  "api_version": "2025-01-27",
  "created": 1719948368,
  "data": {
    "object": {
      "id": "pi_123456",
      "object": "payment_intent",
      "amount": 12345,
      "amount_received": 12345,
      "currency": "gbp",
      "payment_method": "pm_123456",
      "payments_orchestration": {
        "enabled": true
      },// The Payment Record ID remains the same throughout the lifecycle of the PaymentIntent
      "payment_record": "pr_123456",
      // A record of the latest attempt, generated every time you confirm the PaymentIntent
      "latest_payment_attempt_record": "par_123456",
      // Stripe doesn't create charges for payments orchestrated to another processor
      "latest_charge": null,
      ...
      "status": "succeeded"
    }
  }
}
```

## Add rules for your live integration [Dashboard]

After testing your integration, exit your sandbox and [add rules for your live integration](https://dashboard.stripe.com/orchestration/rules/add). Orchestration is enabled as soon as you activate your rules. Learn about other [conditions and actions](https://docs.stripe.com/payments/orchestration/rules.md) to route payments.

### Monitor processor performance

After enabling Orchestration for your live payments, use the Dashboard to monitor performance for your processors.

- On the [Orchestration overview](https://dashboard.stripe.com/payments/orchestration/overview) page, access performance analytics and payment success rates across your processors. You can filter this data to see performance by currency, card brand, card country, card type, or transaction type.
- On the [Payment details](https://dashboard.stripe.com/payments) page, view processor information for an individual payment.
- On the [Payments analytics](https://dashboard.stripe.com/acceptance) page, analyze your overall payment success rate to find out where payments fail. Use the processor filter to view only the payments routed through a specific processor.

The Dashboard doesn’t currently display balance summary and activity reports, dispute status, or receipts for payments processed on other processors. Data can take up to 2 days to populate. The Orchestration data that we share in the Dashboard relies on data provided by you and your other processors.

## Error prevention

If you enable error prevention during onboarding, Stripe makes sure that payments don’t fail solely due to features that aren’t supported by other payment processors through Orchestration. Specifically, when the routing logic directs a payment to a processor (whether it’s the main processor or a retry processor), and a required feature for the payment isn’t supported, Stripe automatically attempts to process the payment on Stripe instead of returning an error. If Stripe is the main processor and the payment fails on Stripe, we evaluate if the retry processor can handle the payment and if not, we don’t attempt to route the payment to the retry processor.

This fallback behavior helps maximize successful payments by preventing failures caused by processor feature limitations.
