---
title: "Stripe Docs — Link in the Payment Element"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-payment-element-link-2025.md"
tags: [stripe, link, payment-element, prefill, autofill, accelerated-signup, defaultValues]
---

## Summary

Integration guide for Link in the Payment Element. Covers two integration paths, the prefill tool, accelerated sign-up, and sandbox testing.

## Integration Options

| Option | When | How |
| --- | --- | --- |
| **Pass email (recommended)** | Email collected earlier in flow | `defaultValues.billingDetails.email` on Payment Element creation |
| **Collect in Payment Element** | No prior email collection | No code change — Link prompts appear automatically |

## `defaultValues` Prefilling

Pass full billing details to speed up checkout:

```js
elements.create('payment', { defaultValues: { billingDetails: { name, email, address } } })
```

## Prefill Tool (on by default)

- Scans surrounding checkout page for email/phone/name input fields
- Auto-populates Link login (email) or sign-up form (email/phone/name)
- Values held **only in local memory** — no cookies, no localStorage
- Disabled/limited by local data privacy laws; customers can opt out
- Disable in Link settings Dashboard (Settings → Link → Features)

## Accelerated Sign-up (on by default)

- Auto-expands Link sign-up fields when customer hasn't enrolled
- Pre-fills email and phone to help customers sign up
- Configurable at Settings → Payment Methods → Link (or Connected Accounts settings)
- Country-dependent; disabled where local regulations prohibit

## Sandbox OTP Codes

Same as Checkout: any 6 digits = success; `000001` = invalid; `000002` = expired; `000003` = max attempts exceeded.

## CDN Assets

- `raw/assets/stripe-link-in-payment-element.png` — Payment Element with Link prompt (430 KB)

## Related Pages

- [[stripe-link]] — Link concept page (Payment Element Integration section)
- [[source-stripe-checkout-link]] — Link with Checkout (same OTP codes)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-payment-element-link-2025]] — verbatim webpage content (116 lines)
