<!-- Source URL: https://docs.stripe.com/payments/off-session-payments/orchestration -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Route off-session payments with Orchestration

Use Stripe Orchestration to route off-session payments across supported processors.

Use Orchestration with the Off-Session Payments API to route an off-session payment across supported processors. Enable Orchestration on each off-session payment request, then use your active Orchestration rules to select the processor.

> Smart Retries is incompatible with Stripe Orchestration.
> 
> Orchestration with the Off-Session Payments API only supports card payments and doesn’t support Connect or requests that contain raw card data.

## Before you begin

- Get access to the Off-Session Payments and Stripe Orchestration private previews.
- [Onboard your destination processor](https://docs.stripe.com/payments/orchestration/route-payments.md).
- Create and activate an [Orchestration routing configuration](https://docs.stripe.com/payments/orchestration/route-payments.md).

## Configure routing rules [Dashboard]

In a sandbox, create and activate [routing rules](https://docs.stripe.com/payments/orchestration/rules.md) in the Dashboard. Rules can evaluate supported payment attributes, such as amount, currency, metadata, and card properties. Each rule can select the main processor and an optional [retry processor](https://docs.stripe.com/payments/orchestration/retries.md).

## Create an off-session payment [Server-side]

Create an [OffSessionPayment](https://docs.stripe.com/api/v2/payments/off-session-payments/create.md?api-version=preview) and enable Orchestration for the request.

```curl
curl -X POST https://api.stripe.com/v2/payments/off_session_payments \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-04-22.preview" \
  --json '{
    "amount": {
        "value": 1000,
        "currency": "usd"
    },
    "customer": "{{CUSTOMER_ID}}",
    "payment_method": "{{PAYMENTMETHOD_ID}}",
    "cadence": "recurring",
    "metadata": {},
    "payments_orchestration": {
        "enabled": true
    }
  }'
```

The `payments_orchestration.enabled` parameter opts this off-session payment into your active routing configuration. Don’t pass a processor ID or routing-rule ID in the request.

## Verify routing

Use sandbox rules and [test payment methods](https://docs.stripe.com/testing.md) to create an off-session payment. Confirm that the payment matched the intended rule and processor. Review [Orchestration feature support](https://docs.stripe.com/payments/orchestration/feature-support.md) for processor-specific limitations.
