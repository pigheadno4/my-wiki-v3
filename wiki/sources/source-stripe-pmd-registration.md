---
title: "Stripe Docs — Register domains for payment methods"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-pmd-registration-2025.md"
tags: [stripe, domain-registration, apple-pay, google-pay, link, amazon-pay, klarna, paypal, elements, checkout]
---

## Summary

Guide for registering web domains to use Apple Pay, Amazon Pay, Google Pay, Klarna, Link, and PayPal in Elements or Checkout's embeddable payment form. Once registered, a domain is ready for future payment methods too.

## Payment Methods Requiring Domain Registration

- **Apple Pay** — Required
- Amazon Pay
- Google Pay
- Klarna
- Link
- PayPal

> Stripe handles Apple Pay merchant validation automatically — no Apple Merchant ID or CSR needed.

## Testing

Register domains in sandbox or live mode (live mode auto-registers in sandboxes). Use ngrok for local HTTPS testing.

## Dashboard Registration

Dashboard → Payment method domains → Add a new domain.

> Connect platforms creating direct charges must use the API (not Dashboard) for connected account domains.

## API

```js
// Register
stripe.paymentMethodDomains.create({ domain_name: 'example.com' })

// Disable
stripe.paymentMethodDomains.update('{{ID}}', { enabled: false })
```

## iframe Rules

- Default: iframe origin must match top-level origin
- Safari 17+: cross-origin iframe allowed with `allow="payment"` attribute; Apple Pay also requires registering the iframe source domain
- If top-level domain ≠ iframe domain: both must be registered on the associated account

## Connect Domain Registration

| Charge type | Authentication |
| --- | --- |
| Direct charges | Platform secret key + `Stripe-Account` header (connected account ID) |
| Destination / Separate charges | Platform secret key only (omit `Stripe-Account` header) |

## Related Pages

- [[stripe-wallets]] — wallets concept page (Apple Pay, Google Pay, Link coverage)
- [[source-stripe-apple-pay]] — Apple Pay integration (domain registration included)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-pmd-registration-2025]] — verbatim webpage content (132 lines)
