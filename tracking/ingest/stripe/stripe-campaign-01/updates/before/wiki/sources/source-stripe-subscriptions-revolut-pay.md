---
title: "Stripe Subscriptions — Set Up Revolut Pay Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-revolut-pay-2026.md"
tags: [stripe, billing, subscriptions, revolut-pay, setup-intents, payment-intents, checkout, mandate]
---

## Summary

Integration guide for Revolut Pay subscriptions. Three integration paths identical in structure to Amazon Pay and Cash App Pay: SetupIntents API, Subscriptions API, and Checkout. Key requirement: `off_session=true` on subscription create (SetupIntents path), `mandate_data` required.

## Three integration paths

### Path 1: SetupIntents API

```bash
# Create SetupIntent
curl /v1/setup_intents \
  -d confirm=true \
  -d usage=off_session \
  -d "payment_method_data[type]=revolut_pay" \
  -d "payment_method_types[]=revolut_pay" \
  -d "mandate_data[...]" \
  --data-urlencode "return_url=..."
```

→ redirect customer to Revolut Pay for authorization → SetupIntent `succeeded` → create subscription with `default_payment_method` + `off_session=true`

### Path 2: Subscriptions API (PaymentIntents)

Create subscription: `payment_behavior=default_incomplete` + `save_default_payment_method='on_subscription'` → confirm PaymentIntent with `payment_method_data[type]=revolut_pay` + `mandate_data` + `return_url` → `requires_action` → customer authenticates → activates

### Path 3: Checkout

```curl
checkout.sessions.create:
  payment_method_types[0]=card
  payment_method_types[1]=revolut_pay
  mode=subscription
```

## Key requirements

- `mandate_data` — required (type=online, IP, user agent, accepted_at)
- `off_session=true` — required on subscription create (SetupIntents path)
- `return_url` — required for redirect

## Testing

Select Revolut Pay → tap Subscribe → authenticate on redirect page. PaymentIntent: `requires_action` → `succeeded`.

## Related pages

- [[stripe-revolut-pay]] — concept page
- [[stripe-amazon-pay]] — same 3-path structure
- [[stripe-cash-app-pay]] — same 3-path structure
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-revolut-pay-2026]] — verbatim Stripe docs webpage
