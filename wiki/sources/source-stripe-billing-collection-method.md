---
title: "Stripe Billing — Collection Methods"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-billing-collection-method-2026.md"
tags: [stripe, billing, invoices, subscriptions, collection-method, payment-behavior, dunning]
---

## Summary

Reference guide for `charge_automatically` vs `send_invoice` collection methods on invoices and subscriptions, including failed payment status flows, `payment_behavior` options, and `send_invoice` due date configuration.

## Two collection methods

| Value | Behavior |
|---|---|
| `charge_automatically` | Auto-charges customer's default PM each billing period |
| `send_invoice` | Generates invoice; customer pays manually (Hosted Invoice Page / email) |

- Bank transfers and some payment methods only support `send_invoice`
- Changing `collection_method` on a subscription only affects **subsequently created** invoices, not the current open one

## Free trial + `charge_automatically`

Valid combo: customer adds PM during trial via Customer Portal. After trial ends, Stripe charges PM. Configurable: pause or cancel if no PM added by trial end.

## `send_invoice` due dates

- Configurable due date with up to 3 reminder emails (range: 10 days before → 60 days after due date)
- Past-due action (at 30/60/90 days): cancel, mark `unpaid`, or leave `past_due`

## `payment_behavior` options (subscription creation)

| Value | Behavior |
|---|---|
| `allow_incomplete` | Immediately attempts payment; → `incomplete` if first payment fails |
| `default_incomplete` | Always initializes as `incomplete` if invoice requires payment; PaymentIntent must be confirmed separately |

Both: → `active` after first invoice paid. If first invoice unpaid after **23 hours** → `incomplete_expired` (final/irreversible — open invoice voided, no future invoices).

## Failed payment status flows

### `charge_automatically` — recurring failure

- Subscription → `past_due`; PaymentIntent → `requires_payment_method` or `requires_action`
- Listen for `customer.subscription.updated` webhook; redirect customer to update PM
- After retries exhausted → `canceled` or `unpaid` (per Dashboard settings)

### `incomplete` subscription restrictions

Only metadata, `save_default_payment_method`, and `description` can be updated on an `incomplete` subscription. No invoice-affecting changes.

### `unpaid` status

Stripe still creates future invoices but leaves them as **drafts**. Option to resend `past_due` invoice or leave closed.

### Standalone invoice failures

| collection_method + auto_advance | Outcome |
|---|---|
| `charge_automatically` + `auto_advance=false` | Stays `open` indefinitely; no auto-retry or close |
| `charge_automatically` + `auto_advance=true` | May → `uncollectible` after retries exhausted |
| `send_invoice` | → `past_due` after due date; can transition to `uncollectible` or `void` |

## Enterprise / wire transfers

`send_invoice` preferred for enterprise clients: generates well-documented invoices suitable for wire transfer payment with audit trails.

## Related pages

- [[stripe-subscriptions-invoices]] — subscription invoice lifecycle and payment priority
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-billing-collection-method-2026]] — verbatim Stripe docs webpage
