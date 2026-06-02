<!-- Source URL: https://docs.stripe.com/payments/payment-records -->
<!-- Fetched: 2026-04-19 -->

# The Payment Records API

Maintain a unified history of your payments, both on and off Stripe.

Use the [Payment Records](https://docs.stripe.com/api/payment-record.md) API to maintain a ledger of all your payments. If you’re processing payments through Stripe (on-Stripe payments) or integrating with third party processors (off-Stripe payments), use this API to keep a unified history of your payments.

The Payment Records API allows you to:

- Make payments with a third-party processor, and report results back to Stripe to take advantage of the full functionality of products such as Subscriptions and Radar.
- Create complex payment flows (such as multi-capture) where you can track each capture.
- Track third-party and partner-initiated payments, including Stripe-instructed card transactions.

## Relationship with PaymentIntents

The [Payment Intents](https://docs.stripe.com/api/payment_intents.md) API manages a variety of payment flows. However, many advanced use cases require a more precise representation of payment history.

If your application accepts payments both on Stripe using PaymentIntents and off Stripe through another processor, you can use PaymentRecords as a complete system of record. If you’ve enabled [Orchestration](https://docs.stripe.com/payments/orchestration.md):

- **On-Stripe payments**: Stripe automatically creates a PaymentRecord for each PaymentIntent.
- **Off-Stripe payments**: You can manually create PaymentRecords by reporting payment data using the Payment Records API.

PaymentRecords enable interoperability across Stripe products. Products such as [Subscriptions](https://docs.stripe.com/subscriptions.md) (with smart retries) and [Invoices paid out of band](https://support.stripe.com/questions/marking-an-invoice-paid-out-of-band) use PaymentRecords as the core primitive for tracking payment outcomes.

To retrieve the PaymentRecord associated with a PaymentIntent that has Orchestration enabled:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentRecord = await stripe.paymentRecords.retrieve(
  "{{PAYMENTINTENT_ID}}",
);
```

## Create and manage PaymentRecords

A PaymentRecord is the record of a payment, and includes all attempts and outcomes associated with it. It’s the primary reference point for understanding the lifecycle and status of a payment.

Each PaymentRecord can have multiple [PaymentAttemptRecords](https://docs.stripe.com/api/payment-attempt-record.md), that each detail a specific attempt to process the payment. This structure allows you to track success, retries, and failures.

Each PaymentAttemptRecord can have multiple PaymentAttemptRecordEntries, that each detail a single event within that attempt, such as initiation, authentication, authorization, or capture. Together, they form an append-only event log you can use to reconstruct the full lifecycle of a payment attempt.
A sample PaymentRecord with PaymentAttemptRecords and PaymentAttemptRecordEntries (See full diagram at https://docs.stripe.com/payments/payment-records)

### Report a new payment

To [report](https://docs.stripe.com/api/payment-record/report-payment/report.md) an off-Stripe payment, create a PaymentRecord with details about the transaction, including the amount, payment method, processor, and relevant timestamps. Stripe automatically creates an associated PaymentAttemptRecord using the data provided, referenced as the `latest_payment_attempt_record` in the response.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentRecord = await stripe.paymentRecords.reportPayment({
  amount_requested: {
    currency: "usd",
    value: 1000,
  },
  initiated_at: 1730253453,
  outcome: "guaranteed",
  guaranteed: {
    guaranteed_at: 1746572320,
  },
  payment_method_details: {
    payment_method: "{{PAYMENTMETHOD_ID}}",
  },
  processor_details: {
    type: "custom",
  },
});
```

### Report a failed payment attempt

Reporting failed payment attempts makes sure Stripe has a complete view of your payment flows, enabling other products to function (for example, [smart retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries.md)). If a payment attempt fails, [report the failure](https://docs.stripe.com/api/payment-record/report-payment-attempt-failed/report.md) by referencing the existing PaymentRecord ID and passing in the time of failure.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentRecord = await stripe.paymentRecords.reportPaymentAttemptFailed(
  "{{PAYMENT_RECORD_ID}}",
  {
    failed_at: 1730253453,
  },
);
```

### Retry failed payments

Sometimes users retry failed payments more than once. You can [report a new payment attempt](https://docs.stripe.com/api/payment-record/report-payment-attempt/report.md) using the same PaymentRecord. Retries can use the same or different payment method and processor.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentRecord = await stripe.paymentRecords.reportPaymentAttempt(
  "{{PAYMENT_RECORD_ID}}",
  {
    initiated_at: 1730253825,
    payment_method_details: {
      payment_method: "{{PAYMENTMETHOD_ID}}",
    },
  },
);
```

### Report a refund

If a payment was successfully processed but later refunded (either fully or partially), you can [report the refund](https://docs.stripe.com/api/payment-record/report-refund/report.md) to maintain accurate payment records. This ensures that Stripe has a complete view of the payment lifecycle, including any refunds processed through your payment processor.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentRecord = await stripe.paymentRecords.reportRefund(
  "{{PAYMENT_RECORD_ID}}",
  {
    processor_details: {
      type: "custom",
      custom: {
        refund_reference: "ref_123456",
      },
    },
    outcome: "refunded",
    refunded: {
      refunded_at: 1730253825,
    },
    amount: {
      value: 1000,
      currency: "usd",
    },
  },
);
```

If you don’t specify an `amount`, the entire guaranteed amount is refunded. You can report multiple partial refunds on the same PaymentRecord until the full amount is refunded.

## Understand the state of your payments

You can use the PaymentRecord for your dashboards and reporting systems. By having one record, you don’t need to reconcile the modeling differences between your other processors and Stripe.

### Retrieve the PaymentRecord

You can retrieve the PaymentRecord using the ID. For orchestrated payments, this is returned in the PaymentIntent response. For historical payments made, you can also retrieve PaymentRecord using the ID of the PaymentIntent.

The latest PaymentAttemptRecord is available on the PaymentRecord and you can retrieve it using the [Payment Attempt Records](https://docs.stripe.com/payments/payment-records.md#retrieve-payment-attempt-record) API. For historical payments that use the Charges API, use the Charge ID to retrieve the PaymentAttemptRecord.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentRecord = await stripe.paymentRecords.retrieve(
  "{{PAYMENT_RECORD_ID}}",
);
```

```json
{
  "processor_details": {
    "type": "processor_a",
  },
  "latest_payment_attempt_record": "{{PAYMENT_ATTEMPT_RECORD_ID}}",
  "amount_guaranteed": {
    "value": 10000,
    "currency": "usd",
  },
  "payment_method_details": {
    "payment_method": "{{PAYMENT_METHOD_ID}}",
    "type": "card",
  },
}
...
```

### Retrieve the PaymentAttemptRecord

In cases where you have multiple payments attempts (for example, a payment failed on a different processor and was retried and succeeded on Stripe), the PaymentRecord includes the latest attempt under `latest_payment_attempt_record`. You can view all attempts by querying the PaymentAttemptRecord:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentAttemptRecords = await stripe.paymentAttemptRecords.list({
  payment_record: "{{PAYMENT_RECORD_ID}}",
});
```

```json
{
  "object": "list",
  "data": [{
    "id": "par_124",
    "amount_requested": 10000,
    "amount_guaranteed": 10000,
    "amount_failed": 0,
  },
  {
    "id": "par_123",
    "amount_requested": 10000,
    "amount_guaranteed": 0,
    "amount_failed": 10000,
  }]
}
...
```

### Retrieve the PaymentAttemptRecordEntry

> PaymentAttemptRecordEntries are currently limited to preview users. Contact your Stripe account representative or Sales if you’re interested in trying it out.

Stripe sends a webhook event containing the `PaymentAttemptRecordEntry` object each time one is created (for example, payment_attempt_record_entry.initiated). Subscribe to these events to react to payment lifecycle changes in real time.

To view all of the PaymentAttemptRecordEntries within a particular payment attempt at once (for example, initiated, authorized, and guaranteed), list the PaymentAttemptRecordEntries using the ID of the PaymentAttemptRecord:

```curl
curl -G https://api.stripe.com/v1/payment_attempt_record_entries \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d payment_attempt_record={{PAYMENT_ATTEMPT_RECORD_ID}}
```

```json
{
  "object": "list",
  "data": [{
    "id": "pare_4",
    "type": "guaranteed",
    "guaranteed": {
      "amount": { "value": 1099, "currency": "usd" }
    }
  },
  {
    "id": "pare_3",
    "type": "authorized",
    "authorized": {
      "amount": { "value": 1099, "currency": "usd" }
    }
  },
  {
    "id": "pare_2",
    "type": "authenticated",
    "authenticated": {
      "amount": { "value": 1099, "currency": "usd" }
    }
  },
  {
    "id": "pare_1",
    "type": "initiated",
    "initiated": {
      "amount": { "value": 1099, "currency": "usd" },
      "payment_method_details": { "type": "card" },
      "processor_details": { "type": "processor_a" }
    }
  }]
}
...
```

You can also view your payments in the [Dashboard](https://dashboard.stripe.com/payments).
