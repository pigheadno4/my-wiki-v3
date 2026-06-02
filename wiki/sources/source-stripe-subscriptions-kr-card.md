---
title: "Stripe Subscriptions — Set Up South Korean Card (KR Card) Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-kr-card-2026.md"
tags: [stripe, billing, subscriptions, kr-card, south-korea, krw, setup-intents, mandate]
---

## Summary

Integration guide for South Korean card (`kr_card`) subscriptions. KRW-only, redirects to local processor's checkout page. Three integration paths: SetupIntents, Subscriptions API, Checkout. Same structure as Revolut Pay but KRW-specific.

## Key constraints

- **KRW only** — must convert prices to KRW
- **Local processor redirect** — customer is redirected to local processor's checkout page
- `off_session=true` required on subscription create (SetupIntents path)
- `mandate_data` required

## Three integration paths

### Path 1: SetupIntents API

```bash
curl /v1/setup_intents \
  -d confirm=true \
  -d usage=off_session \
  -d "payment_method_data[type]=kr_card" \
  -d "payment_method_types[]=kr_card" \
  -d "mandate_data[...]" \
  --data-urlencode "return_url=..."
```

→ redirect to local processor's checkout page → SetupIntent `succeeded` → create subscription with `default_payment_method` + `off_session=true`

### Path 2: Subscriptions API (PaymentIntents)

Create subscription: `default_incomplete` + `save_default_payment_method='on_subscription'` → confirm PaymentIntent with `payment_method_data[type]=kr_card` + `mandate_data` + `return_url` → `requires_action` → customer authenticates → activates

### Path 3: Checkout

```curl
checkout.sessions.create:
  payment_method_types[0]=card
  payment_method_types[1]=kr_card
  mode=subscription
```

## Related pages

- [[stripe-korea-payment-methods]] — concept page (updated with subscription facts)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-kr-card-2026]] — verbatim Stripe docs webpage
