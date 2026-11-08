---
title: "Stripe Subscription Prebilling"
type: concept
category: framework
tags: [stripe, billing, subscriptions, prebilling, flexible-billing, preview]
---

## Overview

Prebilling invoices licensed-price items for multiple future service periods through subscription `billing_schedules`; invoice creation does not establish payment. The 2026-11-07 guide requires `billing_mode=flexible` and API version `2026-05-27.dahlia` or later. The 2026-05-13 public-preview guide stated `2025-09-30.preview` or later. The newer page's omission of “public preview” does not establish general availability or account eligibility.

## Prerequisites

- `billing_mode=flexible` — required; existing subscriptions must already use flexible mode before prebilling is added
- API version `2026-05-27.dahlia` or later in the 2026-11-07 guide

> [!warning] Contradiction
> The May public-preview guide stated `2025-09-30.preview` and barred subscriptions migrated from classic to flexible. November states `2026-05-27.dahlia` and omits that migration restriction. The omission is not proof that a migrated subscription is eligible.

## How it works

Set `billing_schedules[]` on Create or Update Subscription:

```bash
billing_schedules[0][applies_to][0][type]=price
billing_schedules[0][applies_to][0][price]={{PRICE_ID}}   # omit applies_to for applicable licensed items cycling before bill_until
billing_schedules[0][bill_until][type]=duration             # or "timestamp"
billing_schedules[0][bill_until][duration][interval]=month
billing_schedules[0][bill_until][duration][interval_count]=2
```

`proration_behavior` controls invoice timing:
- `always_invoice` — invoice generated immediately
- `create_prorations` — invoice generated at next billing cycle

## End date rules

| Constraint | Rule |
|---|---|
| Minimum | At least one full billing period from the start; November's example is one month from a monthly period start. Which item controls the minimum for mixed intervals is unspecified. |
| Maximum | At most 50 prebilled cycles **across all items**, not 50 per item. |
| Five-year guidance | November advises against an end date more than five years in the future; this is not an established API rejection limit. |

If the end date splits a period, the part before it is prebilled and the remainder follows the subscription configuration.

> [!warning] Contradiction
> The May public-preview guide instead used the shortest billing period for both a one-cycle minimum and a 12-cycle maximum. Those dated rules must not be used as November's mixed-interval minimum or total cap.

## Item-level scoping

- `applies_to[]` — target specific prices by ID
- Omit `applies_to` → all applicable licensed-price items that cycle before the prebilling end date are selected; metered usage items remain excluded
- Usage-based (`usage_type=metered`) prices are always excluded from prebilling
- Cannot set `applies_to[price]` on a metered price

## `bill_until` types

| Type | Parameters | When to use |
|---|---|---|
| `duration` | `interval` + `interval_count` | November 2026 describes it as from the current date; exact off-anchor or mixed-interval arithmetic is not supplied. May 2026 used cycle-start wording and mixed that with “current time” in a later paragraph. |
| `timestamp` | Unix timestamp | Exact end date |

## Limitations (2026-11-07 guide)

1. Incompatible with subscription schedules or schedule-backed subscriptions; clear expired `billing_schedules` before later attaching a schedule.
2. Only `percent_off` coupons with `duration=once` or `forever` are compatible.
3. Metered usage items are excluded; a subscription with only usage-based items cannot enable prebilling.
4. A requested end date beyond scheduled cancellation is automatically capped at that cancellation date.
5. `payment_behavior=pending_if_incomplete` is barred when **updating a subscription with an active billing schedule**.
6. Invoice timing depends on `proration_behavior`: `always_invoice` generates and finalizes immediately; `create_prorations` generates at the next natural billing cycle.

The May public-preview guide also barred migrated classic-to-flexible subscriptions and `proration_behavior=none`. November omits those statements; their omission is not evidence of support. Its broader May `pending_if_incomplete` wording is not the November condition.

## Preview before committing

Use `POST /v1/invoices/create_preview` with `subscription_details.billing_schedules` to preview the prebilling invoice before applying changes to the subscription.

## Use cases

- Send renewal invoice 7 days early (before the billing date)
- Monthly subscription: prebill for 45 days at signup
- Monthly price: invoice 12 months upfront without changing the price to an annual interval (November 2026 example); payment success is a separate outcome

## Sources

- [[source-stripe-subscriptions-prebilling]] — May 2026 public-preview and November 2026 prebilling guides: version, item scope, end-date and duration rules, conditional invoice timing and payment-event distinctions
