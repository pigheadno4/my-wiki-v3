---
title: Payment failures and recovering balances
slug: /docs/subscriptions/customize/payment-failure-retry/
createTime: "2024-07-08T07:11:04.756Z"
updateTime: "2025-05-09T15:44:56.416Z"
---

# Payment failures and recovering balances

You can set payment failure thresholds for subscription plans and capture the outstanding balance for a subscription.

When a subscription exceeds the payment failure threshold:

- The subscription is suspended.
- If a payment fails, PayPal retries the payment every 5 days. PayPal retries the payment up to twice per billing cycle.
- If the second retry fails, PayPal counts this as a payment failure. The failed payment amount is added to the outstanding balance for the next billing cycle.

When you create your plan, you can set the value for the payment_failure_threshold in the payment_preferences object:

#### **`When you create your plan, you can set the value`**

```javascript
"payment_preferences": {
        "auto_bill_outstanding": true,
        "payment_failure_threshold": 2
    }
```

### Example of payment failure threshold

The following example describes a payment failure threshold where:

- A streaming service costs $10 per month
- The payment failure threshold is set to 2
- A subscriber pays on January 1 and is billed on the first of every month at 10:00 AM GMT.

In this example, PayPal can't pull funds from the subscriber on February 1. Paypal retries on February 5 and February 10. No funds are pulled. PayPal counts this as a payment failure. The outstanding amount against the subscription is $10.

$10 is added to the next billing cycle, so the subscriber is charged $20 on March 1. PayPal can't pull funds and reaches the payment failure threshold. The subscription is suspended.

The subscriber cancels the subscription with a $20 outstanding balance. PayPal stops retrying attempts for failed payments. You can settle offline or [capture the payment](/docs/api/subscriptions/v1/#subscriptions_capture) .

If the subscription has an outstanding balance, you can capture the balance. You can do this if the failure threshold is met and the subscription is suspended.

### Sample request

In this example, the outstanding balance being captured is $20. You could also capture $10 of the balance now and the remaining $10 later.

#### **`Sample request`**

```curl

curl -v -X POST https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-BW452GLLEP1G/capture
-H "Content-Type: application/json"
-H "Authorization: Bearer ACCESS-TOKEN"
-H "PayPal-Request-Id: CAPTURE-160919-A0051"
-d '{
   "note": "Charging because the balance reached the limit",
   "capture_type": "OUTSTANDING_BALANCE",
   "amount": {
     "value": "20.00",
     "currency_code": "USD"
   }
 }'

```
