---
title: "Stripe — Payment Element Across Multiple Processors"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-forwarding-third-party-2026.md"
tags: [stripe, vault-and-forward, payment-element, multiprocessor, create-payment-method]
---

## Summary

Integration guide: use Payment Element with `paymentMethodCreation: 'manual'` → `stripe.createPaymentMethod()` → send PM ID to server → `stripe.forwarding.requests.create()`.

## Flow

1. `stripe.elements({ mode: 'payment', paymentMethodCreation: 'manual' })`
2. `elements.submit()` → `stripe.createPaymentMethod({ elements, params })`
3. Send `paymentMethod.id` to server
4. Server: `stripe.forwarding.requests.create({ payment_method: id, url, request: { headers, body }, replacements })`
5. Check `forwardedReq.response_details.status` (Stripe always returns 200)

## Related Pages

- [[stripe-vault-and-forward]] — concept page
- [[source-stripe-vault-and-forward]] — ForwardingRequest API reference

## Raw Sources

- [[stripe-forwarding-third-party-2026]] — verbatim Payment Element multiprocessor guide (262 lines)
