---
title: "Stripe Subscriptions — Pause Payment Collection"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/pause-payment"
raw_files:
  - "stripe-billing-subscriptions-pause-payment-2026-11-07.md"
  - "stripe-subscriptions-pause-payment-2026.md"
tags: [stripe, billing, subscriptions, pause-payment, pause-collection, grace-period, invoices]
---

## Summary

Guide to `pause_collection` on a subscription. The 2026-11-07 capture says the subscription remains `active`, invoices continue to generate, and the customer retains service access while active collection is paused. The three `behavior` options govern invoices created during the paused period. This is distinct from the separate true-pause lifecycle operation; see [[source-stripe-subscriptions-pause]] for that operation's own evidence. Existing invoices created before pausing continue to be retried unless separately voided.

## Key distinction: pause payment collection vs true pause

| Feature | Pause payment collection (`pause_collection`) | True pause (`/pause` endpoint; separate guide) |
|---|---|---|
| Invoice generation | Continues | Halted, per [[source-stripe-subscriptions-pause]] |
| Service delivery | Continues, per this guide | Halted, per [[source-stripe-subscriptions-pause]] |
| Requires flexible billing | Not stated as a requirement here | See separate true-pause guide |
| Available via | Dashboard or API | See separate true-pause guide |

## Three behaviors

### `behavior=void`
Invoices created while collection is paused are voided; no record of charges is created for those periods. The 2026-05-13 guide says they are immediately marked void. The subscription remains `active`; the November capture does not specify a voiding latency.

```js
stripe.subscriptions.update(subId, { pause_collection: { behavior: 'void' } })
```

### `behavior=keep_as_draft`
Invoices stay `draft` with `auto_advance=false`. They can be finalized and collected later. Custom invoice-finalization logic may need adjustment so it does not conflict. To collect after resuming subscription-level collection, set `auto_advance=true` on each retained draft invoice; this invoice-level change does not prove that payment succeeded.

```js
// Resume automatic collection on a specific draft invoice
stripe.invoices.update(invoiceId, { auto_advance: true })
```

### `behavior=mark_uncollectible`
Active collection stops for new invoices. Existing customer balance is still applied: if it pays the full invoice total, the invoice status becomes `paid`; otherwise it becomes `uncollectible`. This is a documented status rule, not evidence of a payment on a particular invoice. The subscription remains `active`.

## Pause and resume

Pause payment collection from the Dashboard or by updating the subscription with `pause_collection[behavior]`. A Dashboard custom date or optional API `pause_collection[resumes_at]` schedules automatic resumption at a future time. Without `resumes_at`, collection remains paused until `pause_collection` is unset. Manual resumption is available in the Dashboard or API:

```js
stripe.subscriptions.update(subId, { pause_collection: '' }) // unset = resume
```

Resuming subscription-level collection governs future invoices. It does not automatically advance invoices kept as drafts. Find those invoices with the subscription ID and `status=draft`, then set `auto_advance=true` on each invoice to collect; the Dashboard **Turn on automatic collection** action changes that same invoice property. These actions do not establish finalization, payment, or settlement.

## Pre-pause invoices

Invoices created **before** the pause continue to be retried unless separately voided.

## Subscription schedules

Scheduled updates still take effect during a collection pause. A schedule phase transition does not automatically remove `pause_collection` set directly on the subscription. If no `resumes_at` was set, unset `pause_collection` manually when collection should resume; a configured `resumes_at` can resume it automatically. To collect retained draft invoices after either form of resumption, separately set `auto_advance=true` on each desired invoice.

## Related pages

- [[stripe-subscriptions-pause]] — concept page comparing collection pause with separate true pause
- [[stripe-subscriptions-cancel]] — cancellation as alternative
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page
- [[source-stripe-subscriptions-pause]] — separate true-pause evidence

## Raw Sources

- [[raw/stripe-billing-subscriptions-pause-payment-2026-11-07|2026-11-07 pause payment collection guide]]
- [[raw/stripe-subscriptions-pause-payment-2026|2026-05-13 pause payment collection guide]]
