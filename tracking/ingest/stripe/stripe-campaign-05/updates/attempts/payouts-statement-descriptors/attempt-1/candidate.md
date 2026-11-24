---
title: "Stripe — Payout Statement Descriptors"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payouts/statement-descriptors
raw_files:
  - "stripe-payouts-statement-descriptors-2026-11-07.md"
  - "stripe-payouts-statement-descriptors-2026.md"
tags: [stripe, payouts, statement-descriptor, bank-statement, connect]
---

## Summary

The May 11 and November 7, 2026 guides describe [[stripe]] statement descriptors for connected-account payouts. Stripe sends descriptor information to the beneficiary bank, which decides whether and how to display it.

## Two Levels

| Level | Scope | Set via |
| --- | --- | --- |
| Account-level | Automatic and manual payouts for the account | Dashboard payout settings |
| Payout-level | One manual payout | Dashboard balance overview when creating the payout, or API `statement_descriptor` |

Stripe uses the payout-level descriptor if supplied, then the account-level descriptor, then the fallback `STRIPE` if neither is configured.

## Standard US ACH transmission

The November 7, 2026 guide maps the descriptor for standard US ACH payouts to the ACH Company Entry Description field. The NACHA field limit is 10 characters. Stripe silently truncates longer values before submission to its banking partner. A descriptor of 10 characters or fewer fits that field, and display remains at the beneficiary bank's discretion.

The separate November [Create a payout API reference](../../raw/stripe-api-payouts-create-2026-11-07.md#L86-L93) documents a generic 22-character maximum for the request field and an initial `pending` Payout object when creation passes its initial checks. The 10-character limit applies to the later standard US ACH transmission.

## API example

The May guide uses Node.js, and the November guide shows the equivalent cURL request. This is the May example's request shape.

```js
stripe.payouts.create({ amount: 100, currency: 'usd', statement_descriptor: 'Cactus Payouts 001' })
```

Both captures show a `pending` response with the long descriptor echoed and a sample amount of `1100` despite the request's `100`. The illustrative response supplies no evidence of the transmitted value, eventual status, or bank display.

## Related Pages

- [[stripe-payouts]] — payout settings and statement descriptors

## Raw Sources

- [[raw/stripe-payouts-statement-descriptors-2026-11-07|November 7, 2026 payout statement descriptors guide]]
- [[raw/stripe-payouts-statement-descriptors-2026|May 11, 2026 payout statement descriptors guide]] — verbatim guide with three SVG diagram references
