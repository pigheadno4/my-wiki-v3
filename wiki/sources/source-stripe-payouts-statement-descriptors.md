---
title: "Stripe — Payout Statement Descriptors"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-payouts-statement-descriptors-2026.md"
tags: [stripe, payouts, statement-descriptor, bank-statement, connect]
---

## Summary

Two levels of payout statement descriptors with a defined precedence order. Banks don't guarantee display.

## Two Levels

| Level | Scope | Set via |
| --- | --- | --- |
| Account-level | All auto + manual payouts | Dashboard → Payout settings |
| Payout-level | Single manual payout only | Dashboard (balance overview) or API `statement_descriptor` field |

## Precedence Order

Payout-level → Account-level → Default (`'STRIPE'`)

## Key Rule

Beneficiary banks don't guarantee they'll display statement descriptors — Stripe sends the info but bank decides.

## API

```js
stripe.payouts.create({ amount: 100, currency: 'usd', statement_descriptor: 'Cactus Payouts 001' })
```

## Related Pages

- [[stripe-payouts]] — concept page (updated with statement descriptor note)

## Raw Sources

- [[stripe-payouts-statement-descriptors-2026]] — verbatim payout statement descriptors guide (3 SVG diagrams)
