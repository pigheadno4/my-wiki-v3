---
title: "Stripe Subscriptions — Pause Payment Collection"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-pause-payment-2026.md"
tags: [stripe, billing, subscriptions, pause-payment, pause-collection, grace-period, invoices]
---

## Summary

Guide to `pause_collection` — stops payment collection on a subscription while invoices continue generating. Distinct from the "true pause" (`/pause` endpoint): service delivery continues, invoices still created. Three `behavior` options control how generated invoices are handled.

## Key distinction: pause payment collection vs true pause

| Feature | Pause payment collection (`pause_collection`) | True pause (`/pause` endpoint) |
|---|---|---|
| Invoice generation | Continues | Halted |
| Service delivery | Continues | Halted |
| Requires flexible billing | No | Yes |
| Available via | Dashboard or API | API only |

## Three behaviors

### `behavior=void`
Invoices immediately voided → customer never charged. No emails/webhooks. Subscription stays `active`.

```js
stripe.subscriptions.update(subId, { pause_collection: { behavior: 'void' } })
```

### `behavior=keep_as_draft`
Invoices stay `draft` with `auto_advance=false`. No emails/webhooks. To collect later: update `auto_advance=true` on draft invoices. Custom finalization logic may conflict.

```js
// Resume collection on a specific draft invoice
stripe.invoices.update(invoiceId, { auto_advance: true })
```

### `behavior=mark_uncollectible`
New invoices marked `uncollectible`. Exception: if customer balance covers full invoice amount → marked `paid`. Accurate downstream reporting. Subscription stays `active`.

## `resumes_at`

Optional Unix timestamp. If not set, pauses indefinitely until `pause_collection` is unset:

```js
stripe.subscriptions.update(subId, { pause_collection: '' })  // unset = resume
```

Resuming only affects future invoices. For `keep_as_draft`, must also manually set `auto_advance=true` on existing draft invoices.

## Pre-pause invoices

Invoices created **before** pause continues to be retried unless you void them manually.

## Subscription schedules

Scheduled updates still apply during pause. When resuming, must manually unpause + set `auto_advance=true` on any draft invoices.

## Related pages

- [[stripe-subscriptions-pause]] — concept page (updated with pause payment collection comparison)
- [[stripe-subscriptions-cancel]] — cancellation as alternative
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-pause-payment-2026]] — verbatim Stripe docs webpage
