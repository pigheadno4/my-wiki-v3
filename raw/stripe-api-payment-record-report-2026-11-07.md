<!-- Source URL: https://docs.stripe.com/api/payment-record/report -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Report a payment

Report a new Payment Record. You may report a Payment Record as it is initialized and later report updates through the other report_* methods, or report Payment Records in a terminal state directly, through this method.

## Request

```curl
curl https://api.stripe.com/v1/payment_records/report_payment \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-10-28.endive" \
  -d "amount_requested[currency]=usd" \
  -d "amount_requested[value]=1000" \
  -d customer_presence=on_session \
  -d "description=computer software" \
  -d initiated_at=1730253453 \
  -d "payment_method_details[custom][display_name]=newpay" \
  -d "payment_method_details[type]=custom" \
  -d "processor_details[type]=custom" \
  -d "processor_details[custom][payment_reference]=npp2358872734k"
```

### Response

```json
{
  "id": "pr_5RV730PrHyAEi",
  "object": "payment_record",
  "amount_canceled": {
    "currency": "usd",
    "value": 0
  },
  "amount_failed": {
    "currency": "usd",
    "value": 0
  },
  "amount_guaranteed": {
    "currency": "usd",
    "value": 0
  },
  "amount_refunded": {
    "currency": "usd",
    "value": 0
  },
  "amount_requested": {
    "currency": "usd",
    "value": 1000
  },
  "created": 1730211363,
  "customer_details": null,
  "customer_presence": "on_session",
  "description": "computer software",
  "latest_payment_attempt_record": "par_1ArV730PrHyQuG",
  "livemode": true,
  "metadata": {},
  "payment_method_details": {
    "billing_details": null,
    "custom": {
      "display_name": "newpay",
      "type": "custom"
    },
    "payment_method": null,
    "type": "custom"
  },
  "processor_details": {
    "type": "custom",
    "custom": {
      "payment_reference": "npp2358872734k"
    }
  },
  "shipping_details": null
}
```

## Parameters

- [`amount_requested`](https://docs.stripe.com/api/payment-record/report.md?query=amount_requested) (object, required)
  The amount you initially requested for this payment.

- `initiated_at` (timestamp, required)
  When the reported payment was initiated. Measured in seconds since the Unix epoch.

- [`payment_method_details`](https://docs.stripe.com/api/payment-record/report.md?query=payment_method_details) (object, required)
  Information about the Payment Method debited for this payment.

- [`canceled`](https://docs.stripe.com/api/payment-record/report.md?query=canceled) (object, optional)
  Information about the payment attempt cancelation.

- [`customer_details`](https://docs.stripe.com/api/payment-record/report.md?query=customer_details) (object, optional)
  Customer information for this payment.

- `customer_presence` (enum, optional)
  Indicates whether the customer was present in your checkout flow during this payment.
Possible enum values:
  - `off_session`
    The customer was not present during the transaction.

  - `on_session`
    The customer was present during the transaction.

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- [`failed`](https://docs.stripe.com/api/payment-record/report.md?query=failed) (object, optional)
  Information about the payment attempt failure.

- [`guaranteed`](https://docs.stripe.com/api/payment-record/report.md?query=guaranteed) (object, optional)
  Information about the payment attempt guarantee.

- `metadata` (map, optional)
  Set of [key-value pairs](https://docs.stripe.com/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `outcome` (enum, optional)
  The outcome of the reported payment.
Possible enum values:
  - `canceled`
    The payment was canceled.

  - `failed`
    The payment failed.

  - `guaranteed`
    The payment was guaranteed.

- [`processor_details`](https://docs.stripe.com/api/payment-record/report.md?query=processor_details) (object, required)
  Processor information for this payment.

- [`shipping_details`](https://docs.stripe.com/api/payment-record/report.md?query=shipping_details) (object, optional)
  Shipping information for this payment.

## Returns

The newly created Payment Record.
